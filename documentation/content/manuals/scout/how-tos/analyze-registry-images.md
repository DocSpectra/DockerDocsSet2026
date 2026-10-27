---
title: Analyze images pushed to a registry
---

## Prerequisites

See [Enable image analysis for repositories](./enable-repositories.md) and [Set up builds with attestations](./build-with-attestations.md).

## Build, push, and view results

To trigger image analysis for an image in a registry, push the image to a
registry that's integrated with Docker Scout, to a repository where image
analysis is activated.

> [!NOTE]
>
> Image analysis on the Docker Scout platform has a maximum image file size
> limit of 10 GB, unless the image has an SBOM attestation.
> See [Maximum image size](/manuals/scout/deep-dive/image-analysis.md#maximum-image-size).

1. Sign in with your Docker ID, either using the `docker login` command or the
   **Sign in** button in Docker Desktop.
2. Build and push the image that you want to analyze.

   ```console
   $ docker build --push --tag <org>/<image:tag> --provenance=true --sbom=true .
   ```

   Building with the `--provenance=true` and `--sbom=true` flags attaches
   [build attestations](/manuals/build/metadata/attestations/_index.md) to the image. Docker
   Scout uses attestations to provide more fine-grained analysis results.

   > [!NOTE]
   >
   > The default `docker` driver only supports build attestations if you use the
   > [containerd image store](/manuals/desktop/features/containerd.md).

3. Go to the [Images page](https://scout.docker.com/reports/images) in the Docker Scout Dashboard.

   The image appears in the list shortly after you push it to the registry.
   It may take a few minutes for the analysis results to appear.
