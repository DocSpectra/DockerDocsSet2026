---
title: "`Docker Desktop Access Denied` error message when starting Docker Desktop"
tags: [Troubleshooting]
---

Platform scope: Windows.

## Error message

When starting Docker Desktop, the following error appears:

```text
Docker Desktop - Access Denied
```

## Cause

The user is not part of the `docker-users` group, which is required for permissions.

## Solution

If your admin account is different to your user account, follow [Add a user to docker-users](/manuals/desktop/setup/install/windows-permission-requirements.md#add-a-user-to-docker-users).

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
