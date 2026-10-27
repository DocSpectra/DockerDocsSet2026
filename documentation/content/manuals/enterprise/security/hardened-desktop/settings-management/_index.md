---
description: Understand how Settings Management works, who it's for, and the benefits it provides
keywords: Settings Management, rootless, docker desktop, hardened desktop, admin control, enterprise
tags: [admin]
title: Settings Management
linkTitle: Settings Management
aliases:
  - /desktop/hardened-desktop/settings-management/
  - /security/for-admins/hardened-desktop/settings-management/
weight: 10
---

{{< summary-bar feature_name="Hardened Docker Desktop" >}}

Settings Management lets administrators configure and enforce Docker Desktop settings across end-user machines. It helps maintain consistent configurations and enhances security within your organization.

## Policy context

Review [Settings Management policies and constraints](policy-model.md) for configuration methods, precedence, developer experience, and limitations.

## Set up Settings Management

You can create settings management policies at any time, but your organization needs to verify a domain before the policies take effect.

1. Check that you have [added and verified](/manuals/enterprise/security/domain-management.md#add-and-verify-a-domain) your organization's domain.
2. [Enforce sign-in](/manuals/enterprise/security/enforce-sign-in/_index.md) to
   ensure all developers authenticate with your organization.
3. Choose a configuration method:
   - Use the `--admin-settings` installer flag on [macOS](/manuals/desktop/setup/install/mac-install.md#install-from-the-command-line) or [Windows](/manuals/desktop/setup/install/windows-install.md#install-from-the-command-line) to automatically create the `admin-settings.json`.
   - Manually create and configure the [`admin-settings.json` file](/manuals/enterprise/security/hardened-desktop/settings-management/configure-json-file.md).
   - Create a settings policy in the [Docker Admin Console](configure-admin-console.md).

After configuration, follow [Apply and inspect managed settings](apply-settings.md).

> [!NOTE]
>
> Docker Desktop doesn't automatically prompt users to restart or re-authenticate after a settings change. You may need to communicate these requirements to your developers.

## Developer experience

See [Developer experience](policy-model.md#developer-experience).

## View applied settings

See [View applied settings](apply-settings.md#view-applied-settings).

## Limitations

See [Settings Management limitations](policy-model.md#limitations).

## Next steps

Get started with Settings Management:

- [Configure Settings Management with the `admin-settings.json` file](configure-json-file.md)
- [Configure Settings Management with the Docker Admin Console](configure-admin-console.md)
