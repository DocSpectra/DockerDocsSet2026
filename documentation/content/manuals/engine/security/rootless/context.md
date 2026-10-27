---
title: How rootless mode works
---

## How it works

Rootless mode executes the Docker daemon and containers inside a user namespace.
This is similar to [`userns-remap` mode](../userns-context.md), except that
with `userns-remap` mode, the daemon itself is running with root privileges,
whereas in rootless mode, both the daemon and the container are running without
root privileges.

Rootless mode does not use binaries with `SETUID` bits or file capabilities,
except `newuidmap` and `newgidmap`, which are needed to allow multiple
UIDs/GIDs to be used in the user namespace.
