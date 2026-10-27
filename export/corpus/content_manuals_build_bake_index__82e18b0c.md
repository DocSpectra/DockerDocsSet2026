---
title: Bake
weight: 50
keywords: build, buildx, bake, buildkit, hcl, json, compose
aliases:
  - /build/customize/bake/
---

Bake is a feature of Docker Buildx that lets you define your build configuration
using a declarative file, as opposed to specifying a complex CLI expression. It
also lets you run multiple builds concurrently with a single invocation.

A Bake file can be written in HCL or JSON format. Bake can also build directly
from a [Docker Compose file](./compose-file.md). Here's an example Bake file in
HCL format:

```hcl {title=docker-bake.hcl}
group "default" {
  targets = ["frontend", "backend"]
}

target "frontend" {
  context = "./frontend"
  dockerfile = "frontend.Dockerfile"
  args = {
    NODE_VERSION = "22"
  }
  tags = ["myapp/frontend:latest"]
}

target "backend" {
  context = "./backend"
  dockerfile = "backend.Dockerfile"
  args = {
    GO_VERSION = "{{% param "example_go_version" %}}"
  }
  tags = ["myapp/backend:latest"]
}
```

The `group` block defines a group of targets that can be built concurrently.
Each `target` block defines a build target with its own configuration, such as
the build context, Dockerfile, and tags.

To invoke a build using the above Bake file, you can run:

```console
$ docker buildx bake
```

This executes the `default` group, which builds the `frontend` and `backend`
targets concurrently.

## Find a Bake task

- [Start with a single build](introduction.md)
- [Define targets and groups](targets.md)
- [Reuse target configuration](inheritance.md)
- [Set and validate variables](variables.md)
- [Override configuration with files, CLI flags, or environment variables](overrides.md)
- [Build variants with matrices](matrices.md)
- [Evaluate expressions](expressions.md) or [define functions](funcs.md)
- [Use additional build contexts](contexts.md)
- [Build from a Compose file](compose-file.md)
- [Load a remote Bake definition](remote-definition.md)

## Follow a guide

- [Build, test, and export artifacts with Bake](/guides/bake/index.md)
- [Extend a Compose project with Bake](/guides/compose-bake/index.md)
- [Use Bake with Docker GitHub Builder](../ci/github-actions/github-builder/bake.md)

## Get started

To learn how to get started with Bake, head over to the [Bake introduction](./introduction.md).
