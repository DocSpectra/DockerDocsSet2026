---
title: Use containers for Go development
linkTitle: Develop your app
weight: 20
keywords: get started, go, golang, local, development
description: Learn how to develop your application locally.
aliases:
  - /get-started/golang/develop/
  - /language/golang/develop/
  - /guides/language/golang/develop/
---

## Prerequisites

See [Go guide prerequisites](prerequisites.md).

Work through the steps of the [run your image as a container](run-containers.md) module to learn how to manage the lifecycle of your containers.

For shared storage and networking context, see [Volumes](/manuals/engine/storage/volumes.md) and [Networking in Compose](/manuals/compose/how-tos/networking.md).

## Introduction

In this module, you'll take a look at running a database engine in a container and connecting it to the extended version of the example application. You are going to see some options for keeping persistent data and for wiring up the containers to talk to one another. Finally, you'll learn how to use Docker Compose to manage such multi-container local development environments effectively.

## Development tasks

1. [Set up CockroachDB](develop-database.md).
2. [Connect and test the Go application](develop-application.md).
3. [Run the stack with Compose](develop-compose.md).

## Local database and containers

See [Local database and containers](develop-database.md#local-database-and-containers).

### Storage

See [Storage](develop-database.md#storage).

### Networking

See [Networking](develop-database.md#networking).

### Choose good names for volumes and networks

See [Choose good names for volumes and networks](develop-database.md#choose-good-names-for-volumes-and-networks).

### Start the database engine

See [Start the database engine](develop-database.md#start-the-database-engine).

### Configure the database engine

See [Configure the database engine](develop-database.md#configure-the-database-engine).

### Meet the example application

See [Meet the example application](develop-application.md#meet-the-example-application).

### Build the application

See [Build the application](develop-application.md#build-the-application).

### Run the application

See [Run the application](develop-application.md#run-the-application).

### Test the application

See [Test the application](develop-application.md#test-the-application).

### Wind down everything

See [Wind down everything](develop-application.md#wind-down-everything).

## Better productivity with Docker Compose

See [Better productivity with Docker Compose](develop-compose.md#better-productivity-with-docker-compose).

### Configure Docker Compose

See [Configure Docker Compose](develop-compose.md#configure-docker-compose).

### The `.env` file

See [The `.env` file](develop-compose.md#the-env-file).

### Merging Compose files

See [Merging Compose files](develop-compose.md#merging-compose-files).

### Variable substitution in Docker Compose

See [Variable substitution in Docker Compose](develop-compose.md#variable-substitution-in-docker-compose).

### Validating Docker Compose configuration

See [Validating Docker Compose configuration](develop-compose.md#validating-docker-compose-configuration).

### Build and run the application using Docker Compose

See [Build and run the application using Docker Compose](develop-compose.md#build-and-run-the-application-using-docker-compose).

### Testing the application

See [Testing the application](develop-compose.md#testing-the-application).

### Shutting down

See [Shutting down](develop-compose.md#shutting-down).

### Detached mode

See [Detached mode](develop-compose.md#detached-mode).

## Further exploration

See [Further exploration](develop-compose.md#further-exploration).

## Wrap up

See [Wrap up](develop-compose.md#wrap-up).

### Persistent storage

See [Persistent storage](develop-compose.md#persistent-storage).

### CockroachDB clusters

See [CockroachDB clusters](develop-compose.md#cockroachdb-clusters).

### Other databases

See [Other databases](develop-compose.md#other-databases).

## Next steps

In this module, you set up a containerized development environment with your application and the database engine running in different containers. You also wrote a Docker Compose file which links the two containers together and provides for easy starting up and tearing down of the development environment.

In the next module, you'll take a look at one possible approach to running functional tests in Docker.
