---
title: Docker Hardened Images in CI/CD pipelines
description: Attestations and DHI usage in build and test pipelines.
---

## Use a DHI in CI/CD pipelines

Docker Hardened Images work just like any other image in your CI/CD pipelines.
You can reference them in Dockerfiles, pull them as part of a pipeline step, or
run containers based on them during builds and tests.

Unlike typical container images, DHIs also include signed
[attestations](attestations.md) such as SBOMs and provenance
metadata. You can incorporate these into your pipeline to support supply chain
security, policy checks, or audit requirements if your tooling supports it.

To strengthen your software supply chain, consider adding your own attestations
when building images from DHIs. This lets you document how the image was built,
verify its integrity, and enable downstream validation and policy enforcement
using tools like Docker Scout.

To learn how to attach attestations during the build process, see [Docker Build
Attestations](/manuals/build/metadata/attestations/_index.md).
