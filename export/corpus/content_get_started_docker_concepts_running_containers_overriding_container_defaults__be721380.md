---
title: Overriding container defaults
weight: 2
keywords: concepts, build, images, container, docker desktop
aliases: 
 - /guides/docker-concepts/running-containers/overriding-container-defaults/
---

{{< youtube-embed PFszWK3BB8I >}}

## Explanation

When a Docker container starts, it executes an application or command. The container gets this executable (script or file) from its image’s configuration. Containers come with default settings that usually work well, but you can change them if needed. These adjustments help the container's program run exactly how you want it to.

For example, if you have an existing database container that listens on the standard port and you want to run a new instance of the same database container, then you might want to change the port settings the new container listens on so that it doesn’t conflict with the existing container. Sometimes you might want to increase the memory available to the container if the program needs more resources to handle a heavy workload or set the environment variables to provide specific configuration details the program needs to function properly.

The `docker run` command offers a powerful way to override these defaults and tailor the container's behavior to your liking. The command offers several flags that let you to customize container behavior on the fly.

Here's a few ways you can achieve this.

### Overriding the network ports

Sometimes you might want to use separate database instances for development and testing purposes. Running these database instances on the same port might conflict. You can use the `-p` option in `docker run` to map container ports to host ports, allowing you to run the multiple instances of the container without any conflict.

```console
$ docker run -d -p HOST_PORT:CONTAINER_PORT postgres
```

### Setting environment variables

This option sets an environment variable `foo` inside the container with the value `bar`.

```console
$ docker run -e foo=bar postgres env
```

You will see output like the following:

```console
HOSTNAME=2042f2e6ebe4
foo=bar
```

> [!TIP]
>
> The `.env` file acts as a convenient way to set environment variables for your Docker containers without cluttering your command line with numerous `-e` flags. To use a `.env` file, you can pass `--env-file` option with the `docker run` command.
> ```console
> $ docker run --env-file .env postgres env
> ```

### Restricting the container to consume the resources

You can use the `--memory` and `--cpus` flags with the `docker run` command to restrict how much CPU and memory a container can use. For example, you can set a memory limit for the Python API container, preventing it from consuming excessive resources on your host. Here's the command:

```console
$ docker run -e POSTGRES_PASSWORD=secret --memory="512m" --cpus="0.5" postgres
 ```

This command limits container memory usage to 512 MB and defines the CPU quota of 0.5 for half a core.

> **Monitor the real-time resource usage**
>
> You can use the `docker stats` command to monitor the real-time resource usage of running containers. This helps you understand whether the allocated resources are sufficient or need adjustment.

By effectively using these `docker run` flags, you can tailor your containerized application's behavior to fit your specific requirements.

## Container networking

Remember that containers, by default, run in isolation and don't know anything about other processes
or containers on the same machine. So, how do you allow one container to talk to another? The answer is
networking. If you place the two containers on the same network, they can talk to each other.

There are two ways to put a container on a network:

- Assign the network when starting the container.
- Connect an already running container to a network.

## Bridge networks and name resolution

By default, containers automatically connect to a special network called a bridge network when you run them. This bridge network acts like a virtual bridge, allowing containers on the same host to communicate with each other while keeping them isolated from the outside world and other hosts. It's a convenient starting point for most container interactions. However, for specific scenarios, you might want more control over the network configuration.

Here's where the custom network comes in. You create a custom network by passing `--network` flag with the `docker run` command. All containers without a `--network` flag are attached to the default bridge network.

> **Key difference between default bridge and custom networks**
>
> 1. DNS resolution: By default, containers connected to the default bridge network can communicate with each other, but only by IP address. (unless you use `--link` option which is considered legacy). It is not recommended for production use due to the various [technical shortcomings](/engine/network/drivers/bridge/#differences-between-user-defined-bridges-and-the-default-bridge). On a custom network, containers can resolve each other by name or alias.
> 2. Isolation: All containers without a `--network` specified are attached to the default bridge network, hence can be a risk, as unrelated containers are then able to communicate. Using a custom network provides a scoped network in which only containers attached to that network are able to communicate, hence providing better isolation.

## Additional resources

* [Ways to set environment variables with Compose](/compose/how-tos/environment-variables/set-environment-variables/)
* [What is a container](/get-started/docker-concepts/the-basics/what-is-a-container/)
