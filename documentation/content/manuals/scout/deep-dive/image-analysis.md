---
title: Image analysis behavior and limits
---

When you activate image analysis for a repository,
Docker Scout automatically analyzes new images that you push to that repository.

Image analysis extracts the Software Bill of Material (SBOM)
and other image metadata, and evaluates it against vulnerability data from
[security advisories](/manuals/scout/deep-dive/advisory-db-sources.md).

If you run image analysis as a one-off task using the CLI or Docker Desktop,
Docker Scout won't store any data about your image.
If you enable Docker Scout for your container image repositories however,
Docker Scout saves a metadata snapshot of your images after the analysis.
As new vulnerability data becomes available, Docker Scout recalibrates the analysis using the metadata snapshot, which means your security status for images is updated in real-time.
This dynamic evaluation means there's no need to re-analyze images when new CVE information is disclosed.

Docker Scout image analysis is available by default for Docker Hub repositories.
You can also integrate third-party registries and other services. To learn more,
see [Integration categories](/manuals/scout/deep-dive/integration-types.md).

## Maximum image size

Image analysis on the Docker Scout platform, and analysis triggered by background
indexing in Docker Desktop, has an image file size limit of 10 GB (uncompressed).
To analyze images larger than that:

- Attach an [SBOM attestation](/manuals/build/metadata/attestations/sbom.md) at build-time. When an image includes an SBOM attestation, Docker Scout uses it instead of generating one, so the 10 GB limit doesn’t apply.
- Alternatively, you can use the [CLI](/reference/cli/docker/scout/cves/) to analyze the image locally. The 10 GB limit doesn’t apply when using the CLI. If the image includes an SBOM attestation, the CLI uses it to complete the analysis faster.
