---
title: Sync frontend files and rebuild a backend
description: Use the Compose Develop frontend and backend example.
---

## Availability and workflow

> [!NOTE]
>
> Develop is an optional part of the Compose Specification. It is available with Docker Compose version 2.22.0 and later.

See [Compose Watch setup and prerequisites](/manuals/compose/how-tos/file-watch.md), [watch rules and action version requirements](develop.md#watch), and [build configuration](build.md).

## Illustrative example

```yaml
services:
  frontend:
    image: example/webapp
    build: ./webapp
    develop:
      watch: 
        # sync static content
        - path: ./webapp/html
          action: sync
          target: /var/www
          ignore:
            - node_modules/

  backend:
    image: example/backend
    build: ./backend
    develop:
      watch: 
        # rebuild image and recreate service
        - path: ./backend/src
          action: rebuild
```

