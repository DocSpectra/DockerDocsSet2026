---
title: Container lifecycle and published ports
description: Context for running, naming, stopping, restarting, and removing containers.
---

## Container isolation

A container is a normal operating system process except that this process is
isolated and has its own file system, its own networking, and its own isolated
process tree separate from the host.

To run an image inside of a container, you use the `docker run` command. It
requires one parameter and that's the image name.

## Publish a port

To publish a port for your container, use the `--publish` flag (`-p` for short)
on the `docker run` command. The format is `[host_port]:[container_port]`.

For port publishing, see [Publishing ports](/get-started/docker-concepts/running-containers/publishing-ports.md).

## Detached mode

Docker can run your container in detached mode in the background. Use
`--detach` or `-d` for short. Docker starts the container, detaches from it,
and returns you to the terminal prompt. It prints the container ID on the terminal.

## List containers

Run `docker ps` to see a list of running containers. This is similar to using
the `ps` command to see a list of processes on a Linux machine.

The output includes the container ID, image, command used to start the
container, when it was created, status, ports, and container names.

The default output only shows running containers. Use `--all` or `-a` for
short to see all containers, including stopped and running containers.

## Stop, restart, and remove containers

When you stop a container, it's not removed. Its status changes to stopped and
the process inside the container stops. Pass its name or ID to `docker stop`.

When you restart a container, it starts with the same flags or commands that
it was originally started with.

To remove a container, run `docker rm` with the container name. You can pass
multiple container names in one command. The process inside a removed container
is terminated and the container metadata is removed; the container is no longer
running or stopped.

## Name containers

Docker generates a random name if you don't provide one. Naming containers
makes it easier to identify the application or service associated with them.
Pass `--name` to `docker run` to name a container.
