---
title: Apply and inspect managed settings
---

## Apply settings

Settings policies take effect after Docker Desktop restarts and users sign in.

For new installations:

1. Launch Docker Desktop.
1. Sign in with your Docker account.

For existing installations:

1. Quit Docker Desktop completely.
1. Relaunch Docker Desktop.

> [!IMPORTANT]
>
> Users must fully quit and reopen Docker Desktop. Restarting from the Docker Desktop menu isn't sufficient.

## View applied settings

When administrators apply Settings Management policies, Docker Desktop greys out most enforced settings in the GUI.

The Docker Desktop GUI doesn't currently display all centralized settings,
particularly Enhanced Container Isolation (ECI) settings that administrators
apply via the Admin Console.

As a workaround, you can check the `settings-store.json` file to view all
applied settings:

- Mac: `~/Library/Application Support/Docker/settings-store.json`
- Windows: `%APPDATA%\Docker\settings-store.json`
- Linux: `~/.docker/desktop/settings-store.json`

The `settings-store.json` file contains all settings, including those that
may not appear in the Docker Desktop GUI.

## Verify policy application

After you apply policies:

- Docker Desktop displays most settings as greyed out
- Some settings, particularly Enhanced Container Isolation configurations,
  may not appear in the GUI
- You can verify all applied settings by checking the [`settings-store.json`
  file](#view-applied-settings) on your system


## Policy update timing

Docker Desktop checks for policy updates:

- At startup
- Every 60 minutes while Docker Desktop is running
- When users restart Docker Desktop

Changes to policies in the Admin Console are available immediately, but users must restart Docker Desktop to apply them.
