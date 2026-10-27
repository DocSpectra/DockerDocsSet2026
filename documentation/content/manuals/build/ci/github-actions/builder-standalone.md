---
title: Use standalone Buildx in GitHub Actions
---

For common setup, see [GitHub Actions prerequisites](/guides/gha.md#prerequisites) and
[repository credentials](registry-credentials.md).

## Standalone mode

If you don't have the Docker CLI installed on the GitHub Runner, the Buildx
binary gets invoked directly, instead of calling it as a Docker CLI plugin. This
can be useful if you want to use the `kubernetes` driver in your self-hosted
runner:

```yaml
name: ci

on:
  push:

jobs:
  buildx:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@{{% param "checkout_action_version" %}}
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
        with:
          driver: kubernetes
      
      - name: Build
        run: |
          buildx build .
```

