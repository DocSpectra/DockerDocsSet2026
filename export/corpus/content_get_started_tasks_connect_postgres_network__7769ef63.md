---
title: Connect Postgres to a custom network
---

## Before you begin

- [Docker Desktop installation](/get-started/get-docker.md)
- [Container defaults and networking](/get-started/docker-concepts/running-containers/overriding-container-defaults.md)

## Run Postgres container in a controlled network

[Review bridge networks and their DNS and isolation differences](/get-started/docker-concepts/running-containers/overriding-container-defaults.md#bridge-networks-and-name-resolution).

Follow the steps to see how to connect a Postgres container to a custom network.

1. Create a new custom network by using the following command:

    ```console
    $ docker network create mynetwork
    ```

2. Verify the network by running the following command:

    ```console
    $ docker network ls
    ```

    This command lists all networks, including the newly created "mynetwork".

3. Connect Postgres to the custom network by using the following command:

    ```console
    $ docker run -d -e POSTGRES_PASSWORD=secret -p 5434:5432 --network mynetwork postgres
    ```

    This will start Postgres container in the background, mapped to the host port 5434 and attached to the `mynetwork` network. You passed the `--network` parameter to override the container default by connecting the container to custom Docker network for better isolation and communication with other containers. You can use `docker network inspect` command to see if the container is tied to this new bridge network.
