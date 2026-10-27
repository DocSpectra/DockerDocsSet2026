---
title: Connect Swarm services to overlay networks
---

## Prerequisites and shared procedures

See [Create, update, and remove Swarm services](service-lifecycle.md) and [How services work](how-swarm-mode-works/services.md).

## Connect the service to an overlay network

You can use overlay networks to connect one or more services within the swarm.

First, create overlay network on a manager node using the `docker network create`
command with the `--driver overlay` flag.

```console
$ docker network create --driver overlay my-network
```

After you create an overlay network in swarm mode, all manager nodes have access
to the network.

You can create a new service and pass the `--network` flag to attach the service
to the overlay network:

```console
$ docker service create \
  --replicas 3 \
  --network my-network \
  --name my-web \
  nginx
```

The swarm extends `my-network` to each node running the service.

You can also connect an existing service to an overlay network using the
`--network-add` flag.

```console
$ docker service update --network-add my-network my-web
```

To disconnect a running service from a network, use the `--network-rm` flag.

```console
$ docker service update --network-rm my-network my-web
```

For more information on overlay networking and service discovery, refer to
[Attach services to an overlay network](networking.md) and
[Docker swarm mode overlay network security model](/manuals/engine/network/drivers/overlay.md).
