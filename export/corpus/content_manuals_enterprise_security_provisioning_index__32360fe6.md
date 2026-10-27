---
description: Learn about provisioning users for your SSO configuration.
keywords: provision users, provisioning, JIT, SCIM, group mapping, sso, docker admin, admin, security
title: Provision users
linkTitle: Provision
weight: 20
aliases:
 - /security/for-admins/provisioning/
grid:
  - title: "SCIM provisioning"
    description: "Enable continuous user data synchronization between your IdP and Docker. Best for larger organizations."
    icon: "sync"
    link: "scim/"
  - title: "Just-in-Time (JIT) provisioning"
    description: "Set up automatic user creation on first sign-in. Ideal for smaller teams with minimal setup requirements."
    icon: "schedule"
    link: "just-in-time/"
  - title: "Auto-provisioning"
    description: "Associate members to an organization when email addresses match a verified domain."
    icon: "group"
    link: "auto-provisioning/"
---

{{< summary-bar feature_name="SSO" >}}

After configuring your SSO connection, the next step is to provision users. This process ensures that users can access your organization through automated user management.

This page provides an overview of user provisioning and the supported provisioning methods.

## What is provisioning?

Review [User provisioning methods and defaults](provisioning-methods.md).

## Default provisioning setup

See [Default provisioning setup](provisioning-methods.md#default-provisioning-setup).

## SSO attributes

See [SSO attributes](sso-attributes.md#sso-attributes), including session duration and default timeouts.

## SAML attribute mapping

See [SAML attribute mapping](sso-attributes.md#saml-attribute-mapping).

## Next steps

Choose the provisioning method that best fits your organization's needs:

{{< grid >}}
