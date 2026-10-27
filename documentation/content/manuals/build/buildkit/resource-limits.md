---
title: Limit BuildKit resources
---

Before following these steps, see [Apply a BuildKit configuration](configuration.md).

## Resource limiting

### Max parallelism

You can limit the parallelism of the BuildKit solver, which is particularly useful
for low-powered machines, using a [BuildKit configuration](toml-configuration.md)
while creating a builder with the [`--buildkitd-config` flag](/reference/cli/docker/buildx/create/#buildkitd-config).

```toml
# /etc/buildkitd.toml
[worker.oci]
  max-parallelism = 4
```

Now you can [create a `docker-container` builder](/manuals/build/builders/drivers/docker-container.md)
that will use this BuildKit configuration to limit parallelism.

```console
$ docker buildx create --use \
  --name mybuilder \
  --driver docker-container \
  --buildkitd-config /etc/buildkitd.toml
```

### TCP connection limit

TCP connections are limited to 4 simultaneous connections per registry for
pulling and pushing images, plus one additional connection dedicated to metadata
requests. This connection limit prevents your build from getting stuck while
pulling images. The dedicated metadata connection helps reduce the overall build
time.

More information: [moby/buildkit#2259](https://github.com/moby/buildkit/pull/2259)

