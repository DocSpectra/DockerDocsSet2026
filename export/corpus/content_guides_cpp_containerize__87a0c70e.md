---
title: Containerize a C++ application
linkTitle: Build and run a C++ application using Docker Compose
weight: 10
keywords: C++, containerize, initialize
description: Learn how to use Docker Compose to build and run a C++ application.
aliases:
  - /language/cpp/containerize/
  - /guides/language/cpp/containerize/
---

## Prerequisites

- See the [Git client prerequisite](/guides/prerequisites.md#git-client).

For context, see [Docker Compose overview](/manuals/compose/_index.md).

## Overview

This section walks you through containerizing and running a C++ application, using Docker Compose.

## Get the sample application

We're using the same sample repository that you used in the previous sections of this guide. If you haven't already cloned the repository, clone it now:

```console
$ git clone https://github.com/dockersamples/c-plus-plus-docker.git
```

You should now have the following contents in your `c-plus-plus-docker` (root)
directory.

```text
├── c-plus-plus-docker/
│ ├── compose.yml
│ ├── Dockerfile
│ ├── LICENSE
│ ├── ok_api.cpp
│ └── README.md

```

To learn more about the files in the repository, see the following:

- [Dockerfile](/reference/dockerfile.md)
- [.dockerignore](/manuals/build/concepts/context.md#dockerignore-files)
- [compose.yml](/reference/compose-file/_index.md)

## Run the application

Inside the `c-plus-plus-docker` directory, follow [Run in the foreground](/guides/run-compose-application.md#run-in-the-foreground).

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You will see a message `{"Status" : "OK"}` in the browser.

In the terminal, press `ctrl`+`c` to stop the application.

### Run the application in the background

Inside the `c-plus-plus-docker` directory, follow [Run in the background](/guides/run-compose-application.md#run-in-the-background).

Open a browser and view the application at [http://localhost:8080](http://localhost:8080).

Follow [Stop the background application](/guides/run-compose-application.md#stop-the-background-application).

For more information about Compose commands, see the [Compose CLI
reference](/reference/cli/docker/compose/).

## Summary

In this section, you learned how you can containerize and run your C++
application using Docker.

Related information:

- [Docker Compose overview](/manuals/compose/_index.md)

## Next steps

In the next section, you'll learn how you can develop your application using
containers.
