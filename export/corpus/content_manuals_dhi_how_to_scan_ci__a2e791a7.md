---
title: Scan DHI application images in GitHub Actions
description: Build, scan, and conditionally push DHI-based images with Docker Scout.
---

Before using this workflow, review [child-image provenance requirements](scan-child-images.md) and [DHI in CI/CD pipelines](../core-concepts/ci.md).

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
