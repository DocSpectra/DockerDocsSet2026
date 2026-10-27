---
title: Common challenges and questions
description: Explore common challenges and questions related to Docker Compose.
weight: 30
---

<!-- vale Docker.HeadingLength = NO -->

### Do I need to maintain a separate Compose file for my development, testing, and staging environments?

You don't necessarily need to maintain entirely separate Compose files for your
development, testing, and staging environments. You can define all your
services in a single Compose file (`compose.yaml`). You can use profiles to
group service configurations specific to each environment (`dev`, `test`,
`staging`).

When you need to spin up an environment, you can activate the corresponding
profiles. For example, to set up the development environment:

```console
$ docker compose --profile dev up
```

This command starts only the services associated with the `dev` profile,
leaving the rest inactive.

For more information on using profiles, see [Using profiles with
Compose](/compose/how-tos/profiles/).

### How can I enforce the database service to start up before the frontend service?

See [Database readiness](/manuals/compose/how-tos/startup-order.md#database-readiness) for dependency order, health checks, and waiting for initialization.

### Can I use Compose to build a Docker image?

See [Build images with Compose](/manuals/compose/intro/compose-cli.md#build-images-with-compose).

### What is the difference between Docker Compose and Dockerfile?

See [Dockerfiles and Compose files](/manuals/compose/intro/compose-cli.md#dockerfiles-and-compose-files).

### What is the difference between the `docker compose up` and `docker compose run` commands?

See [Start an application or run a one-off task](/manuals/compose/intro/compose-cli.md#start-an-application-or-run-a-one-off-task).

<div id="compose-lp-survey-anchor"></div>
