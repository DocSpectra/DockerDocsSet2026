---
title: Separate Swarm control and data traffic
---

## Prerequisites and context

See [Swarm host and network prerequisites](prerequisites.md) and [Swarm traffic and network concepts](network-context.md).

## Use a separate interface for control and data traffic

By default, all swarm traffic is sent over the same interface, including control
and management traffic for maintaining the swarm itself and data traffic to and
from the service containers.

You can separate this traffic by passing
the `--data-path-addr` flag when initializing or joining the swarm. If there are
multiple interfaces, `--advertise-addr` must be specified explicitly, and
`--data-path-addr` defaults to `--advertise-addr` if not specified. Traffic about
joining, leaving, and managing the swarm is sent over the
`--advertise-addr` interface, and traffic among a service's containers is sent 
over the `--data-path-addr` interface. These flags can take an IP address or
a network device name, such as `eth0`.

This example initializes a swarm with a separate `--data-path-addr`. It assumes
that your Docker host has two different network interfaces: 10.0.0.1 should be
used for control and management traffic and 192.168.0.1 should be used for
traffic relating to services.

```console
$ docker swarm init --advertise-addr 10.0.0.1 --data-path-addr 192.168.0.1
```

This example joins the swarm managed by host `192.168.99.100:2377` and sets the
`--advertise-addr` flag to `eth0` and the `--data-path-addr` flag to `eth1`.

```console
$ docker swarm join \
  --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2d7c \
  --advertise-addr eth0 \
  --data-path-addr eth1 \
  192.168.99.100:2377
```
