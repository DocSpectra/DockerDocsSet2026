---
title: Image Access Management
description: Control which Docker Hub images developers can access with Image Access Management for enhanced supply chain security
keywords: image access management, docker official images, verified publisher, supply chain security, docker business, allow list, image restrictions, pull restrictions
tags: [admin]
aliases:
 - /docker-hub/image-access-management/
 - /desktop/hardened-desktop/image-access-management/
 - /admin/organization/image-access/
 - /security/for-admins/image-access-management/
 - /security/for-admins/hardened-desktop/image-access-management/
weight: 50
---

{{< summary-bar feature_name="Hardened Docker Desktop" >}}

For image categories, repository allowlists, and policy scope, review [Image controls](image-registry-controls.md#image-controls).

## Prerequisites

Review the [shared image and registry control prerequisites](image-registry-controls.md#shared-prerequisites).

## Configure image access

> [!NOTE]
>
> Image Access Management is turned off by default for organization members. Organization owners always have access to all images regardless of policy settings.

To configure Image Access Management:

1. Sign in to [Docker Home](https://app.docker.com) and select your organization from the top-left account drop-down.
1. Select **Admin Console**, then **Image access**.
1. Use the **toggle** to enable image access.
1. Select which image types to allow:
    - **Organization images**: Images from your organization (always allowed by default). These can be public or private images created by members within your organization.
    - **Community images**: Images contributed by various users that may pose security risks. This category includes Docker-Sponsored Open Source images and is turned off by default.
    - **Docker Verified Publisher Images**: Images from Docker partners in the Verified Publisher program, qualified for secure supply chains.
    - **Docker Official Images**: Curated Docker repositories that provide OS repositories, best practices for Dockerfiles, drop-in solutions, and timely security updates.
    - **Repository allowlist**: A list of specific repositories that should be
      allowed. Configure in the next step.
1. If **Repository allowlist** is enabled in the previous step,
   you can add or remove specific repositories in the allow list:
    - To add repositories, in the **Repository allowlist** section, select
      **Add repositories to allowlist** and follow the on-screen instructions.
    - To remove a repository, in the **Repository allowlist** section, select
      the trashcan icon next to it.

    Repositories in the allow list are accessible to all organization members regardless of the image type restrictions configured in the previous steps.

After restrictions are applied, organization members can view the permissions page in read-only format.

## Verify access restrictions

After configuring Image Access Management, test that restrictions work correctly.

When developers pull allowed image types:

```console
$ docker pull nginx  # Docker Official Image
# Pull succeeds if Docker Official Images are allowed
```

When developers pull blocked image types:

```console
$ docker pull someuser/custom-image  # Community image
Error response from daemon: image access denied: community images not allowed
```

Image access restrictions apply to all Docker Hub operations including pulls, builds using `FROM` instructions, and Docker Compose services.

## Best practices

Review [Image Access Management best practices](image-registry-controls.md#best-practices).

## Scope and bypass considerations

Review [Scope and bypass considerations](image-registry-controls.md#scope-and-bypass-considerations).

## Next steps

Review [Layer security controls](image-registry-controls.md#layer-security-controls).
