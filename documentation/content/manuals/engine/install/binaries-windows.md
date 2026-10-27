---
title: Install server and client binaries on Windows
---

Before installing, read the shared [binary installation caveats](binary-installation.md).
For upgrades, follow [Upgrade static binaries](binary-installation.md#upgrade-static-binaries).

> [!NOTE]
>
> The following section describes how to install the Docker daemon on Windows
> Server which allows you to run Windows containers only. When you install the
> Docker daemon on Windows Server, the daemon doesn't contain Docker components
> such as `buildx` and `compose`. If you're running Windows 10 or 11,
> we recommend that you install [Docker Desktop](/manuals/desktop/_index.md) instead.

Binary packages on Windows include both `dockerd.exe` and `docker.exe`. On Windows,
these binaries only provide the ability to run native Windows containers (not
Linux containers).

To install server and client binaries, perform the following steps:

1. Download the static binary archive. Go to
    [https://download.docker.com/win/static/stable/x86_64](https://download.docker.com/win/static/stable/x86_64) and select the latest version from the list.

2. Run the following PowerShell commands to install and extract the archive to your program files:

    ```powershell
    PS C:\> Expand-Archive /path/to/<FILE>.zip -DestinationPath $Env:ProgramFiles
    ```

3. Register the service and start the Docker Engine:

    ```powershell
    PS C:\> &$Env:ProgramFiles\Docker\dockerd --register-service
    PS C:\> Start-Service docker
    ```

4.  Verify that Docker is installed correctly by running the `hello-world`
    image.

    ```powershell
    PS C:\> &$Env:ProgramFiles\Docker\docker run hello-world:nanoserver
    ```

    This command downloads a test image and runs it in a container. When the
    container runs, it prints a message and exits.
