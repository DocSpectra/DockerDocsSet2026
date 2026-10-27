---
title: "Bind mounts (alternative)"
description: "Bind mounts (alternative)"
---

## Before you begin

[Docker installed](../prerequisites.md#docker-installed).

## Bind mounts (alternative)

Bind mounts map a specific host directory to a container path. Unlike named volumes, you control exactly where data lives on the host filesystem.

Create a directory on your host machine to store Postgres data.

{{< tabs >}}
{{< tab name="Using DHIs" >}}

[Docker Hardened Images context and authentication](../hardened-image-access.md).

```console
mkdir -p ~/postgres-data && sudo chown -R 999:999 ~/postgres-data
```

Run Postgres using a bind mount.

```console
docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -v ~/postgres-data:/var/lib/postgresql \
  -d dhi.io/postgres:18
```

{{< /tab >}}

{{< tab name="Using DOIs" >}}

```console
$ mkdir -p ~/postgres-data
```

Run Postgres using a bind mount.

```console
$ docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -v ~/postgres-data:/var/lib/postgresql \
  -d postgres:18
```

{{< /tab >}}
{{< /tabs >}}

### When to use bind mounts

Bind mounts are useful when you need direct filesystem access to the data directory for backup scripts that read files directly, when integrating with host-level monitoring tools, or when specific permission requirements exist. For most development and production scenarios, named volumes are simpler and less error-prone.

### Common bind mount issues

Permission errors are the most frequent problem with bind mounts. PostgreSQL runs as user `postgres` (UID 999) inside the container. If your host directory has restrictive permissions, the container fails to start.

Check logs if the container exits immediately:

```console
$ docker logs postgres-dev
```

## Shared procedure and context

[Volume storage and lifecycle](/manuals/engine/storage/volumes.md).
