---
title: "Read Docker Desktop logs"
tags: [Troubleshooting]
---

## Check the logs

In addition to using the diagnose option to submit logs, you can browse the logs yourself.

{{< tabs group="os" >}}
{{< tab name="Windows" >}}

In PowerShell, run:

```powershell
$ code $Env:LOCALAPPDATA\Docker\log
```

This opens up all the logs in your preferred text editor for you to explore.

{{< /tab >}}
{{< tab name="Mac" >}}

### From terminal

To watch the live flow of Docker Desktop logs in the command line, run the following script from your preferred shell.

```console
$ pred='process matches ".*(ocker|vpnkit).*" || (process in {"taskgated-helper", "launchservicesd", "kernel"} && eventMessage contains[c] "docker")'
$ /usr/bin/log stream --style syslog --level=debug --color=always --predicate "$pred"
```

Alternatively, to collect the last day of logs (`1d`) in a file, run:

```console
$ /usr/bin/log show --debug --info --style syslog --last 1d --predicate "$pred" >/tmp/logs.txt
```

### From the Console app

Mac provides a built-in log viewer, named **Console**, which you can use to check
Docker logs.

The Console lives in `/Applications/Utilities`. You can search for it with
Spotlight Search.

To read the Docker app log messages, type `docker` in the Console window search bar and press Enter. Then select `ANY` to expand the drop-down list next to your `docker` search entry, and select `Process`.

![Mac Console search for Docker app](../../images/console.png)

You can use the Console Log Query to search logs, filter the results in various
ways, and create reports.

{{< /tab >}}
{{< tab name="Linux" >}}

You can access Docker Desktop logs by running the following command:

```console
$ journalctl --user --unit=docker-desktop
```

You can also find the logs for the internal components included in Docker
Desktop at `$HOME/.docker/desktop/log/`.

{{< /tab >}}
{{< /tabs >}}

## View the Docker daemon logs

Refer to the [Read the daemon logs](/manuals/engine/daemon/logs.md) section
to learn how to view the Docker Daemon logs.
