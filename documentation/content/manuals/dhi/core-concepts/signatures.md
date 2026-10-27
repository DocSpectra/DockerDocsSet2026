---
title: Code signing
description: Understand how Docker Hardened Images are cryptographically signed using Cosign to verify authenticity, integrity, and secure provenance.
keywords: container image signing, cosign docker image, verify image signature, signed container image, sigstore cosign
---

## What is code signing?

Code signing is the process of applying a cryptographic signature to software
artifacts, such as Docker images, to verify their integrity and authenticity. By
signing an image, you ensure that it has not been altered since it was signed
and that it originates from a trusted source.

In the context of Docker Hardened Images (DHIs), code signing is achieved using
[Cosign](https://docs.sigstore.dev/), a tool developed by the Sigstore project.
Cosign enables secure and verifiable signing of container images, enhancing
trust and security in the software supply chain.

## Why is code signing important?

Code signing plays a crucial role in modern software development and
cybersecurity:

- Authenticity: Verifies that the image was created by a trusted source.
- Integrity: Ensures that the image has not been tampered with since it was
  signed.
- Compliance: Helps meet regulatory and organizational security requirements.

## Docker Hardened Image code signing

Each DHI is cryptographically signed using Cosign, ensuring that the images have
not been tampered with and originate from a trusted source.

## Why sign your own images?

Docker Hardened Images are signed by Docker to prove their origin and integrity,
but if you're building application images that extend or use DHIs as a base, you
should sign your own images as well.

By signing your own images, you can:

- Prove the image was built by your team or pipeline
- Ensure your build hasn't been tampered with after it's pushed
- Support software supply chain frameworks like SLSA
- Enable image verification in deployment workflows

This is especially important in CI/CD environments where you build and push
images frequently, or in any scenario where image provenance must be auditable.

## Shared attestation context

See [Image attestations and provenance](/manuals/security/image-attestations.md).
