---
title: Build and run the Django production image
description: Create the Django Dockerfile and Compose file, then run the application.
---

## Prerequisites

See [Django guide prerequisites](prerequisites.md) and [Create the Django project](create-project.md).

For build-stage context, see [Multi-stage builds](/manuals/build/building/multi-stage.md).

## Create a production Dockerfile

Docker Hardened Images are production-ready base images maintained by Docker
that minimize attack surface. For more details, see [Docker Hardened
Images](/dhi/).

1. Sign in to the DHI registry:

   ```console
   $ docker login dhi.io
   ```

2. Create a `.dockerignore` file to exclude local artifacts from the build
   context:

   ```text {title=".dockerignore"}
   .venv/
   __pycache__/
   *.pyc
   .git/
   ```

3. Create a `Dockerfile` with the following contents:

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

   # Runtime stage: minimal DHI image with no shell or package manager,
   # already runs as the nonroot user.
   FROM dhi.io/python:3.14-alpine3.23

   # Prevent Python from buffering stdout/stderr so logs appear immediately.
   ENV PYTHONUNBUFFERED=1
   # Activate the virtual environment copied from the build stage.
   ENV PATH="/app/.venv/bin:$PATH"

   WORKDIR /app

   # Copy the pre-built virtual environment and application source code.
   COPY --from=builder /app/.venv /app/.venv
   COPY . .

   EXPOSE 8000

   # Run Gunicorn as the production WSGI server.
   CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]
   ```

4. Create a `compose.yaml` file:

   ```yaml {title="compose.yaml"}
   services:
     web:
       build: .
       ports:
         - "8000:8000"
   ```

### Run the application

From the `django-docker` directory, run:

```console
$ docker compose up --build
```

Open a browser and navigate to [http://localhost:8000](http://localhost:8000).
You should see the Django welcome page.

Press `ctrl`+`c` to stop the application.

