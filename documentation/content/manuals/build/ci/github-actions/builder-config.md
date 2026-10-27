---
title: Apply BuildKit configuration in GitHub Actions
---

For common setup, see [GitHub Actions prerequisites](/guides/gha.md#prerequisites) and
[repository credentials](registry-credentials.md).

## BuildKit Daemon configuration

You can provide a [BuildKit configuration](../../buildkit/toml-configuration.md)
to your builder if you're using the [`docker-container` driver](/manuals/build/builders/drivers/docker-container.md)
(default) with the `config` or `buildkitd-config-inline` inputs:

### Registry mirror

You can configure a registry mirror using an inline block directly in your
workflow with the `buildkitd-config-inline` input:

```yaml
name: ci

on:
  push:

jobs:
  buildx:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
        with:
          buildkitd-config-inline: |
            [registry."docker.io"]
              mirrors = ["mirror.gcr.io"]
```

For more information about using a registry mirror, see [Registry mirror](../../buildkit/configure.md#registry-mirror).

### Max parallelism

You can limit the parallelism of the BuildKit solver which is particularly
useful for low-powered machines.

You can use the `buildkitd-config-inline` input like the previous example, or you can use
a dedicated BuildKit config file from your repository if you want with the
`config` input:

```toml
# .github/buildkitd.toml
[worker.oci]
  max-parallelism = 4
```

```yaml
name: ci

on:
  push:

jobs:
  buildx:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
        with:
          config: .github/buildkitd.toml
```

