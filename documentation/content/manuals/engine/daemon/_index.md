---
description: Configuring the Docker daemon
keywords: docker, daemon, configuration
title: Docker daemon configuration overview
linkTitle: Daemon
weight: 60
aliases:
  - /articles/chef/
  - /articles/configuring/
  - /articles/dsc/
  - /articles/puppet/
  - /config/thirdparty/
  - /config/thirdparty/ansible/
  - /config/thirdparty/chef/
  - /config/thirdparty/dsc/
  - /config/thirdparty/puppet/
  - /engine/admin/
  - /engine/admin/ansible/
  - /engine/admin/chef/
  - /engine/admin/configuring/
  - /engine/admin/dsc/
  - /engine/admin/puppet/
  - /engine/articles/chef/
  - /engine/articles/configuring/
  - /engine/articles/dsc/
  - /engine/articles/puppet/
  - /engine/userguide/
  - /config/daemon/
---

Choose a daemon task:

| Task | Page |
| --- | --- |
| Start the daemon | [Start the daemon](start.md) |
| Configure daemon settings and data directories | [Daemon configuration](configuration.md) |
| Configure a proxy | [Daemon proxy configuration](proxy.md) |
| Configure remote access | [Remote access](remote-access.md) |
| Keep containers running during daemon outages | [Live restore](live-restore.md) |
| Use IPv6 | [IPv6 networking](ipv6.md) |
| Configure container runtimes | [Alternative runtimes](alternative-runtimes.md) |
| Collect daemon metrics | [Prometheus](prometheus.md) |
| Read logs and stack traces | [Daemon logs](logs.md) |
| Troubleshoot an error | [Daemon troubleshooting](troubleshoot.md) |

## Configure the Docker daemon

See [Configure the Docker daemon](configuration.md#configure-the-docker-daemon).

### Configuration file

See [Configuration file](configuration.md#configuration-file).

### Configuration using flags

See [Configuration using flags](configuration.md#configuration-using-flags).

## Daemon data directory

See [Daemon data directory](configuration.md#daemon-data-directory).

### Configure the data directory location

See [Configure the data directory location](configuration.md#configure-the-data-directory-location).

## Next steps

Many specific configuration options are discussed throughout the Docker
documentation. Some places to go next include:

- [Automatically start containers](/manuals/engine/containers/start-containers-automatically.md)
- [Limit a container's resources](/manuals/engine/containers/resource_constraints.md)
- [Configure storage drivers](/manuals/engine/storage/drivers/select-storage-driver.md)
- [Container security](/manuals/engine/security/_index.md)
- [Configure the Docker daemon to use a proxy](./proxy.md)
