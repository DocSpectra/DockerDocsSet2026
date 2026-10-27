---
title: "Clean up Docker configuration after uninstalling Docker Desktop on Linux"
---

In `$HOME/.docker/config.json`, remove the `credsStore` and `currentContext` properties.

These entries tell Docker where to store credentials and which context is active. If they remain after uninstalling Docker Desktop, they may conflict with a future Docker setup.
