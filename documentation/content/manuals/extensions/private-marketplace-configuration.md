---
title: Private marketplace settings and allowed extensions
description: Configure private marketplace settings and the list of allowed extensions.
---

## Set the behaviour

The generated `admin-settings.json` file includes various settings you can modify.

> [!IMPORTANT]
>
> If your org is managing settings via the [Admin Console](manuals/enterprise/security/hardened-desktop/settings-management/configure-admin-console/_index.md), you will define the same settings in the Admin Console instead of the `admin-settings.json` file.

Each setting has a `value` that you can set, including a `locked` field that lets you lock the setting and make it unchangeable by your developers.

- `extensionsEnabled` enables Docker Extensions.
- `extensionsPrivateMarketplace` activates the private marketplace and ensures Docker Desktop connects to content defined and controlled by the administrator instead of the public Docker marketplace.
- `onlyMarketplaceExtensions` allows or blocks developers from installing other extensions by using the command line. Teams developing new extensions must have this setting unlocked (`"locked": false`) to install and test extensions being developed.
- `extensionsPrivateMarketplaceAdminContactURL` defines a contact link for developers to request new extensions in the private marketplace. If `value` is empty then no link is shown to your developers on Docker Desktop, otherwise this can be either an HTTP link or a “mailto:” link. For example,

  ```json
  "extensionsPrivateMarketplaceAdminContactURL": {
    "locked": true,
    "value": "mailto:admin@acme.com"
  }
  ```

To find out more information about the `admin-settings.json` file, see [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md).

## List allowed extensions

The generated `extensions.txt` file defines the list of extensions that are available in your private marketplace.

Each line in the file is an allowed extension and follows the format of `org/repo:tag`.

For example, if you want to permit the Disk Usage extension you would enter the following into your `extensions.txt` file:

```console
docker/disk-usage-extension:0.2.8
```

If no tag is provided, the latest tag available for the image is used. You can also comment out lines with `#` so the extension is ignored.

This list can include different types of extension images:

- Extensions from the public marketplace or any public image stored in Docker Hub.
- Extension images stored in Docker Hub as private images. Developers need to be signed in and have pull access to these images.
- Extension images stored in a private registry. Developers need to be signed in and have pull access to these images.

> [!IMPORTANT]
>
> Your developers can only install the version of the extension that you’ve listed.

