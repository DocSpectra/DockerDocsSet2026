---
title: "Uninstall Docker Desktop on Fedora"
---

> [!WARNING]
>
> Before uninstalling, review the [data-loss warning and backup instructions](uninstall-data.md).

To uninstall Docker Desktop for Fedora:

1. Remove the Docker Desktop application. Run:

   ```console
   $ sudo dnf remove docker-desktop
   ```

   This removes the Docker Desktop package itself but doesn’t delete all of its files or settings.

2. Manually remove leftover file.

   ```console
   $ rm -r $HOME/.docker/desktop
   $ sudo rm /usr/local/bin/com.docker.cli
   $ sudo dnf remove docker-desktop
   ```

   This removes configuration and data files at `$HOME/.docker/desktop`, the symlink at `/usr/local/bin/com.docker.cli`, and purges the remaining systemd service files.

3. [Clean up Docker configuration](setup/linux-uninstall-cleanup.md) by removing the credential-store and current-context entries.
