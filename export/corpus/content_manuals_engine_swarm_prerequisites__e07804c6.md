---
title: Swarm host and network prerequisites
---

## Tutorial setup

To run this tutorial, you need:

* [Three Linux hosts which can communicate over a network, with Docker installed](#three-networked-host-machines)
* [The IP address of the manager machine](#the-ip-address-of-the-manager-machine)
* [Open ports between the hosts](#open-protocols-and-ports-between-the-hosts)

### Three networked host machines

This tutorial requires three Linux hosts which have Docker installed and can
communicate over a network. These can be physical machines, virtual machines,
Amazon EC2 instances, or hosted in some other way.

One of these machines is a manager (called `manager1`) and two of them are
workers (`worker1` and `worker2`).

> [!NOTE]
>
> You can follow many of the tutorial steps to test single-node swarm as well, in which case you need only one host. Multi-node commands do not work, but you can initialize a swarm, create services, and scale them.

#### Install Docker Engine on Linux machines

If you are using Linux based physical computers or cloud-provided computers as
hosts, simply follow the [Linux install instructions](../install/_index.md)
for your platform. Spin up the three machines, and you are ready. You can test both
single-node and multi-node swarm scenarios on Linux machines.

### The IP address of the manager machine

The IP address must be assigned to a network interface available to the host
operating system. All nodes in the swarm need to connect to the manager at
the IP address.

Because other nodes contact the manager node on its IP address, you should use a
fixed IP address.

You can run `ifconfig` on Linux or macOS to see a list of the
available network interfaces.

The tutorial uses `manager1` : `192.168.99.100`.

### Open protocols and ports between the hosts

The following ports must be available. On some systems, these ports are open by default.

* Port `2377` TCP for communication with and between manager nodes
* Port `7946` TCP/UDP for overlay network node discovery
* Port `4789` UDP (configurable) for overlay network traffic

If you plan on creating an overlay network with encryption (`--opt encrypted`),
you also need to ensure IP protocol 50 (IPSec ESP) traffic is allowed.

Port `4789` is the default value for the Swarm data path port, also known as the VXLAN port.
It is important to prevent any untrusted traffic from reaching this port, as VXLAN does not
provide authentication. This port should only be opened to a trusted network, and never at a
perimeter firewall.

If the network which Swarm traffic traverses is not fully trusted, it is strongly suggested that
encrypted overlay networks be used. If encrypted overlay networks are in exclusive use, some
additional hardening is suggested:

* Customize the default ingress network to use encryption
* Only accept encrypted packets on the Data Path Port:

```bash
# Example iptables rule (order and other tools may require customization)
iptables -I INPUT -m udp --dport 4789 -m policy --dir in --pol none -j DROP
```

## Ingress network prerequisites

To use the ingress network in the swarm, you need to have the following
ports open between the swarm nodes before you enable Swarm mode:

* Port `7946` TCP/UDP for container network discovery.
* Port `4789` UDP (configurable) for the container ingress network.

See [Open protocols and ports between the hosts](#open-protocols-and-ports-between-the-hosts).

You must also open the published port between the swarm nodes and any external
resources, such as an external load balancer, that require access to the port.
