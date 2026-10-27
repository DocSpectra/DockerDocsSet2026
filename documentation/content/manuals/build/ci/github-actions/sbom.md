---
title: Add an SBOM with GitHub Actions
---

Before using this workflow, see [Attestation defaults and output requirements](attestation-settings.md)
and [repository credentials](registry-credentials.md).

## SBOM

SBOM attestations aren't automatically added to the image. To add SBOM
attestations, set the `sbom` input of the `docker/build-push-action` to true.

```yaml
name: ci

on:
  push:

env:
  IMAGE_NAME: user/app

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

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@{{% param "metadata_action_version" %}}
        with:
          images: ${{ env.IMAGE_NAME }}

      - name: Build and push image
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          sbom: true
          push: true
          tags: ${{ steps.meta.outputs.tags }}
```
