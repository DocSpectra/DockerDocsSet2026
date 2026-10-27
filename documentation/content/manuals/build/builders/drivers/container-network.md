---
title: Use a custom network for a container builder
---

For shared options and behavior, see [docker-container driver reference](docker-container-reference.md).
For shared procedures, see [Select a builder](../selection.md) and
[Load build results](../image-loading.md).

## Custom network

You can customize the network that the builder container uses. This is useful
if you need to use a specific network for your builds.

For example, let's [create a network](/reference/cli/docker/network/create/)
named `foonet`:

```console
$ docker network create foonet
```

Now create a [`docker-container` builder](/reference/cli/docker/buildx/create/)
that will use this network:

```console
$ docker buildx create --use \
  --name mybuilder \
  --driver docker-container \
  --driver-opt "network=foonet"
```

Boot and [inspect `mybuilder`](/reference/cli/docker/buildx/inspect/):

```console
$ docker buildx inspect --bootstrap
```

[Inspect the builder container](/reference/cli/docker/inspect/)
and see what network is being used:

```console
$ docker inspect buildx_buildkit_mybuilder0 --format={{.NetworkSettings.Networks}}
map[foonet:0xc00018c0c0]
```


