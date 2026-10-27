---
title: Preserve a Docker container builder cache
---

For shared options and behavior, see [docker-container driver reference](docker-container-reference.md).
For shared procedures, see [Select a builder](../selection.md) and
[Load build results](../image-loading.md).

## Cache persistence

The `docker-container` driver supports cache persistence, as it stores all the
BuildKit state and related cache into a dedicated Docker volume.

To persist the `docker-container` driver's cache, even after recreating the
driver using `docker buildx rm` and `docker buildx create`, you can destroy the
builder using the `--keep-state` flag:

For example, to create a builder named `container` and then remove it while
persisting state:

```console
# setup a builder
$ docker buildx create --name=container --driver=docker-container --use --bootstrap
container
$ docker buildx ls
NAME/NODE       DRIVER/ENDPOINT              STATUS   BUILDKIT PLATFORMS
container *     docker-container
  container0    desktop-linux                running  v0.10.5  linux/amd64
$ docker volume ls
DRIVER    VOLUME NAME
local     buildx_buildkit_container0_state

# remove the builder while persisting state
$ docker buildx rm --keep-state container
$ docker volume ls
DRIVER    VOLUME NAME
local     buildx_buildkit_container0_state

# the newly created driver with the same name will have all the state of the previous one!
$ docker buildx create --name=container --driver=docker-container --use --bootstrap
container
```


