---
title: "Run a custom JupyterLab environment with Compose"
description: "Run a custom JupyterLab environment with Compose"
---

## Prerequisites

[Latest Docker Desktop](prerequisites.md#latest-docker-desktop).

[JupyterLab and Docker concepts](jupyter-context.md).

[Define the environment in a Dockerfile](jupyter-customize.md#define-your-environment-in-a-dockerfile).

## Use Compose to run your container

Docker Compose is a tool for defining and running multi-container applications.
In this case, the application isn't a multi-container application, but Docker
Compose can make it easier to run by defining all the `docker run` options in a
file.

### Create a Compose file

To use Compose, you need a `compose.yaml` file. In the same directory as your
`Dockerfile`, create a new file named `compose.yaml`.

Open the `compose.yaml` file in an IDE or text editor and add the following
contents.

```yaml
services:
  jupyter:
    build:
      context: .
    ports:
      - 8889:8888
    volumes:
      - jupyter-data:/home/jovyan/work
    command: start-notebook.py --NotebookApp.token='my-token'

volumes:
  jupyter-data:
    name: jupyter-data
```

This Compose file specifies all the options you used in the `docker run` command. For more details about the Compose instructions, see the
[Compose file reference](/reference/compose-file/_index.md).

Before you proceed, save your changes to the `compose.yaml` file.

### Run your container using Compose

Open a terminal, change directory to where your `compose.yaml` file is located, and then run the following command.

```console
$ docker compose up --build
```

This command builds your image and runs it as a container using the instructions
specified in the `compose.yaml` file. The `--build` option ensures that your
image is rebuilt, which is necessary if you made changes to your `Dockerfile`.

To access the container, in a web browser navigate to
[localhost:8889/lab?token=my-token](http://localhost:8889/lab?token=my-token).

In the terminal, press `ctrl`+ `c` to stop the container.
