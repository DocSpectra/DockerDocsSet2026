---
title: Pre-seeding database with schema and data at startup for development environment
linktitle: Pre-seeding database  
description: &desc Pre-seeding database with schema and data at startup for development environment
keywords: Pre-seeding, database, postgres, container-supported development
summary: *desc
tags: [app-dev, databases]
params:
  time: 20 minutes
---

Pre-seeding databases with essential data and schema during local development is a common practice to enhance the development and testing workflow. By simulating real-world scenarios, this practice helps catch frontend issues early, ensures alignment between Database Administrators and Software Engineers, and facilitates smoother collaboration. Pre-seeding offers benefits like confident deployments, consistency across environments, and early issue detection, ultimately improving the overall development process.

In this guide, you will learn how to:

- Use Docker to launch up a Postgres container
- Pre-seed Postgres using a SQL script
- Pre-seed Postgres by copying SQL files into Docker image
- Pre-seed Postgres using JavaScript code

## Using Postgres with Docker

The [official Docker image for Postgres](https://hub.docker.com/_/postgres) provides a convenient way to run Postgres database on your development machine. A Postgres Docker image is a pre-configured environment that encapsulates the PostgreSQL database system. It's a self-contained unit, ready to run in a Docker container. By using this image, you can quickly and easily set up a Postgres instance without the need for manual configuration.

## Prerequisites

The following prerequisites are required to follow along with this how-to guide:

- [Docker Desktop](prerequisites.md#docker-desktop) 

## Launching Postgres

[Launching Postgres](pre-seeding-start.md).

## Pre-seed the Postgres database using a SQL script

[Pre-seed the Postgres database using a SQL script](pre-seeding-sql.md).

## Pre-seed the database by bind-mounting a SQL script

[Pre-seed the database by bind-mounting a SQL script](pre-seeding-image.md).

## Pre-seed the database using JavaScript code

[Pre-seed the database using JavaScript code](pre-seeding-javascript.md).

## Recap

Pre-seeding a database with schema and data at startup is essential for creating a consistent and realistic testing environment, which helps in identifying issues early in development and aligning frontend and backend work. This guide has equipped you with the knowledge and practical steps to achieve pre-seeding using various methods, including SQL script, Docker integration, and JavaScript code.
