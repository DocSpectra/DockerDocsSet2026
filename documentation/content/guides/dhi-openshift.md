---
title: Use Docker Hardened Images with Red Hat OpenShift
description: Deploy Docker Hardened Images on Red Hat OpenShift Container Platform, covering Security Context Constraints, arbitrary user ID assignment, file permissions, and best practices.
summary: Learn how to deploy Docker Hardened Images (DHI) on Red Hat OpenShift, configure Security Context Constraints, handle arbitrary user ID assignment, and set file permissions for both runtime and development image variants.
keywords: docker hardened images, dhi, openshift, OCP, SCC, security context constraints, non-root, distroless, containers, red hat
tags: ["Docker Hardened Images", "dhi"]
params:
  proficiencyLevel: Intermediate
  time: 30 minutes
  prerequisites:
    - An OpenShift cluster (version 4.11 or later recommended)
    - The oc CLI authenticated to your cluster
    - A Docker Hub account with access to Docker Hardened Images
    - Familiarity with OpenShift Security Context Constraints (SCCs)
---


Docker Hardened Images (DHI) can be deployed on Red Hat OpenShift Container
Platform, but OpenShift’s security model differs from standard Kubernetes in
ways that require specific configuration. Because OpenShift runs containers
with an arbitrarily assigned user ID rather than the image’s default, you must
adjust file ownership and group permissions in your Dockerfiles to ensure
writable paths remain accessible.

This guide explains how to deploy Docker Hardened Images in OpenShift
environments, covering Security Context Constraints (SCCs), arbitrary user ID
assignment, file permission requirements, and best practices for both runtime
and development image variants.

## Prerequisites

Review the [OpenShift prerequisites](../manuals/dhi/core-concepts/openshift.md#prerequisites).

## How OpenShift security differs from Kubernetes

[Review the OpenShift security model](../manuals/dhi/core-concepts/openshift.md).

## Pull DHI images into OpenShift

[Create and link a pull secret](../manuals/dhi/how-to/openshift-pull.md).

## Build OpenShift-compatible images from DHI

[Prepare image file permissions](../manuals/dhi/how-to/openshift-permissions.md).

## Example: Nginx for OpenShift

[Deploy Nginx](../manuals/dhi/how-to/openshift-nginx.md).

## Example: Node.js application for OpenShift

[Deploy a Node.js application](../manuals/dhi/how-to/openshift-node.md).

## Handle arbitrary user IDs

[Handle arbitrary UIDs and passwd entries](../manuals/dhi/how-to/openshift-users.md).

## Use the non-root SCC for fixed UIDs

[Configure the nonroot SCC](../manuals/dhi/how-to/openshift-users.md#use-the-non-root-scc-for-fixed-uids).

## Use DHI dev variants in OpenShift

[Use dev variants and debug on the cluster](../manuals/dhi/how-to/openshift-debug.md).

## Deploy DHI Helm charts on OpenShift

[Inspect chart values and install with overrides](../manuals/dhi/how-to/openshift-helm.md).

## Verify your deployment

[Verify security configuration and scan locally](../manuals/dhi/how-to/openshift-verify.md).

## Common issues and solutions

[Troubleshoot OpenShift deployment issues](../manuals/dhi/how-to/openshift-troubleshoot.md).

## DHI and OpenShift compatibility summary

[Compare variant compatibility](../manuals/dhi/core-concepts/openshift.md#dhi-and-openshift-compatibility-summary).

## What’s next

- [Use an image in Kubernetes](/dhi/how-to/kubernetes/) — general DHI Kubernetes deployment guide.
- [Customize an image](/dhi/how-to/customize/) — add packages to DHI images using Enterprise customization.
- [Debug a container](/dhi/troubleshoot/#general-debugging) — troubleshoot distroless containers with Docker Debug (local development).
- [Managing SCCs](https://docs.openshift.com/container-platform/4.14/authentication/managing-security-context-constraints.html) — Red Hat’s reference documentation on Security Context Constraints.
- [Creating images for OpenShift](https://docs.openshift.com/container-platform/4.14/openshift_images/create-images.html) — Red Hat’s guidelines for building OpenShift-compatible container images.
