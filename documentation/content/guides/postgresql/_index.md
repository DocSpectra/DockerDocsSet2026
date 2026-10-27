---
title: PostgreSQL specific guide
linkTitle: PostgreSQL
description: Containerize PostgreSQL databases using Docker
keywords: Docker, getting started, postgresql, language
summary: |
  This guide explains how to containerize PostgreSQL databases using
  Docker.
toc_min: 1
toc_max: 2
tags: [databases]
params:
  time: 20 minutes
---

## Setup and storage

- [Start PostgreSQL](immediate-setup-and-data-persistence.md)
- [Understand data loss on container removal](data-persistence.md)
- [Persist data with a named volume](named-volumes.md)
- [Use a bind mount](bind-mounts.md)
- [Run PostgreSQL with Compose](compose.md)

## Initialization and configuration

- [Configuration overview](advanced-configuration-and-initialization.md)
- [Mount initialization scripts](initialize-database.md)
- [Tune performance](tune-performance.md)
- [Set timezone and locale](configure-locale.md)
- [Open a psql session](psql.md)

## Connections and companion tools

- [Connection options and troubleshooting](networking-and-connectivity.md)
- [Visual management, pooling, and benchmarking](companions-for-postgresql.md)
