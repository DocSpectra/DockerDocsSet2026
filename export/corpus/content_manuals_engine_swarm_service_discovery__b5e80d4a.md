---
title: Configure Swarm service discovery
---

### Configure service discovery

Service discovery is the mechanism Docker uses to route a request from your
service's external clients to an individual swarm node, without the client
needing to know how many nodes are participating in the service or their
IP addresses or ports. You don't need to publish ports which are used between
services on the same network. For instance, if you have a
WordPress service that stores its data in a MySQL service, and they are connected to the same overlay network, you do not need to publish
the MySQL port to the client, only the WordPress HTTP port.

Service discovery can work in two different ways: internal connection-based
load-balancing at Layers 3 and 4 using the embedded DNS and a virtual IP (VIP),
or external and customized request-based load-balancing at Layer 7 using DNS
round robin (DNSRR). You can configure this per service.

- By default, when you attach a service to a network and that service publishes
  one or more ports, Docker assigns the service a virtual IP (VIP), which is the
  "front end" for clients to reach the service. Docker keeps a list of all
  worker nodes in the service, and routes requests between the client and one of
  the nodes. Each request from the client might be routed to a different node.

- If you configure a service to use DNS round-robin (DNSRR) service discovery,
  there is not a single virtual IP. Instead, Docker sets up DNS entries for the
  service such that a DNS query for the service name returns a list of IP
  addresses, and the client connects directly to one of these.

  DNS round-robin is useful in cases where you want to use your own load
  balancer, such as HAProxy. To configure a service to use DNSRR, use the flag
  `--endpoint-mode dnsrr` when creating a new service or updating an existing
  one.
