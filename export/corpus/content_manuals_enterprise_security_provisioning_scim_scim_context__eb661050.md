---
title: SCIM user lifecycle and limits
---

## How SCIM works

SCIM automates user provisioning and de-provisioning for Docker through your
identity provider. After you enable SCIM, any user assigned to your
Docker application in your identity provider is automatically provisioned and
added to your Docker organization. When a user is removed from the Docker
application in your identity provider, SCIM deactivates and removes them from
your Docker organization.

In addition to provisioning and removal, SCIM also syncs profile updates like
name changes made in your identity provider. You can use SCIM alongside Docker's
default Just-in-Time (JIT) provisioning or on its own with JIT disabled.

SCIM automates:

- Creating users
- Updating user profiles
- Removing and deactivating users
- Re-activating users
- Group mapping

> [!NOTE]
>
> SCIM only manages users provisioned through your identity provider after
> SCIM is enabled. It cannot remove users who were manually added to your Docker
> organization before SCIM was set up.
>
> To remove those users, delete them manually from your Docker organization.
> For more information, see
> [Manage organization members](/manuals/admin/organization/manage/members.md).
