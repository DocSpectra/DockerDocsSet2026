---
title: "Timezone and locale configuration"
description: "Timezone and locale configuration"
---

## Before you begin

[Persistent PostgreSQL storage](named-volumes.md).

[PostgreSQL initialization behavior](initialization.md).

## Timezone and locale configuration

Proper localization ensures timestamps and sorting behave correctly for your application's users.

```yaml
services:
  db:
    image: postgres:18
    volumes:
      - postgres_data:/var/lib/postgresql
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
    environment:
      POSTGRES_PASSWORD: mysecretpassword
      TZ: America/New_York

volumes:
  postgres_data:
```

Alternatively, set the timezone using a PostgreSQL command-line parameter:

```yaml
services:
  db:
    image: postgres:18
    command: ["postgres", "-c", "timezone=America/New_York"]
    environment:
      POSTGRES_PASSWORD: mysecretpassword
```

### Setting the locale

Specify locale settings during database initialization using the `POSTGRES_INITDB_ARGS` environment variable:

```yaml
services:
  db:
    image: postgres:18
    volumes:
      - postgres_data:/var/lib/postgresql
    environment:
      POSTGRES_PASSWORD: mysecretpassword
      POSTGRES_INITDB_ARGS: "--encoding=UTF8 --lc-collate=en_US.UTF-8 --lc-ctype=en_US.UTF-8"

volumes:
  postgres_data:
```

This affects collation (sorting) and character processing behavior. Changing this variable after database creation has no effect—it only applies during the first run when the data directory is initialized.
