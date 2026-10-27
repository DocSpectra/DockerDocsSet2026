---
description: Get started with Docker for Windows. This guide covers system requirements,
  where to download, and instructions on how to install and update.
keywords: docker for windows, docker windows, docker desktop for windows, docker on
  windows, install docker windows, install docker on windows, docker windows 10, docker
  run on windows, installing docker for windows, windows containers, wsl, hyper-v
title: Install Docker Desktop on Windows
linkTitle: Windows
weight: 30
aliases:
- /desktop/windows/install/
- /docker-ee-for-windows/install/
- /docker-for-windows/install-windows-home/
- /docker-for-windows/install/
- /ee/docker-ee/windows/docker-ee/
- /engine/installation/windows/
- /engine/installation/windows/docker-ee/
- /install/windows/docker-ee/
- /install/windows/ee-preview/
- /installation/windows/
- /desktop/win/configuring-wsl/
- /desktop/install/windows-install/
---

> **Docker Desktop terms**
>
> Commercial use of Docker Desktop in larger enterprises (more than 250
> employees OR more than $10 million USD in annual revenue) requires a [paid
> subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopWindowsInstall).

This page provides download links, system requirements, and step-by-step installation instructions for Docker Desktop on Windows.

{{< button text="Docker Desktop for Windows - x86_64" url="https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64" >}}
{{< button text="Docker Desktop for Windows - x86_64 on the Microsoft Store" url="https://apps.microsoft.com/detail/xp8cbj40xlbwkx?hl=en-GB&gl=GB" >}}
{{< button text="Docker Desktop for Windows - Arm (Early Access)" url="https://desktop.docker.com/win/main/arm64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-arm64" >}}

_For checksums, see [Release notes](/manuals/desktop/release-notes.md)_

## System requirements

Before installing, review:

- [Windows requirements and WSL setup](windows-requirements.md), including backend and architecture requirements, supported Windows versions, and user-account sharing caveats.
- [Windows permission requirements](windows-permission-requirements.md).
- [Docker Desktop license agreement](/manuals/subscription/desktop-license.md).

## Install Docker Desktop on Windows

### Install interactively

1. Download the installer using the download button at the top of the page, or from the [release notes](/manuals/desktop/release-notes.md).

2. Double-click `Docker Desktop Installer.exe` to run the installer. By default, Docker Desktop is installed at `C:\Program Files\Docker\Docker`.

3. When prompted, ensure the **Use WSL 2 instead of Hyper-V** option on the Configuration page is selected or not depending on your choice of backend.

    On systems that support only one backend, Docker Desktop automatically selects the available option.

4. Follow the instructions on the installation wizard to authorize the installer and proceed with the installation.

5. When the installation is successful, select **Close** to complete the installation process.

6. [Start Docker Desktop](#start-docker-desktop).

If your administrator account is different to your user account, follow [Add a user to docker-users](windows-permission-requirements.md#add-a-user-to-docker-users) for features that require higher privileges, such as the Hyper-V VM or Windows containers.

### Install from the command line

After downloading `Docker Desktop Installer.exe`, run the following command in a terminal to install Docker Desktop:

```console
$ "Docker Desktop Installer.exe" install
```

If you’re using PowerShell you should run it as:

```powershell
Start-Process 'Docker Desktop Installer.exe' -Wait install
```

If using the Windows Command Prompt:

```sh
start /w "" "Docker Desktop Installer.exe" install
```

By default, Docker Desktop is installed at `C:\Program Files\Docker\Docker`.

If your administrator account is different to your user account, follow [Add a user to docker-users](windows-permission-requirements.md#add-a-user-to-docker-users) for the group requirement and command.

See the [Installer flags](#installer-flags) section to see what flags the `install` command accepts.

## Start Docker Desktop

Docker Desktop does not start automatically after installation. To start Docker Desktop:

1. Search for Docker, and select **Docker Desktop** in the search results.

2. The Docker menu ({{< inline-image src="images/whale-x.svg" alt="whale menu" >}}) displays the Docker Subscription Service Agreement.

   Review the [Docker Desktop license agreement](/manuals/subscription/desktop-license.md) for free-use conditions, paid-subscription requirements, government use, and included subscriptions.

3. Select **Accept** to continue. Docker Desktop starts after you accept the terms.

   Note that Docker Desktop won't run if you do not agree to the terms. You can choose to accept the terms at a later date by opening Docker Desktop.

   For more information, see [Docker Desktop Subscription Service Agreement](https://www.docker.com/legal/docker-subscription-service-agreement/). It is recommended that you read the [FAQs](https://www.docker.com/pricing/faq).

## Inventory installations

See [Inventory Docker Desktop installations](inventory.md) for endpoint management resources and license reporting.

## Advanced system configuration and installation options

### WSL: Verification and setup

Follow [WSL verification and setup](windows-requirements.md#wsl-verification-and-setup).

### Installer flags

See [Windows installer flags](installer-options.md#windows-installer-flags), including the PowerShell `ArgumentList` requirement.

#### Installation behavior

See [Windows installation behavior](installer-options.md#windows-installation-behavior).

#### Security and access control

See [Windows security and access control](installer-options.md#windows-security-and-access-control).

#### Proxy configuration

See [Windows proxy configuration](installer-options.md#windows-proxy-configuration).

##### Example of specifying PAC file

See the [Windows PAC file example](installer-options.md#windows-pac-file).

##### Example of specifying PAC script

See the [Windows PAC script example](installer-options.md#windows-pac-script).

#### Data root and disk location

See [Windows data root and disk location](installer-options.md#windows-data-root-and-disk-location).

### Administrator privileges

Installing Docker Desktop requires administrator privileges. However, once installed, it can be used without administrative access. Some actions, though, still need elevated permissions. See [Understand permission requirements for Windows](./windows-permission-requirements.md) for more detail.

See the [FAQs](/manuals/desktop/troubleshoot-and-support/faqs/general.md#how-do-i-run-docker-desktop-without-administrator-privileges) on how to install and run Docker Desktop without needing administrator privileges.

If you're an IT admin and your users do not have administrator rights and plan to perform operations that require elevated privileges, be sure to install Docker Desktop using the `--always-run-service` installer flag. This ensures those actions can still be executed without prompting for User Account Control (UAC) elevation. See [Installer Flags](#installer-flags) for more detail.

### Windows containers

See [Switch between Windows and Linux containers](windows-containers.md) for daemon selection, mode-specific settings, and Windows container resources.

## Where to go next

- Explore [Docker's subscriptions](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopWindowsInstall) to see what Docker can offer you.
- [Get started with Docker](/get-started/introduction/_index.md).
- [Explore Docker Desktop](/manuals/desktop/use-desktop/_index.md) and all its features.
- [Troubleshooting](/manuals/desktop/troubleshoot-and-support/troubleshoot/_index.md) describes common problems, workarounds, and
  how to get support.
- [FAQs](/manuals/desktop/troubleshoot-and-support/faqs/general.md) provide answers to frequently asked questions.
- [Release notes](/manuals/desktop/release-notes.md) lists component updates, new features, and improvements associated with Docker Desktop releases.
- [Back up and restore data](/manuals/desktop/settings-and-maintenance/backup-and-restore.md) provides instructions on backing up and restoring data related to Docker.
