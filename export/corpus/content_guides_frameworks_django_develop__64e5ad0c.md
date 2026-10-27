---
title: Develop Django with PostgreSQL and Compose Watch
description: Add a development stage, PostgreSQL, and Compose Watch to the Django application.
---

## Prerequisites

See [Django guide prerequisites](prerequisites.md) and [Build and run the Django production image](containerize.md).

For shared procedures and context, see [Use Compose Watch](/manuals/compose/how-tos/file-watch.md), [Volumes](/manuals/engine/storage/volumes.md), and [Networking in Compose](/manuals/compose/how-tos/networking.md).

## Set up a development environment

The production setup uses Gunicorn and requires a full image rebuild to pick up
code changes. For development, you can add a `development` stage to your
Dockerfile that uses Django's built-in server, and configure Compose Watch to
automatically sync code changes into the running container without a rebuild.

### Update the Dockerfile

Replace your `Dockerfile` with a multi-stage version that adds a `development`
stage alongside `production`:

```dockerfile {title="Dockerfile"}
# syntax=docker/dockerfile:1

# Build stage: the -dev image includes tools needed to install packages.
FROM dhi.io/python:3.14-alpine3.23-dev AS builder

# Prevent Python from writing .pyc files to disk.
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent Python from buffering stdout/stderr so logs appear immediately.
ENV PYTHONUNBUFFERED=1

RUN pip install --quiet --root-user-action=ignore uv
# Use copy mode since the cache and build filesystem are on different volumes.
ENV UV_LINK_MODE=copy

WORKDIR /app

# Install dependencies into a virtual environment using cache and bind mounts
# so neither uv nor the lock files need to be copied into the image.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# The development stage inherits the -dev image and virtual environment from
# the builder. Django's built-in server reloads when Compose Watch syncs files.
FROM builder AS development

ENV PATH="/app/.venv/bin:$PATH"

COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# The production stage uses the minimal runtime image, which has no shell,
# no package manager, and already runs as the nonroot user.
FROM dhi.io/python:3.14-alpine3.23 AS production

# Prevent Python from buffering stdout/stderr so logs appear immediately.
ENV PYTHONUNBUFFERED=1
# Activate the virtual environment copied from the build stage.
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copy only the pre-built virtual environment and application source code.
COPY --from=builder /app/.venv /app/.venv
COPY . .

EXPOSE 8000

# Run Gunicorn as the production WSGI server.
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Update the Compose file

Replace your `compose.yaml` with the following. It targets the `development`
stage, adds a PostgreSQL database, and configures Compose Watch:

```yaml {title="compose.yaml"}
services:
  web:
    build:
      context: .
      # Build the development stage from the multi-stage Dockerfile.
      target: development
    ports:
      - "8000:8000"
    environment:
      # Enable Django's verbose debug error pages (the dev server always auto-reloads).
      - DEBUG=1
      # Database connection settings passed to Django via environment variables.
      - POSTGRES_DB=myapp
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_HOST=db
      - POSTGRES_PORT=5432
    # Wait for the database to pass its healthcheck before starting the web service.
    depends_on:
      db:
        condition: service_healthy
    develop:
      watch:
        # Sync source file changes directly into the container so Django's
        # dev server can reload them without a full image rebuild.
        - action: sync
          path: .
          target: /app
          ignore:
            - __pycache__/
            - "*.pyc"
            - .git/
            - .venv/
        # Rebuild the image when dependencies change.
        - action: rebuild
          path: pyproject.toml
        - action: rebuild
          path: uv.lock
  db:
    image: dhi.io/postgres:18
    restart: always
    volumes:
      # Persist database data across container restarts.
      - db-data:/var/lib/postgresql
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    # Expose the port only to other services on the Compose network,
    # not to the host machine.
    expose:
      - 5432
    # Only report healthy once PostgreSQL is ready to accept connections,
    # so the web service doesn't start before the database is available.
    healthcheck:
      test: ["CMD", "pg_isready"]
      interval: 10s
      timeout: 5s
      retries: 5
volumes:
  db-data:
```

The `sync` action pushes file changes directly into the running container so
Django's dev server reloads them automatically. A change to `pyproject.toml` or
`uv.lock` triggers a full image rebuild instead.

> [!NOTE]
>
> To learn more about Compose Watch, see [Use Compose
> Watch](/manuals/compose/how-tos/file-watch.md).

### Add the PostgreSQL driver

Add the `psycopg` adapter to your project:

{{< tabs >}} {{< tab name="Local (uv)" >}}

```console
$ uv add 'psycopg[binary]'
```

{{< /tab >}} {{< tab name="Container (DHI)" >}}

```console
$ docker run --rm -v $PWD:$PWD -w $PWD \
  -e UV_LINK_MODE=copy \
  dhi.io/python:3.14-alpine3.23-dev \
  sh -c "pip install --quiet --root-user-action=ignore uv && uv add 'psycopg[binary]'"
```

{{< /tab >}} {{< /tabs >}}

Then update `myapp/settings.py` to read `DEBUG` and `DATABASES` from environment
variables:

```python {title="myapp/settings.py"}
import os

DEBUG = os.environ.get('DEBUG', '0') == '1'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "myapp"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}
```

### Run with Compose Watch

Start the development stack:

```console
$ docker compose watch
```

Open a browser and navigate to [http://localhost:8000](http://localhost:8000).

Try editing a file, for example add a view to `myapp/views.py`. Compose Watch
syncs the change into the container and Django's dev server reloads
automatically. If you update `pyproject.toml` or `uv.lock`, Compose Watch
triggers a full image rebuild.

Press `ctrl`+`c` to stop.

