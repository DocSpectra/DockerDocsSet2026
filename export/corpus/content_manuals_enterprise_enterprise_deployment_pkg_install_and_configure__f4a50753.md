---
title: PKG installer
description: Understand how to use the PKG installer. Also explore additional configuration options.
keywords: pkg, mac, docker desktop, install, deploy, configure, admin, mdm
tags: [admin]
weight: 20
aliases:
 - /desktop/setup/install/enterprise-deployment/pkg-install-and-configure/
---

{{< summary-bar feature_name="PKG installer" >}}

The PKG package supports various MDM (Mobile Device Management) solutions, making it ideal for bulk installations and eliminating the need for manual setups by individual users. With this package, IT administrators can ensure standardized, policy-driven installations of Docker Desktop, enhancing efficiency and software management across their organizations.

## Install interactively

1. [Download the macOS PKG installer](download-installers.md#macos-pkg).
2. Once downloaded, double-click `Docker.pkg` to run the installer.
3. Follow the instructions on the installation wizard to authorize the installer and proceed with the installation.
   - **Introduction**: Select **Continue**.
   - **License**: Review the license agreement and select **Agree**.
   - **Destination Select**: This step is optional. It is recommended that you keep the default installation destination (usually `Macintosh HD`). Select **Continue**.
   - **Installation Type**: Select **Install**.
   - **Installation**: Authenticate using your administrator password or Touch ID.
   - **Summary**: When the installation completes, select **Close**.

## Update behavior

Review [PKG installation update behavior](installer-updates.md#pkg-installations), including the `.dmg` installer exception.

## Install from the command line

1. [Download the macOS PKG installer](download-installers.md#macos-pkg).
2. From your terminal, run the following command:

   ```console
   $ sudo installer -pkg "/path/to/Docker.pkg" -target /Applications
   ```

## Additional resources

- See how you can deploy Docker Desktop for Mac using [Intune](use-intune.md) or [Jamf Pro](use-jamf-pro.md)
- Explore how to [Enforce sign-in](/manuals/enterprise/security/enforce-sign-in/mac-plist.md) for your users.
