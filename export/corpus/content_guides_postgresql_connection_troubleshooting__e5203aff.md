---
title: "Troubleshooting"
description: "Troubleshooting"
---

## Before you begin

[PostgreSQL with persistent storage](named-volumes.md).

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## Troubleshooting

This section covers common PostgreSQL connection issues and their solutions when working with Docker networking.

### "Could not translate host name postgres-dev"

- Both containers must be on the same Docker network (`my-app-net`).
- Verify the network exists: `docker network ls`
- Check which network a container is on: `docker inspect postgres-dev | grep NetworkMode`
- Ensure you're using a user-defined network, not the default bridge network

### "Connection refused" or "could not connect to server"

- **PostgreSQL may still be initializing**: PostgreSQL takes a few seconds to start and initialize the database cluster. Wait 5-10 seconds after container start and retry.
- **Check if the PostgreSQL container is running**:

  ```bash
  docker ps --filter name=postgres-dev
  ```

- **Check PostgreSQL logs for initialization or connection errors**:

  ```bash
  docker logs postgres-dev
  ```

  Look for messages like "database system is ready to accept connections" to confirm PostgreSQL is fully started.

- **Verify the port mapping is correct**:

  ```bash
  docker port postgres-dev
  ```

  This should show `5432/tcp -> 127.0.0.1:5432` (or `0.0.0.0:5432` if bound to all interfaces).

- **Test PostgreSQL connectivity from inside the container**:

  ```bash
  docker exec -it postgres-dev psql -U postgres -c "SELECT version();"
  ```

  If this works but external connections fail, the issue is with port publishing, not PostgreSQL itself.

### "Password authentication failed" or "FATAL: password authentication failed for user"

- **Confirm the password**: Verify you're using the same password set in `POSTGRES_PASSWORD` when you started the container.
- **Existing volume with old credentials**: If you reused an existing volume, the password from the original initialization is still in effect. The `POSTGRES_PASSWORD` environment variable only sets the password during the first database initialization. To reset:
  - Remove the volume: `docker volume rm postgres_data`
  - Or connect with the old password
  - Or change the password after connecting: `ALTER USER postgres WITH PASSWORD 'newpassword';`
- **Try connecting with password prompt**: `psql -h localhost -U postgres -W` (the `-W` flag forces a password prompt)
- **Use PGPASSWORD environment variable**: `PGPASSWORD=mysecretpassword psql -h localhost -U postgres`
- **Check PostgreSQL authentication configuration**: If you've customized `pg_hba.conf`, verify the authentication method allows password authentication

### "Network not found"

- Ensure the network exists before starting containers: `docker network create my-app-net`
- If using Docker Compose, the network is created automatically when you run `docker compose up`
