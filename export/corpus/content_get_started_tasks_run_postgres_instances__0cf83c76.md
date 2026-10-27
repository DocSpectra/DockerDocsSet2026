---
title: Run multiple Postgres instances
---

## Before you begin

- [Docker Desktop installation](/get-started/get-docker.md)
- [Container defaults and networking](/get-started/docker-concepts/running-containers/overriding-container-defaults.md)

## Run multiple instances of the Postgres database

1.  Start a container using the [Postgres image](https://hub.docker.com/_/postgres) with the following command:
    
    ```console
    $ docker run -d -e POSTGRES_PASSWORD=secret -p 5432:5432 postgres
    ```

    This will start the Postgres database in the background, listening on the standard container port `5432` and mapped to port `5432` on the host machine.

2. Start a second Postgres container mapped to a different port. 

    ```console
    $ docker run -d -e POSTGRES_PASSWORD=secret -p 5433:5432 postgres
    ```

    This will start another Postgres container in the background, listening on the standard postgres port `5432` in the container, but mapped to port `5433` on the host machine. You override the host port just to ensure that this new container doesn't conflict with the existing running container.

3. Verify that both containers are running by going to the **Containers** view in the Docker Desktop Dashboard.

    ![A screenshot of the Docker Desktop Dashboard showing the running instances of Postgres containers](/get-started/docker-concepts/running-containers/images/running-postgres-containers.webp?border=true)
