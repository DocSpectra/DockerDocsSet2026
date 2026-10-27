---
title: "Docker Desktop for Windows requirements and WSL setup"
---

## System requirements

> [!TIP]
>
> **Should I use Hyper-V or WSL?**
>
> Docker Desktop's functionality remains consistent on both WSL and Hyper-V, without a preference for either architecture. Hyper-V and WSL have their own advantages and disadvantages, depending on your specific setup and your planned use case. 

{{< tabs >}}
{{< tab name="WSL 2 backend, x86_64" >}}

- WSL version 2.1.5 or later. To check your version, see [WSL: Verification and setup](#wsl-verification-and-setup)
- If you intend to use Enhanced Container Isolation, ensure you’re using WSL version 2.6 or later. This is required because ECI depends on a Linux kernel version of at least 6.3.0, and WSL 2.6+ bundles Linux kernel version 6.6.
- Windows 10 64-bit: Enterprise, Pro, or Education version 22H2 (build 19045).
- Windows 11 64-bit: Enterprise, Pro, or Education version 23H2 (build 22631) or higher.
- Turn on the WSL 2 feature on Windows. For detailed instructions, refer to the
  [Microsoft documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
- The following hardware prerequisites are required to successfully run
  WSL 2 on Windows 10 or Windows 11:
  - 64-bit processor with [Second Level Address Translation (SLAT)](https://en.wikipedia.org/wiki/Second_Level_Address_Translation)
  - 8GB system RAM
  - Enable hardware virtualization in BIOS/UEFI. For more information, see
    [Virtualization](/manuals/desktop/setup/install/windows-virtualization.md).

For more information on setting up WSL 2 with Docker Desktop, see [WSL](/manuals/desktop/features/wsl/_index.md).

> [!NOTE]
>
> Docker only supports Docker Desktop on Windows for those versions of Windows that are still within [Microsoft’s servicing timeline](https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet). Docker Desktop is not supported on server versions of Windows, such as Windows Server 2019 or Windows Server 2022. For more information on how to run containers on Windows Server, see [Microsoft's official documentation](https://learn.microsoft.com/virtualization/windowscontainers/quick-start/set-up-environment).

> [!IMPORTANT]
>
> To run [Windows containers](windows-containers.md), you need Windows 10 or Windows 11 Professional or Enterprise edition.
> Windows Home or Education editions only allow you to run Linux containers.

{{< /tab >}}
{{< tab name="Hyper-V backend, x86_64" >}}

- Windows 10 64-bit: Enterprise, Pro, or Education version 22H2 (build 19045).
- Windows 11 64-bit: Enterprise, Pro, or Education version 23H2 (build 22631) or higher.
- Turn on Hyper-V and Containers Windows features.
- The following hardware prerequisites are required to successfully run Client
  Hyper-V on Windows 10:

  - 64 bit processor with [Second Level Address Translation (SLAT)](https://en.wikipedia.org/wiki/Second_Level_Address_Translation)
  - 8GB system RAM
  - Turn on BIOS/UEFI-level hardware virtualization support in the
    BIOS/UEFI settings. For more information, see
    [Virtualization](/manuals/desktop/setup/install/windows-virtualization.md#virtualization-must-be-turned-on).

> [!NOTE]
>
> Docker only supports Docker Desktop on Windows for those versions of Windows that are still within [Microsoft’s servicing timeline](https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet). Docker Desktop is not supported on server versions of Windows, such as Windows Server 2019 or Windows Server 2022. For more information on how to run containers on Windows Server, see [Microsoft's official documentation](https://learn.microsoft.com/virtualization/windowscontainers/quick-start/set-up-environment).

> [!IMPORTANT]
>
> To run [Windows containers](windows-containers.md), you need Windows 10 or Windows 11 Professional or Enterprise edition.
> Windows Home or Education editions only allow you to run Linux containers.

{{< /tab >}}
{{< tab name="WSL 2 backend, Arm (Early Access)" >}}

- WSL version 2.1.5 or later. To check your version, see [WSL: Verification and setup](#wsl-verification-and-setup)
- Windows 10 64-bit: Enterprise, Pro, or Education version 22H2 (build 19045).
- Windows 11 64-bit: Enterprise, Pro, or Education version 23H2 (build 22631) or higher.
- Turn on the WSL 2 feature on Windows. For detailed instructions, refer to the
  [Microsoft documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
- The following hardware prerequisites are required to successfully run
  WSL 2 on Windows 10 or Windows 11:
  - 64-bit processor with [Second Level Address Translation (SLAT)](https://en.wikipedia.org/wiki/Second_Level_Address_Translation)
  - 8GB system RAM
  - Enable hardware virtualization in BIOS/UEFI. For more information, see
    [Virtualization](/manuals/desktop/setup/install/windows-virtualization.md#virtualization-must-be-turned-on).

> [!IMPORTANT]
>
> Windows containers are not supported.

{{< /tab >}}
{{< /tabs >}}

Containers and images created with Docker Desktop are shared between all
user accounts on machines where it is installed. This is because all Windows
accounts use the same VM to build and run containers. Note that it is not possible to share containers and images between user accounts when using the Docker Desktop WSL 2 backend.

Running Docker Desktop inside a VMware ESXi or Azure VM is supported for Docker Business customers.
It requires enabling nested virtualization on the hypervisor first.
For more information, see [Running Docker Desktop in a VM or VDI environment](/manuals/desktop/setup/vm-vdi.md).


### WSL: Verification and setup

If you have chosen to use WSL, first verify that your installed version meets system requirements by running the following command in your terminal:

```console
wsl --version
```

If version details do not appear, you are likely using the inbox version of WSL. This version does not support modern capabilities and must be updated.

You can update or install WSL using one of the following methods:

#### Option 1: Install or update WSL via the terminal

1. Open PowerShell or Windows Command Prompt in administrator mode.
2. Run either the install or update command. You may be prompted to restart your machine. For more information, refer to [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).
```console
wsl --install

wsl --update
```

#### Option 2: Install WSL via the MSI package

If Microsoft Store access is blocked due to security policies:
1. Go to the official [WSL GitHub Releases page](https://github.com/microsoft/WSL/releases).
2. Download the `.msi` installer from the latest stable release (under the Assets drop-down).
3. Run the downloaded installer and follow the setup instructions.
