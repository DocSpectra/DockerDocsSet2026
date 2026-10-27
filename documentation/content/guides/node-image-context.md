---
title: Node.js image choices and build context
description: Base-image choices, version caveats, and build context for Node.js application images.
---

## Choose a base image

Before creating a Dockerfile, you need to choose a base image. You can either use the [Node.js Official Image](https://hub.docker.com/_/node) or a Docker Hardened Image (DHI) from the [Hardened Image catalog](https://hub.docker.com/hardened-images/catalog).

Choosing DHI offers the advantage of a production-ready image that is lightweight and secure. For more information, see [Docker Hardened Images](https://docs.docker.com/dhi/).

> [!IMPORTANT]
> The application examples use stable Node.js LTS image tags that are considered secure when the guides are written. Because new releases and security patches are published regularly, the tags shown in those examples may no longer be the safest option when you follow the guides. Always review the latest available image tags and select a secure, up-to-date version before building or deploying your application.
>
> Official Node.js Docker Images: https://hub.docker.com/_/node

## Docker Hardened Images for Node.js

Docker Hardened Images (DHIs) are available for Node.js in the [Docker Hardened Images catalog](https://hub.docker.com/hardened-images/catalog/dhi/node). Docker Hardened Images are freely available to everyone with no subscription required. You can pull and use them like any other Docker image after signing in to the DHI registry. For more information, see the [DHI quickstart](/dhi/get-started/) guide.

## Dockerfiles

> [!NOTE]
> A `Dockerfile` is a plain text file that contains step-by-step instructions to build a Docker image. It automates packaging your application along with its dependencies and runtime environment.  
> For full details, see the [Dockerfile reference](/reference/dockerfile/).


## Exclude files from the build context

The `.dockerignore` file tells Docker which files and folders to exclude when building the image.


> [!NOTE]
>This helps:
>- Reduce image size  
>- Speed up the build process  
>- Prevent sensitive or unnecessary files (like `.env`, `.git`, or `node_modules`) from being added to the final image.
>
> To learn more, visit the [.dockerignore reference](/manuals/build/concepts/context.md#dockerignore-files).

## Build an image

> [!NOTE]
> The `docker build` command packages your application into an image using the instructions in the Dockerfile. It includes all necessary files from the current directory (called the [build context](/build/concepts/context/#what-is-a-build-context)).

## Related resources

- [Multi-stage builds](/manuals/build/building/multi-stage.md) – Learn how to separate build and runtime stages.
- [Best practices for writing Dockerfiles](/manuals/build/building/best-practices.md) – Write efficient, maintainable, and secure Dockerfiles.
- [Build context in Docker](/manuals/build/concepts/context.md) – Learn how context affects image builds.
- [`docker init` CLI reference](/reference/cli/docker/init/) – Scaffold Docker assets automatically.
- [`docker build` CLI reference](/reference/cli/docker/image/build/) – Build Docker images from a Dockerfile.
- [`docker images` CLI reference](/reference/cli/docker/image/ls/) – Manage and inspect local Docker images.
- [`docker compose up` CLI reference](/reference/cli/docker/compose/up/) – Start and run multi-container applications.
- [`docker compose down` CLI reference](/reference/cli/docker/compose/down/) – Stop and remove containers, networks, and volumes.
