---
title: Wait for healthy service dependencies
description: Configure dependency startup with short and long depends_on syntax.
---

## Dependency rules and caveats

See [dependency conditions, restart scope, required dependencies, and version requirements](services.md#depends_on), [healthcheck configuration](services.md#healthcheck), and [profile dependency restrictions](profiles.md).

## Start dependencies with short syntax

Simple example:

```yml
services:
  web:
    build: .
    depends_on:
      - db
      - redis
  redis:
    image: redis
  db:
    image: postgres:18
```

Compose guarantees dependency services have been started before
starting a dependent service.
With short syntax, Compose does not wait for dependency services to be "healthy" before
starting a dependent service.

## Wait for healthchecks with long syntax

Service dependencies cause the following behaviors:

- Compose creates services in dependency order. In the following
  example, `db` and `redis` are created before `web`.

- Compose waits for healthchecks to pass on dependencies
  marked with `service_healthy`. In the following example, `db` is expected to
  be "healthy" before `web` is created.

- Compose removes services in dependency order. In the following
  example, `web` is removed before `db` and `redis`.

```yml
services:
  web:
    build: .
    depends_on:
      db:
        condition: service_healthy
        restart: true
      redis:
        condition: service_started
  redis:
    image: redis
  db:
    image: postgres:18
```

Compose guarantees dependency services are started before
starting a dependent service.
Compose guarantees dependency services marked with
`service_healthy` are "healthy" before starting a dependent service.

