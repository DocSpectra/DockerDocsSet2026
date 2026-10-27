---
title: Registry Access Management
description: Control access to approved container registries with Registry Access Management for secure Docker Desktop usage
keywords: registry access management, container registry, security controls, docker business, admin controls
tags: [admin]
aliases:
 - /desktop/hardened-desktop/registry-access-management/
 - /admin/organization/registry-access/
 - /docker-hub/registry-access-management/
 - /security/for-admins/registry-access-management/
 - /security/for-admins/hardened-desktop/registry-access-management/
weight: 40
---

{{< summary-bar feature_name="Registry access management" >}}

For supported registries and filtering scope, review [Registry controls](image-registry-controls.md#registry-controls).

## Prerequisites

Review the [shared image and registry control prerequisites](image-registry-controls.md#shared-prerequisites).

## Configure registry permissions

To configure registry permissions:

1. Sign in to [Docker Home](https://app.docker.com) and select your organization from the top-left account drop-down.
1. Select **Admin Console**, then **Registry access**.
1. Use the **toggle** to enable registry access. By default, Docker Hub is enabled
in the registry list.
1. To add additional registries, select **Add registry** and provide
a **Registry address** and **Registry nickname**.
1. Select **Create**. You can add up to 100 registries.
1. Verify your registry appears in the registry list and select **Save changes**.
   >[!NOTE]
   >
   > Policy changes can take up to 24 hours to propagate. To apply changes immediately, ask developers to sign out and back in to Docker Desktop.

If a developer belongs to multiple organizations with different RAM policies, only the policy for the first organization in the configuration file is enforced.

> [!TIP]
>
> RAM restrictions also apply to Dockerfile `ADD` instructions that fetch content via URL. Include trusted registry domains in your allowlist when using `ADD` with URLs.
>
> RAM is designed for container registries, not general-purpose URLs like package mirrors or storage services. Adding too many domains may cause errors or hit system limits.


## Verify restrictions are working

After users sign in to Docker Desktop with their organization credentials, Registry Access Management takes effect immediately.

When users try to pull from a blocked registry:

```console
$ docker pull blocked-registry.com/image:tag
Error response from daemon: registry access to blocked-registry.com is not allowed
```

Allowed registry access works normally:

```console
$ docker pull allowed-registry.com/image:tag
# Pull succeeds
```

Registry restrictions apply to all Docker operations including pulls, pushes,
and builds that reference external registries.

## Registry limits and platform constraints

See [Registry limits and platform constraints](image-registry-controls.md#registry-limits-and-platform-constraints), including build exceptions, bypass considerations, and allowlist guidance.
