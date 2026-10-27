---
title: How-tos
description: Step-by-step guidance for working with Docker Hardened Images, from discovery to governance.
weight: 20
aliases:
  - /dhi/how-to/manage/
params:
  grid_discover:
    - title: Search and evaluate Docker Hardened Images
      description: Learn how to find and evaluate image repositories, variants, metadata, and attestations in the DHI catalog on Docker Hub.
      icon: travel_explore
      link: /dhi/how-to/explore/
  grid_adopt:
    - title: Get started with DHI Select and Enterprise
      description: Learn how to mirror repositories, customize images, and access compliance variants with DHI Select and Enterprise subscriptions.
      icon: rocket_launch
      link: /dhi/how-to/select-enterprise/
    - title: Use the DHI CLI
      description: Use the dhictl command-line tool to manage and interact with Docker Hardened Images.
      icon: terminal
      link: /dhi/how-to/cli/
    - title: Mirror a Docker Hardened Image repository
      description: Learn how to mirror an image into your organization's namespace and optionally push it to another private registry.
      icon: compare_arrows
      link: /dhi/how-to/mirror/
    - title: Customize a Docker Hardened Image or chart
      description: Learn how to customize Docker Hardened Images and charts.
      icon: settings
      link: /dhi/how-to/customize/
    - title: Use hardened system packages
      description: Learn how to use Docker's hardened system packages in your images.
      icon: inventory_2
      link: /dhi/how-to/hardened-packages/
    - title: Use a Docker Hardened Image
      description: Learn how to pull, run, and reference Docker Hardened Images in Dockerfiles, CI pipelines, and standard development workflows.
      icon: play_arrow
      link: /dhi/how-to/use/
    - title: Use a Docker Hardened Image chart
      description: Learn how to use a Docker Hardened Image chart.
      icon: leaderboard
      link: /dhi/how-to/helm/
  grid_verify:
    - title: Verify a Docker Hardened Image or chart
      description: Use Docker Scout or cosign to verify signed attestations like SBOMs, provenance, and vulnerability data for Docker Hardened Images and charts.
      icon: check_circle
      link: /dhi/how-to/verify/
    - title: Scan Docker Hardened Images
      description: Learn how to scan Docker Hardened Images for known vulnerabilities using Docker Scout, Grype, or Trivy.
      icon: bug_report
      link: /dhi/how-to/scan/
  grid_govern:
    - title: Enforce Docker Hardened Image usage with policies
      description: Learn how to use image policies with Docker Scout for Docker Hardened Images.
      icon: policy
      link: /dhi/how-to/policies/
---

This section provides practical, task-based guidance for working with Docker
Hardened Images (DHIs). Whether you're evaluating DHIs for the first time or
integrating them into a production CI/CD pipeline, these topics cover the key
tasks across the adoption journey: discover, adopt, verify, and govern.

The topics are organized around the typical lifecycle of working with DHIs, but
you can use them as needed based on your specific workflow.

Explore the topics below that match your current needs.

## Discover

Explore available images and metadata in the DHI catalog.

{{< grid
  items="grid_discover"
>}}

## Adopt

Mirror trusted images, customize as needed, and integrate into your workflows.

{{< grid
  items="grid_adopt"
>}}

## Verify

Check signatures, SBOMs, and provenance, and scan for vulnerabilities.

{{< grid
  items="grid_verify"
>}}

## Govern

Enforce policies to maintain security and compliance.

{{< grid
  items="grid_govern"
>}}

## Task directory

### Image use and comparison

- [Authenticate to dhi.io](authenticate.md)
- [Pull, run, and reference images](pull-run.md)
- [Build application images with dev and static variants](build-app-images.md)
- [Compare images](compare-images.md)
- [Use compliance and ELS variants](compliance-variants.md)
- [Create and test Kubernetes pull secrets](kubernetes.md)
- [View and pull images by digest](use-digests.md)

### Definitions and local builds

- [Build the Alpine catalog and minimal examples](build.md)
- [Definition field reference](definition-reference.md)
- [Build, inspect, and publish a definition](build-definition.md)
- [Build Debian Redis with third-party repositories](build-debian.md)
- [Build Nginx with shell pipeline stages](build-nginx.md)
- [Create dev and compatibility variants](build-variants.md)
- [Contribute definitions to the catalog](contribute-definitions.md)

### Mirroring and customization

- [Mirror to a Docker Hub organization](mirror-hub.md)
- [Mirror images, charts, and attestations to another registry](mirror-registry.md)
- [Customize an image](customize-image.md)
- [Customize a Helm chart](customize-chart.md)
- [Create OCI artifact images](create-oci-artifacts.md)
- [Monitor customization builds](monitor-customizations.md)
- [Edit or delete customizations](manage-customizations.md)

### Packages and compliance

- [Configure the public package repository](packages-public.md)
- [Configure the enterprise package repository](packages-enterprise.md)
- [Inspect and verify packages and package attestations](verify-packages.md)
- [Find CIS-compliant images](find-cis.md)
- [Use FIPS images and inspect attestations](use-fips.md)
- [Use STIG images and extract reports](use-stig.md)

### Attestation tasks

- [Discover attestations with ORAS](discover-attestations.md)
- [Retrieve and verify image attestations](verify-attestations.md)
- [Verify chart attestations](verify-charts.md)
- [View and verify SBOMs](verify-sbom.md)
- [Get and verify SLSA provenance](verify-slsa.md)
- [View and verify code signatures](verify-signatures.md)
- [Sign application images](sign-images.md)
- [View and verify test results](verify-tests.md)
- [View and verify malware reports](verify-malware.md)

### Scanner tasks

- [Scan with Docker Scout](scan-docker-scout.md)
- [Scan with Grype](scan-grype.md)
- [Scan with Trivy](scan-trivy.md)
- [Scan with Wiz](scan-wiz.md)
- [Scan with Mend.io](scan-mend.md)
- [Export VEX attestations](export-vex.md)
- [Build child images and apply VEX](scan-child-images.md)
- [Scan in GitHub Actions](scan-ci.md)

### Debugging and OpenShift

- [Debug locally](debug.md)
- [Resolve runtime and build issues](runtime-issues.md)
- [OpenShift prerequisites and task guide](/guides/dhi-openshift/)
- [Configure OpenShift image pulls](openshift-pull.md)
- [Prepare OpenShift file permissions](openshift-permissions.md)
- [Deploy Nginx on OpenShift](openshift-nginx.md)
- [Deploy Node.js on OpenShift](openshift-node.md)
- [Handle arbitrary and fixed OpenShift UIDs](openshift-users.md)
- [Use and debug dev variants on OpenShift](openshift-debug.md)
- [Deploy Helm charts on OpenShift](openshift-helm.md)
- [Verify an OpenShift deployment](openshift-verify.md)
- [Troubleshoot OpenShift](openshift-troubleshoot.md)
