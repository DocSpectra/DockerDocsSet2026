---
title: "pgAdmin 4: Visual management platform"
description: "pgAdmin 4: Visual management platform"
---

## Setup and context

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## pgAdmin 4: Visual management platform

[pgAdmin in containers: server mode, image, and networking](../pgadmin-context.md#pgadmin-in-containers).

### Docker Compose configuration

To quickly deploy pgAdmin:

```yaml
pgadmin:
  image: dpage/pgadmin4:8.14
  environment:
    PGADMIN_DEFAULT_EMAIL: admin@example.com
    PGADMIN_DEFAULT_PASSWORD: secure_password
  volumes:
    - pgadmin_data:/var/lib/pgadmin
  ports:
    - "8080:80"
```

With this configuration, access the pgAdmin interface at `http://localhost:8080`. Use the email and password specified in the environment variables for initial sign in.

> [!IMPORTANT]
>
> In production environments, pass `PGADMIN_DEFAULT_PASSWORD` as an external environment variable or use Docker secrets. Storing passwords in plain text within `docker-compose.yml` poses a security risk.

[Connection pooling context](connection-pooling.md).
