---
title: Software Bill of Materials (SBOMs)
linktitle: SBOMs
description: Learn what SBOMs are, why they matter, and how Docker Hardened Images include signed SBOMs to support transparency and compliance.
keywords: sbom docker image, software bill of materials, signed sbom, container sbom verification, sbom compliance
---

## What is an SBOM?

See [Software bills of materials](/manuals/security/sbom.md) for the definition and [SBOM contents](/manuals/security/sbom.md#contents-of-an-sbom).

## Why are SBOMs important?

See [Why are SBOMs important?](/manuals/security/sbom.md#why-are-sboms-important).

## Docker Hardened Image SBOMs

Docker Hardened Images come with built-in SBOMs, ensuring that every component
in the image is documented and verifiable. These SBOMs are cryptographically
signed, providing a tamper-evident record of the image's contents. This
integration simplifies audits and enhances trust in the software supply chain.

