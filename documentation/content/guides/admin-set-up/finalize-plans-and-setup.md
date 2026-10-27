---
title: Finalize plans and begin setup
description: Collaborate with your MDM team to distribute configurations and set up SSO and Docker product trials.
weight: 20
---

Review [rollout features and stakeholders](rollout-context.md) and [Settings Management policies and constraints](/manuals/enterprise/security/hardened-desktop/settings-management/policy-model.md).

## Send finalized settings files to the MDM team

After reaching an agreement with the relevant teams about your baseline and
security configurations as outlined in the previous section, configure Settings Management using either the [Docker Admin Console](/manuals/enterprise/security/hardened-desktop/settings-management/configure-admin-console.md) or an
[`admin-settings.json` file](/manuals/enterprise/security/hardened-desktop/settings-management/configure-json-file.md).

Once the file is ready, collaborate with your MDM team to deploy your chosen
settings, along with your chosen method for [enforcing sign-in](/manuals/enterprise/security/enforce-sign-in/_index.md).

> [!IMPORTANT]
>
> Test this first with a small number of Docker Desktop developers to verify the functionality works as expected before deploying more widely.

## Manage your organizations

If you have more than one organization, consider either [consolidating them
into one organization](/manuals/admin/organization/setup/orgs.md) or creating a
[Docker company](/manuals/admin/company/_index.md) to manage multiple
organizations.

## Begin setup

### Set up single sign-on and domain verification

Single sign-on (SSO) lets developers authenticate using their identity
providers (IdPs) to access Docker. SSO is available for a whole company and all associated organizations, or an individual organization that has a Docker
Business subscription. For more information, see the
[documentation](/manuals/enterprise/security/single-sign-on/_index.md).

You can also enable [SCIM](/manuals/enterprise/security/provisioning/scim/_index.md)
for further automation of provisioning and deprovisioning of users.

### Set up Docker product entitlements included in the subscription

Review [Docker product entitlements in the rollout](subscription-products.md) for Docker Build Cloud, Docker Scout, Testcontainers Cloud, and Docker Hardened Images setup links.

### Ensure you're running a supported version of Docker Desktop

> [!WARNING]
>
> This step could affect the experience for users on older versions of Docker
> Desktop.

Follow [Plan Docker Desktop versions for a rollout](/manuals/enterprise/enterprise-deployment/supported-desktop-versions.md).
