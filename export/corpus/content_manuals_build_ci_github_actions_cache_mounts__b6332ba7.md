---
title: Preserve cache mounts in GitHub Actions
---

Before using this workflow, see [Cache requirements](cache-requirements.md) and
[repository credentials](registry-credentials.md).

## Cache mounts

BuildKit doesn't preserve cache mounts in the GitHub Actions cache by default.
To put your cache mounts into GitHub Actions cache and reuse it
between builds, you can use a workaround provided by
[`reproducible-containers/buildkit-cache-dance`](https://github.com/reproducible-containers/buildkit-cache-dance).

This GitHub Action creates temporary containers to extract and inject the
cache mount data with your Docker build steps.

The following example shows how to use this workaround with a Go project.

Example Dockerfile in `build/package/Dockerfile`

```Dockerfile
FROM golang:1.21.1-alpine as base-build

WORKDIR /build

RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=bind,source=go.mod,target=go.mod \
    --mount=type=bind,source=go.sum,target=go.sum \
    go mod download

RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    --mount=type=bind,target=. \
    go build -o /bin/app ./src
...
```

Example CI action

```yaml
name: ci

on:
  push:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Login to Docker Hub
        uses: docker/login-action@{{% param "login_action_version" %}}
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Set up QEMU
        uses: docker/setup-qemu-action@{{% param "setup_qemu_action_version" %}}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}

      - name: Docker meta
        id: meta
        uses: docker/metadata-action@{{% param "metadata_action_version" %}}
        with:
          images: user/app
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}

      - name: Go Build Cache for Docker
        uses: actions/cache@{{% param "cache_action_version" %}}
        with:
          path: go-build-cache
          key: ${{ runner.os }}-go-build-cache-${{ hashFiles('**/go.sum') }}

      - name: Inject go-build-cache
        uses: reproducible-containers/buildkit-cache-dance@4b2444fec0c0fb9dbf175a96c094720a692ef810 # v2.1.4
        with:
          cache-source: go-build-cache

      - name: Build and push
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          cache-from: type=gha
          cache-to: type=gha,mode=max
          file: build/package/Dockerfile
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          platforms: linux/amd64,linux/arm64
```

For more information about this workaround, refer to the
[GitHub repository](https://github.com/reproducible-containers/buildkit-cache-dance).

