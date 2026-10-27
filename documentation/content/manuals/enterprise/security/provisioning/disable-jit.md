---
title: Disable JIT provisioning
---

> [!WARNING]
>
> Disabling JIT provisioning may disrupt your users' access and workflows. With JIT disabled, users will not be automatically added to your organization. Users must already be a member of the organization or have a pending invitation to successfully sign in through SSO. To auto-provision users with JIT disabled, [use SCIM](scim/scim-context.md).

You may want to disable JIT provisioning for reasons such as the following:

- You have multiple organizations, have SCIM enabled, and want SCIM to be the source of truth for provisioning
- You want to control and restrict usage based on your organization's security configuration, and want to use SCIM to provision access

Users are provisioned with JIT by default. If you enable SCIM, you can disable JIT:

1. Go to [Docker Home](https://app.docker.com/) and select your organization from the top-left account drop-down.
1. Select **Admin Console**, then **SSO and SCIM**.
1. In the **SSO connections** table, select the **Action** icon, then select **Disable JIT provisioning**.
1. Select **Disable** to confirm.
