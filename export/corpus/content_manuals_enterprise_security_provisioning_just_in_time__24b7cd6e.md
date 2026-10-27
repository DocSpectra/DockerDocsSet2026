---
description: Learn how Just-in-Time provisioning works with your SSO connection.
keywords: user provisioning, just-in-time provisioning, JIT, autoprovision, Docker Admin, admin, security
title: Just-in-Time provisioning
linkTitle: Just-in-Time
weight: 20
aliases:
  - /security/for-admins/provisioning/just-in-time/
---

{{< summary-bar feature_name="SSO" >}}

Just-in-Time (JIT) provisioning streamlines user onboarding by automatically creating and updating user accounts during SSO authentication. This eliminates manual account creation and ensures users have immediate access to your organization's resources. JIT verifies that users belong to the organization and assigns them to the appropriate teams based on your identity provider (IdP) configuration. When you create your SSO connection, JIT provisioning is turned on by default.

This page explains how JIT provisioning works, SSO authentication flows, and how to disable JIT provisioning.

## Prerequisites

Review the [prerequisites for SSO provisioning](/manuals/enterprise/security/provisioning/sso-prerequisites.md).

## SSO authentication with JIT provisioning enabled

See [SSO authentication with JIT enabled](jit-behavior.md#sso-authentication-with-jit-provisioning-enabled).

## SSO authentication with JIT provisioning disabled

See [SSO authentication with JIT disabled](jit-behavior.md#sso-authentication-with-jit-provisioning-disabled).

## Disable JIT provisioning

Follow [Disable JIT provisioning](disable-jit.md), including the access-disruption warning and SCIM requirements.

## Next steps

- Configure [SCIM provisioning](/manuals/enterprise/security/provisioning/scim/_index.md) for advanced user management.
- Set up [group mapping](/manuals/enterprise/security/provisioning/scim/group-mapping.md) to automatically assign users to teams.
- Review [Troubleshoot provisioning](/manuals/enterprise/security/provisioning/troubleshoot-provisioning.md).
