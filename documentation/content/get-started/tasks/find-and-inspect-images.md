---
title: Find, pull, and inspect an image
keywords: concepts, build, images, container, docker desktop
description: What is an image
---

## Before you begin

[What is an image?](/get-started/docker-concepts/the-basics/what-is-an-image.md).

- [Docker Desktop installation](/get-started/get-docker.md)

## Try it out

{{< tabs group=concept-usage persist=true >}}
{{< tab name="Using the GUI" >}}

In this hands-on, you will learn how to search and pull a container image using the Docker Desktop GUI.

### Search for and download an image

1. Open the Docker Desktop Dashboard and select the **Images** view in the left-hand navigation menu.

   ![A screenshot of the Docker Desktop Dashboard showing the image view on the left sidebar](/get-started/docker-concepts/the-basics/images/click-image.webp?border=true&w=1050&h=400)

2. Select the **Search images to run** button. If you don't see it, select the _global search bar_ at the top of the screen.

   ![A screenshot of the Docker Desktop Dashboard showing the search ta](/get-started/docker-concepts/the-basics/images/search-image.webp?border)

3. In the **Search** field, enter "welcome-to-docker". Once the search has completed, select the `docker/welcome-to-docker` image.

   ![A screenshot of the Docker Desktop Dashboard showing the search results for the docker/welcome-to-docker image](/get-started/docker-concepts/the-basics/images/select-image.webp?border=true&w=1050&h=400)

4. Select **Pull** to download the image.

### Learn about the image

Once you have an image downloaded, you can learn quite a few details about the image either through the GUI or the CLI.

1. In the Docker Desktop Dashboard, select the **Images** view.

2. Select the **docker/welcome-to-docker** image to open details about the image.

   ![A screenshot of the Docker Desktop Dashboard showing the images view with an arrow pointing to the docker/welcome-to-docker image](/get-started/docker-concepts/the-basics/images/pulled-image.webp?border=true&w=1050&h=400)

3. The image details page presents you with information regarding the layers of the image, the packages and libraries installed in the image, and any discovered vulnerabilities.

   ![A screenshot of the image details view for the docker/welcome-to-docker image](/get-started/docker-concepts/the-basics/images/image-layers.webp?border=true&w=1050&h=400)

{{< /tab >}}

{{< tab name="Using the CLI" >}}

Follow the instructions to search and pull a Docker image using CLI to view its layers.

### Search for and download an image

1. Open a terminal and search for images using the [`docker search`](/reference/cli/docker/search/) command:

   ```console
   docker search docker/welcome-to-docker
   ```

   You will see output like the following:

   ```console
   NAME                       DESCRIPTION                                     STARS     OFFICIAL
   docker/welcome-to-docker   Docker image for new users getting started w…   20
   ```

   This output shows you information about relevant images available on Docker Hub.

2. Pull the image using the [`docker pull`](/reference/cli/docker/image/pull/) command.

   ```console
   docker pull docker/welcome-to-docker
   ```

   You will see output like the following:

   ```console
   Using default tag: latest
   latest: Pulling from docker/welcome-to-docker
   579b34f0a95b: Download complete
   d11a451e6399: Download complete
   1c2214f9937c: Download complete
   b42a2f288f4d: Download complete
   54b19e12c655: Download complete
   1fb28e078240: Download complete
   94be7e780731: Download complete
   89578ce72c35: Download complete
   Digest: sha256:eedaff45e3c78538087bdd9dc7afafac7e110061bbdd836af4104b10f10ab693
   Status: Downloaded newer image for docker/welcome-to-docker:latest
   docker.io/docker/welcome-to-docker:latest
   ```

   Each of line represents a different downloaded layer of the image. Remember that each layer is a set of filesystem changes and provides functionality of the image.

### Learn about the image

1. List your downloaded images using the [`docker image ls`](/reference/cli/docker/image/ls/) command:

   ```console
   docker image ls
   ```

   You will see output like the following:

   ```console
   REPOSITORY                 TAG       IMAGE ID       CREATED        SIZE
   docker/welcome-to-docker   latest    eedaff45e3c7   4 months ago   29.7MB
   ```

   The command shows a list of Docker images currently available on your system. The `docker/welcome-to-docker` has a total size of approximately 29.7MB.

   > **Image size**
   >
   > The image size represented here reflects the uncompressed size of the image, not the download size of the layers.

2. List the image's layers using the [`docker image history`](/reference/cli/docker/image/history/) command:

   ```console
   docker image history docker/welcome-to-docker
   ```

   You will see output like the following:

   ```console
   IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
   648f93a1ba7d   4 months ago   COPY /app/build /usr/share/nginx/html # buil…   1.6MB     buildkit.dockerfile.v0
   <missing>      5 months ago   /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
   <missing>      5 months ago   /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B
   <missing>      5 months ago   /bin/sh -c #(nop)  EXPOSE 80                    0B
   <missing>      5 months ago   /bin/sh -c #(nop)  ENTRYPOINT ["/docker-entr…   0B
   <missing>      5 months ago   /bin/sh -c #(nop) COPY file:9e3b2b63db9f8fc7…   4.62kB
   <missing>      5 months ago   /bin/sh -c #(nop) COPY file:57846632accc8975…   3.02kB
   <missing>      5 months ago   /bin/sh -c #(nop) COPY file:3b1b9915b7dd898a…   298B
   <missing>      5 months ago   /bin/sh -c #(nop) COPY file:caec368f5a54f70a…   2.12kB
   <missing>      5 months ago   /bin/sh -c #(nop) COPY file:01e75c6dd0ce317d…   1.62kB
   <missing>      5 months ago   /bin/sh -c set -x     && addgroup -g 101 -S …   9.7MB
   <missing>      5 months ago   /bin/sh -c #(nop)  ENV PKG_RELEASE=1            0B
   <missing>      5 months ago   /bin/sh -c #(nop)  ENV NGINX_VERSION=1.25.3     0B
   <missing>      5 months ago   /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B
   <missing>      5 months ago   /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
   <missing>      5 months ago   /bin/sh -c #(nop) ADD file:ff3112828967e8004…   7.66MB
   ```

   This output shows you all of the layers, their sizes, and the command used to create the layer.

   > **Viewing the full command**
   >
   > If you add the `--no-trunc` flag to the command, you will see the full command. Note that, since the output is in a table-like format, longer commands will cause the output to be very difficult to navigate.

{{< /tab >}}
{{< /tabs >}}

In this walkthrough, you searched and pulled a Docker image. In addition to pulling a Docker image, you also learned about the layers of a Docker Image.

## Next steps

Now that you have learned the basics of images, it's time to learn about distributing images through registries.

{{< button text="What is a registry?" url="/get-started/docker-concepts/the-basics/what-is-a-registry" >}}
