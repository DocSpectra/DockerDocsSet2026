---
title: Configure sign-in enforcement
linkTitle: Configure
description: Configure sign-in enforcement for Docker Desktop using registry keys, configuration profiles, plist files, or registry.json files
keywords: authentication, registry.json, configure, enforce sign-in, docker desktop, security, .plist, registry key, mac, windows, linux
tags: [admin]
aliases:
 - /security/for-admins/enforce-sign-in/methods/
---

{{< summary-bar feature_name="Enforce sign-in" >}}

You can enforce sign-in for Docker Desktop using several methods. Choose the method that best fits your organization's infrastructure and security requirements.

## Choose your method

| Method | Platform |
|:-------|:---------|
| [Registry key](windows-registry.md) | Windows only |
| [Configuration profiles](mac-profiles.md) | Mac only |
| [`plist` file](mac-plist.md) | Mac only |
| [`registry.json`](registry-json.md) | All platforms |

> [!TIP]
>
> For Mac, configuration profiles offer the highest security because they're
protected by Apple's System Integrity Protection (SIP).

## Windows: Registry key method

See the [Windows registry key procedure](windows-registry.md).

## Mac: Configuration profiles method (recommended)

See the [Mac configuration profile procedure](mac-profiles.md).

## Mac: plist file method

See the [Mac plist file procedure](mac-plist.md).

## All platforms: registry.json method

See the [`registry.json` procedure](registry-json.md).

## Method precedence

See [Method precedence](method-reference.md#method-precedence).

## Troubleshoot sign-in enforcement

See [Troubleshoot sign-in enforcement](method-reference.md#troubleshoot-sign-in-enforcement).
