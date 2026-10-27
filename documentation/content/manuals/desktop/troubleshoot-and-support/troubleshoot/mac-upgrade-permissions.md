---
title: "Upgrade requires administrator privileges"
tags: [Troubleshooting]
---

Platform scope: Mac.

## Cause 

On macOS, users without administrator privileges cannot perform in-app upgrades from the Docker Desktop Dashboard.

## Solution

> [!IMPORTANT]
>
> Do not uninstall the current version before upgrading. Doing so deletes all local Docker containers, images, and volumes.

To upgrade Docker Desktop:

- Ask an administrator to install the newer version over the existing one.
- Use the [`--user` install flag](/manuals/desktop/setup/install/installer-options.md#mac-installation-behavior) if appropriate for your setup.

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
