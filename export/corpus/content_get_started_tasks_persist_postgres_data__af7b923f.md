---
title: Persist and inspect Postgres data with a volume
keywords: concepts, build, images, container, docker desktop
description: This concept page will teach you the significance of data persistence in Docker
---

## Before you begin

[Persisting container data](/get-started/docker-concepts/running-containers/persisting-container-data.md).

- [Volume lifecycle and procedures](/manuals/engine/storage/volumes.md)

## Try it out

In this guide, you'll practice creating and using volumes to persist data created by a Postgres container. When the database runs, it stores files into the `/var/lib/postgresql` directory. By attaching the volume here, you will be able to restart the container multiple times while keeping the data.

### Use volumes

1. [Download and install](/get-started/get-docker/) Docker Desktop.

2. Start a container using the [Postgres image](https://hub.docker.com/_/postgres) with the following command:

    ```console
    $ docker run --name=db -e POSTGRES_PASSWORD=secret -d -v postgres_data:/var/lib/postgresql postgres:18
    ```

    This will start the database in the background, configure it with a password, and attach a volume to the directory PostgreSQL will persist the database files.

3. Connect to the database by using the following command:

    ```console
    $ docker exec -ti db psql -U postgres
    ```

4. In the PostgreSQL command line, run the following to create a database table and insert two records:

    ```text
    CREATE TABLE tasks (
        id SERIAL PRIMARY KEY,
        description VARCHAR(100)
    );
    INSERT INTO tasks (description) VALUES ('Finish work'), ('Have fun');
    ```

5. Verify the data is in the database by running the following in the PostgreSQL command line:

    ```text
    SELECT * FROM tasks;
    ```

    You should get output that looks like the following:

    ```text
     id | description
    ----+-------------
      1 | Finish work
      2 | Have fun
    (2 rows)
    ```

6. Exit out of the PostgreSQL shell by running the following command:

    ```console
    \q
    ```

7. Stop and remove the database container. Remember that, even though the container has been deleted, the data is persisted in the `postgres_data` volume.

    ```console
    $ docker stop db
    $ docker rm db
    ```

8. Start a new container by running the following command, attaching the same volume with the persisted data:

    ```console
    $ docker run --name=new-db -d -v postgres_data:/var/lib/postgresql postgres:18
    ```

    You might have noticed that the `POSTGRES_PASSWORD` environment variable has been omitted. That’s because that variable is only used when bootstrapping a new database.

9. Verify the database still has the records by running the following command:

    ```console
    $ docker exec -ti new-db psql -U postgres -c "SELECT * FROM tasks"
    ```

### View volume contents

The Docker Desktop Dashboard provides the ability to view the contents of any volume, as well as the ability to export, import, empty, delete and clone volumes.

1. Open the Docker Desktop Dashboard and navigate to the **Volumes** view. In this view, you should see the **postgres_data** volume.

2. Select the **postgres_data** volume’s name.

3. The **Stored Data** tab shows the contents of the volume and provides the ability to navigate the files. The **Container in-use** tab displays the name of the container using the volume, the image name, the port number used by the container, and the target. A target is a path inside a container that gives access to the files in the volume. The **Exports** tab lets you export the volume. Double-clicking on a file will let you see the contents and make changes.

4. Right-click on any file to save it or delete it.


### Remove volumes

Before removing a volume, it must not be attached to any containers. If you haven’t removed the previous container, do so with the following command (the `-f` will stop the container first and then remove it):

```console
$ docker rm -f new-db
```

There are a few methods to remove volumes, including the following:

- Select the **Delete Volume** option on a volume in the Docker Desktop Dashboard.
- Use the `docker volume rm` command:

    ```console
    $ docker volume rm postgres_data
    ```
- Use the `docker volume prune` command to remove all unused volumes:

    ```console
    $ docker volume prune
    ```

## Next steps

Now that you have learned about persisting container data, it’s time to learn about sharing local files with containers.

{{< button text="Sharing local files with containers" url="/get-started/docker-concepts/running-containers/sharing-local-files" >}}
