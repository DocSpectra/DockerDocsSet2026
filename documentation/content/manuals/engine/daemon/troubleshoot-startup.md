---
title: Troubleshoot daemon startup and connectivity
---

For configuration-file locations and startup options, see
[Docker daemon configuration](configuration.md#configure-the-docker-daemon).

## Daemon {#daemon}

### Unable to connect to the Docker daemon {#unable-to-connect-to-the-docker-daemon}

```text
Cannot connect to the Docker daemon. Is 'docker daemon' running on this host?
```

This error may indicate:

- The Docker daemon isn't running on your system. Start the daemon and try
  running the command again.
- Your Docker client is attempting to connect to a Docker daemon on a different
  host, and that host is unreachable.

### Check whether Docker is running {#check-whether-docker-is-running}

The operating-system independent way to check whether Docker is running is to
ask Docker, using the `docker info` command.

You can also use operating system utilities, such as
`sudo systemctl is-active docker` or `sudo status docker` or
`sudo service docker status`, or checking the service status using Windows
utilities.

Finally, you can check in the process list for the `dockerd` process, using
commands like `ps` or `top`.

#### Check which host your client is connecting to {#check-which-host-your-client-is-connecting-to}

To see which host your client is connecting to, check the value of the
`DOCKER_HOST` variable in your environment.

```console
$ env | grep DOCKER_HOST
```

If this command returns a value, the Docker client is set to connect to a Docker
daemon running on that host. If it's unset, the Docker client is set to connect
to the Docker daemon running on the local host. If it's set in error, use the
following command to unset it:

```console
$ unset DOCKER_HOST
```

You may need to edit your environment in files such as `~/.bashrc` or
`~/.profile` to prevent the `DOCKER_HOST` variable from being set erroneously.

If `DOCKER_HOST` is set as intended, verify that the Docker daemon is running on
the remote host and that a firewall or network outage isn't preventing you from
connecting.

### Troubleshoot conflicts between the `daemon.json` and startup scripts {#troubleshoot-conflicts-between-the-daemonjson-and-startup-scripts}

If you use a `daemon.json` file and also pass options to the `dockerd` command
manually or using start-up scripts, and these options conflict, Docker fails to
start with an error such as:

```text
unable to configure the Docker daemon with file /etc/docker/daemon.json:
the following directives are specified both as a flag and in the configuration
file: hosts: (from flag: [unix:///var/run/docker.sock], from file: [tcp://127.0.0.1:2376])
```

If you see an error similar to this one and you are starting the daemon manually
with flags, you may need to adjust your flags or the `daemon.json` to remove the
conflict.

> [!NOTE]
>
> If you see this specific error message about `hosts`, continue to the
> [next section](#configure-the-daemon-host-with-systemd)
> for a workaround.

If you are starting Docker using your operating system's init scripts, you may
need to override the defaults in these scripts in ways that are specific to the
operating system.

#### Configure the daemon host with systemd {#configure-the-daemon-host-with-systemd}

One notable example of a configuration conflict that's difficult to
troubleshoot is when you want to specify a different daemon address from the
default. Docker listens on a socket by default. On Debian and Ubuntu systems
using `systemd`, this means that a host flag `-H` is always used when starting
`dockerd`. If you specify a `hosts` entry in the `daemon.json`, this causes a
configuration conflict and results in the Docker daemon failing to start.

To work around this problem, create a new file
`/etc/systemd/system/docker.service.d/docker.conf` with the following contents,
to remove the `-H` argument that's used when starting the daemon by default.

```systemd
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd
```

There are other times when you might need to configure `systemd` with Docker,
such as [setting HTTP or HTTPS proxy variables](proxy-environment.md).

> [!NOTE]
>
> If you override this option without specifying a `hosts` entry in the
> `daemon.json` or a `-H` flag when starting Docker manually, Docker fails to
> start.

Run `sudo systemctl daemon-reload` before attempting to start Docker. If Docker
starts successfully, it's now listening on the IP address specified in the
`hosts` key of the `daemon.json` instead of a socket.

> [!IMPORTANT]
>
> Setting `hosts` in the `daemon.json` isn't supported on Docker
> Desktop for Windows or Docker Desktop for Mac.

### Out of memory issues {#out-of-memory-issues}

If your containers attempt to use more memory than the system has available, you
may experience an Out of Memory (OOM) exception, and a container, or the Docker
daemon, might be stopped by the kernel OOM killer. To prevent this from
happening, ensure that your application runs on hosts with adequate memory and
see
[Understand the risks of running out of memory](../containers/memory-context.md#understand-the-risks-of-running-out-of-memory).

### Kernel compatibility {#kernel-compatibility}

See [Check kernel compatibility](kernel-requirements.md#kernel-compatibility).

### Kernel cgroup swap limit capabilities {#kernel-cgroup-swap-limit-capabilities}

See [Kernel cgroup swap limit capabilities](kernel-requirements.md#kernel-cgroup-swap-limit-capabilities).
