---
title: "Route traffic to native applications with Traefik"
description: "Route traffic to native applications with Traefik"
---

## Prerequisites

[Docker Desktop](prerequisites.md#docker-desktop).

[Node.js and yarn](prerequisites.md#nodejs-and-yarn).

Basic of Docker.

[Sample application and routing layout](traefik-project.md).

[Traefik providers](traefik-providers.md).

## Sending traffic to non-containerized workloads

In some situations, you may want to forward requests to applications not running in containers. In the following architecture diagram, the same application from before is used, but the API and React apps are now running natively on the host machine.

![An architecture diagram showing several components and the routing between them. Traefik is able to send requests to both non-containerized and containerized workloads](images/traefik-non-containerized-workload-architecture.webp)

To accomplish this, Traefik will need to use another method to configure itself. See the [File provider](traefik-providers.md#file-provider). Here is an example file:

```yaml
http:
  routers:
    native-api:
      rule: "Host(`localhost`) && PathPrefix(`/api`)"
      service: native-api
    native-client:
      rule: "Host(`localhost`)"
      service: native-client

  services:
    native-api:
      loadBalancer:
        servers:
          - url: "http://host.docker.internal:3000/"
    native-client:
      loadBalancer:
        servers:
          - url: "http://host.docker.internal:5173/"
```

This configuration indicates that requests that for `localhost/api` will be forwarded to a service named `native-api`, which then forwards the request to http://host.docker.internal:3000. The hostname `host.docker.internal` is a name that Docker Desktop provides to send requests to the host machine.

With this file, the only change is to the Compose configuration for Traefik. There are specifically two things that have changed:

1. The configuration file is mounted into the Traefik container (the exact destination path is up to you)
2. The `command` is updated to add the file provider and point to the location of the configuration file

  {{< tabs >}}
  {{< tab name="Using DHI image" >}}

  [Authenticate to pull Docker Hardened Images](hardened-image-access.md#authenticate).

  ```yaml
  services:
    proxy:
      image: dhi.io/traefik:3.6.2
      command: --providers.docker --providers.file.filename=/config/traefik-config.yaml --api.insecure
      ports:
        - 80:80
        - 8080:8080
      volumes:
        - /var/run/docker.sock:/var/run/docker.sock
        - ./dev/traefik-config.yaml:/config/traefik-config.yaml
  ```

  {{< /tab >}}

  {{< tab name="Using official image" >}}

  ```yaml
  services:
    proxy:
      image: traefik:v3.6.2
      command: --providers.docker --providers.file.filename=/config/traefik-config.yaml --api.insecure
      ports:
        - 80:80
        - 8080:8080
      volumes:
        - /var/run/docker.sock:/var/run/docker.sock
        - ./dev/traefik-config.yaml:/config/traefik-config.yaml
  ```

  {{< /tab >}}
  {{< /tabs >}}

### Starting the example app

To run the example app that forwards requests from Traefik to native-running apps, use the following steps:

1. If you have the Compose stack still running, stop it with the following command:

   ```console
   $ docker compose down
   ```

2. Start the application using the provided `compose-native.yaml` file:

   ```console
   $ docker compose -f compose-native.yaml up
   ```

   Opening [http://localhost](http://localhost) will return a 502 Bad Gateway because the other apps aren’t running yet.

3. Start the API by running the following steps:

   ```console
   cd api
   yarn install
   yarn dev
   ```

4. Start the frontend by running the following steps in a new terminal (starting from the root of the project):

   ```console
   cd client
   yarn install
   yarn dev
   ```

5. Open the app at [http://localhost](http://localhost). You should see an app that fetches a message from [http://localhost/api/messages](http://localhost/api/messages). You can also open [http://db.localhost](http://db.localhost) to view or adjust the available messages directly from the Mongo database. Traefik will ensure the requests are properly routed to the correct container or application.

6. When you’re done, run `docker compose down` to stop the containers and stop the Yarn apps by hitting `ctrl+c`.
