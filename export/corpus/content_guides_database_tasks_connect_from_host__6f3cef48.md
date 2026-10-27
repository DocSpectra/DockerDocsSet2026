---
title: "Connect to a containerized database from your host"
description: "Connect to a containerized database from your host"
---

## Prerequisites

[Docker installed](../prerequisites.md#docker-installed). This guide uses the MySQL image for examples, but the concepts can be applied to other database images.

## Connect to a containerized database from your host

Connecting to a containerized database from your host machine involves mapping a
port inside the container to a port on your host machine. This process ensures
that the database inside the container is accessible via the host machine's
network. For MySQL, the default port is 3306. By exposing this port, you can use
various database management tools or applications on your host machine to
interact with your MySQL database.

Before you begin, [remove the previous MySQL container](remove-container.md).

Next, you can use either the Docker Desktop GUI or CLI to run the container with
the port mapped.

{{< tabs group="ui" >}}
{{< tab name="CLI" >}}

Run the following command in a terminal.

```console
$ docker run -p 3307:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=mydb -d mysql:latest
```

In this command, `-p 3307:3306` maps port 3307 on the host to port 3306 in the container.

To verify the port is mapped, run the following command.

```console
$ docker ps
```

You should see output like the following.

```console
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                               NAMES
6eb776cfd73c   mysql:latest   "docker-entrypoint.s…"   17 minutes ago   Up 17 minutes   33060/tcp, 0.0.0.0:3307->3306/tcp   my-mysql
```

{{< /tab >}}
{{< tab name="GUI" >}}

To run a container using the GUI:

1. In the Docker Desktop Dashboard, select the global search at the top of the window.
2. Specify `mysql` in the search box, and select the `Images` tab if not already
   selected.
3. Hover over the `mysql` image and select `Run`.
   The **Run a new container** modal appears.
4. Expand **Optional settings**.
5. In the optional settings, specify the following:

   - **Container name**: `my-mysql`
   - **Host port** for the **3306/tcp** port: `3307`
   - **Environment variables**:
     - `MYSQL_ROOT_PASSWORD`:`my-secret-pw`
     - `MYSQL_DATABASE`:`mydb`

   ![The optional settings screen with the options specified.](../images/databases-2.webp)

6. Select `Run`.
7. In the **Containers** view, verify that the port is mapped under the
   **Port(s)** column. You should see **3307:3306** for the **my-mysql**
   container.

{{< /tab >}}
{{< /tabs >}}

At this point, any application running on your host can access the MySQL service in the container at `localhost:3307`.

## Procedure and context reference

[Port publishing](/get-started/docker-concepts/running-containers/publishing-ports.md).
