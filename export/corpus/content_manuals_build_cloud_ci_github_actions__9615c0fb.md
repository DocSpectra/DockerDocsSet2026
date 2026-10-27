---
title: Use Docker Build Cloud with GitHub Actions
---

Before using this example, follow [Docker Build Cloud CI requirements](ci-requirements.md).

## GitHub Actions

```yaml
name: ci

on:
  push:
    branches:
      - "main"

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Login to Docker Hub
        uses: docker/login-action@{{% param "login_action_version" %}}
        with:
          username: ${{ vars.DOCKER_ACCOUNT }}
          password: ${{ secrets.DOCKER_ACCESS_TOKEN }}
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
        with:
          driver: cloud
          endpoint: "${{ vars.DOCKER_ACCOUNT }}/${{ vars.CLOUD_BUILDER_NAME }}" # for example, "acme/default"
      
      - name: Build and push
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          tags: "<IMAGE>" # for example, "acme/my-image:latest"
          # For pull requests, export results to the build cache.
          # Otherwise, push to a registry.
          outputs: ${{ github.event_name == 'pull_request' && 'type=cacheonly' || 'type=registry' }}
```

The example above uses `docker/build-push-action`, which automatically uses the
builder set up by `setup-buildx-action`. If you need to use the `docker build`
command directly instead, you have two options:

- Use `docker buildx build` instead of `docker build`
- Set the `BUILDX_BUILDER` environment variable to use the cloud builder:

  ```yaml
  - name: Set up Docker Buildx
    id: builder
    uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
    with:
      driver: cloud
      endpoint: "${{ vars.DOCKER_ACCOUNT }}/${{ vars.CLOUD_BUILDER_NAME }}"

  - name: Build
    run: |
      docker build .
    env:
      BUILDX_BUILDER: ${{ steps.builder.outputs.name }}
  ```

For more information about the `BUILDX_BUILDER` environment variable, see
[Build variables](/manuals/build/building/variables.md#buildx_builder).

