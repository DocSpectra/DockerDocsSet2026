---
title: Recover data when Docker Desktop fails to start
---

> [!IMPORTANT]
>
> If you use volumes or bind-mounts to store your container data, backing up your containers may not be needed, but make sure to remember the options that were used when creating the container or use a [Docker Compose file](/reference/compose-file/_index.md) if you want to re-create your containers with the same configuration after re-installation.

## If Docker Desktop fails to start 

If Docker Desktop cannot launch and must be reinstalled, you can back up its VM disk and image data directly from disk. Docker Desktop must be fully stopped before backing up these files.

{{< tabs >}}
{{< tab name="Windows" >}}

1. Back up Docker containers/images.

   Backup the following file:

   ```console
   %LOCALAPPDATA%\Docker\wsl\data\docker_data.vhdx
   ```

   Copy it to a safe location. 

1. Back up WSL distributions.

   If you're running any WSL Linux distributions (Ubuntu, Alpine, etc.), back them up using [Microsoft's guide](https://learn.microsoft.com/en-us/windows/wsl/faq#how-can-i-back-up-my-wsl-distributions-).

1. Restore. 

   After reinstalling Docker Desktop, restore the `docker_data.vhdx` to the same location and re-import your WSL distributions if needed.

{{< /tab >}}
{{< tab name="Mac" >}}

1. Back up Docker containers/images.

   Backup the following file:

   ```console
   ~/Library/Containers/com.docker.docker/Data/vms/0/data/Docker.raw
   ```

   Copy it to a safe location. 

1. Restore. 

   After reinstalling Docker Desktop, restore the `Docker.raw` to the same location.

{{< /tab >}}
{{< tab name="Linux" >}}

1. Back up Docker containers/images:

   Backup the following file:

   ```console
   ~/.docker/desktop/vms/0/data/Docker.raw
   ```

   Copy it to a safe location.

1. Restore. 

   After reinstalling Docker Desktop, restore the `Docker.raw` to the same location.

{{< /tab >}}
{{< /tabs >}}
