---
title: WSL 2 requirements and memory reclamation
---

## Prerequisites

Before you turn on the Docker Desktop WSL 2 feature, ensure you have:

- At a minimum WSL version 2.1.5, but ideally the latest version of WSL to avoid Docker Desktop not working as expected.
- Met the Docker Desktop for Windows' [system requirements](/manuals/desktop/setup/install/windows-install.md#system-requirements).
- Installed the WSL 2 feature on Windows. For detailed instructions, refer to the [Microsoft documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

> [!TIP]
>
> Consider enabling the WSL [autoMemoryReclaim](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#experimental-settings) setting, available since WSL 1.3.10 (experimental).
>This setting allows Windows to reclaim unused memory from the WSL virtual machine, preventing the Linux kernel's page cache from holding onto large amounts of RAM after container image builds complete. The result is better memory availability for other applications on the host. 

## Keep WSL up to date

Always use the latest version of WSL. 

At a minimum you must use WSL version 2.1.5, otherwise Docker Desktop may not work as expected. Additionally, if you intend to use Enhanced Container Isolation, ensure you’re using WSL version 2.6 or later. This is required because ECI depends on a Linux kernel version of at least 6.3.0, and WSL 2.6+ bundles Linux kernel version 6.6. Testing, development, and documentation is based on the newest kernel versions. Older versions of WSL can cause:
- Docker Desktop to hang periodically or when upgrading
- Deployment via SCCM to fail
- The `vmmem.exe` to consume all memory 
- Network filter policies to be applied globally, not to specific objects
- GPU failures with containers
