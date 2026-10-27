---
title: Customize the docker_gwbridge network
---

## Prerequisites and context

See [Swarm host and network prerequisites](prerequisites.md) and [Swarm traffic and network concepts](network-context.md).

## Customize the docker_gwbridge

The `docker_gwbridge` is a virtual bridge that connects the overlay networks
(including the `ingress` network) to an individual Docker daemon's physical
network. Docker creates it automatically when you initialize a swarm or join a
Docker host to a swarm, but it is not a Docker device. It exists in the kernel
of the Docker host. If you need to customize its settings, you must do so before
joining the Docker host to the swarm, or after temporarily removing the host
from the swarm.

You need to have the `brctl` application installed on your operating system in
order to delete an existing bridge. The package name is `bridge-utils`.

1.  Stop Docker.

2.  Use the `brctl show docker_gwbridge` command to check whether a bridge
    device exists called `docker_gwbridge`. If so, remove it using
    `brctl delbr docker_gwbridge`.

3.  Start Docker. Do not join or initialize the swarm.

4.  Create or re-create the `docker_gwbridge` bridge with your custom settings.
    This example uses the subnet `10.11.0.0/16`. For a full list of customizable
    options, see [Bridge driver options](/reference/cli/docker/network/create/#bridge-driver-options).

    ```console
    $ docker network create \
    --subnet 10.11.0.0/16 \
    --opt com.docker.network.bridge.name=docker_gwbridge \
    --opt com.docker.network.bridge.enable_icc=false \
    --opt com.docker.network.bridge.enable_ip_masquerade=true \
    docker_gwbridge
    ```

5.  Initialize or join the swarm.
