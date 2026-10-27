---
title: Immediate setup & data persistence
description: Get PostgreSQL running in Docker in under five minutes. Learn how to configure named volumes and bind mounts to persist your database across container restarts.
keywords:
  - PostgreSQL Docker
  - Docker Compose PostgreSQL
  - container database
weight: 10
---

This guide gets you from zero to a running PostgreSQL container in under five minutes, then explains how to keep your data safe across container restarts and removals.

## Overview

Running PostgreSQL in Docker requires understanding one critical concept: containers are ephemeral, but your data shouldn't be. This guide covers:

- Starting PostgreSQL with a single command
- Understanding why containers lose data by default
- Configuring volumes for persistent storage
- Translating your setup to Docker Compose

## Prerequisites

[Docker installed](../prerequisites.md#docker-installed).

## Quick start (minimal viable container)

[Start PostgreSQL and open psql](start.md).

## The data persistence problem

[The data persistence problem](data-persistence.md).

## Named volumes

[Named volumes](named-volumes.md).

## Bind mounts (alternative)

[Bind mounts (alternative)](bind-mounts.md).

## Docker Compose configuration

[Docker Compose configuration](compose.md).

## Next steps

With persistent storage configured, you're ready to customize PostgreSQL further. The next chapter of the guide covers:

- Automated schema creation with initialization scripts
- Performance tuning for containerized workloads
- Timezone and locale configuration
