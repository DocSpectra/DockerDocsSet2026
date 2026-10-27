---
title: Inspect local images and running containers
description: CLI and Docker Desktop checks after building and starting an application.
---

## View local images

After building your Docker image, you can check which images are available on your local machine using either the Docker CLI or [Docker Desktop](/manuals/desktop/use-desktop/images.md). Since you're already working in the terminal, let's use the Docker CLI.

To list all locally available Docker images, run the following command:

```console
$ docker images
```

This output provides key details about your images:

- **Repository** – The name assigned to the image.
- **Tag** – A version label that helps identify different builds (e.g., latest).
- **Image ID** – A unique identifier for the image.
- **Created** – The timestamp indicating when the image was built.
- **Size** – The total disk space used by the image.

## View running containers

To confirm that the container is running, use the `docker ps` command:

```console
$ docker ps
```

This will list all active containers along with their ports, names, and status.
