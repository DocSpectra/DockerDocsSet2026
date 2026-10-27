---
title: "Internal network access (container-to-container)"
description: "Internal network access (container-to-container)"
---

## Before you begin

[PostgreSQL with persistent storage](named-volumes.md).

[User-defined bridge networks](/manuals/engine/network/drivers/bridge.md).

## Internal network access (container-to-container)

When your application runs in another container, connecting to PostgreSQL through a user-defined bridge network is the recommended approach. This setup provides automatic DNS resolution, so your application can connect to PostgreSQL using the container name as the hostname, without needing to track IP addresses.

> **Why not use the default bridge network?** While containers on the default bridge network can communicate, they can only do so by IP address. Since container IP addresses change when containers restart, this would require updating your PostgreSQL connection strings each time. User-defined bridge networks solve this by providing automatic DNS resolution, ensuring your PostgreSQL connection strings remain stable even if containers restart and receive new IP addresses.

Here's a quick comparison:

> [!NOTE]
>
> The following examples show the difference in approach. To actually test this, follow the steps in this guide to set up containers on the appropriate networks first.

With the default bridge network, you'd need to find the IP address first:
```bash
# Get the container's IP address (changes on restart)
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-dev
# Output: 172.17.0.2

# Then connect using that IP address from another container
# (No --network flag needed - containers default to bridge network)
docker run --rm -it \
  -e PGPASSWORD=mysecretpassword \
  postgres:18 \
  psql -h 172.17.0.2 -U postgres
```

With a user-defined network, you simply use the container name:
```bash
# Container name works directly - no IP lookup needed
docker run --rm -it \
  --network my-app-net \
  -e PGPASSWORD=mysecretpassword \
  postgres:18 \
  psql -h postgres-dev -U postgres
```

### Step 1: Create a user-defined network

```bash
docker network create my-app-net

# Example Output
ab7f984be43a0ca15534a9ee568716ddbe869a5875077fad3ef3192e3af7d288

docker network ls
# Output
ab7f984be43a   my-app-net    bridge    local


```

### Step 2: Run PostgreSQL on that network (no port publishing)

Notice there is no `-p 5432:5432` here. This keeps PostgreSQL internal to Docker and not accessible from the host machine, which is more secure for production environments.

```bash
docker run -d --name postgres-dev \
  --network my-app-net \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -v postgres_data:/var/lib/postgresql \
  postgres:18

  # Output
CONTAINER ID  IMAGE        COMMAND                 CREATED         STATUS        PORTS     NAMES
6d351ed89efc  postgres:18  "docker-entrypoint.s…"  9 seconds ago   Up 8 seconds  5432/tcp  postgres-dev

```

### Step 3: Connect from another container using the Postgres container name

You can test connectivity with a temporary `psql` client container:

```bash
docker run --rm -it \
  --network my-app-net \
  -e PGPASSWORD=mysecretpassword \
  postgres:18 \
  psql -h postgres-dev -U postgres
```

**Key point**: `-h postgres-dev` works because Docker DNS resolves the container name on a user-defined network. The container name acts as the hostname.

### Connection string examples

When connecting from your application container, use these PostgreSQL connection strings:

- **PostgreSQL URI format**:
  This is the standard PostgreSQL connection URI format that combines all connection parameters into a single string, widely supported by PostgreSQL clients and libraries.

  ```bash
  postgresql://postgres:mysecretpassword@postgres-dev:5432/postgres
  ```

  This command demonstrates passing a PostgreSQL URI connection string as an environment variable to a container, which your application can then read to connect to the database.

  Example usage in a Docker run command:
  ```bash
  docker run --rm -it \
    --network my-app-net \
    -e DATABASE_URL="postgresql://postgres:mysecretpassword@postgres-dev:5432/postgres" \
    alpine:latest \
    sh -c 'echo "DATABASE_URL is set to: $DATABASE_URL"'
  ```


- **PostgreSQL connection parameters**:
  This format uses key-value pairs separated by spaces, which many PostgreSQL client libraries accept as an alternative to URI format.
  ```bash
  host=postgres-dev
  port=5432
  user=postgres
  password=mysecretpassword
  dbname=postgres
  ```

  Example usage in application code (Python with psycopg2):
  ```python
  conn = psycopg2.connect(
      host="postgres-dev",
      port=5432,
      user="postgres",
      password="mysecretpassword",
      dbname="postgres"
  )
  ```

- **Connecting to a specific database**:
  Replace the database name in the connection string to connect to a specific database instead of the default `postgres` database.
  If you created a custom database (e.g., `testdb`), use:
  ```bash
  postgresql://postgres:mysecretpassword@postgres-dev:5432/testdb
  ```

  Example with SSL disabled (common in Docker networks):
  Add `?sslmode=disable` to the connection string when connecting within a private Docker network where SSL encryption isn't required.
  ```bash
  postgresql://postgres:mysecretpassword@postgres-dev:5432/testdb?sslmode=disable
  ```

> [!NOTE]
>
> The default port `5432` is used in these examples. If you're connecting to a different PostgreSQL instance or have changed the port, update the connection string accordingly. The container name (`postgres-dev`) is resolved by Docker DNS to the container's IP address on the network.
