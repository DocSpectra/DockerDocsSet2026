---
title: Run the Node.js application
weight: 25
description: Start, verify, and stop the containerized Node.js application.
---

## Prerequisites

[Build the Node.js image](build-images.md).

For image and container inspection, see [Inspect local images and running containers](/guides/image-build-and-inspect.md).

## Start and verify the application

Inside the `docker-nodejs-sample` directory, run the following command in a terminal.

```console
$ docker compose up app-dev --build
```

The development application will start with both servers:

- **API Server**: [http://localhost:3000](http://localhost:3000) - Express.js backend with REST API
- **Frontend**: [http://localhost:5173](http://localhost:5173) - Vite dev server with React frontend
- **Health Check**: [http://localhost:3000/health](http://localhost:3000/health) - Application health status

For production deployment, you can use:

```console
$ docker compose up app-prod --build
```

Which serves the full-stack app at [http://localhost:8080](http://localhost:8080) with the Express server running on port 3000 internally, mapped to port 8080 externally.

You should see a modern Todo List application with React 19 and a fully functional REST API.

Press `CTRL + C` in the terminal to stop your application.

### Run the application in the background

You can run the application detached from the terminal by adding the `-d` option. Inside the `docker-nodejs-sample` directory, run the following command in a terminal.

```console
$ docker compose up app-dev --build -d
```

Open a browser and view the application at [http://localhost:3000](http://localhost:3000) (API) or [http://localhost:5173](http://localhost:5173) (frontend). You should see the Todo application running.

To confirm that the container is running, use `docker ps` command:

```console
$ docker ps
```

This will list all active containers along with their ports, names, and status. Look for a container exposing ports 3000, 5173, and 9229 for the development app.

Example Output:

```shell
CONTAINER ID   IMAGE                          COMMAND                  CREATED          STATUS                 PORTS                                                                                                                                   NAMES
93f3faee32c3   docker-nodejs-sample-app-dev   "docker-entrypoint.s…"   33 seconds ago   Up 31 seconds          0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp, 0.0.0.0:5173->5173/tcp, [::]:5173->5173/tcp, 0.0.0.0:9230->9229/tcp, [::]:9230->9229/tcp   todoapp-dev
```

### Run different profiles

You can run different configurations using Docker Compose profiles:

```console
# Run production
$ docker compose up app-prod -d

# Run tests
$ docker compose up app-test -d
```

To stop the application, run:

```console
$ docker compose down
```

> [!NOTE]
> For more information about Compose commands, see the [Compose CLI
> reference](/reference/cli/docker/compose/).

---


## Continue

[Develop the Node.js application](develop.md).
