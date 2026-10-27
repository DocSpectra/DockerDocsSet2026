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

Choose a task:

- Scan a DHI with [Docker Scout](#docker-scout), [Grype](#grype), [Trivy](#trivy), [Wiz](#wiz), or [Mend.io](#mendio)
- [Export VEX attestations](#export-vex-attestations), including CLI version and registry-access requirements
- [Build and scan child images](./scan-child-images.md)
- [Automate scanning in CI/CD](./scan-child-images.md#automate-dhi-scanning-in-cicd-with-docker-scout)

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

Docker Scout is integrated into Docker Desktop and the Docker CLI. It provides
vulnerability insights, CVE summaries, and direct links to remediation guidance.

### Scan a DHI using Docker Scout

To scan a Docker Hardened Image using Docker Scout, run the following
command:

```console
$ docker login dhi.io
$ docker scout cves dhi.io/<image>:<tag> --platform <platform>
```

Example output:

```plaintext
    v SBOM obtained from attestation, 101 packages found
    v Provenance obtained from attestation
    v VEX statements obtained from attestation
    v No vulnerable package detected
    ...
```

For more detailed filtering and JSON output, see [Docker Scout CLI reference](/reference/cli/docker/scout/).

### Build child images with provenance attestations

For the required build flags, their effect on base-image VEX, and a build
command, see [Build child images with provenance
attestations](./scan-child-images.md#build-child-images-with-provenance-attestations).

### VEX attestations in child images

For a child VEX document and commands to attach it, see [VEX attestations in
child images](./scan-child-images.md#vex-attestations-in-child-images).

### Automate DHI scanning in CI/CD with Docker Scout

For the GitHub Actions workflow and its containerd image store requirements, see
[Automate DHI scanning in CI/CD with Docker
Scout](./scan-child-images.md#automate-dhi-scanning-in-cicd-with-docker-scout).

#### Example GitHub Actions workflow

See the [GitHub Actions workflow](./scan-child-images.md#example-github-actions-workflow).

## Grype

[Grype](https://github.com/anchore/grype) is an open-source scanner that checks
container images against vulnerability databases like the NVD and distro
advisories.

### Scan a DHI using Grype

To scan a Docker Hardened Image using Grype with VEX filtering, first export
the VEX attestation and then scan with the `--vex` flag:

```console
$ docker login dhi.io
$ docker pull dhi.io/<image>:<tag>
$ docker scout vex get dhi.io/<image>:<tag> --output vex.json
$ grype dhi.io/<image>:<tag> --vex vex.json
```

The `--vex` flag applies VEX statements during the scan, filtering out known
non-exploitable CVEs for accurate results.

For more information on exporting VEX attestations, see [Export VEX
attestations](#export-vex-attestations).

## Trivy

[Trivy](https://github.com/aquasecurity/trivy) is an open-source vulnerability
scanner for containers and other artifacts. It detects vulnerabilities in OS
packages and application dependencies.

### Scan a DHI using Trivy

After installing Trivy, you can scan a Docker Hardened Image by pulling
the image and running the scan command:

```console
$ docker login dhi.io
$ docker pull dhi.io/<image>:<tag>
$ trivy image --scanners vuln dhi.io/<image>:<tag>
```

To filter vulnerabilities using VEX statements, Trivy supports multiple
approaches. Docker recommends using VEX Hub, which provides a seamless workflow
for automatically downloading and applying VEX statements from configured
repositories.

#### Using VEX Hub (recommended)

Configure Trivy to download the Docker Hardened Images advisories repository
from VEX Hub. Run the following commands to set up the VEX repository:

```console
$ trivy vex repo init
$ cat << REPO > ~/.trivy/vex/repository.yaml
repositories:
  - name: default
    url: https://github.com/aquasecurity/vexhub
    enabled: true
    username: ""
    password: ""
    token: ""
  - name: dhi-vex
    url: https://github.com/docker-hardened-images/advisories
    enabled: true
REPO
$ trivy vex repo list
$ trivy vex repo download
```

After setting up VEX Hub, you can scan a Docker Hardened Image with VEX filtering:

```console
$ docker login dhi.io
$ docker pull dhi.io/<image>:<tag>
$ trivy image --scanners vuln --vex repo dhi.io/<image>:<tag>
```

For example, scanning the `dhi.io/python:3.13` image:

```console
$ trivy image --scanners vuln --vex repo dhi.io/python:3.13
```

Example output:

```plaintext
Report Summary

┌─────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┐
│                                   Target                                    │    Type    │ Vulnerabilities │
├─────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ dhi.io/python:3.13 (debian 13.2)                                            │   debian   │        0        │
├─────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┤
│ opt/python-3.13.11/lib/python3.13/site-packages/pip-25.3.dist-info/METADATA │ python-pkg │        0        │
└─────────────────────────────────────────────────────────────────────────────┴────────────┴─────────────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)
```

The `--vex repo` flag applies VEX statements from the configured repository during the scan,
which filters out known non-exploitable CVEs.

#### Using local VEX files

In addition to VEX Hub, Trivy also supports the use of local VEX files for
vulnerability filtering. You can download the VEX attestation that Docker
Hardened Images provide and use it directly with Trivy.

First, download the VEX attestation for your image:

```console
$ docker scout vex get dhi.io/<image>:<tag> --output vex.json
```

Then scan the image with the local VEX file:

```console
$ trivy image --scanners vuln --vex vex.json dhi.io/<image>:<tag>
```

## Wiz

[Wiz](https://www.wiz.io/) is a cloud security platform that includes container
image scanning capabilities with support for DHI VEX attestations. Wiz CLI
automatically consumes VEX statements from Docker Hardened Images to provide
accurate vulnerability assessments.

### Scan a DHI using Wiz CLI

After acquiring a Wiz subscription and installing the Wiz CLI, you can scan a
Docker Hardened Image by pulling the image and running the scan command:

```console
$ docker login dhi.io
$ docker pull dhi.io/<image>:<tag>
$ wizcli scan container-image dhi.io/<image>:<tag>
```

## Mend.io

[Mend.io](https://www.mend.io/) is an application security platform that
includes container image scanning with support for DHI VEX attestations.
Mend Container automatically retrieves and applies VEX statements from Docker
Hardened Images and combines them with Mend's reachability analysis for
comprehensive vulnerability assessment.

### Scan a DHI using Mend.io

After acquiring a Mend.io subscription and configuring
[Mend Container](https://docs.mend.io/container/latest/), Mend automatically
detects Docker Hardened Images and applies their VEX data without requiring any
additional configuration. When you scan a Docker Hardened Image through the Mend
AppSec Platform, VEX statements are automatically retrieved and attached as risk
factors to each finding.

You can view and filter DHI-specific findings in the Mend AppSec Platform under
**Security > Containers > Packages**, where a Docker badge identifies hardened
image packages. Use the **Risk Factors** column to filter by VEX statuses such
as Not Affected, Fixed, or Under Investigation.

For more information, see the [Mend.io Docker Hardened Images
documentation](https://docs.mend.io/platform/latest/docker-hardened-images).

## Export VEX attestations

For scanners that need local VEX files (like Grype or Trivy with local files),
you can export the VEX attestations from Docker Hardened Images.

> [!NOTE]
>
> By default, VEX attestations are fetched from `registry.scout.docker.com`. Ensure that you can access this registry
> if your network has outbound restrictions. You can also mirror the attestations to an alternate registry. For more
> details, see [Mirror to a third-party registry](mirror.md#mirror-a-dhi-repository-to-a-third-party-registry).

Export VEX attestations to a JSON file:

```console
$ docker scout vex get dhi.io/<image>:<tag> --output vex.json
```

> [!NOTE]
>
> The `docker scout vex get` command requires [Docker Scout
> CLI](https://github.com/docker/scout-cli/) version 1.18.3 or later.
>
> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use
> `registry://docs/dhi-python:3.13` instead of `docs/dhi-python:3.13`.
