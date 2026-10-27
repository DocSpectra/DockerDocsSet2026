---
title: Turn on the Docker Desktop WSL 2 backend
---

Before you begin, see [WSL 2 requirements](requirements.md).

## Turn on Docker Desktop WSL 2

Before installing Docker Desktop, uninstall any version of Docker Engine or the Docker CLI
that was installed directly inside a WSL Linux distribution. Running both can cause conflicts.

1. Download and install the latest version of [Docker Desktop for Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-windows).
2. Follow the usual installation instructions to install Docker Desktop. Depending on which version of Windows you are using, Docker Desktop may prompt you to turn on WSL 2 during installation. Read the information displayed on the screen and turn on the WSL 2 feature to continue.
3. Start Docker Desktop from the **Windows Start** menu.
4. Navigate to **Settings**.
5. From the **General** tab, select **Use WSL 2 based engine**.

    If you have installed Docker Desktop on a system that supports WSL 2, this option is turned on by default.
6. Select **Apply**.

`docker` commands are now available from any Windows terminal using the WSL 2 engine.

> [!TIP]
>
> By default, Docker Desktop stores the data for the WSL 2 engine at `C:\Users\[USERNAME]\AppData\Local\Docker\wsl`.
> If you want to change the location, go to `Settings -> Resources -> Advanced` page from the Docker Dashboard.
> Read more about this and other Windows settings at [Changing settings](/manuals/desktop/settings-and-maintenance/settings.md)
