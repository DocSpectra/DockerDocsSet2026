---
title: Containerize a R application
linkTitle: Containerize your app
weight: 10
keywords: R, containerize, initialize
description: Learn how to containerize a R application.
aliases:
  - /language/R/build-images/
  - /language/R/run-containers/
  - /language/r/containerize/
  - /guides/language/r/containerize/
---

## Prerequisites

- See the [Git client prerequisite](/guides/prerequisites.md#git-client).

For context, see [Docker Compose overview](/manuals/compose/_index.md).

## Overview

This section walks you through containerizing and running a R application.

## Get the sample application

The sample application uses the popular [Shiny](https://shiny.posit.co/) framework.

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

```console
$ git clone https://github.com/mfranzon/r-docker-dev.git && cd r-docker-dev
```

You should now have the following contents in your `r-docker-dev`
directory.

```text
├── r-docker-dev/
│ ├── src/
│ │ └── app.R
│ ├── src_db/
│ │ └── app_db.R
│ ├── compose.yaml
│ ├── Dockerfile
│ └── README.md
```

To learn more about the files in the repository, see the following:

- [Dockerfile](/reference/dockerfile.md)
- [.dockerignore](/manuals/build/concepts/context.md#dockerignore-files)
- [compose.yaml](/reference/compose-file/_index.md)

## Run the application

Inside the `r-docker-dev` directory, follow [Run in the foreground](/guides/run-compose-application.md#run-in-the-foreground).

Open a browser and view the application at [http://localhost:3838](http://localhost:3838). You should see a simple Shiny application.

In the terminal, press `ctrl`+`c` to stop the application.

### Run the application in the background

Inside the `r-docker-dev` directory, follow [Run in the background](/guides/run-compose-application.md#run-in-the-background).

Open a browser and view the application at [http://localhost:3838](http://localhost:3838).

You should see a simple Shiny application.

Follow [Stop the background application](/guides/run-compose-application.md#stop-the-background-application).

For more information about Compose commands, see the [Compose CLI
reference](/reference/cli/docker/compose/).

## Summary

In this section, you learned how you can containerize and run your R
application using Docker.

Related information:

- [Docker Compose overview](/manuals/compose/_index.md)

## Next steps

In the next section, you'll learn how you can develop your application using
containers.
