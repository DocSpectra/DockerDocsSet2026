---
description: Run Docker Engine in swarm mode
keywords: guide, swarm mode, node, Docker Engines
title: Run Docker Engine in swarm mode
---

When you first install and start working with Docker Engine, Swarm mode is
disabled by default. When you enable Swarm mode, you work with the concept of
services managed through the `docker service` command.

There are two ways to run the engine in Swarm mode:

* Create a new swarm, covered in this article.
* [Join an existing swarm](join-nodes.md).

When you run the engine in Swarm mode on your local machine, you can create and
test services based upon images you've created or other available images. In
your production environment, Swarm mode provides a fault-tolerant platform with
cluster management features to keep your services running and available.

Read [Swarm host and network prerequisites](prerequisites.md) before initialization.

These instructions assume you have installed the Docker Engine on
a machine to serve as a manager node in your swarm.

If you haven't already, read through the [Swarm mode key concepts](key-concepts.md)
and try the [Swarm mode tutorial](swarm-tutorial/_index.md).

## Create a swarm

When you run the command to create a swarm, Docker Engine starts running in Swarm mode.

Run [`docker swarm init`](/reference/cli/docker/swarm/init/)
to create a single-node swarm on the current node. The engine sets up the swarm
as follows:

* Switches the current node into Swarm mode.
* Creates a swarm named `default`.
* Designates the current node as a leader manager node for the swarm.
* Names the node with the machine hostname.
* Configures the manager to listen on an active network interface on port `2377`.
* Sets the current node to `Active` availability, meaning it can receive tasks
from the scheduler.
* Starts an internal distributed data store for Engines participating in the
swarm to maintain a consistent view of the swarm and all services running on it.
* By default, generates a self-signed root CA for the swarm.
* By default, generates tokens for worker and manager nodes to join the
swarm.
* Creates an overlay network named `ingress` for publishing service ports
external to the swarm.
* Creates an overlay default IP addresses and subnet mask for your networks

The output for `docker swarm init` provides the connection command to use when
you join new worker nodes to the swarm:

```console
$ docker swarm init
Swarm initialized: current node (dxn1zf6l61qsb1josjja83ngz) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
    192.168.99.100:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

### Configuring default address pools

See [Configure Swarm overlay address pools](address-pools.md).

### Configure the advertise address

See [Configure the manager advertise address](advertise-address.md).

### View the join command or update a swarm join token

See [View and rotate join tokens](join-tokens.md), including token secrecy and rotation guidance.

## Learn more

* [Join nodes to a swarm](join-nodes.md)
* `swarm init` [command line reference](/reference/cli/docker/swarm/init/)
* [Swarm mode tutorial](swarm-tutorial/_index.md)
