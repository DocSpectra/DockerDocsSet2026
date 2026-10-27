---
title: Publishing and exposing ports
keywords: concepts, build, images, container, docker desktop
weight: 1
aliases: 
 - /guides/docker-concepts/running-containers/publishing-ports/
---

{{< youtube-embed 9JnqOmJ96ds >}}

## Explanation

If you've been following the guides so far, you understand that containers provide isolated processes for each component of your application. Each component - a React frontend, a Python API, and a Postgres database - runs in its own sandbox environment, completely isolated from everything else on your host machine. This isolation is great for security and managing dependencies, but it also means you can’t access them directly. For example, you can’t access the web app in your browser.

That’s where port publishing comes in.

### Publishing ports

Publishing a port provides the ability to break through a little bit of networking isolation by setting up a forwarding rule. As an example, you can indicate that requests on your host’s port `8080` should be forwarded to the container’s port `80`. Publishing ports happens during container creation using the `-p` (or `--publish`) flag with `docker run`. The syntax is:

```console
$ docker run -d -p HOST_PORT:CONTAINER_PORT nginx
```

- `HOST_PORT`: The port number on your host machine where you want to receive traffic
- `CONTAINER_PORT`: The port number within the container that's listening for connections

For example, to publish the container's port `80` to host port `8080`:

```console
$ docker run -d -p 8080:80 nginx
```

Now, any traffic sent to port `8080` on your host machine will be forwarded to port `80` within the container.

> [!IMPORTANT]
>
> When a port is published, it's published to all network interfaces by default. This means any traffic that reaches your machine can access the published application. Be mindful of publishing databases or any sensitive information. [Learn more about published ports here](/engine/network/#published-ports).

### Publishing to ephemeral ports

At times, you may want to simply publish the port but don’t care which host port is used. In these cases, you can let Docker pick the port for you. To do so, simply omit the `HOST_PORT` configuration. 

For example, the following command will publish the container’s port `80` onto an ephemeral port on the host:

```console
$ docker run -p 80 nginx
```
 
Once the container is running, using `docker ps` will show you the port that was chosen:

```console
docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                    NAMES
a527355c9c53   nginx         "/docker-entrypoint.…"   4 seconds ago    Up 3 seconds    0.0.0.0:54772->80/tcp    romantic_williamson
```

In this example, the app is exposed on the host at port `54772`.

### Publishing all ports

When creating a container image, the `EXPOSE` instruction is used to indicate the packaged application will use the specified port. These ports aren't published by default. 

With the `-P` or `--publish-all` flag, you can automatically publish all exposed ports to ephemeral ports. This is quite useful when you’re trying to avoid port conflicts in development or testing environments.

For example, the following command will publish all of the exposed ports configured by the image:

```console
$ docker run -P nginx
```

## Additional resources

If you’d like to dive in deeper on this topic, be sure to check out the following resources:

* [`docker container port` CLI reference](/reference/cli/docker/container/port/)
* [Published ports](/engine/network/#published-ports)
