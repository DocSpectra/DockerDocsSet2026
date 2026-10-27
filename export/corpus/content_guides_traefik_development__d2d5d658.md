---
title: "Route a development stack with Traefik"
description: "Route a development stack with Traefik"
---

## Prerequisites

[Docker Desktop](prerequisites.md#docker-desktop).

[Node.js and yarn](prerequisites.md#nodejs-and-yarn).

Basic of Docker.

[Docker provider and routing labels](traefik-providers.md#docker-provider).

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## Using Traefik in development

[Sample application and routing layout](traefik-project.md).

1. In the `compose.yaml` file, Traefik is using the following configuration:

   {{< tabs >}}
   {{< tab name="Using DHI image" >}}

   ```yaml
   services:
     proxy:
       image: dhi.io/traefik:3.6.2
       command: --providers.docker
       ports:
         - 80:80
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock
   ```

   {{< /tab >}}

   {{< tab name="Using official image" >}}

   ```yaml
   services:
     proxy:
       image: traefik:v3.6.2
       command: --providers.docker
       ports:
         - 80:80
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock
   ```

   {{< /tab >}}
   {{< /tabs >}}

   Note that this is essentially the same configuration as used earlier, but now in a Compose syntax.

2. The client service has the following configuration, which will start the container and provide it with the labels to receive requests at localhost.

   {{< tabs >}}
   {{< tab name="Using Docker Hardened Images" >}}

   Docker Hardened Images (DHI) for Nginx are available on [Nginx DHI image](https://hub.docker.com/hardened-images/catalog/dhi/nginx).

   [Authenticate to pull Docker Hardened Images](hardened-image-access.md#authenticate).

   You can use it as your base image as shown following:

   ```yaml
   services:
     # …
     client:
       image: dhi.io/nginx:1.29.3-alpine3.21
       volumes:
         - "./client:/usr/share/nginx/html"
       labels:
         traefik.http.routers.client.rule: "Host(`localhost`)"
   ```

   {{< /tab >}}

   {{< tab name="Using the official image" >}}

   ```yaml
   services:
     # …
     client:
       image: nginx:1.29.3-alpine3.22
       volumes:
         - "./client:/usr/share/nginx/html"
       labels:
         traefik.http.routers.client.rule: "Host(`localhost`)"
   ```

   {{< /tab >}}
   {{< /tabs >}}

3. The api service has a similar configuration, but you’ll notice the routing rule has two conditions - the host must be “localhost” and the URL path must have a prefix of “/api”. Since this rule is more specific, Traefik will evaluate it first compared to the client rule.

   ```yaml {hl_lines=[7,8]}
   services:
     # …
     api:
       build: ./dev/api
       volumes:
         - "./api:/var/www/html/api"
       labels:
         traefik.http.routers.api.rule: "Host(`localhost`) && PathPrefix(`/api`)"
   ```

4. And finally, the `phpmyadmin` service is configured to receive requests for the hostname “db.localhost”. The service also has environment variables defined to automatically log in, making it a little easier to get into the app.

   ```yaml {hl_lines=[5,6]}
   services:
     # …
     phpmyadmin:
       image: phpmyadmin:5.2.1
       labels:
         traefik.http.routers.db.rule: "Host(`db.localhost`)"
       environment:
         PMA_USER: root
         PMA_PASSWORD: password
   ```

5. Before starting the stack, stop the Nginx container if it is still running.

   And that’s it. Now, you only need to spin up the Compose stack with a `docker compose up` and all of the services and applications will be ready for development.
