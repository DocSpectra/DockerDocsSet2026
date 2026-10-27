---
title: How Docker Scout uses SBOMs
---

For SBOM contents and security context, see [Software bills of materials](/manuals/security/sbom.md).

Docker Scout uses SBOMs to determine the components that are used in a Docker
image. When you analyze an image, Docker Scout will either use the SBOM that is
attached to the image as an attestation, or it will generate an SBOM on the fly
by analyzing the contents of the image.

The SBOM is cross-referenced with the [advisory database](/manuals/scout/deep-dive/advisory-db-sources.md)
to determine if any of the components in the image have known vulnerabilities.


Docker Scout recommends using SBOM attestations when available on the image.

## Docker Desktop analysis and vulnerability matching

Docker Desktop first analyzes images locally, where it generates a software bill of materials (SBOM).
Docker Desktop, Docker Hub, and the Docker Scout Dashboard and CLI all use the [package URL (PURL) links](https://github.com/package-url/purl-spec)
in this SBOM to query for matching Common Vulnerabilities and Exposures (CVEs) in [Docker Scout's advisory database](/manuals/scout/deep-dive/advisory-db-sources.md).
