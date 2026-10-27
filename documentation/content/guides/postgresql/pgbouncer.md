---
title: "PgBouncer: Lightweight connection pooling"
description: "PgBouncer: Lightweight connection pooling"
---

## Setup and context

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## PgBouncer: Lightweight connection pooling

[Connection pooling, pooling modes, and when to use PgBouncer](connection-pooling.md).

### Complete Docker Compose setup

To run PostgreSQL and PgBouncer together, you need three files: `docker-compose.yml`, `pgbouncer.ini`, and `userlist.txt`.

First, create the PgBouncer configuration file (`pgbouncer.ini`):

```bash
[databases]
benchmark = host=postgres port=5432 dbname=benchmark user=postgres

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
auth_type = trust
auth_file = /etc/pgbouncer/userlist.txt
admin_users = postgres
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 50
min_pool_size = 10
reserve_pool_size = 10
max_db_connections = 100
```

Next, create the user authentication file (`userlist.txt`):

```bash
"postgres" "postgres"
```

Finally, create the Docker Compose file (`docker-compose.yml`):

```yaml
services:
  postgres:
    image: postgres:18
    container_name: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: benchmark
      POSTGRES_HOST_AUTH_METHOD: trust
    volumes:
      - postgres_data:/var/lib/postgresql
    ports:
      - "5432:5432"
    networks:
      - pgnet
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  pgbouncer:
    image: percona/percona-pgbouncer:1.25.0
    container_name: pgbouncer
    volumes:
      - ./pgbouncer.ini:/etc/pgbouncer/pgbouncer.ini
      - ./userlist.txt:/etc/pgbouncer/userlist.txt
    ports:
      - "6432:6432"
    networks:
      - pgnet
    depends_on:
      postgres:
        condition: service_healthy

volumes:
  postgres_data:

networks:
  pgnet:
    driver: bridge
```

Key configuration notes:

- `PgBouncer` listens on port **6432**, avoiding confusion with the direct PostgreSQL connection on port 5432
- The `depends_on` directive with `service_healthy` condition ensures PgBouncer starts only after PostgreSQL is ready
- `pool_mode = transaction` is the optimal choice for most web applications
- The [Percona PgBouncer image](https://hub.docker.com/r/percona/percona-pgbouncer) requires mounted configuration files (without the `:ro` flag, as the entrypoint script needs to modify them)
- This example uses `trust` authentication for simplicity. In production, configure proper SCRAM-SHA-256 authentication

> [!NOTE]
>
> The `Percona PgBouncer` entrypoint script processes the configuration files on startup. Mount them without the read-only flag to avoid permission errors.
