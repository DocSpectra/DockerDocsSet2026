---
title: Scan images built from Docker Hardened Images
linktitle: Scan child images and CI builds
description: Build child images with provenance, attach child VEX attestations, and scan in CI with Docker Scout.
weight: 47
---

For scanning a DHI directly or exporting its VEX attestations, see [Scan Docker
Hardened Images](./scan.md). For authentication and image references, see
[Pull, run, and reference DHIs](./use.md#pull-run-and-reference-dhis).

Choose a task:

- [Build with provenance and SBOM attestations](#build-child-images-with-provenance-attestations)
- [Attach VEX for layers you introduce](#vex-attestations-in-child-images)
- [Scan in GitHub Actions](#automate-dhi-scanning-in-cicd-with-docker-scout)

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

## Automate DHI scanning in CI/CD with Docker Scout

Integrating Docker Scout into your CI/CD pipeline enables you to automatically
verify that images built from Docker Hardened Images remain free from known
vulnerabilities during the build process. This proactive approach ensures the
continued security integrity of your images throughout the development
lifecycle.

### Example GitHub Actions workflow

The following is a sample GitHub Actions workflow that builds an image, scans it and pushes to the registry only if the scan passes:

```yaml {collapse="true"}
name: DHI Vulnerability Scan

on:
  push:
    branches:
      - main
  pull_request:

env:
  REGISTRY: docker.io
  IMAGE_NAME: ${{ github.repository }}
  SHA: ${{ github.event.pull_request.head.sha || github.event.after }}

jobs:
  scan:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      pull-requests: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@{{% param "checkout_action_version" %}}

      - name: Set up Docker with containerd image store
        uses: docker/setup-docker-action@{{% param "setup_docker_action_version" %}}
        with:
          daemon-config: |
            {
              "features": {
                 "containerd-snapshotter": true
              }
            }

      - name: Log in to Docker Hub
        uses: docker/login-action@{{% param "login_action_version" %}}
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          context: .
          sbom: true
          tags: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ env.SHA }}
      
      - name: Run Docker Scout CVE scan
        uses: docker/scout-action@v1
        with:
          command: cves
          image: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ env.SHA }}
          only-severities: critical,high
          exit-code: true

      - name: Push image
        if: success()
        run: |
          docker push ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ env.SHA }}
```

The `exit-code: true` parameter ensures that the workflow fails if any critical or
high-severity vulnerabilities are detected, preventing the deployment of
insecure images.

> [!NOTE]
>
> The `--provenance=mode=max` and `--sbom=true` flags are required so that
> Docker Scout can trace the DHI base image lineage and correctly apply its
> VEX statements. Enabling the containerd image store via
> `docker/setup-docker-action` allows BuildKit to store attestations locally
> without pushing to a registry first. Without the containerd image store,
> Docker Engine rejects the build with: `Attestation is not supported for the docker driver. 
> Switch to a different driver, or turn on the containerd image store, and try again.`
> The `Push image` step runs only if the scan passes, using `if: success()`
> to ensure images are only pushed to the registry when they are free of
> critical or high-severity vulnerabilities.

For more details on using Docker Scout in CI, see [Integrating Docker
Scout with other systems](/manuals/scout/integrations/_index.md).

