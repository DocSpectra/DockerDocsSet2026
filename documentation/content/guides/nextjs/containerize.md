---
title: Containerize a Next.js Application
linkTitle: Containerize
weight: 10
keywords: next.js, node, image, initialize, build
description: Learn how to containerize a Next.js application with Docker by creating an optimized, production-ready image using best practices for performance, security, and scalability.

---

## Prerequisites

Install the latest version of [Docker Desktop](/get-started/get-docker.md) and have a [Git client](/guides/prerequisites.md#git-client).

> **New to Docker?**  
> Start with the [Docker basics](/get-started/docker-concepts/the-basics/what-is-a-container.md) guide to get familiar with key concepts like images, containers, and Dockerfiles.

---

## Overview

This guide walks you through containerizing a Next.js application with Docker.
You'll learn how to create a production-ready Docker image using best
practices that improve performance, security, scalability, and deployment
efficiency.

By the end of this guide, you will:

- Containerize a Next.js application using Docker.
- Create and optimize a Dockerfile for production builds. 
- Use multi-stage builds to minimize image size.
- Leverage Next.js standalone or export output for efficient containerization.
- Follow best practices for building secure and maintainable Docker images. 

---

## Get the sample application

Clone the sample application to use with this guide. Open a terminal, change
directory to a directory that you want to work in, and run the following command
to clone the git repository:

```console
$ git clone https://github.com/kristiyan-velkov/docker-nextjs-sample
```
---

## Generate a Dockerfile

For the scaffolding procedure and generated files, see [Initialize Docker assets](/guides/docker-init.md).

To begin, navigate to the project directory:

```console
$ cd docker-nextjs-sample
```

Follow [Generate the files](/guides/docker-init.md#generate-the-files) from this directory.

The CLI will prompt you with a few questions about your app setup.
For consistency, please use the same responses shown in the example below when prompted:

| Question                                                   | Answer          |
|------------------------------------------------------------|-----------------|
| What application platform does your project use?           | Node            |
| What version of Node do you want to use?                   | 24.14.0-alpine  |
| Which package manager do you want to use?                  | npm             |
| Do you want to run "npm run build" before starting server? | yes             |
| What directory is your build output to?                    | .next           |
| What command do you want to use to start the app?          | npm run start   |
| What port does your server listen on?                      | 3000            |

After completion, your project directory will contain the following new files:

```text
├── docker-nextjs-sample/
│ ├── Dockerfile
│ ├── .dockerignore
│ ├── compose.yaml
│ └── README.Docker.md
```

---

## Continue

1. Choose [standalone output](standalone.md) or [static export](export.md).
2. [Build the Next.js image](build-images.md).
3. [Run the Next.js application](run.md).
