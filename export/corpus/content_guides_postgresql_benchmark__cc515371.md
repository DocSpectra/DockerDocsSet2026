---
title: "`pgbench`: Performance benchmarking"
description: "`pgbench`: Performance benchmarking"
---

## Setup and context

[PostgreSQL and PgBouncer setup](pgbouncer.md).

[Connection pooling context](connection-pooling.md).

## `pgbench`: Performance benchmarking

`pgbench` is a benchmarking utility included with the official PostgreSQL image. It allows you to simulate heavy workloads and verify how your Docker configuration performs under pressure.

### Initialize benchmark tables

First, create the test tables. The `-s` (scale) parameter determines data size—scale factor 50 creates approximately 5 million rows:

```bash
docker exec postgres pgbench -i -s 50 -U postgres benchmark
```

### Run stress tests

Key parameters:

- `-c`: Number of simulated clients
- `-j`: Number of threads
- `-T`: Duration in seconds

Test with direct PostgreSQL connection:

```bash
docker exec postgres pgbench -h localhost -U postgres -c 50 -j 4 -T 60 benchmark
```

Test through PgBouncer:

```bash
docker exec postgres pgbench -h pgbouncer -p 6432 -U postgres -c 50 -j 4 -T 60 benchmark
```

## Understanding benchmark results

Does PgBouncer actually make a difference? Run the benchmarks yourself to find out. Your results will vary based on your hardware, Docker configuration, network setup, and system load.

### What to expect

When you run these benchmarks, you'll observe patterns rather than specific numbers. Think of it like comparing two different routes to work: the "faster" route depends on traffic conditions, time of day, and your vehicle.

### Key observations

When comparing direct connections versus PgBouncer, you'll typically notice:

#### 1. Connection overhead differs significantly

Direct connections require PostgreSQL to spawn a new process for each client. PgBouncer reuses existing connections. Watch the "initial connection time" metric in your results—PgBouncer often shows dramatically faster connection setup.

#### 2. Behavior under pressure reveals the real difference

Try increasing the client count (`-c` parameter) gradually: 50, 100, 150, 200. At some point, direct connections will fail with "too many clients already" while PgBouncer continues handling requests. This is PgBouncer's primary value: **it prevents connection exhaustion**.

#### 3. Throughput varies by environment

On some systems, direct connections show higher transactions per second (TPS) at low concurrency. On others, PgBouncer wins even with few clients. The difference depends on:
- CPU and memory available
- Docker networking overhead
- Disk I/O speed
- Whether connections are being rapidly opened and closed
