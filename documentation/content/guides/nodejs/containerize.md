---
title: Containerize a Node.js application
linkTitle: Containerize
weight: 10
keywords: node.js, node, containerize, initialize
description: Learn how to containerize a Node.js application with Docker by creating an optimized, production-ready image using best practices for performance, security, and scalability.
aliases:
  - /get-started/nodejs/build-images/
  - /language/nodejs/build-images/
  - /language/nodejs/run-containers/
  - /language/nodejs/containerize/
  - /guides/language/nodejs/containerize/
---

## Prerequisites

Install the latest version of [Docker Desktop](/get-started/get-docker.md) and have a [Git client](/guides/prerequisites.md#git-client).

> **New to Docker?**  
> Start with the [Docker basics](/get-started/docker-concepts/the-basics/what-is-a-container.md) guide to get familiar with key concepts like images, containers, and Dockerfiles.

---

## Overview

This guide walks you through the complete process of containerizing a Node.js application with Docker. You’ll learn how to create a production-ready Docker image using best practices that enhance performance, security, scalability, and operational efficiency.

By the end of this guide, you will:

- Containerize a Node.js application using Docker.
- Create and optimize a Dockerfile tailored for Node.js environments.
- Use multi-stage builds to separate dependencies and reduce image size.
- Configure the container for secure, efficient runtime using a non-root user.
- Follow best practices for building secure, lightweight, and maintainable Docker images.

## Get the sample application

Clone the sample application to use with this guide. Open a terminal, change
directory to a directory that you want to work in, and run the following command
to clone the git repository:

```console
$ git clone https://github.com/kristiyan-velkov/docker-nodejs-sample
```

## Generate a Dockerfile

For the scaffolding procedure and generated files, see [Initialize Docker assets](/guides/docker-init.md).

To begin, navigate to the root of your project directory:

```console
$ cd docker-nodejs-sample
```

Follow [Generate the files](/guides/docker-init.md#generate-the-files) from this directory.

The CLI will prompt you with a few questions about your app setup.
For consistency, use the same responses shown in the example following when prompted:

| Question | Answer |
|------------------------------------------------------------|-----------------|
| What application platform does your project use? | Node |
| What version of Node do you want to use? | 24.11.1-alpine |
| Which package manager do you want to use? | npm |
| Do you want to run "npm run build" before starting server? | yes |
| What directory is your build output to? | dist |
| What command do you want to use to start the app? | npm run dev |
| What port does your server listen on? | 3000 |

After completion, your project directory will contain the following new files:

```text
├── docker-nodejs-sample/
│ ├── Dockerfile
│ ├── .dockerignore
│ ├── compose.yaml
│ └── README.Docker.md
```

## Continue

1. [Configure Compose and environment settings](configure-compose.md).
2. [Build the Node.js image](build-images.md).
3. [Run the Node.js application](run.md).
