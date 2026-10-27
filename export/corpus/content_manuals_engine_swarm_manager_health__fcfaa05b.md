---
title: Monitor and troubleshoot Swarm manager health
---

## Context and caveats

Read [Plan managers and maintain quorum](manager-quorum.md) and [How nodes work](how-swarm-mode-works/nodes.md).

## Monitor swarm health

You can monitor the health of manager nodes by querying the docker `nodes` API
in JSON format through the `/nodes` HTTP endpoint. Refer to the
[nodes API documentation](/reference/api/engine/version/v1.25/#tag/Node)
for more information.

From the command line, run `docker node inspect <id-node>` to query the nodes.
For instance, to query the reachability of the node as a manager:


```console
$ docker node inspect manager1 --format "{{ .ManagerStatus.Reachability }}"
reachable
```


To query the status of the node as a worker that accept tasks:


```console
$ docker node inspect manager1 --format "{{ .Status.State }}"
ready
```


From those commands, we can see that `manager1` is both at the status
`reachable` as a manager and `ready` as a worker.

An `unreachable` health status means that this particular manager node is unreachable
from other manager nodes. In this case you need to take action to restore the unreachable
manager:

- Restart the daemon and see if the manager comes back as reachable.
- Reboot the machine.
- If neither restarting nor rebooting works, you should add another manager node or promote a worker to be a manager node. You also need to cleanly remove the failed node entry from the manager set with `docker node demote <NODE>` and `docker node rm <id-node>`.

Alternatively you can also get an overview of the swarm health from a manager
node with `docker node ls`:

```console
$ docker node ls
ID                           HOSTNAME  MEMBERSHIP  STATUS  AVAILABILITY  MANAGER STATUS
1mhtdwhvsgr3c26xxbnzdc3yp    node05    Accepted    Ready   Active
516pacagkqp2xc3fk9t1dhjor    node02    Accepted    Ready   Active        Reachable
9ifojw8of78kkusuc4a6c23fx *  node01    Accepted    Ready   Active        Leader
ax11wdpwrrb6db3mfjydscgk7    node04    Accepted    Ready   Active
bb1nrq2cswhtbg4mrsqnlx1ck    node03    Accepted    Ready   Active        Reachable
di9wxgz8dtuh9d2hn089ecqkf    node06    Accepted    Ready   Active
```

## Troubleshoot a manager node

You should never restart a manager node by copying the `raft` directory from another node. The data directory is unique to a node ID. A node can only use a node ID once to join the swarm. The node ID space should be globally unique.

To cleanly re-join a manager node to a cluster:

1. Demote the node to a worker using `docker node demote <NODE>`.
2. Remove the node from the swarm using `docker node rm <NODE>`.
3. Re-join the node to the swarm with a fresh state using `docker swarm join`.

For more information on joining a manager node to a swarm, refer to
[Join nodes to a swarm](join-nodes.md).

## Forcibly remove a node

In most cases, you should shut down a node before removing it from a swarm with
the `docker node rm` command. If a node becomes unreachable, unresponsive, or
compromised you can forcefully remove the node without shutting it down by
passing the `--force` flag. For instance, if `node9` becomes compromised:

```console
$ docker node rm node9

Error response from daemon: rpc error: code = 9 desc = node node9 is not down and can't be removed

$ docker node rm --force node9

Node node9 removed from swarm
```

Before you forcefully remove a manager node, you must first demote it to the
worker role. Make sure that you always have an odd number of manager nodes if
you demote or remove a manager.
