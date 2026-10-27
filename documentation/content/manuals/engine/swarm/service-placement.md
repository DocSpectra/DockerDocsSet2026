---
title: Control Swarm service scale and placement
---

## Prerequisites and shared procedures

See [Create, update, and remove Swarm services](service-lifecycle.md) and [How services work](how-swarm-mode-works/services.md).

## Control service placement

Swarm services provide a few different ways for you to control scale and
placement of services on different nodes.

- You can specify whether the service needs to run a specific number of replicas
  or should run globally on every worker node. See
  [Replicated or global services](#replicated-or-global-services).

- You can configure the service's
  [CPU or memory requirements](#reserve-memory-or-cpus-for-a-service), and the
  service only runs on nodes which can meet those requirements.

- [Placement constraints](#placement-constraints) let you configure the service
  to run only on nodes with specific (arbitrary) metadata set, and cause the
  deployment to fail if appropriate nodes do not exist. For instance, you can
  specify that your service should only run on nodes where an arbitrary label
  `pci_compliant` is set to `true`.

- [Placement preferences](#placement-preferences) let you apply an arbitrary
  label with a range of values to each node, and spread your service's tasks
  across those nodes using an algorithm. Currently, the only supported algorithm
  is `spread`, which tries to place them evenly. For instance, if you
  label each node with a label `rack` which has a value from 1-10, then specify
  a placement preference keyed on `rack`, then service tasks are placed as
  evenly as possible across all nodes with the label `rack`, after taking other
  placement constraints, placement preferences, and other node-specific
  limitations into account.

  Unlike constraints, placement preferences are best-effort, and a service does
  not fail to deploy if no nodes can satisfy the preference. If you specify a
  placement preference for a service, nodes that match that preference are
  ranked higher when the swarm managers decide which nodes should run the
  service tasks. Other factors, such as high availability of the service,
  also factor into which nodes are scheduled to run service tasks. For
  example, if you have N nodes with the rack label (and then some others), and
  your service is configured to run N+1 replicas, the +1 is scheduled on a
  node that doesn't already have the service on it if there is one, regardless
  of whether that node has the `rack` label or not.


### Replicated or global services

Swarm mode has two types of services: replicated and global. For replicated
services, you specify the number of replica tasks for the swarm manager to
schedule onto available nodes. For global services, the scheduler places one
task on each available node that meets the service's
[placement constraints](#placement-constraints) and
[resource requirements](#reserve-memory-or-cpus-for-a-service).

You control the type of service using the `--mode` flag. If you don't specify a
mode, the service defaults to `replicated`. For replicated services, you specify
the number of replica tasks you want to start using the `--replicas` flag. For
example, to start a replicated nginx service with 3 replica tasks:

```console
$ docker service create \
  --name my_web \
  --replicas 3 \
  nginx
```

To start a global service on each available node, pass `--mode global` to
`docker service create`. Every time a new node becomes available, the scheduler
places a task for the global service on the new node. For example to start a
service that runs alpine on every node in the swarm:

```console
$ docker service create \
  --name myservice \
  --mode global \
  alpine top
```

Service constraints let you set criteria for a node to meet before the scheduler
deploys a service to the node. You can apply constraints to the
service based upon node attributes and metadata or engine metadata. For more
information on constraints, refer to the `docker service create`
[CLI reference](/reference/cli/docker/service/create/).

### Reserve memory or CPUs for a service

To reserve a given amount of memory or number of CPUs for a service, use the
`--reserve-memory` or `--reserve-cpu` flags. If no available nodes can satisfy
the requirement (for instance, if you request 4 CPUs and no node in the swarm
has 4 CPUs), the service remains in a pending state until an appropriate node is
available to run its tasks.

#### Out Of Memory Exceptions (OOME)

If your service attempts to use more memory than the swarm node has available,
you may experience an Out Of Memory Exception (OOME) and a container, or the
Docker daemon, might be killed by the kernel OOM killer. To prevent this from
happening, ensure that your application runs on hosts with adequate memory and
see
[Understand the risks of running out of memory](/manuals/engine/containers/resource_constraints.md#understand-the-risks-of-running-out-of-memory).

Swarm services allow you to use resource constraints, placement preferences, and
labels to ensure that your service is deployed to the appropriate swarm nodes.

### Placement constraints

Use placement constraints to control the nodes a service can be assigned to. In
the following example, the service only runs on nodes with the
[label](manage-nodes.md#add-or-remove-label-metadata) `region` set
to `east`. If no appropriately-labelled nodes are available, tasks will wait in
`Pending` until they become available. The `--constraint` flag uses an equality
operator (`==` or `!=`). For replicated services, it is possible that all
services run on the same node, or each node only runs one replica, or that some
nodes don't run any replicas. For global services, the service runs on every
node that meets the placement constraint and any [resource requirements](#reserve-memory-or-cpus-for-a-service).

```console
$ docker service create \
  --name my-nginx \
  --replicas 5 \
  --constraint node.labels.region==east \
  nginx
```

You can also use the `constraint` service-level key in a `compose.yaml`
file.

If you specify multiple placement constraints, the service only deploys onto
nodes where they are all met. The following example limits the service to run on
all nodes where `region` is set to `east` and `type` is not set to `devel`:

```console
$ docker service create \
  --name my-nginx \
  --mode global \
  --constraint node.labels.region==east \
  --constraint node.labels.type!=devel \
  nginx
```

You can also use placement constraints in conjunction with placement preferences
and CPU/memory constraints. Be careful not to use settings that are not
possible to fulfill.

For more information on constraints, refer to the `docker service create`
[CLI reference](/reference/cli/docker/service/create/).

### Placement preferences

While [placement constraints](#placement-constraints) limit the nodes a service
can run on, _placement preferences_ try to place tasks on appropriate nodes
in an algorithmic way (currently, only spread evenly). For instance, if you
assign each node a `rack` label, you can set a placement preference to spread
the service evenly across nodes with the `rack` label, by value. This way, if
you lose a rack, the service is still running on nodes on other racks.

Placement preferences are not strictly enforced. If no node has the label
you specify in your preference, the service is deployed as though the
preference were not set.

> [!NOTE]
>
> Placement preferences are ignored for global services.

The following example sets a preference to spread the deployment across nodes
based on the value of the `datacenter` label. If some nodes have
`datacenter=us-east` and others have `datacenter=us-west`, the service is
deployed as evenly as possible across the two sets of nodes.

```console
$ docker service create \
  --replicas 9 \
  --name redis_2 \
  --placement-pref 'spread=node.labels.datacenter' \
  redis:7.4.0
```

> [!NOTE]
>
> Nodes which are missing the label used to spread still receive
> task assignments. As a group, these nodes receive tasks in equal
> proportion to any of the other groups identified by a specific label
> value. In a sense, a missing label is the same as having the label with
> a null value attached to it. If the service should only run on
> nodes with the label being used for the spread preference, the
> preference should be combined with a constraint.

You can specify multiple placement preferences, and they are processed in the
order they are encountered. The following example sets up a service with
multiple placement preferences. Tasks are spread first over the various
datacenters, and then over racks (as indicated by the respective labels):

```console
$ docker service create \
  --replicas 9 \
  --name redis_2 \
  --placement-pref 'spread=node.labels.datacenter' \
  --placement-pref 'spread=node.labels.rack' \
  redis:7.4.0
```

You can also use placement preferences in conjunction with placement constraints
or CPU/memory constraints. Be careful not to use settings that are not
possible to fulfill.

This diagram illustrates how placement preferences work:

![How placement preferences work](images/placement_prefs.png)

When updating a service with `docker service update`, `--placement-pref-add`
appends a new placement preference after all existing placement preferences.
`--placement-pref-rm` removes an existing placement preference that matches the
argument.
