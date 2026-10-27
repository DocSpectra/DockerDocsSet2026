---
title: Build and push the concepts to-do image
keywords: concepts, build, images, container, docker desktop
description: This concept page will teach you how to build, tag, and publish an image to Docker Hub or any other registry 
summary: |
  Building, tagging, and publishing Docker images are key steps in the
  containerization workflow. In this guide, you’ll learn how to create Docker
  images, how to tag those images with a unique identifier, and how to publish
  your image to a public registry.
---

## Before you begin

[Build, tag, and publish an image](/get-started/docker-concepts/building-images/build-tag-and-publish-an-image.md).

- [Docker Hub account and repository procedure](/get-started/shared/docker-hub-access.md)

## Try it out

In this hands-on guide, you will build a simple image using a provided Dockerfile and push it to Docker Hub.

### Set up

1. Get the sample application.

   If you have Git, you can clone the repository for the sample application. Otherwise, you can download the sample application. Choose one of the following options.

   {{< tabs >}}
   {{< tab name="Clone with git" >}}

   Use the following command in a terminal to clone the sample application repository.

   ```console
   $ git clone https://github.com/docker/getting-started-todo-app
   ```
   {{< /tab >}}
   {{< tab name="Download" >}}

   Download the source and extract it.

   {{< button url="https://github.com/docker/getting-started-todo-app/raw/cd61f824da7a614a8298db503eed6630eeee33a3/app.zip" text="Download the source" >}}

   {{< /tab >}}
   {{< /tabs >}}


2. [Download and install](https://www.docker.com/products/docker-desktop/) Docker Desktop.

3. If you don't have a Docker account yet, [create one now](https://hub.docker.com/). Once you've done that, sign in to Docker Desktop using that account.


### Build an image

Now that you have a repository on Docker Hub, it's time for you to build an image and push it to the repository.

1. Using a terminal in the root of the sample app repository, run the following command. Replace `YOUR_DOCKER_USERNAME` with your Docker Hub username:

    ```console
    $ docker build -t <YOUR_DOCKER_USERNAME>/concepts-build-image-demo .
    ```

    As an example, if your username is `mobywhale`, you would run the command:

    ```console
    $ docker build -t mobywhale/concepts-build-image-demo .
    ```

2. Once the build has completed, you can view the image by using the following command:

    ```console
    $ docker image ls
    ```

    The command will produce output similar to the following:

    ```plaintext
    REPOSITORY                             TAG       IMAGE ID       CREATED          SIZE
    mobywhale/concepts-build-image-demo    latest    746c7e06537f   24 seconds ago   354MB
    ```

3. You can actually view the history (or how the image was created) by using the [docker image history](/reference/cli/docker/image/history/) command:

    ```console
    $ docker image history mobywhale/concepts-build-image-demo
    ```

    You'll then see output similar to the following:

    ```plaintext
    IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
    f279389d5f01   8 seconds ago   CMD ["node" "./src/index.js"]                   0B        buildkit.dockerfile.v0
    <missing>      8 seconds ago   EXPOSE map[3000/tcp:{}]                         0B        buildkit.dockerfile.v0 
    <missing>      8 seconds ago   WORKDIR /app                                    8.19kB    buildkit.dockerfile.v0
    <missing>      4 days ago      /bin/sh -c #(nop)  CMD ["node"]                 0B
    <missing>      4 days ago      /bin/sh -c #(nop)  ENTRYPOINT ["docker-entry…   0B
    <missing>      4 days ago      /bin/sh -c #(nop) COPY file:4d192565a7220e13…   20.5kB
    <missing>      4 days ago      /bin/sh -c apk add --no-cache --virtual .bui…   7.92MB
    <missing>      4 days ago      /bin/sh -c #(nop)  ENV YARN_VERSION=1.22.19     0B
    <missing>      4 days ago      /bin/sh -c addgroup -g 1000 node     && addu…   126MB
    <missing>      4 days ago      /bin/sh -c #(nop)  ENV NODE_VERSION=20.12.0     0B
    <missing>      2 months ago    /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
    <missing>      2 months ago    /bin/sh -c #(nop) ADD file:d0764a717d1e9d0af…   8.42MB
    ```

    This output shows the layers of the image, highlighting the layers you added and those that were inherited from your base image.

### Push the image

Now that you have an image built, it's time to push the image to a registry.

1. Push the image using the [docker push](/reference/cli/docker/image/push/) command:

    ```console
    $ docker push <YOUR_DOCKER_USERNAME>/concepts-build-image-demo
    ```

    If you receive a `requested access to the resource is denied`, make sure you are both logged in and that your Docker username is correct in the image tag.

    After a moment, your image should be pushed to Docker Hub.

## Next steps

Now that you have learned about building and publishing images, it's time to learn how to speed up the build process using the Docker build cache.

{{< button text="Using the build cache" url="/get-started/docker-concepts/building-images/using-the-build-cache" >}}
