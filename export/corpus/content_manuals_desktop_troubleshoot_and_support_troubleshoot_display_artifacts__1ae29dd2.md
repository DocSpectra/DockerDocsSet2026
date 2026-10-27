---
title: "Docker Desktop's UI appears green, distorted, or has visual artifacts"
tags: [Troubleshooting]
---

Platform scope: All platforms.

## Cause

Docker Desktop uses hardware-accelerated graphics by default, which may cause problems for some GPUs.

## Solution

Disable hardware acceleration:

1. Edit Docker Desktop's `settings-store.json` file. You can find this file at:

   - Mac: `~/Library/Group Containers/group.com.docker/settings-store.json`
   - Windows: `C:\Users\[USERNAME]\AppData\Roaming\Docker\settings-store.json`
   - Linux: `~/.docker/desktop/settings-store.json.`

2. Add the following entry:

   ```JSON
   $ "disableHardwareAcceleration": true
   ```

3. Save the file and restart Docker Desktop.

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
