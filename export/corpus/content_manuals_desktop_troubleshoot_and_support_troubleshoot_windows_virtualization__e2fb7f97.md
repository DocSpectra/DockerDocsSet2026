---
title: "Docker Desktop fails due to Virtualization not working"
tags: [Troubleshooting]
---

Platform scope: Windows.

## Error message

A typical error message is "Docker Desktop - Unexpected WSL error" mentioning the error code
`Wsl/Service/RegisterDistro/CreateVm/HCS/HCS_E_HYPERV_NOT_INSTALLED`. Manually executing `wsl` commands
also fails with the same error code.

## Cause

- Virtualization settings are disabled in the BIOS.
- Windows Hyper-V or WSL 2 components are missing.

Note some third-party software such as Android emulators will disable Hyper-V on install.

## Solutions

Follow [Set up Windows virtualization for Docker Desktop](/manuals/desktop/setup/install/windows-virtualization.md) for WSL 2, Hyper-V, BIOS virtualization, hypervisor startup, and nested virtualization checks.

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
