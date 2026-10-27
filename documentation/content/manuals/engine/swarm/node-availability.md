---
title: Swarm node availability and drain behavior
---

The `AVAILABILITY` column shows whether or not the scheduler can assign tasks to
the node:

* `Active` means that the scheduler can assign tasks to the node.
* `Pause` means the scheduler doesn't assign new tasks to the node, but existing
  tasks remain running.
* `Drain` means the scheduler doesn't assign new tasks to the node. The
   scheduler shuts down any existing tasks and schedules them on an available
   node.

## Tutorial drain behavior


In earlier steps of the tutorial, all the nodes have been running with `Active`
availability. The swarm manager can assign tasks to any `Active` node, so up to
now all nodes have been available to receive tasks.

Sometimes, such as planned maintenance times, you need to set a node to `Drain`
availability. `Drain` availability  prevents a node from receiving new tasks
from the swarm manager. It also means the manager stops tasks running on the
node and launches replica tasks on a node with `Active` availability.

> [!IMPORTANT]: 
>
> Setting a node to `Drain` does not remove standalone containers from that node,
> such as those created with `docker run`, `docker compose up`, or the Docker Engine
> API. A node's status, including `Drain`, only affects the node's ability to schedule
> swarm service workloads.
