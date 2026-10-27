---
title: "Connecting to the database"
description: "Connecting to the database"
---

## Before you begin

[Persistent PostgreSQL storage](named-volumes.md).

[Volume storage and lifecycle](/manuals/engine/storage/volumes.md).

## Connecting to the database

You can interact with PostgreSQL running in a container even without `psql` installed on your host machine.

### Interactive shell

Open a `psql` session inside the container:

```console
$ docker exec -it postgres-container psql -U postgres
```

Connect to a specific database:

```console
$ docker exec -it postgres-container psql -U postgres -d mydb
```
