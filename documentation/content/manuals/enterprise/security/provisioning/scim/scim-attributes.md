---
title: SCIM attributes and JIT precedence
---

## Supported attributes

SCIM uses attributes (name, email, etc.) to sync user information between your
identity provider and Docker. Properly mapping these attributes in your identity
provider ensures that user provisioning works smoothly and prevents issues like
duplicate user accounts
when using single sign-on.

Docker supports the following SCIM attributes:

| Attribute         | Description                                                                       |
| :---------------- | :-------------------------------------------------------------------------------- |
| `userName`        | User's primary email address, used as the unique identifier                       |
| `name.givenName`  | User's first name                                                                 |
| `name.familyName` | User's surname                                                                    |
| `active`          | Indicates if a user is enabled or disabled, set to "false" to de-provision a user |

For additional details about supported attributes and SCIM, see
[Docker Hub API SCIM reference](/reference/api/hub/latest.md#tag/scim).

> [!IMPORTANT]
>
> By default, Docker uses Just-in-Time (JIT) provisioning for SSO. If SCIM is
> enabled, JIT values still take precedence and will overwrite attribute values
> set by SCIM. To avoid conflicts, make sure your JIT attribute values match
> your SCIM values.
>
> Alternatively, you can disable JIT provisioning to rely solely on SCIM.
> For details, see [Disable JIT provisioning](/manuals/enterprise/security/provisioning/disable-jit.md).
