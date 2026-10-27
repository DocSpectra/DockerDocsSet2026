---
title: "Uninstall Docker Desktop on Mac"
---

> [!WARNING]
>
> Before uninstalling, review the [data-loss warning and backup instructions](uninstall-data.md).

## From the GUI

1. Open Docker Desktop. 
2. In the top-right corner of the Docker Desktop Dashboard, select the **Troubleshoot** icon.
3. Select **Uninstall**.
4. When prompted, confirm by selecting **Uninstall** again.

You can then move the Docker application to the trash. 

## From the CLI

Run:

```console
$ /Applications/Docker.app/Contents/MacOS/uninstall
```

You can then move the Docker application to the trash. 

> [!NOTE]
> You may encounter the following error when uninstalling Docker Desktop using the uninstall command.
>
> ```console
> $ /Applications/Docker.app/Contents/MacOS/uninstall
> Password:
> Uninstalling Docker Desktop...
> Error: unlinkat /Users/<USER_HOME>/Library/Containers/com.docker.docker/.com.apple.containermanagerd.metadata.plist: > operation not permitted
> ```
>
> The operation not permitted error is reported either on the file `.com.apple.containermanagerd.metadata.plist` or on the parent directory `/Users/<USER_HOME>/Library/Containers/com.docker.docker/`. This error can be ignored as you have successfully uninstalled Docker Desktop.
> You can remove the directory `/Users/<USER_HOME>/Library/Containers/com.docker.docker/` later by allowing **Full Disk Access** to the terminal application you are using (**System Settings** > **Privacy & Security** > **Full Disk Access**).

## Remove residual files

After uninstalling Docker Desktop, some residual files may remain which you can remove:

```console
$ rm -rf ~/Library/Group\ Containers/group.com.docker
$ rm -rf ~/.docker
```
