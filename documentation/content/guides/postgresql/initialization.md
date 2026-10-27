---
title: "PostgreSQL initialization behavior"
description: "PostgreSQL initialization behavior"
---

## Initialization scripts

The official PostgreSQL Docker image supports running initialization scripts automatically when the container starts for the first time. Any files placed in the `/docker-entrypoint-initdb.d/` directory are executed in alphabetical order.

### How initialization works

When the container starts, it checks whether the PostgreSQL data directory is empty. If the directory already contains data, PostgreSQL starts immediately without running any initialization. If the directory is empty, the container runs `initdb` to create a new database cluster, then executes all scripts in `/docker-entrypoint-initdb.d/` in alphabetical order before starting PostgreSQL.

### Supported file formats

| Format | Description |
|--------|-------------|
| `.sql` | SQL commands executed directly |
| `.sql.gz` | Gzip-compressed SQL files |
| `.sh` | Shell scripts executed with bash |

> [!IMPORTANT]
>
> Initialization scripts only run when the PostgreSQL data directory (`/var/lib/postgresql/data`) is empty. If you mount a volume containing existing data, initialization is skipped. This behavior prevents overwriting existing databases.
