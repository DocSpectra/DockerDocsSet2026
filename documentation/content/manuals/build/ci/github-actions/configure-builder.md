---
title: Configuring your GitHub Actions builder
linkTitle: BuildKit configuration
description: Configuring BuildKit instances for building in CI with GitHub Actions
keywords: ci, github actions, gha, buildkit, buildx
---

This page contains instructions on configuring your BuildKit instances when
using our [Setup Buildx Action](https://github.com/docker/setup-buildx-action).


For common setup, see [GitHub Actions prerequisites](/guides/gha.md#prerequisites).

## Version pinning

See [Pin Buildx and BuildKit versions in GitHub Actions](builder-versions.md).

## BuildKit container logs

See [View BuildKit logs in GitHub Actions](builder-logs.md).

## BuildKit Daemon configuration

See [Apply BuildKit configuration in GitHub Actions](builder-config.md).

### Registry mirror

See [Registry mirror](builder-config.md#registry-mirror).

### Max parallelism

See [Max parallelism](builder-config.md#max-parallelism).

## Append additional nodes to the builder

See [Append builder nodes in GitHub Actions](builder-nodes.md).

## Authentication for remote builders

See [Authenticate to remote builders in GitHub Actions](builder-authentication.md).

### SSH authentication

See [SSH authentication](builder-authentication.md#ssh-authentication).

### TLS authentication

See [TLS authentication](builder-authentication.md#tls-authentication).

## Standalone mode

See [Use standalone Buildx in GitHub Actions](builder-standalone.md).

## Isolated builders

See [Select isolated builders in GitHub Actions](builder-isolation.md).
