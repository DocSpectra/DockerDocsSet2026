---
title: Get and verify DHI SLSA provenance
description: Task steps and examples for DHI slsa.
---

See [SLSA context](../core-concepts/slsa.md). For registry access, see [Authenticate to dhi.io](authenticate.md). For attestation verification requirements, see [Retrieve and verify attestations](verify-attestations.md).

## Get and verify SLSA provenance for Docker Hardened Images

Each Docker Hardened Image (DHI) is cryptographically signed and includes
attestations. These attestations provide verifiable build provenance and
demonstrate adherence to SLSA Build Level 3 standards.

To get and verify SLSA provenance for a DHI, you can use Docker Scout.

```console
$ docker scout attest get dhi.io/<image>:<tag> \
  --predicate-type https://slsa.dev/provenance/v0.2 \
  --verify
```

For example:

```console
$ docker scout attest get dhi.io/node:20.19-debian12 \
  --predicate-type https://slsa.dev/provenance/v0.2 \
  --verify
```

## Resources

For Docker Build provenance, see [SLSA provenance
attestations](/manuals/build/metadata/attestations/slsa-provenance.md).
