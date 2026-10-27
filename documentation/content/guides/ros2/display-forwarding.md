---
title: "Forward container displays to Linux or macOS"
description: "Forward container displays to Linux or macOS"
---

## Configure display forwarding

### Linux

Allow Docker access to your X server:

```console
$ xhost +local:docker
```

### macOS

On macOS, use XQuartz to provide X11 support. Install XQuartz using Homebrew:

1. Install XQuartz using Homebrew:

   ```console
   $ brew install --cask xquartz
   ```

2. Open XQuartz from Applications, then navigate to `Preferences > Security` and enable `Allow connections from network clients`. Restart your computer to ensure the changes take effect.

3. After rebooting, open a terminal and allow local connections:

   ```console
   $ defaults write org.xquartz.X11 nolisten_tcp -bool false
   $ xhost +localhost
   $ xhost + 127.0.0.1
   ```
