---
title: Connect containers and host services
---

For port-publishing concepts, see [Publishing ports](/get-started/docker-concepts/running-containers/publishing-ports.md). For routing and limitations, see [Networking on Docker Desktop](_index.md).

## Connect a container to a service on the host

The host has a changing IP address, or none if you have no network access. To connect to services running on your host, use the special DNS name:

| Name                      | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `host.docker.internal`    | Resolves to the internal IP address of your host |
| `gateway.docker.internal` | Resolves to the gateway IP of the Docker VM      |


### Example

Run a simple HTTP server on port `8000`:

```console
$ python -m http.server 8000
```

Then run a container, install `curl`, and try to connect to the host using the following commands:

```console
$ docker run --rm -it alpine sh
# apk add curl
# curl http://host.docker.internal:8000
# exit
```

## Connect to a container from the host

To access containerized services from your host or local network, publish ports with the `-p` or `--publish` flag. For example:

```console
$ docker run -d -p 80:80 --name webserver nginx
```

Docker Desktop makes whatever is running on port `80` in the container, in
this case, `nginx`, available on port `80` of `localhost`. 

> [!TIP]
>
> The syntax for `-p` is `HOST_PORT:CLIENT_PORT`.

To publish all ports, use the `-P` flag. For example, the following command
starts a container (in detached mode) and the `-P` flag publishes all exposed ports of the
container to random ports on the host.

```console
$ docker run -d -P --name webserver nginx
``` 

Alternatively, you can also use [host networking](/manuals/engine/network/drivers/host.md#docker-desktop)
to give the container direct access to the network stack of the host.

See the [run command](/reference/cli/docker/container/run/) for more details on
publish options used with `docker run`.

All inbound connections pass through the Docker Desktop backend process (`com.docker.backend` (Mac), `com.docker.backend` (Windows), or `qemu` (Linux), which handles port forwarding into the VM.
For more details, see [How exposed ports work](/manuals/desktop/features/networking/_index.md#how-exposed-ports-work)
