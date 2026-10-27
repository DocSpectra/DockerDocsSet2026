---
title: "Permissions errors on data directories for shared volumes"
tags: [Troubleshooting]
---

Platform scope: Windows.

## Cause 

When sharing files from Windows, Docker Desktop sets permissions on [shared volumes](/manuals/desktop/settings-and-maintenance/settings.md#file-sharing)
to a default value of [0777](https://chmodcommand.com/chmod-0777/)
(`read`, `write`, `execute` permissions for `user` and for `group`).

The default permissions on shared volumes are not configurable. 

## Solution

If you are
working with applications that require different permissions, either:
 - Use non-host-mounted volumes  
 - Find a way to make the applications work with the default file permissions

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
