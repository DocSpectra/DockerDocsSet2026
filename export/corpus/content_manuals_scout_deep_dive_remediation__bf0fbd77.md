---
title: Policy remediation requirements and recommendations
---

## Up-to-Date Base Images remediation

The **Up-to-Date Base Images** policy checks whether the base image you use is
up-to-date. The recommended actions displayed in the remediation side panel
depend on how much information Docker Scout has about your image. The more
information that's available, the better the recommendations.

The following scenarios outline the different recommendations depending on the
information available about the image.

### No provenance attestations

For Docker Scout to be able to evaluate this policy, you must add [provenance
attestations](/manuals/build/metadata/attestations/slsa-provenance.md) to your image. If
your image doesn't have provenance attestations, compliance is undeterminable.

### Provenance attestations available

With provenance attestations added, Docker Scout can correctly detect the base
image version that you're using. The version found in the attestations is
cross-referenced against the current version of the corresponding tag to
determine if it's up-to-date.

If there's a policy violation, the recommended actions show how to update your
base image version to the latest version, while also pinning the base image
version to a specific digest. For more information, see [Pin base image
versions](/manuals/build/building/best-practices.md#pin-base-image-versions).

### GitHub integration enabled

If you're hosting the source code for your image on GitHub, you can enable the
GitHub integration. This
integration enables Docker Scout to provide even more useful remediation
advice, and lets you initiate remediation for violations directly from the
Docker Scout Dashboard.

With the GitHub integration enabled, you can use the remediation side panel to
raise a pull request on the GitHub repository of the image. The pull request
automatically updates the base image version in your Dockerfile to the
up-to-date version.

This automated remediation pins your base image to a specific digest, while
helping you stay up-to-date as new versions become available. Pinning the base
image to a digest is important for reproducibility, and helps avoid unwanted
changes from making their way into your supply chain.

For more information about base image pinning, see [Pin base image
versions](/manuals/build/building/best-practices.md#pin-base-image-versions).

## Supply Chain Attestations remediation

The default **Supply Chain Attestations** policy requires full provenance and
SBOM attestations on images. If your image is missing an attestation, or if an
attestation doesn't contain enough information, the policy is violated.

The recommendations available in the remediation side panel helps guide you to
what action you need to take to address the issues. For example, if your image
has a provenance attestation, but the attestation doesn't contain enough
information, you're recommended to re-build your image with
[`mode=max`](/manuals/build/metadata/attestations/slsa-provenance.md#max) provenance.
