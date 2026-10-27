---
title: Attestations
keywords: build, attestations, sbom, provenance, metadata
description: |
  Introduction to SBOM and provenance attestations with Docker Build,
  what they are, and why they exist
weight: 50
---

{{< youtube-embed qOzcycbTs4o >}}

## Attestation concepts and build flags

See [Image attestations and provenance](/manuals/security/image-attestations.md).

## Docker Scout evaluation and recommendations

Docker Scout uses build attestations to evaluate the image's security and
supply chain posture, and to provide remediation recommendations for issues. If
issues are detected, such as missing or outdated attestations, Docker Scout can
guide you on how to add or update them, ensuring compliance and improving
visibility into the image's security status.

<div id="scout-lp-survey-anchor"></div>
