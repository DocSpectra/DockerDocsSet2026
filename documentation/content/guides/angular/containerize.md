---
title: Containerize an Angular Application
linkTitle: Containerize
weight: 10
keywords: angular, node, image, initialize, build
description: Learn how to containerize an Angular application with Docker by creating an optimized, production-ready image using best practices for performance, security, and scalability.

---

## Prerequisites

Install the latest version of [Docker Desktop](/get-started/get-docker.md) and have a [Git client](/guides/prerequisites.md#git-client).

> **New to Docker?**  
> Start with the [Docker basics](/get-started/docker-concepts/the-basics/what-is-a-container.md) guide to get familiar with key concepts like images, containers, and Dockerfiles.

---

## Overview

This guide walks you through the complete process of containerizing an Angular application with Docker. You’ll learn how to create a production-ready Docker image using best practices that improve performance, security, scalability, and deployment efficiency.

By the end of this guide, you will:

- Containerize an Angular application using Docker.
- Create and optimize a Dockerfile for production builds. 
- Use multi-stage builds to minimize image size.
- Serve the application efficiently with a custom Nginx configuration.
- Build secure and maintainable Docker images by following best practices.

---

## Get the sample application

Clone the sample application to use with this guide. Open a terminal, navigate to the directory where you want to work, and run the following command
to clone the git repository:

```console
$ git clone https://github.com/kristiyan-velkov/docker-angular-sample
```
---

## Generate a Dockerfile

For the scaffolding procedure and generated files, see [Initialize Docker assets](/guides/docker-init.md).

To begin, navigate to the root of your project directory:

```console
$ cd docker-angular-sample
```

Follow [Generate the files](/guides/docker-init.md#generate-the-files) from this directory.

The CLI will prompt you with a few questions about your app setup.
For consistency, please use the same responses shown in the example below when prompted:

| Question                                                   | Answer          |
|------------------------------------------------------------|-----------------|
| What application platform does your project use?           | Node            |
| What version of Node do you want to use?                   | 24.12.0-alpine  |
| Which package manager do you want to use?                  | npm             |
| Do you want to run "npm run build" before starting server? | yes             |
| What directory is your build output to?                    | dist            |
| What command do you want to use to start the app?          | npm run start   |
| What port does your server listen on?                      | 8080            |

After completion, your project directory will contain the following new files:

```text
├── docker-angular-sample/
│ ├── Dockerfile
│ ├── .dockerignore
│ ├── compose.yaml
│ └── README.Docker.md
```

---

## Continue

1. [Build the Angular image](build-images.md).
2. [Run the Angular application](run.md).
