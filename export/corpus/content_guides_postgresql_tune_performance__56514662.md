---
title: "Performance tuning"
description: "Performance tuning"
---

## Before you begin

[Persistent PostgreSQL storage](named-volumes.md).

[Initialization script setup](initialize-database.md).

[Volume storage and lifecycle](/manuals/engine/storage/volumes.md).

## Performance tuning

Default PostgreSQL settings are conservative to work on systems with limited resources. For production workloads, you should tune these parameters based on your container's allocated resources.

### Custom configuration file

For complete control, mount a custom `postgresql.conf` file. First, extract the default configuration:

```console
$ docker run -i --rm postgres:18 cat /usr/share/postgresql/postgresql.conf.sample > my-postgres.conf
```

Edit `my-postgres.conf` with your desired settings, then mount it in your Compose file:

```yaml
services:
  db:
    image: postgres:18
    volumes:
      - ./my-postgres.conf:/etc/postgresql/postgresql.conf
      - ./init-db:/docker-entrypoint-initdb.d
      - postgres_data:/var/lib/postgresql
    command: postgres -c config_file=/etc/postgresql/postgresql.conf
    environment:
      POSTGRES_PASSWORD: mysecretpassword

volumes:
  postgres_data:
```

## Key configuration parameters

The following tables list important `postgresql.conf` parameters for containerized PostgreSQL deployments.

### Connection settings

| Parameter | Description | Default |
|-----------|-------------|---------|
| `listen_addresses` | IP addresses to listen on | `localhost` |
| `port` | TCP port number | `5432` |
| `max_connections` | Maximum concurrent connections | `100` |

### Memory settings

| Parameter | Description | Recommended starting value |
|-----------|-------------|---------------------------|
| `shared_buffers` | Shared memory for caching | 25% of container memory |
| `work_mem` | Memory per query operation | 4MB - 64MB |
| `maintenance_work_mem` | Memory for VACUUM, CREATE INDEX | 64MB - 256MB |
| `effective_cache_size` | Planner's cache size estimate | 50-75% of container memory |

#### Docker memory limits

When tuning memory parameters, set explicit memory limits on your container using `deploy.resources.limits.memory` in Compose or `--memory` with `docker run`. Without limits, PostgreSQL sees the host's total RAM and may allocate more than intended. For example, if your container should use 4GB maximum, set `shared_buffers` to approximately 1GB (25%).

### I/O settings

| Parameter | Description | Recommended starting value |
|-----------|-------------|---------------------------|
| `effective_io_concurrency` | Concurrent disk I/O operations | `200` for SSDs, `2` for HDDs |

### Timeout settings

| Parameter | Description | Default |
|-----------|-------------|---------|
| `statement_timeout` | Max time for any statement | `0` (disabled) |
| `lock_timeout` | Max time to wait for a lock | `0` (disabled) |
| `deadlock_timeout` | Time before checking for deadlock | `1s` |
| `transaction_timeout` | Max time for a transaction | `0` (disabled) |

> [!NOTE]
>
> Setting `shared_buffers` too high in a container can exceed kernel shared memory limits. Use no more than 25-30% of the container's memory limit.
