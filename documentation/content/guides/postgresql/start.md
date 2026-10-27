---
title: "Start PostgreSQL and open psql"
description: "Start PostgreSQL and open psql"
---

## Prerequisites

[Docker installed](../prerequisites.md#docker-installed).

[Port publishing](/get-started/docker-concepts/running-containers/publishing-ports.md).

## Quick start (minimal viable container)

[Docker Hardened Images context and authentication](../hardened-image-access.md).

Run PostgreSQL immediately with this single command:

{{< tabs >}}
{{< tab name="Using DHIs" >}}

[Authenticate to pull Docker Hardened Images](../hardened-image-access.md#authenticate).

```console
docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -d dhi.io/postgres:18
```

{{< /tab >}}

{{< tab name="Using DOIs" >}}

```console
$ docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -d postgres:18
```

{{< /tab >}}
{{< /tabs >}}

### Understanding the flags

| Flag | Purpose |
|------|---------|
| `--rm` | Automatically removes the container when it stops |
| `--name postgres-dev` | Assigns a memorable name instead of a random string |
| `-e POSTGRES_PASSWORD=...` | Sets the superuser password (required) |
| `-p 5432:5432` | Maps host port 5432 to container port 5432 |
| `-d` | Runs the container in the background (detached mode) |

Verify the container is running:

```console
$ docker ps --filter name=postgres-dev
CONTAINER ID   IMAGE         COMMAND                  STATUS         PORTS                    NAMES
a1b2c3d4e5f6   postgres:18   "docker-entrypoint.s…"   Up 2 seconds   0.0.0.0:5432->5432/tcp   postgres-dev
```

Connect using `psql` from inside the container:

```console
$ docker exec -it postgres-dev psql -U postgres
psql (18.0)
Type "help" for help.

postgres=#
```

You now have a working PostgreSQL instance. But there's a problem—stop this container and your data disappears.
