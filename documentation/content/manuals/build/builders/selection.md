---
title: Select a builder
description: Select a builder and choose how build commands use it.
---

## Selected builder

Selected builder refers to the builder that's used by default when you run
build commands.

When you run a build, or interact with builders in some way using the CLI,
you can use the optional `--builder` flag, or the `BUILDX_BUILDER`
[environment variable](/manuals/build/building/variables.md#buildx_builder),
to specify a builder by name. If you don't specify a builder,
the selected builder is used.

Use `docker buildx ls` to see builder instances available on your system, and
the drivers they're using.
The asterisk (`*`) next to a builder name indicates the selected builder.

```console
$ docker buildx ls
NAME/NODE       DRIVER/ENDPOINT      STATUS   BUILDKIT PLATFORMS
default *       docker
  default       default              running  v0.11.6  linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/386
my_builder      docker-container
  my_builder0   default              running  v0.11.6  linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/386
```

### Select a different builder

To switch between builders, use the `docker buildx use <name>` command.

After running this command, the builder you specify is automatically
selected when you invoke builds.

### Difference between `docker build` and `docker buildx build`

Even though `docker build` is an alias for `docker buildx build`, there are
subtle differences between the two commands. With Buildx, the build client and
the daemon (BuildKit) are decoupled. This means you can use multiple
builders from a single client, even remote ones.

The `docker build` command always defaults to using the default builder that
comes bundled with the Docker Engine, to ensure backwards compatibility with
older versions of the Docker CLI. The `docker buildx build` command, on the
other hand, checks whether you've set a different builder as the default
builder before it sends your build to BuildKit.

To use the `docker build` command with a non-default builder, you must either
specify the builder explicitly:

- Using the `--builder` flag:

  ```console
  $ docker build --builder my_builder .
  ```

- Or the `BUILDX_BUILDER` environment variable:

  ```console
  $ BUILDX_BUILDER=my_builder docker build .
  ```

<!-- vale Docker.We = NO -->

In general, we recommend that you use the `docker buildx build` command when
you want to use custom builders. This ensures that your [selected
builder](#selected-builder) configuration is interpreted correctly.

<!-- vale Docker.We = YES -->
