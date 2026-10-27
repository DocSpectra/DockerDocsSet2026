---
title: Select Docker Build Cloud for builds
---

Before following this task, see [Docker Build Cloud setup](setup.md).

For shared command behavior, see [Select a builder](/manuals/build/builders/selection.md).

## Use by default

If you want to use Docker Build Cloud without having to specify the `--builder` flag
each time, you can set it as the default builder.

{{< tabs group="ui" >}}
{{< tab name="CLI" >}}

Run the following command:

```console
$ docker buildx use cloud-<ORG>-<BUILDER_NAME> --global
```

{{< /tab >}}
{{< tab name="Docker Desktop" >}}

1. Open the Docker Desktop settings and navigate to the **Builders** tab.
2. Find the cloud builder under **Available builders**.
3. Open the drop-down menu and select **Use**.

   ![Selecting the cloud builder as default using the Docker Desktop GUI](/build/images/set-default-builder-gui.webp)

{{< /tab >}}
{{< /tabs >}}

Changing your default builder with `docker buildx use` only changes the default
builder for the `docker buildx build` command. The `docker build` command still
uses the `default` builder, unless you specify the `--builder` flag explicitly.

If you use build scripts, such as `make`, that use the `docker build` command,
we recommend updating your build commands to `docker buildx build`. Alternatively,
you can set the [`BUILDX_BUILDER` environment
variable](/manuals/build/building/variables.md#buildx_builder) to specify which
builder `docker build` should use.

## Unset Docker Build Cloud as the default builder

If you've set a cloud builder as the default builder
and want to revert to the default `docker` builder,
run the following command:

```console
$ docker context use default
```

This doesn't remove the builder from your system.
It only changes the builder that's automatically selected to run your builds.

