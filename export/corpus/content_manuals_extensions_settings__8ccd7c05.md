---
title: Change extension settings
description: Enable extensions, control installation sources, and show extension containers.
---

For extension capabilities and access rights, see [Extension security](extensions-sdk/architecture/security.md).

## Settings

### Turn on or turn off extensions

Docker Extensions is switched on by default. To change your settings:

1. Navigate to **Settings**.
2. Select the **Extensions** tab.
3. Next to **Enable Docker Extensions**, select or clear the checkbox to set your desired state.
4. In the bottom-right corner, select **Apply**.

> [!NOTE]
>
> If you are an [organization owner](/manuals/admin/organization/manage/manage-a-team.md#what-is-an-organization-owner), you can turn off extensions for your users. Open the `settings-store.json` file, and set `"extensionsEnabled"` to `false`.
> The `settings-store.json` file is located at:
>   - `~/Library/Group Containers/group.com.docker/settings-store.json` on Mac
>   - `C:\Users\[USERNAME]\AppData\Roaming\Docker\settings-store.json` on Windows
>
> This can also be done with [Hardened Docker Desktop](/manuals/enterprise/security/hardened-desktop/_index.md)

> [!NOTE]
>
> Enabling extensions doesn't use computer resources (CPU / Memory) by itself.
>
> Specific extensions might use computer resources, depending on the features and implementation of each extension, but there is no reserved resources or usage cost associated with enabling extensions.


### Turn on or turn off extensions not available in the Marketplace

You can install extensions through the Marketplace or through the Extensions SDK tools. You can choose to only allow published extensions. These are extensions that have been reviewed and published in the Extensions Marketplace.

1. Navigate to **Settings**.
2. Select the **Extensions** tab.
3. Next to **Allow only extensions distributed through the Docker Marketplace**, select or clear the checkbox to set your desired state.
4. In the bottom-right corner, select **Apply**.

### See containers created by extensions

By default, containers created by extensions are hidden from the list of containers in the Docker Desktop Dashboard and the Docker CLI. To make them visible
update your settings:

1. Navigate to **Settings**.
2. Select the **Extensions** tab.
3. Next to **Show Docker Extensions system containers**, select or clear the checkbox to set your desired state.
4. In the bottom-right corner, select **Apply**.

