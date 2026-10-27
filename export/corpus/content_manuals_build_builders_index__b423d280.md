---
title: Builders
weight: 40
keywords: build, buildx, builders, buildkit, drivers, backend
description: Learn about builders and how to manage them
---

A builder is a BuildKit daemon that you can use to run your builds. BuildKit
is the build engine that solves the build steps in a Dockerfile to produce a
container image or other artifacts.

You can create and manage builders, inspect them, and even connect to builders
running remotely. You interact with builders using the Docker CLI.

## Default builder

Docker Engine automatically creates a builder that becomes the default backend
for your builds. This builder uses the BuildKit library bundled with the
daemon. This builder requires no configuration.

The default builder is directly bound to the Docker daemon and its
[context](/manuals/engine/manage-resources/contexts.md). If you change the
Docker context, your `default` builder refers to the new Docker context.

## Build drivers

Buildx implements a concept of [build drivers](drivers/_index.md) to refer to
different builder configurations. The default builder created by the daemon
uses the [`docker` driver](drivers/docker.md).

Buildx supports the following build drivers:

- `docker`: uses the BuildKit library bundled into the Docker daemon.
- `docker-container`: creates a dedicated BuildKit container using Docker.
- `kubernetes`: creates BuildKit pods in a Kubernetes cluster.
- `remote`: connects directly to a manually managed BuildKit daemon.

## Selected builder

For builder selection, command differences, and examples, see
[Select a builder](selection.md).

### Select a different builder

See [Select a different builder](selection.md#select-a-different-builder).

### Difference between `docker build` and `docker buildx build`

See [Command differences](selection.md#difference-between-docker-build-and-docker-buildx-build).
