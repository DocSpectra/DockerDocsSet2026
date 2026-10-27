---
title: "Run and access a JupyterLab container"
description: "Run and access a JupyterLab container"
---

## Prerequisites

[Latest Docker Desktop](prerequisites.md#latest-docker-desktop).

[JupyterLab and Docker concepts](jupyter-context.md).

[Port publishing](/get-started/docker-concepts/running-containers/publishing-ports.md).

## Run and access a JupyterLab container

In a terminal, run the following command to run your JupyterLab container.

```console
$ docker run --rm -p 8889:8888 quay.io/jupyter/base-notebook start-notebook.py --NotebookApp.token='my-token'
```

The following are the notable parts of the command:

- `-p 8889:8888`: Maps port 8889 from the host to port 8888 on the container.
- `start-notebook.py --NotebookApp.token='my-token'`: Sets an access token
  rather than using a random token.

For more details, see the [Jupyter Server Options](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#jupyter-server-options) and the [docker run CLI reference](/reference/cli/docker/container/run/).

If this is the first time you are running the image, Docker will download and
run it. The amount of time it takes to download the image will vary depending on
your network connection.

After the image downloads and runs, you can access the container. To access the
container, in a web browser navigate to
[localhost:8889/lab?token=my-token](http://localhost:8889/lab?token=my-token).

To stop the container, in the terminal press `ctrl`+`c`.
