---
title: Get Docker Desktop 
keywords: concepts, container, docker desktop
description: This concept page will teach you download Docker Desktop and install it on Windows, Mac, and Linux
summary: |
  Getting Docker Desktop up and running is the first crucial step for
  developers diving into containerization, offering a seamless and
  user-friendly interface for managing Docker containers. Docker Desktop
  simplifies the process of building, sharing, and running applications in
  containers, ensuring consistency across different environments.
weight: 1
aliases:
 - /getting-started/get-docker-desktop/
---

{{< youtube-embed C2bPVhiNU-0 >}}

## Explanation

Docker Desktop is the all-in-one package to build images, run containers, and so much more.
This guide will walk you through the installation process, enabling you to experience Docker Desktop firsthand.


## Install Docker Desktop

[Choose your platform, review the Docker Desktop terms, and complete setup](/get-started/get-docker.md).

## Try it out

In this hands-on guide, you will see how to run a Docker container using Docker Desktop.

Follow the instructions to run a container using the CLI.


## Run your first container

[Review port publishing and its network-interface caveat](/get-started/docker-concepts/running-containers/publishing-ports.md#publishing-ports).

Open your CLI terminal and start a container by running the `docker run` command:



```console
$ docker run -d -p 8080:80 docker/welcome-to-docker
```

## Access the frontend

For this container, the frontend is accessible on port `8080`. To open the website, visit [http://localhost:8080](http://localhost:8080) in your browser.





![Screenshot of the landing page of the Nginx web server, coming from the running container](../docker-concepts/the-basics/images/access-the-frontend.webp?border=true)

## Manage containers using Docker Desktop


1. Open Docker Desktop and select the **Containers** field on the left sidebar.
2. You can view information about your container including logs, and files, and even access the shell by selecting the **Exec** tab.

   ![Screenshot of exec into the running container in Docker Desktop](images/exec-into-docker-container.webp?border=true)


3. Select the **Inspect** field to obtain detailed information about the container. You can perform various actions such as pause, resume, start or stop containers, or explore the **Logs**, **Bind mounts**, **Exec**, **Files**, and **Stats** tabs.

![Screenshot of inspecting the running container in Docker Desktop](images/inspecting-container.webp?border=true)

Docker Desktop simplifies container management for developers by streamlining the setup, configuration, and compatibility of applications across different environments, thereby addressing the pain points of environment inconsistencies and deployment challenges.

## What's next?

Now that you have Docker Desktop installed and ran your first container, it's time to start developing with containers.

{{< button text="Develop with containers" url="develop-with-containers" >}}
