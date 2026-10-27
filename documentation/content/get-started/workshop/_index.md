---
title: Overview of the Docker workshop
linkTitle: Docker workshop
keywords: docker basics, how to start a docker container, container settings, setup
  docker, how to setup docker, setting up docker, docker container guide, how to get
  started with docker
description: Get started with the Docker basics in this workshop, You'll
  learn about containers, images, and how to containerize your first application.
aliases:
- /guides/get-started/
- /get-started/hands-on-overview/
- /guides/workshop/
---

This 45-minute workshop contains step-by-step instructions on how to get started with Docker. This workshop shows you how to:

- Build and run an image as a container.
- Share images using Docker Hub.
- Deploy Docker applications using multiple containers with a database.
- Run applications using Docker Compose.

> [!NOTE]
>
> For a quick introduction to Docker and the benefits of containerizing your
> applications, see [Getting started](/get-started/introduction/_index.md).

## Before you begin

- [Docker workshop prerequisites](/get-started/shared/workshop-prerequisites.md)
- [Containers: isolation and lifecycle](/get-started/docker-concepts/the-basics/what-is-a-container.md#container-isolation-and-lifecycle)
- [Images: filesystem and configuration](/get-started/docker-concepts/the-basics/what-is-an-image.md#filesystem-and-container-configuration)

## Workshop steps

1. [Containerize an application](02_our_app.md)
2. [Update the application](03_updating_app.md)
3. [Share the application](04_sharing_app.md)
4. [Persist the DB](05_persisting_data.md)
5. [Use bind mounts](06_bind_mounts.md)
6. [Run multiple containers](07_multi_container.md)
7. [Use Docker Compose](08_using_compose.md)
8. [Apply image-building best practices](09_image_best.md)
9. [What next](10_what_next.md)

## Next steps

In this section, you learned about containers and images.

Next, you'll containerize a simple application and get hands-on with the concepts.

{{< button text="Containerize an application" url="02_our_app.md" >}}
