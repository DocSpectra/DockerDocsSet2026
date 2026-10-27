---
title: Container process responsibilities
---

A container's main running process is the `ENTRYPOINT` and/or `CMD` at the
end of the `Dockerfile`. It's best practice to separate areas of concern by
using one service per container. That service may fork into multiple
processes (for example, Apache web server starts multiple worker processes).
It's ok to have multiple processes, but to get the most benefit out of Docker,
avoid one container being responsible for multiple aspects of your overall
application. You can connect multiple containers using user-defined networks and
shared volumes.

The container's main process is responsible for managing all processes that it
starts. In some cases, the main process isn't well-designed, and doesn't handle
"reaping" (stopping) child processes gracefully when the container exits. If
your process falls into this category, you can use the `--init` option when you
run the container. The `--init` flag inserts a tiny init-process into the
container as the main process, and handles reaping of all processes when the
container exits. Handling such processes this way is superior to using a
full-fledged init process such as `sysvinit` or `systemd` to handle process
lifecycle within your container.

## Using a process manager inside containers {#using-a-process-manager-inside-containers}

Process managers can also run within the container to check whether a process is
running and starts/restart it if not.

> [!WARNING]
>
> These aren't Docker-aware, and only monitor operating system processes within
> the container. Docker doesn't recommend this approach, because it's
> platform-dependent and may differ between versions of a given Linux
> distribution.
