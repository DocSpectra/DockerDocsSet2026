---
title: Docker Offload quickstart
linktitle: Quickstart
weight: 10
description: Learn how to use Docker Offload to build and run your container images in the cloud.
keywords: cloud, quickstart, Docker Desktop, offload
---

{{< summary-bar feature_name="Docker Offload" >}}

[Docker Offload](./about.md) lets you build and run containers in the cloud
while using your local Docker Desktop tools and workflow. This means faster
builds, access to powerful cloud resources, and a seamless development
experience.

This quickstart covers the steps developers need to get started with Docker Offload.

## Prerequisites

See [Docker Offload prerequisites and access requirements](requirements.md).

## Step 1: Verify access to Docker Offload

Follow [Verify access to Docker Offload](access.md).

## Step 2: Start Docker Offload

You can start Docker Offload from the CLI or in the header of the Docker Desktop
Dashboard. The following steps describe how to start Docker Offload using the
CLI.

1. Start Docker Desktop and sign in.
2. Open a terminal and run the following command to start Docker Offload:

   ```console
   $ docker offload start
   ```

   > [!TIP]
   >
   > To learn more about the Docker Offload CLI commands, see the [Docker Offload CLI
   > reference](/reference/cli/docker/offload/).

3. If you are a member of multiple organizations that have access to Docker
   Offload, you have the option to select a profile. Your usage will be
   associated with the organization of the selected profile.


When Docker Offload is started, you'll see a cloud icon ({{< inline-image
src="./images/cloud-mode.png" alt="Offload mode icon" >}}) in the Docker Desktop
Dashboard header, and the Docker Desktop Dashboard appears purple. You can run
`docker offload status` in a terminal to check the status of Docker Offload.

## Step 3: Run a container with Docker Offload

After starting Docker Offload, Docker Desktop connects to a secure cloud
environment that mirrors your local experience. When you run builds or
containers, they execute remotely, but behave just like local ones.

To verify that Docker Offload is working, run a container:

```console
$ docker run --rm hello-world
```

If Docker Offload is working, you'll see `Hello from Docker!` in the terminal output.

## Step 4: Monitor your Offload session

Follow [Monitor the current Docker Offload session](session-monitoring.md).

## Step 5: Stop Docker Offload

Docker Offload automatically
[idles](./about.md#session-management-and-idle-state) if you do not respond to
periodic prompts that appear in the Docker Desktop Dashboard. You can stop your
Docker Offload session at any time.

When you stop Docker Offload, the cloud environment is terminated and all
running containers and images are removed. When Docker Offload has been idle for
5 minutes, the environment is also terminated and all running containers and
images are removed.

To stop Docker Offload:

```console
$ docker offload stop
```

To start Docker Offload again, run the `docker offload start` command.
