---
title: Customize the Swarm ingress network
---

## Prerequisites and context

See [Swarm host and network prerequisites](prerequisites.md) and [Swarm traffic and network concepts](network-context.md).

## Customize the ingress network {#customize-ingress}

Most users never need to configure the `ingress` network, but Docker allows you
to do so. This can be useful if the automatically-chosen subnet
conflicts with one that already exists on your network, or you need to customize
other low-level network settings such as the MTU, or if you want to
[enable encryption](network-context.md#encryption).

Customizing the `ingress` network involves removing and recreating it. This is
usually done before you create any services in the swarm. If you have existing
services which publish ports, those services need to be removed before you can
remove the `ingress` network.

During the time that no `ingress` network exists, existing services which do not
publish ports continue to function but are not load-balanced. This affects
services which publish ports, such as a WordPress service which publishes port
80.

1.  Inspect the `ingress` network using `docker network inspect ingress`, and
    remove any services whose containers are connected to it. These are services
    that publish ports, such as a WordPress service which publishes port 80. If
    all such services are not stopped, the next step fails.

2.  Remove the existing `ingress` network:

    ```console
    $ docker network rm ingress

    WARNING! Before removing the routing-mesh network, make sure all the nodes
    in your swarm run the same docker engine version. Otherwise, removal may not
    be effective and functionality of newly created ingress networks will be
    impaired.
    Are you sure you want to continue? [y/N]
    ```

3.  Create a new overlay network using the `--ingress` flag, along  with the
    custom options you want to set. This example sets the MTU to 1200, sets
    the subnet to `10.11.0.0/16`, and sets the gateway to `10.11.0.2`.

    ```console
    $ docker network create \
      --driver overlay \
      --ingress \
      --subnet=10.11.0.0/16 \
      --gateway=10.11.0.2 \
      --opt com.docker.network.driver.mtu=1200 \
      my-ingress
    ```

    > [!NOTE]
    >
    > You can name your `ingress` network something other than
    > `ingress`, but you can only have one. An attempt to create a second one
    > fails.

4.  Restart the services that you stopped in the first step.
