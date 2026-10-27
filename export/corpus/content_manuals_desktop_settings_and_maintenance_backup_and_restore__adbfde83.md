---
title: How to back up and restore your Docker Desktop data
linkTitle: Backup and restore data
keywords: Docker Desktop, backup, restore, migration, reinstall, containers, images,
  volumes
weight: 20
aliases:
 - /desktop/backup-and-restore/
---

Use this procedure to back up and restore your images and container data. This is useful if you want to reset your VM disk or to move your Docker environment to a new computer, or recover from a failed Docker Desktop update or installation.

> [!IMPORTANT]
>
> If you use volumes or bind-mounts to store your container data, backing up your containers may not be needed, but make sure to remember the options that were used when creating the container or use a [Docker Compose file](/reference/compose-file/_index.md) if you want to re-create your containers with the same configuration after re-installation.

## If Docker Desktop is functioning normally

See [Back up and restore data when Docker Desktop starts](backup-running-desktop.md).

### Save your data

See [Save your data](backup-running-desktop.md#save-your-data).

### Restore your data

See [Restore your data](backup-running-desktop.md#restore-your-data).

## If Docker Desktop fails to start

See [Recover data when Docker Desktop fails to start](backup-vm-disk.md).
