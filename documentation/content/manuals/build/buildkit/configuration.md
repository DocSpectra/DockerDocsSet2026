---
title: Apply a BuildKit configuration
description: Apply custom configuration when creating a builder.
---

If you create a `docker-container` or `kubernetes` builder with Buildx, you can
apply a custom [BuildKit configuration](toml-configuration.md) by passing the
[`--buildkitd-config` flag](/reference/cli/docker/buildx/create/#buildkitd-config)
to the `docker buildx create` command.

