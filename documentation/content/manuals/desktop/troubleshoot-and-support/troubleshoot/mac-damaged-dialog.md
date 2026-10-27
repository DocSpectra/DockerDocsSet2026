---
description: Fix "Docker.app is damaged and can't be opened. You should move it to the Trash" dialog on macOS
keywords: docker desktop mac, damaged app, move to trash, gatekeeper, installation issues, troubleshooting
title: Fix "Docker.app is damaged and can't be opened" on macOS
linkTitle: MacOS app damaged dialog
tags: [Troubleshooting]
weight: 30
---

## Error message

macOS shows the following dialog when you try to open Docker Desktop:

```text
Docker.app is damaged and can't be opened. You should move it to the Trash.
```

This error prevents Docker Desktop from launching and can occur during installation or after updates.

## Possible cause

This issue occurs due to a non-atomic copy during a drag/drop installation. When you drag and drop `Docker.app` from a DMG file while another application, like VS Code, is invoking the Docker CLI through symlinks, the copy operation may be interrupted, leaving the app in a partially copied state that Gatekeeper marks as "damaged".

## Solution

Follow [Recover a partial Docker Desktop installation on Mac](/manuals/desktop/setup/install/mac-reinstall.md) to quit third-party software, remove the partial installation, and reinstall.

### If the dialog persists

If you continue to see the "damaged" dialog after following the recovery steps:

1. Gather diagnostics using the terminal. Follow the instructions in [Diagnose from the terminal](/manuals/desktop/troubleshoot-and-support/troubleshoot/diagnostics.md#diagnose-from-the-terminal).

   - Note down the your diagnostics ID displayed in the terminal after running diagnostics.

2. [Use your diagnostics ID to get help](diagnostics.md#use-your-diagnostics-id-to-get-help), including the ID noted in step 1.

## Prevention

Review [Prepare to install or update Docker Desktop on Mac](/manuals/desktop/setup/install/mac-preparation.md) for in-app updates, background applications, managed installations, and installer volumes.

## Related information

- [Install Docker Desktop on Mac](/manuals/desktop/setup/install/mac-interactive.md)
- [PKG installer documentation](/manuals/enterprise/enterprise-deployment/pkg-install-and-configure.md)
- [Troubleshoot Docker Desktop](/manuals/desktop/troubleshoot-and-support/troubleshoot/_index.md)
- [Known issues](/manuals/desktop/troubleshoot-and-support/troubleshoot/known-issues.md)
