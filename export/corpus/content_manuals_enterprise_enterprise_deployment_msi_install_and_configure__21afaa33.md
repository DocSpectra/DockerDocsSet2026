---
title: MSI installer
description: Understand how to use the MSI installer. Also explore additional configuration options.
keywords: msi, windows, docker desktop, install, deploy, configure, admin, mdm
tags: [admin]
weight: 10
aliases:
  - /desktop/install/msi/install-and-configure/
  - /desktop/setup/install/msi/install-and-configure/
  - /desktop/install/msi/
  - /desktop/setup/install/msi/
  - /desktop/setup/install/enterprise-deployment/msi-install-and-configure/
---

{{< summary-bar feature_name="MSI installer" >}}

The MSI package supports various MDM (Mobile Device Management) solutions, making it ideal for bulk installations and eliminating the need for manual setups by individual users. With this package, IT administrators can ensure standardized, policy-driven installations of Docker Desktop, enhancing efficiency and software management across their organizations.

## Install interactively

1. [Download the Windows MSI installer](download-installers.md#windows-msi).
2. Once downloaded, double-click `Docker Desktop Installer.msi` to run the installer.
3. After accepting the license agreement, choose the install location. By default, Docker Desktop is installed at `C:\Program Files\Docker\Docker`.
4. Configure the Docker Desktop installation. You can:
   - Create a desktop shortcut

   - Set the Docker Desktop service startup type to automatic

   - Disable Windows Container usage

   - Select the Docker Desktop backend: WSL or Hyper-V. If only one is supported by your system, you won't be able to choose.

5. Follow the instructions on the installation wizard to authorize the installer and proceed with the install.
6. When the installation is successful, select **Finish** to complete the installation process.

If your administrator account is different from your user account, you must add the user to the **docker-users** group to access features that require higher privileges, such as creating and managing the Hyper-V VM, or using Windows containers:

1. Run **Computer Management** as an **administrator**.
2. Navigate to **Local Users and Groups** > **Groups** > **docker-users**.
3. Right-click to add the user to the group.
4. Sign out and sign back in for the changes to take effect.

## Update behavior

Review [MSI installation update behavior](installer-updates.md#msi-installations), including the Docker Desktop 4.60 exception.

## Install from the command line

This section covers command line installations of Docker Desktop using PowerShell. It provides common installation commands that you can run. You can also add additional arguments which are outlined in [configuration options](#configuration-options).

When installing Docker Desktop, you can choose between interactive or non-interactive installations.

Interactive installations, without specifying `/quiet` or `/qn`, display the user interface and let you select your own properties.

When installing via the user interface it's possible to:

- Choose the destination folder
- Create a desktop shortcut
- Configure the Docker Desktop service startup type
- Disable Windows Containers
- Choose between the WSL or Hyper-V engine

Non-interactive installations are silent and any additional configuration must be passed as arguments.

### Common installation commands

Admin rights are required to run any of the following commands.

#### Install interactively with verbose logging

```powershell
msiexec /i "DockerDesktop.msi" /L*V ".\msi.log"
```

#### Install interactively without verbose logging

```powershell
msiexec /i "DockerDesktop.msi"
```

#### Install non-interactively with verbose logging

```powershell
msiexec /i "DockerDesktop.msi" /L*V ".\msi.log" /quiet
```

#### Install non-interactively and suppressing reboots

```powershell
msiexec /i "DockerDesktop.msi" /L*V ".\msi.log" /quiet /norestart
```

#### Install non-interactively with admin settings

```powershell
msiexec /i "DockerDesktop.msi" /L*V ".\msi.log" /quiet /norestart ADMINSETTINGS="{""configurationFileVersion"":2,""enhancedContainerIsolation"":{""value"":true,""locked"":false}}" ALLOWEDORG="your-organization"
```

#### Install interactively and allow users to switch to Windows containers without admin rights

```powershell
msiexec /i "DockerDesktop.msi" /L*V ".\msi.log" /quiet /norestart ALLOWEDORG="your-organization" ALWAYSRUNSERVICE=1
```

#### Install interactively specifying a PAC file

```powershell
PowerShell
 msiexec --% /i "DockerDesktop.msi" /L*V ".\msi.log"  PROXYHTTPMODE="manual" OVERRIDEPROXYPAC="http://localhost:8080/myproxy.pac"
```

#### Install interactively specifying a PAC script

```powershell
PowerShell
 msiexec --% /i "DockerDesktop.msi" /L*V ".\msi.log"  PROXYHTTPMODE="manual" OVERRIDEPROXYEMBEDDEDPAC="function FindProxyForURL(url,host) {return ""DIRECT"" ;; }"
```

#### Install with the passive display option

You can use the `/passive` display option instead of `/quiet` when you want to perform a non-interactive installation but show a progress dialog.

In passive mode the installer doesn't display any prompts or error messages to the user and the installation cannot be cancelled.

For example:

```powershell
msiexec /i "DockerDesktop.msi" /L*V ".\msi.log" /passive /norestart
```

> [!TIP]
>
> When creating a value that expects a JSON string:
>
> - The property expects a JSON formatted string
> - The string should be wrapped in double quotes
> - The string shouldn't contain any whitespace
> - Property names are expected to be in double quotes

### Common uninstall commands

See [Uninstall Docker Desktop with MSI](msi-uninstall.md).

### Configuration options

See [MSI properties, reboots, and analytics](msi-reference.md).

## Analytics

See [MSI analytics](msi-reference.md#analytics), including opt-out and persistence.

## Additional resources

- [Explore the FAQs](/manuals/enterprise/enterprise-deployment/faq.md)
