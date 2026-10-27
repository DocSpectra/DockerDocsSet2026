---
title: Initialize Docker assets
description: Generate Docker assets and find their references.
---

## Generate the files

Docker Desktop's built-in Docker Init feature can help create the necessary
Docker assets to containerize your application. Run `docker init` in the
application directory. It provides some default configuration, but you'll need
to answer a few questions about your application.

The utility creates the following files with sensible defaults for your project:

- `.dockerignore`
- `Dockerfile`
- `compose.yaml`
- `README.Docker.md`

## File references

- [Dockerfile](/reference/dockerfile.md)
- [.dockerignore](/manuals/build/concepts/context.md#dockerignore-files)
- [compose.yaml](/reference/compose-file/_index.md)

For running the application, see [Run an application with Compose](/guides/run-compose-application.md).
