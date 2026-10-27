---
title: Override Postgres startup commands
---

## Before you begin

- [Docker Desktop installation](/get-started/get-docker.md)
- [Container defaults and networking](/get-started/docker-concepts/running-containers/overriding-container-defaults.md)

## Override the default CMD and ENTRYPOINT in Docker Compose



Sometimes, you might need to override the default commands (`CMD`) or entry points (`ENTRYPOINT`) defined in a Docker image, especially when using Docker Compose.

1. Create a `compose.yml` file with the following content:

    ```yaml
    services:
      postgres:
        image: postgres:18
        entrypoint: ["docker-entrypoint.sh", "postgres"]
        command: ["-h", "localhost", "-p", "5432"]
        environment:
          POSTGRES_PASSWORD: secret 
    ```


    The Compose file defines a service named `postgres` that uses the official Postgres image, sets an entrypoint script, and starts the container with password authentication.

2. Bring up the service by running the following command:

    ```console
    $ docker compose up -d
    ```

    This command starts the Postgres service defined in the Docker Compose file.

3. Verify the authentication with Docker Desktop Dashboard.

    Open the Docker Desktop Dashboard, select the **Postgres** container and select **Exec** to enter into the container shell. You can type the following command to connect to the Postgres database:

    ```console
    # psql -U postgres
    ```

    ![A screenshot of the Docker Desktop Dashboard selecting the Postgres container and entering into its shell using EXEC button](/get-started/docker-concepts/running-containers/images/exec-into-postgres-container.webp?border=true)


    > [!NOTE]
    > 
    > The PostgreSQL image sets up trust authentication locally so you may notice a password isn't required when connecting from localhost (inside the same container). However, a password will be required if connecting from a different host/container.

## Override the default CMD and ENTRYPOINT with `docker run`

You can also override defaults directly using the `docker run` command with the following command:

```console 
$ docker run -e POSTGRES_PASSWORD=secret postgres docker-entrypoint.sh -h localhost -p 5432
```

This command runs a Postgres container, sets an environment variable for password authentication, overrides the default startup commands and configures hostname and port mapping.
