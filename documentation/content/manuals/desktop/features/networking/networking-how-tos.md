---
description: Learn how to connect containers to the host, across containers, or through proxies and VPNs in Docker Desktop.
keywords: docker desktop, networking, vpn, proxy, port mapping, dns
title: Explore networking how-tos on Docker Desktop
linkTitle: How-tos
aliases:
- /desktop/linux/networking/
- /docker-for-mac/networking/
- /mackit/networking/
- /desktop/mac/networking/
- /docker-for-win/networking/
- /docker-for-windows/networking/
- /desktop/windows/networking/
- /desktop/networking/
---

This page explains how to configure and use networking features, connect containers to host services, work behind proxies or VPNs, and troubleshoot common issues.

For details on how Docker Desktop routes network traffic and file I/O between containers, the VM, and the host, see [Network overview](/manuals/desktop/features/networking/_index.md#overview).

## Core networking how-tos

### Connect a container to a service on the host

See [Connect containers and host services](connect-host.md#connect-a-container-to-a-service-on-the-host).

#### Example

See [Host HTTP server example](connect-host.md#example).

### Connect to a container from the host

See [Connect to a container from the host](connect-host.md#connect-to-a-container-from-the-host).

### Working with VPNs

See [Use Docker Desktop with a VPN](vpn.md).

### Working with proxies

See [Configure a Docker Desktop proxy](proxies.md).

## Network how-tos for Mac and Windows

See [Networking mode and DNS settings](network-settings.md).

### Default networking mode

See [Default networking mode](network-settings.md#default-networking-mode).

### DNS resolution behavior

See [DNS resolution behavior](network-settings.md#dns-resolution-behavior).

## Network how-tos for Mac and Linux

See [Forward the host SSH agent](ssh-agent.md).

### SSH agent forwarding

See [SSH agent forwarding](ssh-agent.md#ssh-agent-forwarding).

## Known limitations

See [Known limitations](_index.md#known-limitations).

### Changing internal IP addresses

See [Changing internal IP addresses](_index.md#changing-internal-ip-addresses).

### There is no `docker0` bridge on the host

See [There is no `docker0` bridge on the host](_index.md#there-is-no-docker0-bridge-on-the-host).

### I cannot ping my containers

See [I cannot ping my containers](_index.md#i-cannot-ping-my-containers).

### Per-container IP addressing is not possible

See [Per-container IP addressing is not possible](_index.md#per-container-ip-addressing-is-not-possible).
