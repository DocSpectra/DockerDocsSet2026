---
description: Use swarm mode overlay networking features
keywords: swarm, networking, ingress, overlay, service discovery
title: Manage swarm service networks
toc_max: 3
---

This page describes networking for swarm services.

## Swarm and types of traffic

See [Swarm traffic](network-context.md#swarm-and-types-of-traffic).

## Key network concepts

See [Overlay, ingress, and docker_gwbridge concepts](network-context.md#key-network-concepts).

## Firewall considerations

Read [Swarm host and network prerequisites](prerequisites.md). Docker daemons participating in a swarm need port `7946` TCP/UDP for container network discovery and port `4789` UDP (configurable) for the overlay network (including ingress) data path.

## Overlay networking

When you initialize a swarm or join a Docker host to an existing swarm, two
new networks are created on that Docker host:

- An overlay network called `ingress`, which handles the control and data traffic
  related to swarm services. When you create a swarm service and do not
  connect it to a user-defined overlay network, it connects to the `ingress`
  network by default.
- A bridge network called `docker_gwbridge`, which connects the individual
  Docker daemon to the other daemons participating in the swarm.

### Create an overlay network

To create an overlay network, specify the `overlay` driver when using the
`docker network create` command:

```console
$ docker network create \
  --driver overlay \
  my-network
```

The above command doesn't specify any custom options, so Docker assigns a
subnet and uses default options. You can see information about the network using
`docker network inspect`.

When no containers are connected to the overlay network, its configuration is
not very exciting:

```console
$ docker network inspect my-network
[
    {
        "Name": "my-network",
        "Id": "fsf1dmx3i9q75an49z36jycxd",
        "Created": "0001-01-01T00:00:00Z",
        "Scope": "swarm",
        "Driver": "overlay",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": []
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "Containers": null,
        "Options": {
            "com.docker.network.driver.overlay.vxlanid_list": "4097"
        },
        "Labels": null
    }
]
```

In the above output, notice that the driver is `overlay` and that the scope is
`swarm`, rather than `local`, `host`, or `global` scopes you might see in
other types of Docker networks. This scope indicates that only hosts which are
participating in the swarm can access this network.

The network's subnet and gateway are dynamically configured when a service
connects to the network for the first time. The following example shows
the same network as above, but with three containers of a `redis` service
connected to it.

```console
$ docker network inspect my-network
[
    {
        "Name": "my-network",
        "Id": "fsf1dmx3i9q75an49z36jycxd",
        "Created": "2017-05-31T18:35:58.877628262Z",
        "Scope": "swarm",
        "Driver": "overlay",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "10.0.0.0/24",
                    "Gateway": "10.0.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "Containers": {
            "0e08442918814c2275c31321f877a47569ba3447498db10e25d234e47773756d": {
                "Name": "my-redis.1.ka6oo5cfmxbe6mq8qat2djgyj",
                "EndpointID": "950ce63a3ace13fe7ef40724afbdb297a50642b6d47f83a5ca8636d44039e1dd",
                "MacAddress": "02:42:0a:00:00:03",
                "IPv4Address": "10.0.0.3/24",
                "IPv6Address": ""
            },
            "88d55505c2a02632c1e0e42930bcde7e2fa6e3cce074507908dc4b827016b833": {
                "Name": "my-redis.2.s7vlybipal9xlmjfqnt6qwz5e",
                "EndpointID": "dd822cb68bcd4ae172e29c321ced70b731b9994eee5a4ad1d807d9ae80ecc365",
                "MacAddress": "02:42:0a:00:00:05",
                "IPv4Address": "10.0.0.5/24",
                "IPv6Address": ""
            },
            "9ed165407384f1276e5cfb0e065e7914adbf2658794fd861cfb9b991eddca754": {
                "Name": "my-redis.3.hbz3uk3hi5gb61xhxol27hl7d",
                "EndpointID": "f62c686a34c9f4d70a47b869576c37dffe5200732e1dd6609b488581634cf5d2",
                "MacAddress": "02:42:0a:00:00:04",
                "IPv4Address": "10.0.0.4/24",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.driver.overlay.vxlanid_list": "4097"
        },
        "Labels": {},
        "Peers": [
            {
                "Name": "moby-e57c567e25e2",
                "IP": "192.168.65.2"
            }
        ]
    }
]
```

### Customize an overlay network

There may be situations where you don't want to use the default configuration
for an overlay network. For a full list of configurable options, run the
command `docker network create --help`. The following are some of the most
common options to change.

#### Configure the subnet and gateway

By default, the network's subnet and gateway are configured automatically when
the first service is connected to the network. You can configure these when
creating a network using the `--subnet` and `--gateway` flags. The following
example extends the previous one by configuring the subnet and gateway.

```console
$ docker network create \
  --driver overlay \
  --subnet 10.0.9.0/24 \
  --gateway 10.0.9.99 \
  my-network
```

##### Using custom default address pools

See [Configure Swarm overlay address pools](address-pools.md).

##### Overlay network size limitations

See [Overlay network size limitations](address-pools.md#overlay-network-size-limitations).

#### Configure encryption of application data {#encryption}

See [Application data encryption](network-context.md#encryption).

## Attach a service to an overlay network

To attach a service to an existing overlay network, pass the `--network` flag to
`docker service create`, or the `--network-add` flag to `docker service update`.

```console
$ docker service create \
  --replicas 3 \
  --name my-web \
  --network my-network \
  nginx
```

Service containers connected to an overlay network can communicate with
each other across it.

To see which networks a service is connected to, use `docker service ls` to find
the name of the service, then `docker service ps <service-name>` to list the
networks. Alternately, to see which services' containers are connected to a
network, use `docker network inspect <network-name>`. You can run these commands
from any swarm node which is joined to the swarm and is in a `running` state.

### Configure service discovery

See [Configure Swarm service discovery](service-discovery.md).

## Customize the ingress network {#customize-ingress}

See [Customize the Swarm ingress network](network-ingress.md).

## Customize the docker_gwbridge

See [Customize the docker_gwbridge network](network-gwbridge.md).

## Use a separate interface

See [Separate Swarm control and data traffic](network-interfaces.md).

## Publish ports on an overlay network

Swarm services connected to the same overlay network effectively expose all
ports to each other. For a port to be accessible outside of the service, that
port must be _published_ using the `-p` or `--publish` flag on `docker service
create` or `docker service update`. Both the legacy colon-separated syntax and
the newer comma-separated value syntax are supported. The longer syntax is
preferred because it is somewhat self-documenting.

<table>
<thead>
<tr>
<th>Flag value</th>
<th>Description</th>
</tr>
</thead>
<tr>
<td><tt>-p 8080:80</tt> or<br /><tt>-p published=8080,target=80</tt></td>
<td>Map TCP port 80 on the service to port 8080 on the routing mesh.</td>
</tr>
<tr>
<td><tt>-p 8080:80/udp</tt> or<br /><tt>-p published=8080,target=80,protocol=udp</tt></td>
<td>Map UDP port 80 on the service to port 8080 on the routing mesh.</td>
</tr>
<tr>
<td><tt>-p 8080:80/tcp -p 8080:80/udp</tt> or <br /><tt>-p published=8080,target=80,protocol=tcp -p published=8080,target=80,protocol=udp</tt></td>
<td>Map TCP port 80 on the service to TCP port 8080 on the routing mesh, and map UDP port 80 on the service to UDP port 8080 on the routing mesh.</td>
</tr>
</table>

## Learn more

* [Swarm administration guide](admin_guide.md)
* [Networking overview](/manuals/engine/network/_index.md)
* [Docker CLI reference](/reference/cli/docker/)
