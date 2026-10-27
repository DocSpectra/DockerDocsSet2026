---
title: Store configuration data using Docker Configs
description: How to store configuration data separate from the runtime
keywords: swarm, configuration, configs
---

## About configs

See [Docker config lifecycle and platform support](configs-context.md).

### Windows support

See [Config support on Windows](configs-context.md#windows-support).

## How Docker manages configs

See [Config storage, access, and lifecycle](configs-context.md#how-docker-manages-configs).

See [Rotate a config](configs-nginx.md#example-rotate-a-config) for a way to remove a config without disrupting running services.

## Read more about `docker config` commands

Use these links to read about specific commands, or continue to the
[example about using configs with a service](#advanced-example-use-configs-with-a-nginx-service).

- [`docker config create`](/reference/cli/docker/config/create/)
- [`docker config inspect`](/reference/cli/docker/config/inspect/)
- [`docker config ls`](/reference/cli/docker/config/ls/)
- [`docker config rm`](/reference/cli/docker/config/rm/)

## Examples

This section includes graduated examples which illustrate how to use
Docker configs.

> [!NOTE]
>
> These examples use a single-engine swarm and unscaled services for
> simplicity. The examples use Linux containers, but Windows containers also
> support configs.

### Defining and using configs in compose files

The `docker stack` command supports defining configs in a Compose file.
However, the `configs` key is not supported for `docker compose`. See
[the Compose file reference](/reference/compose-file/configs.md) for details.

### Simple example: Get started with configs

See [Use a config with Redis](configs-redis.md).

### Simple example: Use configs in a Windows service

See [Use a config with IIS on Windows](configs-windows.md).

### Example: Use a templated config

See [Use a templated config](configs-template.md).

### Advanced example: Use configs with a Nginx service

See [Configure Nginx with configs and rotate its configuration](configs-nginx.md).


#### Generate the site certificate

See [Generate the site certificate](configs-nginx.md#generate-the-site-certificate).

#### Configure the Nginx container

See [Configure Nginx](configs-nginx.md#configure-the-nginx-container).

### Example: Rotate a config

See [Rotate a config](configs-nginx.md#example-rotate-a-config).
