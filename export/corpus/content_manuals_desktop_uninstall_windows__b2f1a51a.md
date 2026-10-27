---
title: "Uninstall Docker Desktop on Windows"
---

> [!WARNING]
>
> Before uninstalling, review the [data-loss warning and backup instructions](uninstall-data.md).

## From the GUI

1. From the Windows **Start** menu, select **Settings** > **Apps** > **Apps & features**.
2. Select **Docker Desktop** from the **Apps & features** list and then select **Uninstall**.
3. Select **Uninstall** to confirm your selection.

## From the CLI

1. Locate the installer:
   ```console
   $ C:\Program Files\Docker\Docker\Docker Desktop Installer.exe
   ```
2. Uninstall Docker Desktop.

   In PowerShell, run:
    ```console
    $ Start-Process 'Docker Desktop Installer.exe' -Wait uninstall
    ```

   In the Command Prompt, run:
    ```console
    $ start /w "" "Docker Desktop Installer.exe" uninstall
    ```

## Remove residual files

After uninstalling Docker Desktop, some residual files may remain which you can remove manually. These are:

```console
C:\ProgramData\Docker
C:\ProgramData\DockerDesktop
C:\Program Files\Docker
C:\Users\<your user name>\AppData\Local\Docker
C:\Users\<your user name>\AppData\Roaming\Docker
C:\Users\<your user name>\AppData\Roaming\Docker Desktop
C:\Users\<your user name>\.docker
```
