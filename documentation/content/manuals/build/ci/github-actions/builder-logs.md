---
title: View BuildKit logs in GitHub Actions
---

For common setup, see [GitHub Actions prerequisites](/guides/gha.md#prerequisites) and
[repository credentials](registry-credentials.md).

## BuildKit container logs

To display BuildKit container logs when using the `docker-container` driver,
you must either [enable step debug logging](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging#enabling-step-debug-logging),
or set the `--debug` buildkitd flag in the [Docker Setup Buildx](https://github.com/marketplace/actions/docker-setup-buildx) action:

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
          buildkitd-flags: --debug
      
      - name: Build
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
```

Logs will be available at the end of a job:

![BuildKit container logs](images/buildkit-container-logs.png)

