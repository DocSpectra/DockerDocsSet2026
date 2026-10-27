---
title: Create and distribute admin-settings.json
---

For Settings Management context, see [Policies and constraints](policy-model.md).

You can create the `admin-settings.json` file in two ways:

- Use the `--admin-settings` installer flag to auto-generate the file:
  - [Mac](/manuals/desktop/setup/install/mac-install.md#install-from-the-command-line) installation guide
  - [Windows](/manuals/desktop/setup/install/windows-install.md#install-from-the-command-line) installation guide
- Create it manually (UTF-8 without BOM) and place it in the following locations:
  - Mac: `/Library/Application\ Support/com.docker.docker/admin-settings.json`
  - Windows: `C:\ProgramData\DockerDesktop\admin-settings.json`
  - Linux: `/usr/share/docker-desktop/admin-settings.json`

> [!IMPORTANT]
>
> Place the file in a protected directory to prevent unauthorized changes. Use Mobile Device Management (MDM) tools like Jamf to distribute the file at scale across your organization.
