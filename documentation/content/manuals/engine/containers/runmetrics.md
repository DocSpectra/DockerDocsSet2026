---
description: Learn how to measure running containers, and about the different metrics
keywords: docker, metrics, CPU, memory, disk, IO, run, runtime, stats
title: Runtime metrics
weight: 50
aliases:
  - /articles/runmetrics/
  - /engine/articles/run_metrics/
  - /engine/articles/runmetrics/
  - /engine/admin/runmetrics/
  - /config/containers/runmetrics/
---

## Docker stats

You can use the `docker stats` command to live stream a container's
runtime metrics. The command supports CPU, memory usage, memory limit,
and network IO metrics.

The following is a sample output from the `docker stats` command

```console
$ docker stats redis1 redis2

CONTAINER           CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O
redis1              0.07%               796 KB / 64 MB        1.21%               788 B / 648 B       3.568 MB / 512 KB
redis2              0.07%               2.746 MB / 64 MB      4.29%               1.266 KB / 648 B    12.4 MB / 0 B
```

The [`docker stats`](/reference/cli/docker/container/stats/) reference
page has more details about the `docker stats` command.

## Control groups

See [Control groups](cgroups.md#control-groups).

### Enumerate cgroups

See [Enumerate cgroups](cgroups.md#enumerate-cgroups).

#### cgroup v1

See [cgroup v1](cgroups.md#cgroup-v1).

#### cgroup v2

See [cgroup v2](cgroups.md#cgroup-v2).

### Changing cgroup version

See [Changing cgroup version](cgroups.md#changing-cgroup-version).

### Running Docker on cgroup v2

See [Running Docker on cgroup v2](cgroups.md#running-docker-on-cgroup-v2).

### Find the cgroup for a given container

See [Find the cgroup for a given container](cgroups.md#find-the-cgroup-for-a-given-container).

### Metrics from cgroups: memory, CPU, block I/O

See [Metrics from cgroups: memory, CPU, block I/O](cgroup-metrics.md#metrics-from-cgroups-memory-cpu-block-io).

#### Memory metrics: `memory.stat`

See [Memory metrics: `memory.stat`](cgroup-metrics.md#memory-metrics-memorystat).

### CPU metrics: `cpuacct.stat`

See [CPU metrics: `cpuacct.stat`](cgroup-metrics.md#cpu-metrics-cpuacctstat).

#### Block I/O metrics

See [Block I/O metrics](cgroup-metrics.md#block-io-metrics).

### Network metrics

See [Network metrics](network-metrics.md#network-metrics).

#### iptables

See [iptables](network-metrics.md#iptables).

#### Interface-level counters

See [Interface-level counters](network-metrics.md#interface-level-counters).

## Tips for high-performance metric collection

See [Tips for high-performance metric collection](metrics-collection.md#tips-for-high-performance-metric-collection).

## Collect metrics when a container exits

See [Collect metrics when a container exits](metrics-collection.md#collect-metrics-when-a-container-exits).

