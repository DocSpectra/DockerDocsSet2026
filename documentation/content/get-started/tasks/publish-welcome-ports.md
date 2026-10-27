---
title: Publish the welcome application with CLI or Compose
keywords: concepts, build, images, container, docker desktop
description: This concept page will teach you the significance of publishing and exposing ports in Docker 
---

## Before you begin

[Publishing and exposing ports](/get-started/docker-concepts/running-containers/publishing-ports.md).

- [Port-publishing caveat](/get-started/docker-concepts/running-containers/publishing-ports.md#publishing-ports)

## Try it out

In this hands-on guide, you'll learn how to publish container ports using both the CLI and Docker Compose for deploying a web application.

### Use the Docker CLI

In this step, you will run a container and publish its port using the Docker CLI.

1. [Download and install](/get-started/get-docker/) Docker Desktop.

2. In a terminal, run the following command to start a new container:

    ```console
    $ docker run -d -p 8080:80 docker/welcome-to-docker
    ```

    The first `8080` refers to the host port. This is the port on your local machine that will be used to access the application running inside the container. The second `80` refers to the container port. This is the port that the application inside the container listens on for incoming connections. Hence, the command binds to port `8080` of the host to port `80` on the container system.

3. Verify the published port by going to the **Containers** view of the Docker Desktop Dashboard.

   ![A screenshot of Docker Desktop Dashboard showing the published port](/get-started/docker-concepts/running-containers/images/published-ports.webp?w=5000&border=true)

4. Open the website by either selecting the link in the **Port(s)** column of your container or visiting [http://localhost:8080](http://localhost:8080) in your browser.

   ![A screenshot of the landing page of the Nginx web server running in a container](/get-started/docker-concepts/the-basics/images/access-the-frontend.webp?border=true)


### Use Docker Compose

This example will launch the same application using Docker Compose:

1. Create a new directory and inside that directory, create a `compose.yaml` file with the following contents:

    ```yaml
    services:
      app:
        image: docker/welcome-to-docker
        ports:
          - 8080:80
    ```

    The `ports` configuration accepts a few different forms of syntax for the port definition. In this case, you’re using the same `HOST_PORT:CONTAINER_PORT` used in the `docker run` command.

2. Open a terminal and navigate to the directory you created in the previous step.

3. Use the `docker compose up` command to start the application. 

4. Open your browser to [http://localhost:8080](http://localhost:8080).

## Next steps

Now that you understand how to publish and expose ports, you're ready to learn how to override the container defaults using the `docker run` command.

{{< button text="Overriding container defaults" url="/get-started/docker-concepts/running-containers/overriding-container-defaults" >}}
