---
title: "Connect to a containerized database from another container"
description: "Connect to a containerized database from another container"
---

## Prerequisites

[Docker installed](../prerequisites.md#docker-installed). This guide uses the MySQL image for examples, but the concepts can be applied to other database images.

## Connect to a containerized database from another container

Connecting to a containerized database from another container is a common
scenario in microservices architecture and during development processes.
Docker's networking capabilities make it easy to establish this connection
without having to expose the database to the host network. This is achieved by
placing both the database container and the container that needs to access it on
the same Docker network.

Before you begin, [remove the previous MySQL container](remove-container.md).

To create a network and run containers on it:

1. Run the following command to create a Docker network named my-network.

   ```console
   $ docker network create my-network
   ```

2. Run your database container and specify the network using the `--network`
   option. This runs the container on the my-network network.

   ```console
   $ docker run --name my-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=mydb --network my-network -d mysql:latest
   ```

3. Run your other containers and specify the network using the `--network`
   option. For this example, you'll run a phpMyAdmin container that can connect
   to your database.

   1. Run a phpMyAdmin container. Use the `--network` option to specify the
      network, the `-p` option to let you access the container from your host
      machine, and the `-e` option to specify a required environment variable
      for this image.

      ```console
      $ docker run --name my-phpmyadmin -d --network my-network -p 8080:80 -e PMA_HOST=my-mysql phpmyadmin
      ```

4. Verify that the containers can communicate. For this example, you'll access
   phpMyAdmin and verify that it connects to the database.

   1. Open [http://localhost:8080](http://localhost:8080) to access your phpMyAdmin container.
   2. Log in using `root` as the username and `my-secret-pw` as the password.
      You should connect to the MySQL server and see your database listed.

At this point, any application running on your `my-network` container network
can access the MySQL service in the container at `my-mysql:3306`.

## Procedure and context reference

[Docker networks](/manuals/engine/network/_index.md).
