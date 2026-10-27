---
title: Run the Next.js application
weight: 25
description: Start, verify, and stop the containerized Next.js application.
---

## Prerequisites

[Build the Next.js image](build-images.md).

For image and container inspection, see [Inspect local images and running containers](/guides/image-build-and-inspect.md).

## Start and verify the application

Run the following command in a terminal. Use the port that matches your setup: **standalone** uses port 3000, **export** uses port 8080.

```console
$ docker run -p 3000:3000 nextjs-sample
```

For **export** output, use port 8080 instead:

```console
$ docker run -p 8080:8080 nextjs-sample
```

Open a browser and view the application: [http://localhost:3000](http://localhost:3000) for **standalone** or [http://localhost:8080](http://localhost:8080) for **export**. You should see your Next.js web application.

Press `ctrl+c` in the terminal to stop your application.

### Run the application in the background

You can run the application detached from the terminal by adding the `-d` option and `--name` to give the container a name so you can stop it later:

```console
$ docker run -d -p 3000:3000 --name nextjs-app nextjs-sample
```

For **export** output, use port 8080:

```console
$ docker run -d -p 8080:8080 --name nextjs-app nextjs-sample
```

Open a browser and view the application: [http://localhost:3000](http://localhost:3000) for **standalone** or [http://localhost:8080](http://localhost:8080) for **export**. You should see your web application.

To confirm that the container is running, use the `docker ps` command:

```console
$ docker ps
```

This will list all active containers along with their ports, names, and status. Look for a container exposing port 3000 (standalone) or 8080 (export).

Example Output:

```shell
CONTAINER ID   IMAGE           COMMAND                  CREATED             STATUS             PORTS                    NAMES
f49b74736a9d   nextjs-sample   "node server.js"         About a minute ago   Up About a minute   0.0.0.0:3000->3000/tcp nextjs-app
```

To stop the application, run:

```console
$ docker stop nextjs-app
```

> [!NOTE]
> For more information about running containers, see the [`docker run` CLI reference](/reference/cli/docker/container/run/) and the [`docker stop` CLI reference](/reference/cli/docker/container/stop/).

---


## Continue

[Develop the Next.js application](develop.md).

## Related resources

- [`docker run` CLI reference](/reference/cli/docker/container/run/) – Run a command in a new container.
- [`docker stop` CLI reference](/reference/cli/docker/container/stop/) – Stop one or more running containers.
