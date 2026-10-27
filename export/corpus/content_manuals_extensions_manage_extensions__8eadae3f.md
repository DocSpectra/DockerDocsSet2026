---
title: Manage installed extensions
description: List, update, and uninstall extensions.
---

## List installed extensions with the CLI

Regardless whether the extension was installed from the Marketplace or manually by using the Extensions CLI, you can use the `docker extension ls` command to display the list of extensions installed.
As part of the output you'll see the extension ID, the provider, version, the title and whether it runs a backend container or has deployed binaries to the host, for example:

```console
$ docker extension ls
ID                  PROVIDER            VERSION             UI                    VM                  HOST
john/my-extension   John                latest              1 tab(My-Extension)   Running(1)          -
```

### View a non-marketplace extension in Docker Desktop

Go to the Docker Desktop Dashboard, select **Add Extensions** and on the **Managed** tab to see the new extension installed.
Notice that an `UNPUBLISHED` label displays which indicates that the extension has not been installed from the Marketplace.

## Update and uninstall from Docker Desktop

### Update an extension

You can update any extension outside of Docker Desktop releases. To update an extension to the latest version, navigate to the Docker Desktop Dashboard and select the **Manage** tab.

The **Manage** tab displays with all your installed extensions. If an extension has a new version available, it displays an **Update** button.


### Uninstall an extension

You can uninstall an extension at any time.

> [!NOTE]
>
> Any data used by the extension that's stored in a volume must be manually deleted.

1. Navigate to the Docker Desktop Dashboard and select the **Manage** tab.
   This displays a list of extensions you've installed.
2. Select the ellipsis to the right of extension you want to uninstall.
3. Select **Uninstall**.

## Update and uninstall non-marketplace extensions with the CLI

### Update a non-marketplace extension 

To update an extension which isn't present in the Marketplace, in a terminal type `docker extension update IMAGE[:TAG]` where the `TAG` should be different from the extension that's already installed.

For instance, if you installed an extension with `docker extension install john/my-extension:0.0.1`, you can update it by running `docker extension update john/my-extension:0.0.2`.
Go to the Docker Desktop Dashboard to see the new extension updated.

> [!NOTE]
>
> Extensions that aren't installed through the Marketplace don't receive update notifications from Docker Desktop.

### Uninstall a non-marketplace extension

To uninstall an extension which is not present in the Marketplace, you can either navigate to the **Managed** tab in the Marketplace and select the **Uninstall** button, or from a terminal type `docker extension uninstall IMAGE[:TAG]`.
