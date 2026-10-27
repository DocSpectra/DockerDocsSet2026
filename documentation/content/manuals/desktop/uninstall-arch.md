---
title: "Uninstall Docker Desktop on Arch"
---

> [!WARNING]
>
> Before uninstalling, review the [data-loss warning and backup instructions](uninstall-data.md).

To uninstall Docker Desktop for Arch:

1. Remove the Docker Desktop application. Run:

   ```console
   $ sudo pacman -Rns docker-desktop
   ```

   This removes the Docker Desktop package along with its configuration files and dependencies not required by other packages.

2. Manually remove leftover files.

   ```console
   $ rm -r $HOME/.docker/desktop
   ```

   This removes configuration and data files at `$HOME/.docker/desktop`.

3. [Clean up Docker configuration](setup/linux-uninstall-cleanup.md) by removing the credential-store and current-context entries.
