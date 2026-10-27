---
title: Configure the Swarm manager advertise address
---

## Configure the advertise address

Manager nodes use an advertise address to allow other nodes in the swarm access
to the Swarmkit API and overlay networking. The other nodes on the swarm must be
able to access the manager node on its advertise address.

If you don't specify an advertise address, Docker checks if the system has a
single IP address. If so, Docker uses the IP address with the listening port
`2377` by default. If the system has multiple IP addresses, you must specify the
correct `--advertise-addr` to enable inter-manager communication and overlay
networking:

```console
$ docker swarm init --advertise-addr <MANAGER-IP>
```

You must also specify the `--advertise-addr` if the address where other nodes
reach the first manager node is not the same address the manager sees as its
own. For instance, in a cloud setup that spans different regions, hosts have
both internal addresses for access within the region and external addresses that
you use for access from outside that region. In this case, specify the external
address with `--advertise-addr` so that the node can propagate that information
to other nodes that subsequently connect to it.

Refer to the `docker swarm init` [CLI reference](/reference/cli/docker/swarm/init/)
for more detail on the advertise address.
