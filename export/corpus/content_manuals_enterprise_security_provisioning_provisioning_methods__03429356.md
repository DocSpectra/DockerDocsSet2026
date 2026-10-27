---
title: User provisioning methods and defaults
---

## What is provisioning?

Provisioning helps manage users by automating tasks like account creation, updates, and deactivation based on data from your identity provider (IdP). There are several methods for user provisioning, each offering benefits for different organizational needs:

| Provisioning method | Description | Default setting in Docker | Recommended for |
| :--- | :--- | :------------- | :--- |
| System for Cross-domain Identity Management (SCIM) | Continuously syncs user data between your IdP and Docker, ensuring user attributes remain updated without manual intervention | Disabled by default | Larger organizations or environments with frequent changes in user information or roles |
| Group mapping | Maps user groups from your IdP to specific roles and permissions within Docker, enabling fine-grained access control based on group membership | Disabled by default | Organizations requiring strict access control and role-based user management |
| Just-in-Time (JIT) | Automatically creates and provisions user accounts when they first sign in via SSO | Enabled by default | Organizations needing minimal setup, smaller teams, or low-security environments |
| Auto-provision | Adds users when email addresses match a verified domain | Disabled by default | Orgs without SSO that need to add existing Docker users by domain |

## Default provisioning setup

By default, Docker enables JIT provisioning when you configure an SSO connection. With JIT enabled, user accounts are automatically created the first time a user signs in using your SSO flow.

JIT provisioning may not provide sufficient control or security for some organizations. In such cases, SCIM or group mapping can be configured to give administrators more control over user access and attributes.

## Provisioning with SSO

Docker automatically provisions users through Just-in-Time (JIT) provisioning when they sign in via SSO. You can also manually manage users and configure different provisioning methods.

### How provisioning works

Docker supports the following provisioning methods:

- JIT provisioning (default): Users are automatically added to your organization
when they sign in via SSO
- SCIM provisioning: Sync users and groups from your identity provider to Docker
- Group mapping: Sync user groups from your identity provider with teams in your Docker organization
- Manual provisioning: Turn off automatic provisioning and manually invite users

For supported attributes, see [SSO attributes](sso-attributes.md).

