---
title: Containerize a Golang application
linkTitle: Containerize your app
weight: 20
keywords: go, golang, containerize, initialize
description: Learn how to containerize a Golang application.
---

Containerization helps you bundle the application and its dependencies into a single package called a container. This package can run on any platform without worrying about the environment. In this section, you will learn how to containerize a Golang application using Docker.

To containerize a Golang application, you first need to create a Dockerfile. The Dockerfile contains instructions to build and run the application in a container. Also, when creating a Dockerfile, you can follow different sets of best practices to optimize the image size and make it more secure.

## Prerequisites

[Prepare the Go monitoring sample](setup.md).

## Creating a Dockerfile

[Define the Go monitoring image](image.md#creating-a-dockerfile).

## Understanding the Dockerfile

[Build and final stages](image.md#understanding-the-dockerfile).

## Build the Docker image and run the application

One you have the Dockerfile, you can build the Docker image and run the application in a container.

To build the Docker image, run the following command in the terminal:

```console
$ docker build -t go-api:latest .
```

After building the image, you can run the application in a container using the following command:

```console
$ docker run -p 8000:8000 go-api:latest
```

The application will start running inside the container, and you can access it at `http://localhost:8000`. You can also check the running containers using the `docker ps` command.

```console
$ docker ps
```

## Summary

In this section, you learned how to containerize a Golang application using a Dockerfile. You created a multi-stage Dockerfile to build and run the application in a container. You also learned about best practices to optimize the Docker image size and make it more secure.

Related information:

 - [Dockerfile reference](/reference/dockerfile.md)
 - [.dockerignore file](/manuals/build/concepts/context.md#dockerignore-files)

## Next steps

In the next section, you will learn how to use Docker Compose to connect and run multiple services together to monitor a Golang application with Prometheus and Grafana.
