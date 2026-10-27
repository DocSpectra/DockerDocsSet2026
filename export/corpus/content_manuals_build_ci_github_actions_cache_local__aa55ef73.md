---
title: Use local cache in GitHub Actions
---

Before using this workflow, see [Cache requirements](cache-requirements.md) and
[repository credentials](registry-credentials.md).

## Local cache

> [!WARNING]
>
> At the moment, old cache entries aren't deleted, so the cache size [keeps growing](https://github.com/docker/build-push-action/issues/252).
> The following example uses the `Move cache` step as a workaround (see [`moby/buildkit#1896`](https://github.com/moby/buildkit/issues/1896)
> for more info).

You can also leverage [GitHub cache](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
using the [actions/cache](https://github.com/actions/cache) and [local cache exporter](../../cache/backends/local.md)
with this action:

```yaml
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Login to Docker Hub
        uses: docker/login-action@{{% param "login_action_version" %}}
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}

      - name: Cache Docker layers
        uses: actions/cache@{{% param "cache_action_version" %}}
        with:
          path: ${{ runner.temp }}/.buildx-cache
          key: ${{ runner.os }}-buildx-${{ github.sha }}
          restore-keys: |
            ${{ runner.os }}-buildx-

      - name: Build and push
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          push: true
          tags: user/app:latest
          cache-from: type=local,src=${{ runner.temp }}/.buildx-cache
          cache-to: type=local,dest=${{ runner.temp }}/.buildx-cache-new,mode=max

      - # Temp fix
        # https://github.com/docker/build-push-action/issues/252
        # https://github.com/moby/buildkit/issues/1896
        name: Move cache
        run: |
          rm -rf ${{ runner.temp }}/.buildx-cache
          mv ${{ runner.temp }}/.buildx-cache-new ${{ runner.temp }}/.buildx-cache
```
