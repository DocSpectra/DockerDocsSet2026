---
title: "Docker Compose configuration"
description: "Docker Compose configuration"
---

## Before you begin

[Docker installed](../prerequisites.md#docker-installed).

## Docker Compose configuration

Docker Compose captures your entire configuration in a file, making setups reproducible and easier to manage as complexity grows.

Create a `compose.yaml` file:

```yaml
services:
  db:
    image: postgres:18
    container_name: postgres-dev
    environment:
      POSTGRES_PASSWORD: mysecretpassword
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql

volumes:
  postgres_data:
```

Start the database:

```console
$ docker compose up -d
```

Stop and remove containers (volume persists):

```console
$ docker compose down
```

Alternatively, you can stop, remove containers, and delete the volume:

```console
$ docker compose down -v
```

This compose file becomes the foundation for adding initialization scripts, performance tuning, and companion services covered in subsequent guides.

### Environment variables reference

The official PostgreSQL image supports these environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `POSTGRES_PASSWORD` | Yes | Superuser password |
| `POSTGRES_USER` | No | Superuser name (default: `postgres`) |
| `POSTGRES_DB` | No | Default database name (default: value of `POSTGRES_USER`) |

## Shared procedure and context

[Compose file reference](/reference/compose-file/_index.md).
