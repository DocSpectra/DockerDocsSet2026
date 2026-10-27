---
title: Export to Docker with GitHub Actions
linkTitle: Export to Docker
description: Load the build results to the image store with GitHub Actions
keywords: ci, github actions, gha, buildkit, buildx, docker, export, load
---

For prerequisites, see [GitHub Actions guide](/guides/gha.md#prerequisites).
For Docker Hub setup, see [Configure registry credentials](registry-credentials.md).
Follow the variable and secret names in the workflow below.


You may want your build result to be available in the Docker client through
`docker images` to be able to use it in another step of your workflow:

```yaml
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
      
      - name: Build
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          load: true
          tags: myimage:latest
      
      - name: Inspect
        run: |
          docker image inspect myimage:latest
```
