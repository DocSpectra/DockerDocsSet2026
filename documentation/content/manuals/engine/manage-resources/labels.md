---
description: Learn about labels, a tool to manage metadata on Docker objects.
keywords: labels, metadata, docker, annotations
title: Docker object labels
aliases:
  - /engine/userguide/labels-custom-metadata/
  - /config/labels-custom-metadata/
---

Before adding or querying labels, read [label keys, values, and lifecycle](label-concepts.md).
For shared CLI syntax, see [filters](../cli/filter.md) and [output formatting](../cli/formatting.md).

## Label keys and values

See [Label keys and values](label-concepts.md#label-keys-and-values).

### Key format recommendations

See [Key format recommendations](label-concepts.md#key-format-recommendations).

### Value guidelines

See [Value guidelines](label-concepts.md#value-guidelines).

## Manage labels on objects

### Images

Add labels to images using the [`LABEL` instruction](/reference/dockerfile.md#label) in a Dockerfile:

```dockerfile
LABEL com.example.version="1.0"
LABEL com.example.description="Web application"
```

You can also set labels at build time with the `--label` flag, without needing
a `LABEL` instruction in the Dockerfile:

```console
$ docker build --label "com.example.version=1.0" -t myapp .
```

Inspect labels on an image using `docker inspect`:

```console
$ docker inspect --format='{{json .Config.Labels}}' myapp
```

Filter images by label with [`docker image ls --filter`](/reference/cli/docker/image/ls/#filter):

```console
$ docker image ls --filter "label=com.example.version"
```

### Containers

Override or add labels when starting a container with
[`docker run --label`](/reference/cli/docker/container/run/#label):

```console
$ docker run --label "com.example.env=prod" myapp
```

Inspect labels on a container:

```console
$ docker inspect --format='{{json .Config.Labels}}' mycontainer
```

Filter containers by label with [`docker container ls --filter`](/reference/cli/docker/container/ls/#filter):

```console
$ docker container ls --filter "label=com.example.env=prod"
```

### Local Docker daemons

Add labels to the Docker daemon by passing `--label` flags when starting
`dockerd`, or by setting `"labels"` in the
[daemon configuration file](/reference/cli/dockerd.md#daemon-configuration-file):

```json
{
  "labels": ["com.example.environment=production"]
}
```

View daemon labels with `docker system info`.

### Volumes

Add labels when [creating a volume](/reference/cli/docker/volume/create/):

```console
$ docker volume create --label "com.example.purpose=database" myvolume
```

Inspect volume labels:

```console
$ docker volume inspect myvolume --format='{{json .Labels}}'
```

Filter volumes by label with [`docker volume ls --filter`](/reference/cli/docker/volume/ls/#filter):

```console
$ docker volume ls --filter "label=com.example.purpose"
```

### Networks

Add labels when [creating a network](/reference/cli/docker/network/create/):

```console
$ docker network create --label "com.example.purpose=frontend" mynetwork
```

Inspect network labels:

```console
$ docker network inspect mynetwork --format='{{json .Labels}}'
```

Filter networks by label with [`docker network ls --filter`](/reference/cli/docker/network/ls/#filter):

```console
$ docker network ls --filter "label=com.example.purpose"
```

### Swarm nodes

- [Adding or updating a Swarm node's labels](/reference/cli/docker/node/update/#label-add)
- [Filtering Swarm nodes by label](/reference/cli/docker/node/ls/#filter)

### Swarm services

- [Adding labels when creating a Swarm service](/reference/cli/docker/service/create/#label)
- [Updating a Swarm service's labels](/reference/cli/docker/service/update/)
- [Filtering Swarm services by label](/reference/cli/docker/service/ls/#filter)
