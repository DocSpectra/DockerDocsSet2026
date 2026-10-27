---
title: Docker Hardened Images
description: Secure, minimal, and production-ready base images
weight: 8
params:
  sidebar:
    group: Products
    badge:
      color: green
      text: New
  grid_sections:
    - title: Quickstart
      description: Follow a step-by-step guide to explore and run a Docker Hardened Image.
      icon: rocket_launch
      link: /dhi/get-started/
    - title: Explore
      description: Learn what Docker Hardened Images are, how they're built, and what sets them apart from typical base images.
      icon: info
      link: /dhi/explore/
    - title: Features
      description: Discover the security, compliance, and enterprise-readiness features built into Docker Hardened Images.
      icon: lock
      link: /dhi/features/
    - title: How-tos
      description: Step-by-step guides for using, verifying, scanning, and migrating to Docker Hardened Images.
      icon: play_arrow
      link: /dhi/how-to/
    - title: Core concepts
      description: Understand the secure supply chain principles that make Docker Hardened Images production-ready.
      icon: fact_check
      link: /dhi/core-concepts/
    - title: Troubleshoot
      description: Resolve common issues with building, running, or debugging Docker Hardened Images.
      icon: help_center
      link: /dhi/troubleshoot/
    - title: Additional resources
      description: Guides, blog posts, Docker Hub catalog, GitHub repositories, and more.
      icon: link
      link: /dhi/resources/
---

Docker Hardened Images (DHI) provide minimal, secure, and production-ready
container images, Helm charts, and system packages maintained by Docker.
Designed to reduce vulnerabilities and simplify compliance, DHI integrates
easily into your existing Docker-based workflows with little to no retooling
required.

## Choose a task

| Task | Start here |
|---|---|
| Pull and run a Community image | [Quickstart](./get-started.md) |
| Set up Select or Enterprise | [Subscription prerequisites and walkthrough](./how-to/select-enterprise.md) |
| Choose an image or variant | [Search and evaluate](./how-to/explore.md), [image types](./explore/available.md) |
| Migrate an application | [Migration checklist](./migration/checklist.md), [migration paths](./migration/_index.md) |
| Build from a YAML definition | [Create and build an image](./how-to/build.md) |
| Customize a mirrored image or chart | [Customize](./how-to/customize.md) |
| Deploy to Kubernetes or OpenShift | [Kubernetes](./how-to/kubernetes.md), [Helm](./how-to/helm.md), [OpenShift](/guides/dhi-openshift/) |
| Inspect security evidence or vulnerabilities | [Verify](./how-to/verify.md), [scan](./how-to/scan.md), [scan child images and CI builds](./how-to/scan-child-images.md) |
| Resolve a build or runtime issue | [Troubleshoot](./troubleshoot.md) |

## Compare subscriptions

DHI is available in the following three subscriptions.

| Feature | Community | Select | Enterprise |
|---|---|---|---|
| Hardened, minimal images | ✅ | ✅ | ✅ |
| Near-zero CVEs | ✅ | ✅ | ✅ |
| Verifiable SBOMs & SLSA Build L3 provenance | ✅ | ✅ | ✅ |
| Full, unsuppressed CVE visibility | ✅ | ✅ | ✅ |
| Drop-in adoption, no workflow changes | ✅ | ✅ | ✅ |
| Full catalog of open source images under Apache 2.0 | ✅ | ✅ | ✅ |
| Built with Docker Hardened System Packages | ✅ | ✅ | ✅ |
| Upstream cadence for Docker-released patches | ✅ | ✅ | ✅ |
| FIPS/STIG variants | ❌ | ✅ | ✅ |
| Critical CVE fixes < 7 days with SLA-backed continuous patching | ❌ | ✅ | ✅ |
| Customizations | ❌ | Up to 5 | Unlimited |
| Access to Hardened System Packages repository | ❌ | ❌ | ✅ |
| Full catalog access available | ❌ | ❌ | ✅ |
| Extended Lifecycle Support add-on available | ❌ | ❌ | ✅<br><br>Includes:<br>✅ +5 years of hardened updates<br>✅ Maintains security updates after upstream EOL<br>✅ SBOMs & provenance<br>✅ Protects long-lived workloads |

For pricing and more details, see the [Docker Hardened Images subscription
comparison](https://www.docker.com/products/hardened-images/#compare).

## Browse the documentation

Explore the sections below to get started with Docker Hardened Images, integrate
them into your workflow, and learn what makes them secure and enterprise-ready.

{{< grid
  items="grid_sections"
>}}
