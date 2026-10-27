---
title: Verify Docker Hardened Image Helm chart attestations
description: List, retrieve, and validate Helm chart attestations with Docker Scout.
---

Before you begin, review [verification tools and keys](../core-concepts/verification.md), [authenticate to dhi.io](authenticate.md), and see the [shared attestation procedure](verify-attestations.md) for registry and transparency-log caveats.

## Verify Helm chart attestations with Docker Scout

Docker Hardened Image Helm charts include the same comprehensive attestations
as container images. The verification process for charts is identical to that
for images, using the same Docker Scout CLI commands.

### List available chart attestations

To view the specific predicate type URIs for chart attestations, use Docker Scout.

To list attestations for a DHI Helm chart:

```console
$ docker scout attest list dhi.io/<chart>:<version>
```

For example, to list attestations for the external-dns chart:

```console
$ docker scout attest list dhi.io/external-dns-chart:1.20.0
```

This command shows all available chart attestations, including SBOMs, provenance, vulnerability reports, and more.

### Retrieve a specific chart attestation

To retrieve a specific attestation from a Helm chart, use the `--predicate-type` flag with the full predicate type URI:

```console
$ docker scout attest get \
  --predicate-type https://cyclonedx.org/bom/v1.6 \
  dhi.io/<chart>:<version>
```

For example:

```console
$ docker scout attest get \
  --predicate-type https://cyclonedx.org/bom/v1.6 \
  dhi.io/external-dns-chart:1.20.0
```

To retrieve only the predicate body:

```console
$ docker scout attest get \
  --predicate-type https://cyclonedx.org/bom/v1.6 \
  --predicate \
  dhi.io/<chart>:<version>
```

### Validate chart attestations with Docker Scout

To validate a chart attestation using Docker Scout, use the `--verify` flag:

```console
$ docker scout attest get dhi.io/<chart>:<version> \
   --predicate-type https://scout.docker.com/sbom/v0.1 --verify
```

For example, to verify the SBOM attestation for the external-dns chart:

```console
$ docker scout attest get dhi.io/external-dns-chart:1.20.0 \
   --predicate-type https://scout.docker.com/sbom/v0.1 --verify
```

The same `--skip-tlog` flag described in [Handle missing transparency log
entries](verify-attestations.md#handle-missing-transparency-log-entries) can also be used with chart
attestations when needed.
