---
title: "Mounting initialization scripts"
description: "Mounting initialization scripts"
---

## Before you begin

[Persistent PostgreSQL storage](named-volumes.md).

[PostgreSQL initialization behavior](initialization.md).

## Mounting initialization scripts

Use Docker Compose to mount initialization scripts into the container. First, create a project directory:

```console
$ mkdir -p postgres-project/init-db
$ cd postgres-project
```

Create a `compose.yaml` file:

```yaml
services:
  db:
    image: postgres:18
    volumes:
      - ./init-db:/docker-entrypoint-initdb.d
      - postgres_data:/var/lib/postgresql
    environment:
      POSTGRES_PASSWORD: mysecretpassword

volumes:
  postgres_data:
```

All scripts in the `./init-db` directory execute when the container starts for the first time. This is great for bootstrapping databases.

## Initialization script example

Create a file named `init.sql` in your `init-db` directory:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

This script runs automatically when the container starts for the first time, creating your initial database schema.

> [!NOTE]
>
> Ensure initialization scripts have proper read permissions. If you encounter "Permission denied" errors, run `chmod 644 init-db/*.sql` to make the files readable by the container.
