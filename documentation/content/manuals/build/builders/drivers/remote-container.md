---
title: Connect Buildx to a manually managed BuildKit container
---

For shared options and behavior, see [remote driver reference](remote-reference.md).
For shared procedures, see [Select a builder](../selection.md) and
[Load build results](../image-loading.md).

## Example: Remote BuildKit in Docker container

This guide will show you how to create setup similar to the `docker-container`
driver, by manually booting a BuildKit Docker container and connecting to it
using the Buildx remote driver. This procedure will manually create a container
and access it via it's exposed port. (You'd probably be better of just using the
`docker-container` driver that connects to BuildKit through the Docker daemon,
but this is for illustration purposes.)

1.  Generate certificates for BuildKit.

    You can use this [bake definition](https://github.com/moby/buildkit/blob/master/examples/create-certs)
    as a starting point:

    ```console
    SAN="localhost 127.0.0.1" docker buildx bake "https://github.com/moby/buildkit.git#master:examples/create-certs"
    ```

    Note that while it's possible to expose BuildKit over TCP without using
    TLS, it's not recommended. Doing so allows arbitrary access to BuildKit
    without credentials.

2.  With certificates generated in `.certs/`, startup the container:

    ```console
    $ docker run -d --rm \
      --name=remote-buildkitd \
      --privileged \
      -p 1234:1234 \
      -v $PWD/.certs:/etc/buildkit/certs \
      moby/buildkit:latest \
      --addr tcp://0.0.0.0:1234 \
      --tlscacert /etc/buildkit/certs/daemon/ca.pem \
      --tlscert /etc/buildkit/certs/daemon/cert.pem \
      --tlskey /etc/buildkit/certs/daemon/key.pem
    ```

    This command starts a BuildKit container and exposes the daemon's port 1234
    to localhost.

3.  Connect to this running container using Buildx:

    ```console
    $ docker buildx create \
      --name remote-container \
      --driver remote \
      --driver-opt cacert=${PWD}/.certs/client/ca.pem,cert=${PWD}/.certs/client/cert.pem,key=${PWD}/.certs/client/key.pem,servername=<TLS_SERVER_NAME> \
      tcp://localhost:1234
    ```

    Alternatively, use the `docker-container://` URL scheme to connect to the
    BuildKit container without specifying a port:

    ```console
    $ docker buildx create \
      --name remote-container \
      --driver remote \
      docker-container://remote-container
    ```


