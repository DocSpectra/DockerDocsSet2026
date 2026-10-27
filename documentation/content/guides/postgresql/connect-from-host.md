---
title: "Connecting from the Host (external access)"
description: "Connecting from the Host (external access)"
---

## Before you begin

[PostgreSQL with persistent storage](named-volumes.md).

[Port publishing](/get-started/docker-concepts/running-containers/publishing-ports.md).

## Connecting from the Host (external access)

To connect to PostgreSQL from your host machine using tools like `psql`, `pgAdmin`, `DBeaver`, or database management scripts, you need to publish PostgreSQL's port (`5432`) to the host. This allows external tools to reach the PostgreSQL container.

### Expose Postgres to localhost only (recommended for development)

This binds to `127.0.0.1` so it's only reachable from your local machine, not from other devices on your network. This is the most secure option for development.

```bash
docker run -d --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 127.0.0.1:5432:5432 \
  -v postgres_data:/var/lib/postgresql \
  postgres:18
```

Now connect from your host:

- **Host**: `localhost` or `127.0.0.1`
- **Port**: `5432`

If you have `psql` installed on your host:
```bash
psql -h localhost -p 5432 -U postgres
```

You'll be prompted for the password. Alternatively, you can use the `PGPASSWORD` environment variable:
```bash
PGPASSWORD=mysecretpassword psql -h localhost -p 5432 -U postgres
```

### Connecting with PostgreSQL GUI tools

Popular PostgreSQL GUI tools can connect using these common connection details: Host: `localhost`, Port: `5432`, User: `postgres`, Database: `postgres` (or your database name).

- **pgAdmin**: A web-based PostgreSQL administration and development platform
- **DBeaver**: A universal database tool that supports PostgreSQL and many other databases. Select PostgreSQL as the connection type
- **TablePlus**: A modern, native database management tool for macOS and Windows with a clean interface

All tools will prompt for the password you set with `POSTGRES_PASSWORD`.

### Expose Postgres to all network interfaces (use with caution)

To allow connections from other devices on your network, use `-p 5432:5432` instead of `-p 127.0.0.1:5432:5432`. This binds PostgreSQL to all network interfaces on your host, making it accessible from any device that can reach your host, not just localhost.

```bash
docker run -d --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql \
  postgres:18
```

> [!WARNING]
>
> Exposing PostgreSQL to all network interfaces (`0.0.0.0:5432`) makes it accessible from any device that can reach your host. Only use this in trusted network environments or behind a firewall. For production, consider using a reverse proxy or VPN instead.

### PostgreSQL security considerations for external access

When exposing PostgreSQL to external access, follow these PostgreSQL-specific security practices:

- **Avoid using the `postgres` superuser**: The default `postgres` user has full database privileges. Create dedicated users with only the permissions your application needs.
- **Use strong passwords**: PostgreSQL passwords should be complex. Consider using environment variables or secrets management instead of `hardcoding` passwords.
- **Limit network exposure**: Binding to `127.0.0.1` (localhost only) is safer than exposing to all interfaces (`0.0.0.0`).
- **Consider SSL/TLS**: For production, configure PostgreSQL to require SSL connections. The [Advanced Configuration and Initialization](advanced-configuration-and-initialization.md) guide shows how to configure PostgreSQL settings.
- **Create application-specific users**: Use initialization scripts to create users with limited privileges. For example, a read-only user for reporting or a user that can only access specific databases.

The [Advanced configuration and initialization](advanced-configuration-and-initialization.md) guide shows how to use initialization scripts to create users and roles automatically.
