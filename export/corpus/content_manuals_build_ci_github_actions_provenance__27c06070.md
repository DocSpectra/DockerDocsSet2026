---
title: Add max-level provenance with GitHub Actions
---

Before using this workflow, see [Attestation defaults and output requirements](attestation-settings.md)
and [repository credentials](registry-credentials.md).

## Max-level provenance

It's recommended that you build your images with max-level provenance
attestations. Private repositories only add min-level provenance by default,
but you can manually override the provenance level by setting the `provenance`
input on the `docker/build-push-action` GitHub Action to `mode=max`.

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
          push: true
          provenance: mode=max
          tags: ${{ steps.meta.outputs.tags }}
```

