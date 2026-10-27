---
title: Publish the Node.js quickstart image
keywords: concepts, build, images, container, docker desktop
description: What is a registry? This Docker Concept will explain what a registry is, explore their interoperability, and have you interact with registries.
---

## Before you begin

[What is a registry?](/get-started/docker-concepts/the-basics/what-is-a-registry.md).

- [Docker Hub account procedure](/get-started/shared/docker-hub-access.md)

## Try it out

In this hands-on, you will learn how to build and push a Docker image to the Docker Hub repository.

### Sign up for a free Docker account

[Create and verify your Docker account](/get-started/shared/docker-hub-access.md#sign-up-for-a-free-docker-account).

### Create your first repository

1. Sign in to [Docker Hub](https://hub.docker.com).
2. Select the **Create repository** button in the top-right corner.
3. Select your namespace (most likely your username) and enter `docker-quickstart` as the repository name.

    ![Screenshot of the Docker Hub page that shows how to create a public repository](/get-started/docker-concepts/the-basics/images/create-hub-repository.webp?border)

4. Set the visibility to **Public**. 
5. Select the **Create** button to create the repository.

That's it. You've successfully created your first repository. 🎉

This repository is empty right now. You'll now fix this by pushing an image to it.

### Sign in with Docker Desktop

1. [Download and install](https://www.docker.com/products/docker-desktop/) Docker Desktop, if not already installed.
2. In the Docker Desktop GUI, select the **Sign in** button in the top-right corner

### Clone sample Node.js code

In order to create an image, you first need a project. To get you started quickly, you'll use a sample Node.js project found at [github.com/dockersamples/helloworld-demo-node](https://github.com/dockersamples/helloworld-demo-node). This repository contains a pre-built Dockerfile necessary for building a Docker image.

Don't worry about the specifics of the Dockerfile, as you'll learn about that in later sections.

1. Clone the GitHub repository using the following command:

    ```console
    git clone https://github.com/dockersamples/helloworld-demo-node
    ```

2. Navigate into the newly created directory.

    ```console
    cd helloworld-demo-node
    ```

3. Run the following command to build a Docker image, swapping out `YOUR_DOCKER_USERNAME` with your username.

    ```console
    docker build -t <YOUR_DOCKER_USERNAME>/docker-quickstart .
    ```

    > [!NOTE]
    >
    > Make sure you include the dot (.) at the end of the `docker build` command. This tells Docker where to find the Dockerfile.

4. Run the following command to list the newly created Docker image:

    ```console
    docker images
    ```

    You will see output like the following:

    ```console
    REPOSITORY                                 TAG       IMAGE ID       CREATED         SIZE
    <YOUR_DOCKER_USERNAME>/docker-quickstart   latest    476de364f70e   2 minutes ago   170MB
    ```

5. Start a container to test the image by running the following command (swap out the username with your own username):

    ```console
    docker run -d -p 8080:8080 <YOUR_DOCKER_USERNAME>/docker-quickstart 
    ```

    You can verify if the container is working by visiting [http://localhost:8080](http://localhost:8080) with your browser.

6. Use the [`docker tag`](/reference/cli/docker/image/tag/) command to tag the Docker image. Docker tags allow you to label and version your images. 

    ```console 
    docker tag <YOUR_DOCKER_USERNAME>/docker-quickstart <YOUR_DOCKER_USERNAME>/docker-quickstart:1.0 
    ```

7. Finally, it's time to push the newly built image to your Docker Hub repository by using the [`docker push`](/reference/cli/docker/image/push/) command:

    ```console 
    docker push <YOUR_DOCKER_USERNAME>/docker-quickstart:1.0
    ```

8. Open [Docker Hub](https://hub.docker.com) and navigate to your repository. Navigate to the **Tags** section and see your newly pushed image.

    ![Screenshot of the Docker Hub page that displays the newly added image tag](/get-started/docker-concepts/the-basics/images/dockerhub-tags.webp?border=true) 

In this walkthrough, you signed up for a Docker account, created your first Docker Hub repository, and built, tagged, and pushed a container image to your Docker Hub repository.

## Next steps

Now that you understand the basics of containers and images, you're ready to learn about Docker Compose.

{{< button text="What is Docker Compose?" url="/get-started/docker-concepts/the-basics/what-is-docker-compose" >}}
