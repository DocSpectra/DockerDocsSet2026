---
title: Scan Docker Hardened Images
linktitle: Scan an image
description: Learn how to scan Docker Hardened Images for known vulnerabilities using Docker Scout, Grype, Trivy, Wiz, or Mend.io.
keywords: scan container image, docker scout cves, grype scanner, trivy container scanner, mend.io, vex attestation
weight: 46
---

Docker Hardened Images (DHIs) are designed to be secure by default, but like any
container image, it's important to scan them regularly as part of your
vulnerability management process.

## Scan with OpenVEX-compliant scanners

To get accurate vulnerability assessments, use scanners that support
[VEX](/manuals/dhi/core-concepts/vex.md) attestations. The following scanners can
read and apply the VEX statements included with Docker Hardened Images:

- [Docker Scout](#docker-scout): Automatically applies VEX statements with zero configuration
- [Trivy](#trivy): Supports VEX through VEX Hub or local VEX files
- [Grype](#grype): Supports VEX via the `--vex` flag
- [Wiz](#wiz): Automatically applies VEX statements with
  zero configuration
- [Mend.io](#mendio): Automatically applies VEX statements with
  zero configuration

For guidance on choosing the right scanner and understanding the differences
between VEX-enabled and non-VEX scanners, see [Scanner
integrations](/manuals/dhi/explore/scanner-integrations.md).

## Docker Scout

[Scan with Docker Scout](scan-docker-scout.md).

## Grype

[Scan with Grype](scan-grype.md).

## Trivy

[Scan with Trivy](scan-trivy.md).

## Wiz

[Scan with Wiz](scan-wiz.md).

## Mend.io

[Scan with Mend.io](scan-mend.md).

## Build child images with provenance attestations

[Build child images and apply base and child VEX statements](scan-child-images.md).

## Automate DHI scanning in CI/CD with Docker Scout

[Scan in GitHub Actions](scan-ci.md).

## Export VEX attestations

[Export VEX files and review retrieval requirements](export-vex.md).
