---
title: Single sign-on overview
linkTitle: Single sign-on
description: Learn how single sign-on works, how to set it up, and the required SSO attributes.
keywords: Single Sign-On, SSO, sign-in, admin, docker hub, admin console, security, identity provider, SSO configuration, enterprise login, Docker Business, user authentication
aliases:
  - /single-sign-on/
  - /admin/company/settings/sso/
  - /admin/organization/security-settings/sso-management/
  - /security/for-admins/single-sign-on/
weight: 10
---

{{< summary-bar feature_name="SSO" >}}

Single sign-on (SSO) lets users access Docker by authenticating through their
identity providers (IdPs). SSO can be configured for an entire company,
including all associated organizations, or for a single organization that has a
Docker Business subscription.

## How SSO works

See [SSO authentication and user access](sso-context.md).

## Set up SSO

To configure SSO in Docker, follow these steps:

1. [Configure your domain](connect.md) by creating and verifying it.
1. [Create your SSO connection](connect.md) in Docker and your IdP.
1. Link Docker to your identity provider.
1. Test your SSO connection.
1. Provision users in Docker.
1. Optional. [Enforce sign-in](../enforce-sign-in/_index.md).
1. [Manage your SSO configuration](manage.md).

For post-setup user access and the CLI password deprecation warning, see [SSO authentication and user access](sso-context.md).

## Next steps

- Start [configuring SSO](connect.md).
- Read the [FAQs](/manuals/enterprise/security/single-sign-on/FAQs/general.md).
- [Troubleshoot](/manuals/enterprise/security/single-sign-on/troubleshoot-sso.md) SSO issues.
