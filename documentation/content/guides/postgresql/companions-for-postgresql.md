---
title: Companions for PostgreSQL
linkTitle: Companions for PostgreSQL
description: This module explains how to customize PostgreSQL for real-world use in Docker, covering automated database initialization, performance tuning, and timezone configuration once persistent storage is in place.
keywords:
  - PostgreSQL Docker
  - Docker Compose PostgreSQL
  - container database
weight: 40
---


## PostgreSQL Ecosystem companions: pgAdmin, PgBouncer, and Performance Testing

Running a standalone PostgreSQL container is often just the beginning. What happens when thousands of connections arrive, or when you need a visual interface to manage your database?

This is where **companion tools** come into play. These applications extend PostgreSQL with capabilities the core database engine doesn't provide natively: visual administration, connection pooling, and performance benchmarking. This guide covers how to deploy pgAdmin 4, PgBouncer, Pgpool-II, and `pgbench` in Docker, when to use each tool, and real-world benchmark results demonstrating their performance impact.

## pgAdmin 4: Visual management platform

[pgAdmin 4: Visual management platform](pgadmin.md).

## PgBouncer: Lightweight connection pooling

[PgBouncer: Lightweight connection pooling](pgbouncer.md).

## `pgbench`: Performance benchmarking

[`pgbench`: Performance benchmarking](benchmark.md).

## Understanding benchmark results

[Benchmark observations and environment-dependent results](benchmark.md#understanding-benchmark-results).
