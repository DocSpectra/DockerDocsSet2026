---
title: Enterprise installer update behavior
---

## MSI installations

> [!NOTE]
>
> When installing Docker Desktop with the MSI, in-app updates are automatically disabled by default. This ensures organizations can maintain version consistency and prevent unapproved updates.
> Starting with Docker Desktop version 4.60 and later, in-app updates from an MSI installation can be enabled by changing the `disableUpdate` setting to `false` through [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/policy-model.md).
>
> Docker Desktop notifies you when an update is available. To update Docker Desktop, download the latest installer from the Docker Admin Console. Navigate to the **Enterprise deployment** page.
>
> To keep up to date with new releases, check the [release notes](/manuals/desktop/release-notes.md) page.


## PKG installations

> [!NOTE]
>
> When installing Docker Desktop with the PKG, in-app updates are automatically disabled. This ensures organizations can maintain version consistency and prevent unapproved updates. For Docker Desktop installed with the `.dmg` installer, in-app updates remain supported.
>
> Docker Desktop notifies you when an update is available. To update Docker Desktop, download the latest installer from the Docker Admin Console. Navigate to the **Enterprise deployment** page.
>
> To keep up to date with new releases, check the [release notes](/manuals/desktop/release-notes.md) page.


## Microsoft Store installations

### Developer-managed installations

For developers who install Docker Desktop directly:

- The Microsoft Store does not automatically update Win32 apps like Docker Desktop for most users.
- Only a subset of users (approximately 20%) may receive update notifications on the Microsoft Store page.
- Most users must manually check for and apply updates within the Store.

### Intune-managed installations

In environments managed with Intune:
- Intune checks for updates approximately every 8 hours.
- When a new version is detected, Intune triggers a `winget` upgrade.  
- If appropriate policies are configured, updates can occur automatically without user intervention. 
- Updates are handled by Intune's management infrastructure rather than the Microsoft Store itself.
