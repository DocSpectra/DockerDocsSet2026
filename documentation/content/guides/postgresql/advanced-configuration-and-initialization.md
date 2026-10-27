---
title: Advanced Configuration and Initialization
weight: 20
description: Configure PostgreSQL initialization scripts, tune performance parameters, and set timezone and locale settings for containerized deployments.
keywords:
  - PostgreSQL Docker
  - Docker Compose PostgreSQL
  - container database
  - PostgreSQL performance tuning
---

With [persistent storage](named-volumes.md) configured, you're ready to customize PostgreSQL for real-world use. This guide covers advanced configuration techniques for running PostgreSQL in Docker containers, including automated database initialization, performance tuning, and timezone configuration.

## Overview

While PostgreSQL containers can be started quickly with default settings, production environments require customized configurations. This guide explains how to:

- Automate database, schema, and user creation during container startup
- Tune PostgreSQL performance parameters for containerized workloads
- Configure timezone and locale settings

## Initialization scripts

[Initialization behavior, supported files, and existing-data caveat](initialization.md).

## Mounting initialization scripts

[Mounting initialization scripts](initialize-database.md).

## Initialization script example

[Create the initialization SQL file](initialize-database.md#initialization-script-example).

## Performance tuning

[Performance tuning](tune-performance.md).

## Key configuration parameters

[Connection, memory, I/O, and timeout parameters](tune-performance.md#key-configuration-parameters).

## Timezone and locale configuration

[Timezone and locale configuration](configure-locale.md).

## Connecting to the database

[Connecting to the database](psql.md).
