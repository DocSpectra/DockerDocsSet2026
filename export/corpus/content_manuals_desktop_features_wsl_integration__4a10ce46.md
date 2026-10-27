---
title: Enable Docker in a WSL 2 distribution
---

Before you begin, see [WSL 2 requirements](requirements.md).

## Enable Docker in a WSL 2 distribution

WSL 2 lets multiple Linux distributions run side-by-side on a single shared kernel. Docker Desktop doesn't require a particular distribution to be installed, and `docker` commands work from Windows without one. However, enabling WSL integration for a distribution gives you direct access to `docker` commands from that distribution's terminal — which is useful for Linux-native development workflows.

1. Ensure the distribution runs in WSL 2 mode. WSL can run distributions in both v1 or v2 mode.

    To check the WSL mode, run:

     ```console
     $ wsl.exe -l -v
     ```

    To upgrade the Linux distribution to v2, run:

    ```console
    $ wsl.exe --set-version (distribution name) 2
    ```

    To set v2 as the default version for future installations, run:

    ```console
    $ wsl.exe --set-default-version 2
    ```

2. When Docker Desktop starts, go to **Settings** > **Resources** > **WSL Integration**.

    The Docker-WSL integration is enabled on the default WSL distribution, which is [Ubuntu](https://learn.microsoft.com/en-us/windows/wsl/install). To change your default WSL distribution, run:
     ```console
    $ wsl.exe --set-default <distribution name>
    ```
   If **WSL integrations** isn't available under **Resources**, Docker may be in Windows container mode. In your taskbar, select the Docker menu and then **Switch to Linux containers**.

3. Select **Apply**.
