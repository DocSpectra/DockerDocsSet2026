---
title: Run the Angular application
weight: 25
description: Start, verify, and stop the containerized Angular application.
---

## Prerequisites

[Build the Angular image](build-images.md).

For image and container inspection, see [Inspect local images and running containers](/guides/image-build-and-inspect.md).

## Start and verify the application

Use [foreground startup](/guides/run-compose-application.md#run-in-the-foreground) or [background startup](/guides/run-compose-application.md#run-in-the-background) in the `docker-angular-sample` directory.

Open a browser at [http://localhost:8080](http://localhost:8080). You should see your Angular application running.

### Check the running container

Follow [View running containers](/guides/image-build-and-inspect.md#view-running-containers) and look for a container exposing port 8080.

Example Output:

```shell
CONTAINER ID   IMAGE                          COMMAND                  CREATED             STATUS             PORTS                    NAMES
eb13026806d1   docker-angular-sample-server   "nginx -c /etc/nginx…"   About a minute ago  Up About a minute  0.0.0.0:8080->8080/tcp   docker-angular-sample-server-1
```


### Stop the application

Use `ctrl+c` for the foreground application or [stop the background application](/guides/run-compose-application.md#stop-the-background-application).


> [!NOTE]
> For more information about Compose commands, see the [Compose CLI
> reference](/reference/cli/docker/compose/).

---


## Continue

[Develop the Angular application](develop.md).
