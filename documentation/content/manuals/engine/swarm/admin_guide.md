---
description: Manager administration guide
keywords: docker, container, swarm, manager, raft
title: Administer and maintain a swarm of Docker Engines
aliases:
- /engine/swarm/manager-administration-guide/
---

When you run a swarm of Docker Engines, manager nodes are the key components
for managing the swarm and storing the swarm state. It is important to
understand some key features of manager nodes to properly deploy and
maintain the swarm.

Refer to [How nodes work](how-swarm-mode-works/nodes.md)
for a brief overview of Docker Swarm mode and the difference between manager and
worker nodes.

## Operate manager nodes in a swarm

See [Operate manager nodes in a swarm](manager-quorum.md#operate-manager-nodes-in-a-swarm).

### Maintain the quorum of managers

See [Maintain the quorum of managers](manager-quorum.md#maintain-the-quorum-of-managers).

## Configure the manager to advertise on a static IP address

See [Configure the manager to advertise on a static IP address](manager-quorum.md#configure-the-manager-to-advertise-on-a-static-ip-address).

## Add manager nodes for fault tolerance

See [Add manager nodes for fault tolerance](manager-quorum.md#add-manager-nodes-for-fault-tolerance).

### Distribute manager nodes

See [Distribute manager nodes](manager-quorum.md#distribute-manager-nodes).

### Run manager-only nodes

See [Run manager-only nodes](manager-quorum.md#run-manager-only-nodes).

## Add worker nodes for load balancing

[Add nodes to the swarm](join-nodes.md) to balance your swarm's
load. Replicated service tasks are distributed across the swarm as evenly as
possible over time, as long as the worker nodes are matched to the requirements
of the services. When limiting a service to run on only specific types of nodes,
such as nodes with a specific number of CPUs or amount of memory, remember that
worker nodes that do not meet these requirements cannot run these tasks.

## Monitor swarm health

See [Monitor swarm health](manager-health.md#monitor-swarm-health).

## Troubleshoot a manager node

See [Troubleshoot a manager node](manager-health.md#troubleshoot-a-manager-node).

## Forcibly remove a node

See [Forcibly remove a node](manager-health.md#forcibly-remove-a-node).

## Back up the swarm

See [Back up the swarm](backup-recovery.md#back-up-the-swarm).

## Recover from disaster

See [Recover from disaster](backup-recovery.md#recover-from-disaster).

### Restore from a backup

See [Restore from a backup](backup-recovery.md#restore-from-a-backup).

### Recover from losing the quorum

See [Recover from losing the quorum](backup-recovery.md#recover-from-losing-the-quorum).

## Force the swarm to rebalance

See [Force the swarm to rebalance](rebalance.md#force-the-swarm-to-rebalance).
