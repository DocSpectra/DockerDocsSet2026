---
title: "Recover a partial Docker Desktop installation on Mac"
---

Follow these steps to resolve the issue:

## Step one: Quit third-party software

Close any applications that might call Docker in the background:

- Visual Studio Code and other IDEs
- Terminal applications
- Agent apps or development tools
- Any scripts or processes that use the Docker CLI

## Step two: Remove any partial installation

1. Move `/Applications/Docker.app` to Trash and empty Trash.
2. If you used a DMG installer, eject and re-mount the Docker DMG.

## Step three: Reinstall Docker Desktop

Follow the instructions in the [macOS installation guide](/manuals/desktop/setup/install/mac-interactive.md) to reinstall Docker Desktop.
