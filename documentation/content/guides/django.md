---
title: Containerize a Django application
linkTitle: Django
description: Learn how to containerize a Django application using Docker.
keywords: python, django, containerize, initialize, gunicorn, compose watch, uv
summary: |
  This guide shows how to containerize a Django application using Docker.
  You'll scaffold the project with uv, create a production-ready Dockerfile
  using a Docker Hardened Image, then add a development stage and Compose Watch
  for fast iteration.
languages: [python]
tags: [dhi]
params:
  time: 25 minutes
---

## Prerequisites

See [Django guide prerequisites](/guides/frameworks/django/prerequisites.md).

## Overview

This guide walks you through containerizing a Django application with Docker. By
the end, you will:

- Initialize a Django project using uv, either locally or inside a Docker
  Hardened Image container.
- Create a production-ready Dockerfile using [Docker Hardened Images
  (DHI)](/dhi/).
- Add a `development` stage to your Dockerfile and configure Compose Watch for
  automatic code syncing.

---

## Create the Django project

Follow [Create the Django project with uv](/guides/frameworks/django/create-project.md).

## Create a production Dockerfile

Follow [Build and run the Django production image](/guides/frameworks/django/containerize.md).

### Run the application

See [Run the application](/guides/frameworks/django/containerize.md#run-the-application).

## Set up a development environment

Follow [Develop Django with PostgreSQL and Compose Watch](/guides/frameworks/django/develop.md).

### Update the Dockerfile

See [Update the Dockerfile](/guides/frameworks/django/develop.md#update-the-dockerfile).

### Update the Compose file

See [Update the Compose file](/guides/frameworks/django/develop.md#update-the-compose-file).

### Add the PostgreSQL driver

See [Add the PostgreSQL driver](/guides/frameworks/django/develop.md#add-the-postgresql-driver).

### Run with Compose Watch

See [Run with Compose Watch](/guides/frameworks/django/develop.md#run-with-compose-watch).

## Summary

In this guide, you:

- Bootstrapped a Django project using uv, with options for both local and
  containerized setup.
- Created a production-ready Dockerfile using Docker Hardened Images and uv for
  dependency management.
- Added a `development` stage to the `Dockerfile` and configured Compose Watch
  for fast iterative development with a PostgreSQL database.

Related information:

- [Dockerfile reference](/reference/dockerfile.md)
- [Compose file reference](/reference/compose-file/_index.md)
- [Use Compose Watch](/manuals/compose/how-tos/file-watch.md)
- [Docker Hardened Images](/dhi/)
- [Multi-stage builds](/manuals/build/building/multi-stage.md)
- [uv documentation](https://docs.astral.sh/uv/)
