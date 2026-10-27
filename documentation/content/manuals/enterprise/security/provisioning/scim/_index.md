---
title: SCIM overview
linkTitle: SCIM
weight: 10
description: Learn how System for Cross-domain Identity Management works and how to set it up.
keywords: SCIM, SSO, user provisioning, de-provisioning, role mapping, assign users
aliases:
  - /security/for-admins/scim/
  - /docker-hub/scim/
  - /security/for-admins/provisioning/scim/
---

{{< summary-bar feature_name="SSO" >}}

Automate user management for your Docker organization using System for
Cross-domain Identity Management (SCIM). SCIM automatically provisions and
de-provisions users, synchronizes team memberships, and keeps your Docker
organization in sync with your identity provider.

This page shows you how to automate user provisioning and de-provisioning for
Docker using SCIM.

## Prerequisites

Review the [prerequisites for SSO provisioning](/manuals/enterprise/security/provisioning/sso-prerequisites.md).

## How SCIM works

Review [SCIM user lifecycle and limits](scim-context.md).

## Set up SCIM

Follow [Set up SCIM provisioning](provision-scim.md).

## Next steps

- [Migrate JIT to SCIM](/manuals/enterprise/security/provisioning/scim/migrate-scim.md) if users were provisioned with Just-in-Time (JIT) before you enabled SCIM.
- [Group mapping](/manuals/enterprise/security/provisioning/scim/group-mapping.md) to sync identity provider groups with members.
- [Troubleshoot provisioning](/manuals/enterprise/security/provisioning/troubleshoot-provisioning.md) for SCIM, JIT, and attribute issues.
