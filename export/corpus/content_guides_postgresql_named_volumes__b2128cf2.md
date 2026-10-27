---
title: "Named volumes"
description: "Named volumes"
---

## Context

[Data persistence demonstration](data-persistence.md).

## Named volumes

Named volumes are Docker-managed storage locations that persist independently of containers. Docker handles the filesystem location, permissions, and lifecycle.

Create a container with a named volume:

{{< tabs >}}
{{< tab name="Using DHIs" >}}

[Authenticate to pull Docker Hardened Images](../hardened-image-access.md#authenticate).

```console
$ docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql \
  -d dhi.io/postgres:18
```

{{< /tab >}}

{{< tab name="Using DOIs" >}}

```console
$ docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql \
  -d postgres:18
```

{{< /tab >}}
{{< /tabs >}}


The `-v postgres_data:/var/lib/postgresql` flag mounts a named volume called `postgres_data` to PostgreSQL's data directory. If the volume doesn't exist, Docker creates it automatically.

> [!NOTE]
>
> PostgreSQL 18+ stores data in a version-specific subdirectory under `/var/lib/postgresql`. Mounting at this level (rather than `/var/lib/postgresql/data`) allows for easier upgrades using `pg_upgrade --link`.

### Verify persistence works

To verify data persistence, repeat the [data persistence test](data-persistence.md), but this time with the named volume attached in place.

{{< tabs >}}
{{< tab name="Using DHIs" >}}

```console
$ docker exec postgres-dev psql -U postgres -c "CREATE DATABASE testdb;"
CREATE DATABASE

$ docker stop postgres-dev
postgres-dev

$ docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql \
  -d dhi.io/postgres:18

$ docker exec postgres-dev psql -U postgres -c "\l" | grep testdb
 testdb    | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |
```

{{< /tab >}}

{{< tab name="Using DOIs" >}}

```console
$ docker exec postgres-dev psql -U postgres -c "CREATE DATABASE testdb;"
CREATE DATABASE

$ docker stop postgres-dev
postgres-dev

$ docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql \
  -d postgres:18

$ docker exec postgres-dev psql -U postgres -c "\l" | grep testdb
 testdb    | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |
```

{{< /tab >}}

{{< /tabs >}}

If you see `testdb` in the output, persistence works: The database survived because the volume preserved the data directory.

### Managing volumes

List all volumes:

```console
$ docker volume ls --filter name=postgres_data
DRIVER    VOLUME NAME
local     postgres_data
```

Inspect a volume to see its details:

```console
$ docker volume inspect postgres_data
[
    {
        "CreatedAt": "2025-01-05T10:30:00Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/postgres_data/_data",
        "Name": "postgres_data",
        "Options": null,
        "Scope": "local"
    }
]
```

Remove an unused volume (warning: this deletes all data):

```console
$ docker volume rm postgres_data
```

## Shared procedure and context

[Volume storage and lifecycle](/manuals/engine/storage/volumes.md).
