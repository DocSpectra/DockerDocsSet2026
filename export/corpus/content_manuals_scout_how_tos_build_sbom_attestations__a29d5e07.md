---
title: Build an image with the Docker Scout SBOM generator
---

## Prerequisites

For image-store requirements and Docker Desktop setup, see [Set up builds with attestations](/manuals/scout/how-tos/build-with-attestations.md).

## Generate and attach an SBOM

You can generate the SBOM and attach it to the image at build-time as an
[attestation](/manuals/build/metadata/attestations/_index.md). BuildKit provides a default
SBOM generator which is different from what Docker Scout uses.
You can configure BuildKit to use the Docker Scout SBOM generator
using the `--attest` flag for the `docker build` command.
The Docker Scout SBOM indexer provides richer results
and ensures better compatibility with the Docker Scout image analysis.

```console
$ docker build --tag <org>/<image> \
  --attest type=sbom,generator=docker/scout-sbom-indexer:latest \
  --push .
```
