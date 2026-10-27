---
title: "Using Docker Compose for networking"
description: "Using Docker Compose for networking"
---

## Before you begin

[PostgreSQL with persistent storage](named-volumes.md).

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## Using Docker Compose for networking

Docker Compose automatically creates a network for your services, making networking configuration simpler. Here's an example that combines both internal and external access:

```yaml
services:
  db:
    image: postgres:18
    container_name: postgres-dev
    environment:
      POSTGRES_PASSWORD: mysecretpassword
    volumes:
      - postgres_data:/var/lib/postgresql
    ports:
      - "127.0.0.1:5432:5432"  # Expose to localhost only
    networks:
      - app-network

  app:
    build: ./my-app
    environment:
      DATABASE_URL: postgresql://postgres:mysecretpassword@db:5432/mydb
    networks:
      - app-network
    depends_on:
      - db

volumes:
  postgres_data:

networks:
  app-network:
    driver: bridge
```

In this PostgreSQL-focused setup:
- The `app` service connects to PostgreSQL using the service name (`db`) as the hostname in the connection string
- PostgreSQL is accessible from your host at `localhost:5432` for external tools
- Both services are isolated on a custom network, providing network-level security
- The `depends_on` directive ensures PostgreSQL starts before your application

PostgreSQL connection details for the app service:
- Hostname: `db` (resolved by Docker DNS)
- Port: `5432` (PostgreSQL default port)
- Database: `mydb` (as specified in the connection string)
- User: `postgres` (or a custom user you've created)

> [!NOTE]
>
> Docker Compose automatically creates a network for your project. Services can reach each other by service name without explicit network configuration, but defining a custom network gives you more control. For PostgreSQL, this means your application can always connect using the service name, regardless of container restarts or IP changes.
