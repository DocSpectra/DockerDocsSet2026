---
title: Swarm traffic and network concepts
---

## Swarm and types of traffic

A Docker swarm generates two different kinds of traffic:

- Control and management plane traffic: This includes swarm management
  messages, such as requests to join or leave the swarm. This traffic is
  always encrypted.

- Application data plane traffic: This includes container traffic and
  traffic to and from external clients.

## Key network concepts

The following three network concepts are important to swarm services:

- Overlay networks manage communications among the Docker daemons
  participating in the swarm. You can create overlay networks, in the same way
  as user-defined networks for standalone containers. You can attach a service
  to one or more existing overlay networks as well, to enable service-to-service
  communication. Overlay networks are Docker networks that use the `overlay`
  network driver.

- The ingress network is a special overlay network that facilitates
  load balancing among a service's nodes. When any swarm node receives a
  request on a published port, it hands that request off to a module called
  `IPVS`. `IPVS` keeps track of all the IP addresses participating in that
  service, selects one of them, and routes the request to it, over the
  `ingress` network.

  The `ingress` network is created automatically when you initialize or join a
  swarm. Most users do not need to customize its configuration, but Docker allows
  you to do so.

- The docker_gwbridge is a bridge network that connects the overlay
  networks (including the `ingress` network) to an individual Docker daemon's
  physical network. By default, each container a service is running is connected
  to its local Docker daemon host's `docker_gwbridge` network.

  The `docker_gwbridge` network is created automatically when you initialize or
  join a swarm. Most users do not need to customize its configuration, but
  Docker allows you to do so.

> [!TIP]
>
> See also [Networking overview](/manuals/engine/network/_index.md) for more details about Swarm networking in general.

## Configure encryption of application data {#encryption}

Management and control plane data related to a swarm is always encrypted.
For more details about the encryption mechanisms, see the
[Docker swarm mode overlay network security model](/manuals/engine/network/drivers/overlay.md).

Application data among swarm nodes is not encrypted by default. To encrypt this
traffic on a given overlay network, use the `--opt encrypted` flag on `docker
network create`. This enables IPSEC encryption at the level of the vxlan. This
encryption imposes a non-negligible performance penalty, so you should test this
option before using it in production.

> [!NOTE]
>
> You must customize the automatically created ingress
> to enable encryption. By default, all ingress traffic is unencrypted, as encryption
> is a network-level option.
