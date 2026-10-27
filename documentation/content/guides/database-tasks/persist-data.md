---
title: "Persist database data in a volume"
description: "Persist database data in a volume"
---

## Prerequisites

[Docker installed](../prerequisites.md#docker-installed). This guide uses the MySQL image for examples, but the concepts can be applied to other database images.

## Persist database data in a volume

Persisting database data in a Docker volume is necessary for ensuring that your
data survives container restarts and removals. A Docker volume lets you store
database files outside the container's writable layer, making it possible to
upgrade the container, switch bases, and share data without losing it. Here’s
how you can attach a volume to your database container using either the Docker
CLI or the Docker Desktop GUI.

Before you begin, [remove the previous MySQL container](remove-container.md).

Next, you can use either the Docker Desktop GUI or CLI to run the container with a volume.

{{< tabs group="ui" >}}
{{< tab name="CLI" >}}

To run your database container with a volume attached, include the `-v` option
with your `docker run` command, specifying a volume name and the path where the
database stores its data inside the container. If the volume doesn't exist,
Docker automatically creates it for you.

To run a database container with a volume attached, and then verify that the
data persists:

1. Run the container and attach the volume.

   ```console
   $ docker run --name my-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=mydb -v my-db-volume:/var/lib/mysql -d mysql:latest
   ```

   This command mounts the volume named `my-db-volume` to the `/var/lib/mysql` directory in the container.

2. Create some data in the database. Use the `docker exec` command to run
   `mysql` inside the container and create a table.

   ```console
   $ docker exec my-mysql mysql -u root -pmy-secret-pw -e "CREATE TABLE IF NOT EXISTS mydb.mytable (column_name VARCHAR(255)); INSERT INTO mydb.mytable (column_name) VALUES ('value');"
   ```

   This command uses the `mysql` tool in the container to create a table named
   `mytable` with a column named `column_name`, and finally inserts a value of
   `value`.

3. Stop and remove the container. Without a volume, the table you created would
   be lost when removing the container.

   ```console
   $ docker rm --force my-mysql
   ```

4. Start a new container with the volume attached. This time, you don't need to
   specify any environment variables as the configuration is saved in the
   volume.

   ```console
   $ docker run --name my-mysql -v my-db-volume:/var/lib/mysql -d mysql:latest
   ```

5. Verify that the table you created still exists. Use the `docker exec` command
   again to run `mysql` inside the container.

   ```console
   $ docker exec my-mysql mysql -u root -pmy-secret-pw -e "SELECT * FROM mydb.mytable;"
   ```

   This command uses the `mysql` tool in the container to select all the
   records from the `mytable` table.

   You should see output like the following.

   ```console
   column_name
   value
   ```

{{< /tab >}}
{{< tab name="GUI" >}}

To run a database container with a volume attached, and then verify that the
data persists:

1. Run a container with a volume attached.

   1. In the Docker Desktop Dashboard, select the global search at the top of the window.
   2. Specify `mysql` in the search box, and select the **Images** tab if not
      already selected.
   3. Hover over the **mysql** image and select **Run**.
      The **Run a new container** modal appears.
   4. Expand **Optional settings**.
   5. In the optional settings, specify the following:

      - **Container name**: `my-mysql`
      - **Environment variables**:
        - `MYSQL_ROOT_PASSWORD`:`my-secret-pw`
        - `MYSQL_DATABASE`:`mydb`
      - **Volumes**:
        - `my-db-volume`:`/var/lib/mysql`

      ![The optional settings screen with the options specified.](../images/databases-3.webp)

      Here, the name of the volume is `my-db-volume` and it is mounted in the
      container at `/var/lib/mysql`.

   6. Select `Run`.

2. Create some data in the database.

   1. In the **Containers** view, next to your container select the **Show
      container actions** icon, and then select **Open in terminal**.
   2. Run the following command in the container's terminal to add a table.

      ```console
      # mysql -u root -pmy-secret-pw -e "CREATE TABLE IF NOT EXISTS mydb.mytable (column_name VARCHAR(255)); INSERT INTO mydb.mytable (column_name) VALUES ('value');"
      ```

      This command uses the `mysql` tool in the container to create a table
      named `mytable` with a column named `column_name`, and finally inserts a
      value of value`.

3. In the **Containers** view, select the **Delete** icon next to your
   container, and then select **Delete forever**. Without a volume, the table
   you created would be lost when deleting the container.
4. Run a container with a volume attached.

   1. In the Docker Desktop Dashboard, select the global search at the top of the window.
   2. Specify `mysql` in the search box, and select the **Images** tab if not
      already selected.
   3. Hover over the **mysql** image and select **Run**.
      The **Run a new container** modal appears.
   4. Expand **Optional settings**.
   5. In the optional settings, specify the following:

      - **Container name**: `my-mysql`
      - **Environment variables**:
        - `MYSQL_ROOT_PASSWORD`:`my-secret-pw`
        - `MYSQL_DATABASE`:`mydb`
      - **Volumes**:
        - `my-db-volume`:`/var/lib/mysql`

      ![The optional settings screen with the options specified.](../images/databases-3.webp)

   6. Select `Run`.

5. Verify that the table you created still exists.

   1. In the **Containers** view, next to your container select the **Show
      container actions** icon, and then select **Open in terminal**.
   2. Run the following command in the container's terminal to verify that table
      you created still exists.

      ```console
      # mysql -u root -pmy-secret-pw -e "SELECT * FROM mydb.mytable;"
      ```

      This command uses the `mysql` tool in the container to select all the
      records from the `mytable` table.

      You should see output like the following.

      ```console
      column_name
      value
      ```

{{< /tab >}}
{{< /tabs >}}

At this point, any MySQL container that mounts the `my-db-volume` will be able
to access and save persisted data.

## Procedure and context reference

[Volume storage and lifecycle](/manuals/engine/storage/volumes.md).
