---
title: Historical Docker Desktop upgrade and update procedures
linkTitle: Historical upgrade procedures
---

- [AUFS disk reset after Desktop 18.06](#aufs-disk-reset-after-desktop-1806)
- [Docker Desktop 3.3.0 update controls](#docker-desktop-330-update-controls)
- [Windows MSI updates](#windows-msi-updates)

For rollout, downloads, and system requirements, see [release availability](/manuals/desktop/release-availability.md).

## AUFS disk reset after Desktop 18.06

### Mac

AUFS storage driver is deprecated in Docker Desktop and AUFS support will be removed in the next major release. You can continue with AUFS in Docker Desktop 18.06.x, but you will need to reset disk image (in Preferences > Reset menu) before updating to the next major update. You can check documentation to [save images](/reference/cli/docker/image/save/#examples) and [back up volumes](/manuals/engine/storage/volumes.md#back-up-restore-or-migrate-data-volumes)

### Windows

AUFS storage driver is deprecated in Docker Desktop and AUFS support will be removed in the next major release. You can continue with AUFS in Docker Desktop 18.06.x, but you will need to reset the disk image (in Settings > Reset menu) before updating to the next major update. You can check documentation to [save images](/reference/cli/docker/image/save/#examples) and [backup volumes](/manuals/engine/storage/volumes.md#back-up-restore-or-migrate-data-volumes)

## Docker Desktop 3.3.0 update controls

### Download and install an update

You can now specify when to download and install a Docker Desktop update. When an update becomes available, Docker Desktop displays an icon to indicate the availability of a newer version. You can download the update in the background whenever convenient. When the download is complete, all you need to do is to click Update and restart to install the latest update.

### Skip a notification with a paid subscription

Developers who use Docker Desktop for professional development purposes may at times need to skip a specific update. For this reason, users with a paid Docker subscription can skip notifications for a particular update when a reminder appears.

### Opt out in an IT managed environment

For developers in IT managed environments, who don’t have administrative access to install updates to Docker Desktop, there is now an option in the Settings menu to opt out of notifications altogether for Docker Desktop updates if your Docker ID is part of a Team subscription.

## Windows MSI updates

Release entries: 4.60.0, 4.61.0, 4.62.0, 4.63.0, 4.64.0, and 4.65.0.

The Windows MSI installer cannot update an existing Docker Desktop installation when the current version is between 4.56 and 4.65. As a workaround, uninstall the existing version before reinstalling the latest version. Note that uninstalling removes all associated data.
