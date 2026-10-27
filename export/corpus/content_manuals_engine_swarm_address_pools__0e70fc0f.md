---
title: Configure Swarm overlay address pools
---

## Configuring default address pools

By default Swarm mode uses a default address pool `10.0.0.0/8` for global scope (overlay) networks. Every 
network that does not have a subnet specified will have a subnet sequentially allocated from this pool. In 
some circumstances it may be desirable to use a different default IP address pool for networks. 

For example, if the default `10.0.0.0/8` range conflicts with already allocated address space in your network, 
then it is desirable to ensure that networks use a different range without requiring swarm users to specify 
each subnet with the `--subnet` command. 

To configure custom default address pools, you must define pools at swarm initialization using the 
`--default-addr-pool` command line option. This command line option uses CIDR notation for defining the subnet mask.
To create the custom address pool for Swarm, you must define at least one default address pool, and an optional default address pool subnet mask. For example, for the `10.0.0.0/27`, use the value `27`.

Docker allocates subnet addresses from the address ranges specified by the `--default-addr-pool` option. For example, a command line option `--default-addr-pool 10.10.0.0/16` indicates that Docker will allocate subnets from that `/16` address range. If `--default-addr-pool-mask-len` were unspecified or set explicitly to 24, this would result in 256 `/24` networks of the form `10.10.X.0/24`.

The subnet range comes from the `--default-addr-pool`, (such as `10.10.0.0/16`). The size of 16 there represents the number of networks one can create within that `default-addr-pool` range. The `--default-addr-pool` option may occur multiple times with each option providing additional addresses for docker to use for overlay subnets.

The format of the command is:

```console
$ docker swarm init --default-addr-pool <IP range in CIDR> [--default-addr-pool <IP range in CIDR> --default-addr-pool-mask-length <CIDR value>]
```

The command to create a default IP address pool with a /16 (class B) for the `10.20.0.0` network looks like this:

```console
$ docker swarm init --default-addr-pool 10.20.0.0/16
```

The command to create a default IP address pool with a `/16` (class B) for the `10.20.0.0` and `10.30.0.0` networks, and to 
create a subnet mask of `/26` for each network looks like this:

```console
$ docker swarm init --default-addr-pool 10.20.0.0/16 --default-addr-pool 10.30.0.0/16 --default-addr-pool-mask-length 26
```

In this example, `docker network create -d overlay net1` will result in `10.20.0.0/26` as the allocated subnet for `net1`, 
and `docker network create -d overlay net2` will result in `10.20.0.64/26` as the allocated subnet for `net2`. This continues until 
all the subnets are exhausted. 

See the [`docker swarm init` CLI reference](/reference/cli/docker/swarm/init/) for more detail on the `--default-addr-pool` flag.

## Using custom default address pools

To customize subnet allocation for your Swarm networks, you can optionally configure them during `swarm init`.

For example, the following command is used when initializing Swarm:

```console
$ docker swarm init --default-addr-pool 10.20.0.0/16 --default-addr-pool-mask-length 26
```

Whenever a user creates a network, but does not use the `--subnet` command line option, the subnet for this network will be allocated sequentially from the next available subnet from the pool. If the specified network is already allocated, that network will not be used for Swarm. 

Multiple pools can be configured if discontiguous address space is required. However, allocation from specific pools is not supported. Network subnets will be allocated sequentially from the IP pool space and subnets will be reused as they are deallocated from networks that are deleted.

The default mask length can be configured and is the same for all networks. It is set to `/24` by default. To change the default subnet mask length, use the `--default-addr-pool-mask-length` command line option.

> [!NOTE]
>
> Default address pools can only be configured on `swarm init` and cannot be altered after cluster creation.

## Overlay network size limitations

Docker recommends creating overlay networks with `/24` blocks. The `/24` overlay network blocks limit the network to 256 IP addresses. 

This recommendation addresses [limitations with swarm mode](https://github.com/moby/moby/issues/30820). 
If you need more than 256 IP addresses, do not increase the IP block size. You can either use `dnsrr` 
endpoint mode with an external load balancer, or use multiple smaller overlay networks. See 
[Configure service discovery](service-discovery.md) for more information about different endpoint modes.
