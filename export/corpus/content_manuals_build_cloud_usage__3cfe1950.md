---
title: Building with Docker Build Cloud
linkTitle: Usage
weight: 20
description: Invoke your cloud builds with the Buildx CLI client
keywords: build, cloud build, usage, cli, buildx, client
aliases:
  - /build/cloud/usage/
---

For prerequisites and connection steps, see [Docker Build Cloud setup](setup.md).

- [Build an image](build.md)
- [Select the cloud builder](select-builder.md)
- [Build Compose services](compose.md)
- [Choose outputs and platforms](outputs.md)
- [Inspect builds in Docker Desktop](desktop-builds.md)
- [Use build secrets](secrets.md)
- [Manage build cache](cache.md)

## Use by default

See [Use by default](select-builder.md#use-by-default).

## Use with Docker Compose

See [Use with Docker Compose](compose.md).

## Loading build results

See [Loading build results](outputs.md#loading-build-results).

## Multi-platform builds

See [Multi-platform builds](outputs.md#multi-platform-builds).

## Cloud builds in Docker Desktop

See [Cloud builds in Docker Desktop](desktop-builds.md).

## Use secrets with Docker Build Cloud

See [Use secrets with Docker Build Cloud](secrets.md).

## Managing build cache

See [Managing build cache](cache.md).

## Unset Docker Build Cloud as the default builder

See [Unset Docker Build Cloud as the default builder](select-builder.md#unset-docker-build-cloud-as-the-default-builder).

## Registries on internal networks

It is possible to use Docker Build Cloud with a [private registry](/manuals/build-cloud/builder-settings.md#private-resource-access)
or registry mirror on an internal network.
