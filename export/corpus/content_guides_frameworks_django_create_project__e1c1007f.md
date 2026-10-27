---
title: Create the Django project with uv
description: Scaffold the Django project locally or in a Docker Hardened Image container.
---

## Prerequisites

See [Django guide prerequisites](prerequisites.md).

## Create the Django project

You can bootstrap the project with a local uv installation, or entirely inside a
container using the same DHI image the Dockerfile uses, with no local Python
required.

{{< tabs >}} {{< tab name="Local (uv)" >}}

1. Initialize the project pinned to Python 3.14, then navigate into it:

   ```console
   $ uv init --python 3.14 django-docker
   $ cd django-docker
   ```

2. Add Django and Gunicorn, then scaffold the Django project:

   ```console
   $ uv add django gunicorn
   $ uv run django-admin startproject myapp .
   ```

{{< /tab >}} {{< tab name="Container (DHI)" >}}

The DHI dev image already has Python 3.14, so the bootstrapped project will
match the Dockerfile exactly.

1. Create the project directory and navigate into it:

   ```console
   $ mkdir django-docker && cd django-docker
   ```

2. Initialize the project, add dependencies, and scaffold. All in one container
   run:

   ```console
   $ docker run --rm -v $PWD:$PWD -w $PWD \
     -e UV_LINK_MODE=copy \
     dhi.io/python:3.14-alpine3.23-dev \
     sh -c "pip install --quiet --root-user-action=ignore uv && uv init --name django-docker --python 3.14 . && uv add django gunicorn && uv run django-admin startproject myapp ."
   ```

   > [!NOTE]
   >
   > The previous command uses Mac/Linux shell syntax. On Windows, adjust
   > the path: PowerShell uses `${PWD}`, Command Prompt uses `%cd%`, Git Bash
   > requires `MSYS_NO_PATHCONV=1` with `$(pwd -W)`.

{{< /tab >}} {{< /tabs >}}

Your directory should now contain the following files:

```text
├── .python-version
├── main.py
├── manage.py
├── myapp/
│ ├── __init__.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── pyproject.toml
├── uv.lock
└── README.md
```

