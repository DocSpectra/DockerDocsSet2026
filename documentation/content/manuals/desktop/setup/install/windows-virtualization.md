---
title: "Set up Windows virtualization for Docker Desktop"
---

## Solutions

Your machine must have the following features for Docker Desktop to function correctly:

### WSL 2 and Windows Home

1. Virtual Machine Platform
2. [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
3. [Virtualization enabled in the BIOS](https://support.microsoft.com/en-gb/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1)
   Note that many Windows devices already have virtualization enabled, so this may not apply.
4. Hypervisor enabled at Windows startup

![WSL 2 enabled](../../images/wsl2-enabled.png)

It must be possible to run WSL 2 commands without error, for example:

```console
PS C:\users\> wsl -l -v
  NAME              STATE           VERSION
* Ubuntu            Running         2
  docker-desktop    Stopped         2
PS C:\users\> wsl -d docker-desktop echo WSL 2 is working
WSL 2 is working
```

If the features are enabled but the commands are not working, first check [Virtualization is turned on](#virtualization-must-be-turned-on)
then [enable the Hypervisor at Windows startup](#hypervisor-enabled-at-windows-startup) if required. If running Docker
Desktop in a Virtual Machine, ensure [the hypervisor has nested virtualization enabled](#turn-on-nested-virtualization).

### Hyper-V

On Windows 10 Pro or Enterprise, you can also use Hyper-V with the following features enabled:

1. [Hyper-V](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-technology-overview)
   installed and working
2. [Virtualization enabled in the BIOS](https://support.microsoft.com/en-gb/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1)
   Note that many Windows devices already have virtualization enabled, so this may not apply.
3. Hypervisor enabled at Windows startup

![Hyper-V on Windows features](../../images/hyperv-enabled.png)

Docker Desktop requires Hyper-V as well as the Hyper-V Module for Windows
PowerShell to be installed and enabled. The Docker Desktop installer enables
it for you.

Docker Desktop also needs two CPU hardware features to use Hyper-V: Virtualization and Second Level Address Translation (SLAT), which is also called Rapid Virtualization Indexing (RVI). On some systems, Virtualization must be enabled in the BIOS. The steps required are vendor-specific, but typically the BIOS option is called `Virtualization Technology (VTx)` or something similar. Run the command `systeminfo` to check all required Hyper-V features. See [Pre-requisites for Hyper-V on Windows 10](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/hyper-v-requirements) for more details.

To install Hyper-V manually, see [Install Hyper-V on Windows 10](https://msdn.microsoft.com/en-us/virtualization/hyperv_on_windows/quick_start/walkthrough_install). A reboot is *required* after installation. If you install Hyper-V without rebooting, Docker Desktop does not work correctly.

From the start menu, type **Turn Windows features on or off** and press enter.
In the subsequent screen, verify that Hyper-V is enabled.

### Virtualization must be turned on

In addition to [Hyper-V](#hyper-v) or [WSL 2](/manuals/desktop/features/wsl/_index.md), virtualization must be turned on. Check the
Performance tab on the Task Manager. Alternatively, you can type `systeminfo` into your terminal. If you see `Hyper-V Requirements: A hypervisor has been detected. Features required for Hyper-V will not be displayed`, then virtualization is enabled.

![Task Manager](../../images/virtualization-enabled.png)

If you manually uninstall Hyper-V, WSL 2 or turn off virtualization,
Docker Desktop cannot start. 

To turn on nested virtualization, see [Run Docker Desktop for Windows in a VM or VDI environment](/manuals/desktop/setup/vm-vdi.md#turn-on-nested-virtualization).

### Hypervisor enabled at Windows startup

If you have completed the previous steps and are still experiencing
Docker Desktop startup issues, this could be because the Hypervisor is installed,
but not launched during Windows startup. Some tools (such as older versions of 
Virtual Box) and video game installers turn off hypervisor on boot. To turn it back on:

1. Open an administrative console prompt.
2. Run `bcdedit /set hypervisorlaunchtype auto`.
3. Restart Windows.

You can also refer to the [Microsoft TechNet article](https://social.technet.microsoft.com/Forums/en-US/ee5b1d6b-09e2-49f3-a52c-820aafc316f9/hyperv-doesnt-work-after-upgrade-to-windows-10-1809?forum=win10itprovirt) on Code flow guard (CFG) settings.

### Turn on nested virtualization

If you are using Hyper-V and you get the following error message when running Docker Desktop in a VDI environment:

```console
The Virtual Machine Management Service failed to start the virtual machine 'DockerDesktopVM' because one of the Hyper-V components is not running
```

Try [enabling nested virtualization](/manuals/desktop/setup/vm-vdi.md#turn-on-nested-virtualization).
