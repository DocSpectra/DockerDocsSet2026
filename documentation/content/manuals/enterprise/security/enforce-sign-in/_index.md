---
title: Enforce sign-in for Docker Desktop
linkTitle: Enforce sign-in
description: Require users to sign in to Docker Desktop to access organization benefits and security features
toc_max: 2
keywords: authentication, registry.json, configure, enforce sign-in, docker desktop, security, .plist, registry key, mac, windows, organization
tags: [admin]
aliases:
 - /security/for-admins/configure-sign-in/
 - /docker-hub/configure-sign-in/
 - /security/for-admins/enforce-sign-in/
weight: 30
---

{{< summary-bar feature_name="Enforce sign-in" >}}

By default, users can access Docker Desktop without signing in to your organization.
When users don't sign in as organization members, they miss out on subscription benefits and can bypass security features configured for your organization.

You can enforce sign-in using several methods, depending on your setup:

- [Registry key method (Windows only)](windows-registry.md)
- [Configuration profiles method (Mac only)](mac-profiles.md)
- [`.plist` method (Mac only)](mac-plist.md)
- [`registry.json` method (All)](registry-json.md)

This page provides an overview of how sign-in enforcement works.

## How sign-in enforcement works

See [Docker Desktop sign-in and SSO enforcement](enforcement-model.md) for prompt behavior, CLI scope, and the enforcement comparison.

## Enforcing sign-in versus enforcing single sign-on (SSO)

See the [enforcement comparison](enforcement-model.md#enforcing-sign-in-versus-enforcing-single-sign-on-sso).

## Next steps

- To set up sign-in enforcement, see [Configure sign-in enforcement](/manuals/enterprise/security/enforce-sign-in/methods.md).
- To configure SSO enforcement, see [Enforce SSO](/manuals/enterprise/security/single-sign-on/connect.md).
