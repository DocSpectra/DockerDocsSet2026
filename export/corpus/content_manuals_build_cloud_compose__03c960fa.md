---
title: Build Compose services with Docker Build Cloud
---

Before following this task, see [Docker Build Cloud setup](setup.md).

## Use with Docker Compose

To build with Docker Build Cloud using `docker compose build`, first set the
cloud builder as your selected builder, then run your build.

> [!NOTE]
>
> Make sure you're using a supported version of Docker Compose, see
> [Prerequisites](setup.md#prerequisites).

```console
$ docker buildx use cloud-<ORG>-<BUILDER_NAME>
$ docker compose build
```

In addition to `docker buildx use`, you can also use the `docker compose build
--builder` flag or the [`BUILDX_BUILDER` environment
variable](/manuals/build/building/variables.md#buildx_builder) to select the cloud builder.


