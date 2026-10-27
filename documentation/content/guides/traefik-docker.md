---
title: "Route between containers with Traefik"
description: "Route between containers with Traefik"
---

## Prerequisites

[Docker Desktop](prerequisites.md#docker-desktop).

[Node.js and yarn](prerequisites.md#nodejs-and-yarn).

Basic of Docker.

[Docker networks](/manuals/engine/network/_index.md).

## Using Traefik with Docker

[Docker provider and routing labels](traefik-providers.md#docker-provider).

Let’s do a quick demo of starting Traefik and then configuring two additional containers to be accessible using different hostnames.

1. In order for two containers to be able to communicate with each other, they need to be on the same network. Create a network named `traefik-demo` using the `docker network create` command:

   ```console
   $ docker network create traefik-demo
   ```

2. Start a Traefik container using one of the following methods. These commands exposes Traefik on port 80, mounts the Docker socket (which is used to monitor containers to update configuration), and passes the `--providers.docker` argument to configure Traefik to use the Docker provider.

   {{< tabs >}}
   {{< tab name="Using Docker Hardened Images" >}}

   Docker Hardened Images (DHI) for Traefik are available on [Docker Hub](https://hub.docker.com/hardened-images/catalog/dhi/traefik).
   [Authenticate to pull Docker Hardened Images](hardened-image-access.md#authenticate).

   Then start a container using the Hardened image:

   ```console
   $ docker run -d --network=traefik-demo \
     -p 80:80 \
     -v /var/run/docker.sock:/var/run/docker.sock \
     dhi.io/traefik:3.6.2 \
     --providers.docker
   ```

   {{< /tab >}}

   {{< tab name="Using the official image" >}}

   You can also use the official image from Docker Hub:

   ```console
   $ docker run -d --network=traefik-demo \
     -p 80:80 \
     -v /var/run/docker.sock:/var/run/docker.sock \
     traefik:v3.6.2 \
     --providers.docker
   ```

   {{< /tab >}}
   {{< /tabs >}}

3. Now, start a simple Nginx container and define the labels Traefik is watching for to configure the HTTP routing. Note that the Nginx container is not exposing any ports.

   {{< tabs >}}
   {{< tab name="Using Docker Hardened Images" >}}

   Docker Hardened Images (DHI) for Nginx are available on [Nginx DHI image](https://hub.docker.com/hardened-images/catalog/dhi/nginx).
   [Authenticate to pull Docker Hardened Images](hardened-image-access.md#authenticate).

   ```console
   $ docker run -d --network=traefik-demo \
     --label 'traefik.http.routers.nginx.rule=Host(`nginx.localhost`)' \
     dhi.io/nginx:1.29.3
   ```

   {{< /tab >}}

   {{< tab name="Using the official image" >}}

   You can also run the official Nginx image as follows:

   ```console
   $ docker run -d --network=traefik-demo \
     --label 'traefik.http.routers.nginx.rule=Host(`nginx.localhost`)' \
     nginx:1.29.3
   ```

   {{< /tab >}}
   {{< /tabs >}}

   Once the container starts, open your browser to [http://nginx.localhost](http://nginx.localhost) to see the app (all Chromium-based browsers route \*.localhost requests locally with no additional setup).

4. Start a second application that will use a different hostname.

   ```console
   $ docker run -d --network=traefik-demo --label 'traefik.http.routers.welcome.rule=Host(`welcome.localhost`)' docker/welcome-to-docker
   ```

   Once the container starts, open your browser to http://welcome.localhost. You should see a “Welcome to Docker” website.
