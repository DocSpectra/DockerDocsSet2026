---
title: Manage a Compose application
description: Commands for starting, stopping, inspecting, and building Compose applications.
---

The Docker CLI lets you interact with your Docker Compose applications through the `docker compose` command and its subcommands. If you're using Docker Desktop, the Docker Compose CLI is included by default.

Using the CLI, you can manage the lifecycle of your multi-container applications defined in the `compose.yaml` file. The CLI commands enable you to start, stop, and configure your applications effortlessly.

## Key commands 

To start all the services defined in your `compose.yaml` file:

```console
$ docker compose up
```

To stop and remove the running services:

```console
$ docker compose down 
```

If you want to monitor the output of your running containers and debug issues, you can view the logs with: 

```console
$ docker compose logs
```

To list all the services along with their current status:

```console
$ docker compose ps
```

For a full list of all the Compose CLI commands, see the [reference documentation](/reference/cli/docker/compose/).


## Build images with Compose

You can use Docker Compose to build Docker images. Docker Compose is a
tool for defining and running multi-container applications. Even if your
application isn't a multi-container application, Docker Compose can make it
easier to run by defining all the `docker run` options in a file.

To use Compose, you need a `compose.yaml` file. In this file, you can specify
the build context and Dockerfile for each service. When you run the command
`docker compose up --build`, Docker Compose will build the images for each
service and then start the containers.

For more information on building Docker images using Compose, see the [Compose
Build Specification](/reference/compose-file/build.md).

## Dockerfiles and Compose files

A Dockerfile provides instructions to build a container image while a Compose
file defines your running containers. Quite often, a Compose file references a
Dockerfile to build an image to use for a particular service.

## Start an application or run a one-off task

The `docker compose up` command creates and starts all your services. It's
perfect for launching your development environment or running the entire
application. The `docker compose run` command focuses on individual services.
It starts a specified service along with its dependencies, allowing you to run
tests or perform one-off tasks within that container.
