---
description: How to configure and use Docker Extensions' private marketplace
keywords: Docker Extensions, Docker Desktop, Linux, Mac, Windows, Marketplace, private, security, admin
title: Configure a private marketplace for extensions
tags: [admin]
linkTitle: Configure a private marketplace
weight: 30
aliases:
 - /desktop/extensions/private-marketplace/
---

{{< summary-bar feature_name="Private marketplace" >}}

Learn how to configure and set up a private marketplace with a curated list of extensions for your Docker Desktop users.

Docker Extensions' private marketplace is designed specifically for organizations who don’t give developers root access to their machines. It makes use of [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md) so administrators have complete control over the private marketplace.

## Prerequisites

- [Download and install Docker Desktop](https://docs.docker.com/desktop/release-notes/).
- You must be an administrator for your organization.
- You have the ability to push the `extension-marketplace` folder and `admin-settings.json` file to the locations specified below through device management software such as [Jamf](https://www.jamf.com/).

## Step one: Initialize the private marketplace

1. Create a folder locally for the content that will be deployed to your developers’ machines:

   ```console
   $ mkdir my-marketplace
   $ cd my-marketplace
   ```

2. Initialize the configuration files for your marketplace:

   {{< tabs group="os_version" >}}
   {{< tab name="Mac" >}}

   ```console
   $ /Applications/Docker.app/Contents/Resources/bin/extension-admin init
   ```

   {{< /tab >}}
   {{< tab name="Windows" >}}

   ```console
   $ C:\Program Files\Docker\Docker\resources\bin\extension-admin init
   ```

   {{< /tab >}}
   {{< tab name="Linux" >}}

   ```console
   $ /opt/docker-desktop/extension-admin init
   ```

   {{< /tab >}}
   {{< /tabs >}}

This creates 2 files:

- `admin-settings.json`, which activates the private marketplace feature once it’s applied to Docker Desktop on your developers’ machines.
- `extensions.txt`, which determines which extensions to list in your private marketplace.

> [!IMPORTANT]
>
> If your org is using [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md) via the [Admin Console](manuals/enterprise/security/hardened-desktop/settings-management/configure-admin-console/_index.md), you will not need the `admins-settings.json` file. Delete the generated file and keep only the `extensions.txt` file.

## Step two: Set the behaviour

Follow [Set the behaviour](private-marketplace-configuration.md#set-the-behaviour) for the generated `admin-settings.json` file or the Admin Console.

## Step three: List allowed extensions

Follow [List allowed extensions](private-marketplace-configuration.md#list-allowed-extensions) to configure `extensions.txt`.

## Step four: Generate the private marketplace

Once the list in `extensions.txt` is ready, you can generate the marketplace:

{{< tabs group="os_version" >}}
{{< tab name="Mac" >}}

```console
$ /Applications/Docker.app/Contents/Resources/bin/extension-admin generate
```

{{< /tab >}}
{{< tab name="Windows" >}}

```console
$ C:\Program Files\Docker\Docker\resources\bin\extension-admin generate
```

{{< /tab >}}
{{< tab name="Linux" >}}

```console
$ /opt/docker-desktop/extension-admin generate
```

{{< /tab >}}
{{< /tabs >}}

This creates an `extension-marketplace` directory and downloads the marketplace metadata for all the allowed extensions.

The marketplace content is generated from extension image information as image labels, which is the [same format as public extensions](extensions-sdk/extensions/labels.md). It includes the extension title, description, screenshots, links, etc.

## Step five: Test the private marketplace setup

It's recommended that you try the private marketplace on your Docker Desktop installation.

> [!IMPORTANT]
>
> If your org is managing settings via the [Admin Console](manuals/enterprise/security/hardened-desktop/settings-management/configure-admin-console/_index.md), in Docker Desktop 4.59 and earlier, you must manually delete the `admin-settings.json` file created in the target folder by the `apply` command before step 2. In Docker Desktop 4.60 and later, this step is no longer necessary. 

1. Run the following command in your terminal. This command automatically copies the generated files to the location where Docker Desktop reads the configuration files. Depending on your operating system, the location is:

    - Mac: `/Library/Application\ Support/com.docker.docker`
    - Windows: `C:\ProgramData\DockerDesktop`
    - Linux: `/usr/share/docker-desktop`

   {{< tabs group="os_version" >}}
   {{< tab name="Mac" >}}

   ```console
   $ sudo /Applications/Docker.app/Contents/Resources/bin/extension-admin apply
   ```

   {{< /tab >}}
   {{< tab name="Windows (run as admin)" >}}

   ```console
   $ C:\Program Files\Docker\Docker\resources\bin\extension-admin apply
   ```

   {{< /tab >}}
   {{< tab name="Linux" >}}

   ```console
   $ sudo /opt/docker-desktop/extension-admin apply
   ```

   {{< /tab >}}
   {{< /tabs >}}

2. Quit and re-open Docker Desktop. 
3. Sign in with a Docker account.

When you select the **Extensions** tab, you should see the private marketplace listing only the extensions you have allowed in `extensions.txt`.

![Extensions Private Marketplace](/assets/images/extensions-private-marketplace.webp)

## Step six: Distribute the private marketplace

Once you’ve confirmed that the private marketplace configuration works, the final step is to distribute the files to the developers’ machines with the MDM software your organization uses. For example, [Jamf](https://www.jamf.com/).

The files to distribute are:
* `admin-settings.json` (except if your org is managing settings via the [Admin Console](manuals/enterprise/security/hardened-desktop/settings-management/configure-admin-console/_index.md))
* the entire `extension-marketplace` folder and its subfolders

These files must be placed on developer's machines. Depending on your operating system, the target location is (as mentioned above):

- Mac: `/Library/Application\ Support/com.docker.docker`
- Windows: `C:\ProgramData\DockerDesktop`
- Linux: `/usr/share/docker-desktop`

Make sure your developers are signed in to Docker Desktop in order for the private marketplace configuration to take effect. As an administrator, you should [enforce sign-in](/manuals/enterprise/security/enforce-sign-in/_index.md).

## Feedback

Give feedback or report any bugs you may find by emailing `extensions@docker.com`.
