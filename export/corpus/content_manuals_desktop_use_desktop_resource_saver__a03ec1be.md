---
description: Understand what Docker Desktop Resource Saver mode is and how to configure it
keywords: Docker Dashboard, resource saver, manage, containers, gui, dashboard, user manual
title: Configure Docker Desktop Resource Saver mode
linkTitle: Resource Saver mode
weight: 70
---

For resource savings, automatic wake-up behavior, Windows WSL differences, and precedence over Pause, see [Resource Saver and manual Pause behavior](resource-saving-context.md).

## Configure Resource Saver 

Resource Saver is enabled by default but can be disabled by navigating to the **Resources** tab, in **Settings**. You can also configure the idle
timer as shown below.

![Resource Saver Settings](../images/resource-saver-settings.webp) 

If the values available aren't sufficient for your
needs, you can reconfigure it to any value, as long as the value is larger than 30 seconds, by
changing `autoPauseTimeoutSeconds` in the Docker Desktop `settings-store.json` file (or `settings.json` for Docker Desktop versions 4.34 and earlier): 

  - Mac: `~/Library/Group Containers/group.com.docker/settings-store.json`
  - Windows: `C:\Users\[USERNAME]\AppData\Roaming\Docker\settings-store.json`
  - Linux: `~/.docker/desktop/settings-store.json`

There's no need to restart Docker Desktop after reconfiguring. 


## Resource Saver mode versus Pause

See [Resource Saver precedence over Pause](resource-saving-context.md#resource-saver-mode-versus-pause).

## Resource Saver mode on Windows

See [Resource Saver on Windows and WSL](resource-saving-context.md#resource-saver-mode-on-windows).
