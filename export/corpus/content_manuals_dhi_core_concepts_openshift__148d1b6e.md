---
title: DHI and OpenShift security constraints
description: SCC behavior, arbitrary UIDs, root-group permissions, and image variant compatibility.
---

## Prerequisites

- An OpenShift cluster (version 4.11 or later recommended)
- The `oc` CLI authenticated to your cluster
- A Docker Hub account with access to Docker Hardened Images
- Familiarity with OpenShift Security Context Constraints (SCCs)

## How OpenShift security differs from Kubernetes

OpenShift extends Kubernetes with Security Context Constraints (SCCs), which
control what actions a pod can perform and what resources it can access. While
vanilla Kubernetes uses Pod Security Standards (PSS) for similar purposes, SCCs
are more granular and enforced by default.

The key differences that affect DHI deployments:

**Arbitrary user IDs.** By default, OpenShift runs containers using an
arbitrarily assigned user ID (UID) from a range allocated to each project. The
default `restricted-v2` SCC (introduced in OpenShift 4.11) uses the
`MustRunAsRange` strategy, which overrides the `USER` directive in the container
image with a UID from the project’s allocated range (typically starting higher than
1000000000). This means even though a DHI image specifies a non-root user
(UID 65532), OpenShift will run the container as a different, unpredictable UID.

**Root group requirement.** OpenShift assigns the arbitrary UID to the root
group (GID 0). The container process always runs with `gid=0(root)`. Any
directories or files that the process needs to write to must be owned by the
root group (GID 0) with group read/write permissions. This is documented in the
[Red Hat guidelines for creating images](https://docs.openshift.com/container-platform/4.14/openshift_images/create-images.html#use-uid_create-images).

> [!IMPORTANT]
> 
> DHI images set file ownership to `nonroot:nonroot` (65532:65532) by default.
> Because the OpenShift arbitrary UID is NOT in the `nonroot` group (65532), it
> cannot write to those files — even though the pod is admitted by the SCC and
> the container starts. You must change group ownership to GID 0 for any
> writable path. This is the most common source of permission errors when
> deploying DHI on OpenShift.

**Capability restrictions.** The `restricted-v2` SCC drops all Linux
capabilities by default and enforces `allowPrivilegeEscalation: false`,
`runAsNonRoot: true`, and a `seccompProfile` of type `RuntimeDefault`. DHI
runtime images already satisfy these constraints because they run as a non-root
user and don’t require elevated capabilities.

## DHI and OpenShift compatibility summary

|Feature                      |DHI runtime                      |DHI `-dev`          |DHI with Enterprise customization|
|-----------------------------|---------------------------------|--------------------|---------------------------------|
|Default SCC (`restricted-v2`)|Yes, with GID 0 permissions      |Requires `anyuid`   |Yes, with GID 0 permissions      |
|Non-root by default          |Yes (UID 65532)                  |No (root)           |Yes (configurable UID)           |
|Arbitrary UID support        |Yes, with `chown <UID>:0`        |Yes                 |Yes, with `chown <UID>:0`        |
|Distroless (no shell)        |Yes — no `RUN` in Dockerfile     |No                  |Yes — no `RUN` in Dockerfile     |
|Unprivileged ports           |Yes (higher than 1024)                 |Configurable        |Yes (higher than 1024)                 |
|SLSA Build Level 3           |Yes                              |Yes                 |Yes                              |
|Debug on cluster             |`oc debug` / ephemeral containers|`oc exec` with shell|`oc debug` / ephemeral containers|
