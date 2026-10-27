---
title: Build and scan child images with DHI VEX
description: Preserve DHI base-image lineage and add child-image VEX attestations.
---

See [DHI VEX conventions](../core-concepts/vex.md) and [scanner integrations](../explore/scanner-integrations.md) for context.

## Build child images with provenance attestations

When you build a custom image that uses a Docker Hardened Image as its base, you must build with `--provenance=mode=max` and `--sbom=true` so that Docker Scout can trace the base image lineage and correctly apply VEX statements.

Without these flags, Docker Scout cannot identify the DHI base image in
the provenance chain. As a result, it reports CVEs that are already suppressed
by VEX statements in the base image, producing false CVE positives in your
scan results.

> [!NOTE]
> **Why provenance attestation is required**
>
> Docker Scout uses max-mode provenance attestations to identify the DHI base image
> and track its lineage. A cryptographically signed provenance attestation ensures that
> base image lineage is verified and tamper-resistant, giving Docker Scout the trust
> anchor it needs to correctly apply VEX statements from the base image.

To build with maximum provenance and SBOM attestations:

```console
$ docker build \
    --provenance=mode=max \
    --sbom=true \
    --push \
    -t docker.io/<namespace>/<image>:<tag> .
```

After building with these flags, Docker Scout reads the full provenance
chain, matches the DHI base image, and applies its VEX statements. Scans of
your child image then reflect the correct suppressed CVEs, giving you an
accurate vulnerability assessment.

## VEX attestations in child images

If you introduce new layers in your child image and want to suppress CVEs in those layers, you can attach your own VEX attestation to the child image independently, you do not need to duplicate or aggregate the VEX statements from the DHI base image.

When `docker scout cves` runs against your child image, Scout reads VEX attestations from the full provenance chain and applies them cumulatively:

- **Base image VEX** - attached to the DHI, applied to CVEs in base image layers
- **Child image VEX** - attached to your image, applied to CVEs in layers you introduced

For example, if you add a `requests` layer to a DHI Python base image and attach a VEX statement suppressing `CVE-2024-47081`, Scout applies both VEX attestations independently and attributes each to its respective author:

```text
✓ VEX statements obtained from attestation
CVE-2024-47081  VEX: not affected [vulnerable code not present] : <your-namespace>
```

Scout suppresses CVEs from the DHI base VEX and CVEs from your child VEX in the same scan - no aggregate VEX document is required.

To create and attach a VEX attestation to your child image:

```bash
cat > child-vex.json << 'EOF'
{
  "@context": "https://openvex.dev/ns/v0.2.0",
  "@id": "https://<your-namespace>/vex/<image-name>/1",
  "author": "<your-namespace>",
  "timestamp": "<timestamp>",
  "version": 1,
  "statements": [
    {
      "vulnerability": {
        "name": "<CVE-ID>"
      },
      "products": [
        {
          "@id": "pkg:pypi/<package>@<version>"
        }
      ],
      "status": "not_affected",
      "justification": "vulnerable_code_not_present"
    }
  ]
}
EOF

docker scout attestation add \
  --file child-vex.json \
  --predicate-type https://openvex.dev/ns/v0.2.0 \
  docker.io/<your-namespace>/<image>:<tag>
```

> [!NOTE]
> This is only possible because you built with `--provenance=mode=max`. Without the full
> provenance chain, Scout cannot traverse back to the base image to retrieve its VEX attestations.
