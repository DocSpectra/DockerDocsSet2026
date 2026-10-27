---
description: Learn how to run, connect to, and persist data in a local containerized database.
keywords: database, mysql
title: Use containerized databases
summary: |
  Learn how to effectively run and manage databases as containers.
tags: [databases]
aliases:
  - /guides/use-case/databases/
params:
  time: 20 minutes
---

Using a local containerized database offers flexibility and ease of setup,
letting you mirror production environments closely without the overhead of
traditional database installations. Docker simplifies this process, enabling you
to deploy, manage, and scale databases in isolated containers with just a few
commands.

In this guide, you'll learn how to:

- Run a local containerized database
- Access the shell of a containerized database
- Connect to a containerized database from your host
- Connect to a containerized database from another container
- Persist database data in a volume
- Build a customized database image
- Use Docker Compose to run a database

This guide uses the MySQL image for examples, but the concepts can be applied to other database images.

## Prerequisites

[Docker installed](prerequisites.md#docker-installed).

## Run a local containerized database

[Run a local containerized database](database-tasks/run.md).

## Access the shell of a containerized database

[Access the shell of a containerized database](database-tasks/shell.md).

## Connect to a containerized database from your host

[Connect to a containerized database from your host](database-tasks/connect-from-host.md).

## Connect to a containerized database from another container

[Connect to a containerized database from another container](database-tasks/connect-from-container.md).

## Persist database data in a volume

[Persist database data in a volume](database-tasks/persist-data.md).

## Build a customized database image

[Build a customized database image](database-tasks/custom-image.md).

## Use Docker Compose to run a database

[Use Docker Compose to run a database](database-tasks/compose.md).

## Summary

This guide introduced you to the essentials of using containerized databases,
specifically focusing on MySQL, to enhance flexibility, ease of setup, and
consistency across your development environments. The use-cases covered in
this guide not only streamline your development workflows but also prepare you
for more advanced database management and deployment scenarios, ensuring your
data-driven applications remain robust and scalable.

Related information:

- [Docker Hub database images](https://hub.docker.com/search?q=database&type=image)
- [Dockerfile reference](/reference/dockerfile/)
- [Compose file reference](/reference/compose-file/)
- [CLI reference](/reference/cli/docker/)
- [Database samples](../reference/samples/_index.md#databases)
