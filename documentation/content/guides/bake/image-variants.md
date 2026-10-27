---
title: Build release and debug image variants with Bake
---

Before following this task, see [Set up the Bake example project](project-setup.md).

For shared procedure and context, see [Matrices](/manuals/build/bake/matrices.md) and
[Expressions](/manuals/build/bake/expressions.md).

## Building variants

Sometimes you need to build more than one version of a program. The following
example uses Bake to build separate "release" and "debug" variants of the
program, using [matrices](/manuals/build/bake/matrices.md). Using matrices lets
you run parallel builds with different configurations, saving time and ensuring
consistency.

A matrix expands a single build into multiple builds, each representing a
unique combination of matrix parameters. This means you can orchestrate Bake
into building both the production and development build of your program in
parallel, with minimal configuration changes.

The example project for this guide is set up to use a build-time option to
conditionally enable debug logging and tracing capabilities.

- If you compile the program with `go build -tags="debug"`, the additional
  logging and tracing capabilities are enabled (development mode).
- If you build without the `debug` tag, the program is compiled with a default
  logger (production mode).

Update the Bake file by adding a matrix attribute which defines the variable
combinations to build:

```diff {title="docker-bake.hcl"}
 target "default" {
+  matrix = {
+    mode = ["release", "debug"]
+  }
+  name = "image-${mode}"
   target = "image"
```

The `matrix` attribute defines the variants to build ("release" and "debug").
The `name` attribute defines how the matrix gets expanded into multiple
distinct build targets. In this case, the matrix attribute expands the build
into two workflows: `image-release` and `image-debug`, each using different
configuration parameters.

Next, define a build argument named `BUILD_TAGS` which takes the value of the
matrix variable.

```diff {title="docker-bake.hcl"}
   target = "image"
+  args = {
+    BUILD_TAGS = mode
+  }
   tags = [
```

You'll also want to change how the image tags are assigned to these builds.
Currently, both matrix paths would generate the same image tag names, and
overwrite each other. Update the `tags` attribute use a conditional operator to
set the tag depending on the matrix variable value.

```diff {title="docker-bake.hcl"}
   tags = [
-    "bakeme:latest",
+    mode == "release" ? "bakeme:latest" : "bakeme:dev"
   ]
```

- If `mode` is `release`, the tag name is `bakeme:latest`
- If `mode` is `debug`, the tag name is `bakeme:dev`

For the Dockerfile changes, see [Configure build tags](build-tags.md).

That's all. With these changes, your `docker buildx bake` command now builds
two multi-platform image variants. You can introspect the canonical build
configuration that Bake generates using the `docker buildx bake --print`
command. Running this command shows that Bake will run a `default` group with
two targets with different build arguments and image tags.

```json {collapse=true}
{
  "group": {
    "default": {
      "targets": ["image-release", "image-debug"]
    }
  },
  "target": {
    "image-debug": {
      "attest": ["type=provenance,mode=max", "type=sbom"],
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "BUILD_TAGS": "debug"
      },
      "tags": ["bakeme:dev"],
      "target": "image",
      "platforms": ["linux/amd64", "linux/arm64", "linux/riscv64"]
    },
    "image-release": {
      "attest": ["type=provenance,mode=max", "type=sbom"],
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "BUILD_TAGS": "release"
      },
      "tags": ["bakeme:latest"],
      "target": "image",
      "platforms": ["linux/amd64", "linux/arm64", "linux/riscv64"]
    }
  }
}
```

Factoring in all of the platform variants as well, this means that the build
configuration generates 6 different images.

```console
$ docker buildx bake
$ docker image ls --tree

IMAGE                   ID             DISK USAGE   CONTENT SIZE   USED
bakeme:dev              f7cb5c08beac       49.3MB         28.9MB
├─ linux/riscv64        0eae8ba0367a       9.18MB         9.18MB
├─ linux/arm64          56561051c49a         30MB         9.89MB
└─ linux/amd64          e8ca65079c1f        9.8MB          9.8MB

bakeme:latest           20065d2c4d22       44.4MB         25.9MB
├─ linux/riscv64        7cc82872695f       8.21MB         8.21MB
├─ linux/arm64          e42220c2b7a3       27.1MB         8.93MB
└─ linux/amd64          af5b2dd64fde       8.78MB         8.78MB
```


