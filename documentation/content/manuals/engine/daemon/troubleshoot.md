---
title: Troubleshooting the Docker daemon
description: Learn how to troubleshoot errors and misconfigurations in the Docker daemon
keywords: |
  docker, daemon, configuration, troubleshooting, error, fail to start,
  networking, dns resolver, ip forwarding, dnsmasq, firewall,
  Cannot connect to the Docker daemon. Is 'docker daemon' running on this host?
aliases:
  - /engine/install/troubleshoot/
  - /storage/troubleshooting_volume_errors/
  - /config/daemon/troubleshooting/
tags: [Troubleshooting]
---

This page describes how to troubleshoot and debug the daemon if you run into
issues.

You can [turn on debugging](logs.md#enable-debugging) on the daemon to learn about the runtime activity of
the daemon and to aid in troubleshooting. If the daemon is unresponsive, you can
also [force a full stack trace](logs.md#force-a-stack-trace-to-be-logged) of all
threads to be added to the daemon log by sending the `SIGUSR` signal to the
Docker daemon.

## Daemon

### Unable to connect to the Docker daemon

See [Unable to connect to the Docker daemon](troubleshoot-startup.md#unable-to-connect-to-the-docker-daemon).

### Check whether Docker is running

See [Check whether Docker is running](troubleshoot-startup.md#check-whether-docker-is-running).

#### Check which host your client is connecting to

See [Check which host your client is connecting to](troubleshoot-startup.md#check-which-host-your-client-is-connecting-to).

### Troubleshoot conflicts between the `daemon.json` and startup scripts

See [Troubleshoot conflicts between the `daemon.json` and startup scripts](troubleshoot-startup.md#troubleshoot-conflicts-between-the-daemonjson-and-startup-scripts).

#### Configure the daemon host with systemd

See [Configure the daemon host with systemd](troubleshoot-startup.md#configure-the-daemon-host-with-systemd).

### Out of memory issues

See [Out of memory issues](troubleshoot-startup.md#out-of-memory-issues).

### Kernel compatibility

See [Kernel compatibility](troubleshoot-startup.md#kernel-compatibility).

### Kernel cgroup swap limit capabilities

See [Kernel cgroup swap limit capabilities](troubleshoot-startup.md#kernel-cgroup-swap-limit-capabilities).

## Networking

### IP forwarding problems

See [IP forwarding problems](troubleshoot-network.md#ip-forwarding-problems).

### DNS resolver issues

See [DNS resolver issues](troubleshoot-network.md#dns-resolver-issues).

### Specify DNS servers for Docker

See [Specify DNS servers for Docker](troubleshoot-network.md#specify-dns-servers-for-docker).

### Turn off `dnsmasq`

See [Turn off `dnsmasq`](troubleshoot-network.md#turn-off-dnsmasq).

### Docker networks disappearing

See [Docker networks disappearing](troubleshoot-network.md#docker-networks-disappearing).

#### Uninstall `netscript`

See [Uninstall `netscript`](troubleshoot-network.md#uninstall-netscript).

#### Un-manage Docker interfaces

See [Un-manage Docker interfaces](troubleshoot-network.md#un-manage-docker-interfaces).

### Prevent Netplan from overriding network configuration

See [Prevent Netplan from overriding network configuration](troubleshoot-network.md#prevent-netplan-from-overriding-network-configuration).

## Volumes

### Unable to remove filesystem

See [Unable to remove filesystem](troubleshoot-volume-removal.md#unable-to-remove-filesystem).

