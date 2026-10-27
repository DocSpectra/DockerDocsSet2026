---
title: Sign-in enforcement precedence and troubleshooting
---

## Method precedence

When multiple configuration methods exist on the same system, Docker Desktop uses this precedence order:

1. Registry key (Windows only)
1. Configuration profiles (Mac only)
1. plist file (Mac only)
1. registry.json file

## Troubleshoot sign-in enforcement

If sign-in enforcement doesn't work:

- Verify file locations and permissions
- Check that organization names use lowercase letters
- Restart Docker Desktop or reboot the system
- Confirm users are members of the specified organizations
- Update Docker Desktop to the latest version
