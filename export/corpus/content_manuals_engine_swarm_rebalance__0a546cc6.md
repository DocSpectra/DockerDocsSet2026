---
title: Rebalance Swarm service tasks
---

Read [How services work](how-swarm-mode-works/services.md) and [Create, update, and remove services](service-lifecycle.md).

## Force the swarm to rebalance

Generally, you do not need to force the swarm to rebalance its tasks. When you
add a new node to a swarm, or a node reconnects to the swarm after a
period of unavailability, the swarm does not automatically give a workload to
the idle node. This is a design decision. If the swarm periodically shifted tasks
to different nodes for the sake of balance, the clients using those tasks would
be disrupted. The goal is to avoid disrupting running services for the sake of
balance across the swarm. When new tasks start, or when a node with running
tasks becomes unavailable, those tasks are given to less busy nodes. The goal
is eventual balance, with minimal disruption to the end user.

You can use the `--force` or `-f` flag with the `docker service update` command
to force the service to redistribute its tasks across the available worker nodes.
This causes the service tasks to restart. Client applications may be disrupted.
If you have configured it, your service uses a [rolling update](service-updates.md#configure-a-services-update-behavior).

If you use an earlier version and you want to achieve an even balance of load
across workers and don't mind disrupting running tasks, you can force your swarm
to re-balance by temporarily scaling the service upward. Use
`docker service inspect --pretty <servicename>` to see the configured scale
of a service. When you use `docker service scale`, the nodes with the lowest
number of tasks are targeted to receive the new workloads. There may be multiple
under-loaded nodes in your swarm. You may need to scale the service up by modest
increments a few times to achieve the balance you want across all the nodes.

When the load is balanced to your satisfaction, you can scale the service back
down to the original scale. You can use `docker service ps` to assess the current
balance of your service across nodes.

See also
[`docker service scale`](/reference/cli/docker/service/scale/) and
[`docker service ps`](/reference/cli/docker/service/ps/).
