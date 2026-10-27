---
title: "The data persistence problem"
description: "The data persistence problem"
---

## Before you begin

[Quick start](start.md#quick-start-minimal-viable-container).

## The data persistence problem

Containers use an ephemeral filesystem. When a container is removed, everything inside it, including your database files, is deleted.

Demonstrate this yourself:

{{< tabs >}}
{{< tab name="Using DHIs" >}}

[Docker Hardened Images context and authentication](../hardened-image-access.md).

```console
$ docker exec postgres-dev psql -U postgres -c "CREATE DATABASE testdb;"
CREATE DATABASE

$ docker exec postgres-dev psql -U postgres -c "\l" | grep testdb
 testdb    | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |

$ docker stop postgres-dev
postgres-dev

$ docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -d dhi.io/postgres:18

$ docker exec postgres-dev psql -U postgres -c "\l" | grep testdb
(no output - database is gone)
```

{{< /tab >}}

{{< tab name="Using DOIs" >}}

```console
$ docker exec postgres-dev psql -U postgres -c "CREATE DATABASE testdb;"
CREATE DATABASE

$ docker exec postgres-dev psql -U postgres -c "\l" | grep testdb
 testdb    | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |

$ docker stop postgres-dev
postgres-dev

$ docker run --rm --name postgres-dev \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -d postgres:18

$ docker exec postgres-dev psql -U postgres -c "\l" | grep testdb
(no output - database is gone)
```

{{< /tab >}}
{{< /tabs >}}

Your `testdb` database vanished because the new container started with a fresh filesystem. This is expected behavior—and exactly why volumes exist.

## Shared procedure and context

[Volume storage and lifecycle](/manuals/engine/storage/volumes.md).
