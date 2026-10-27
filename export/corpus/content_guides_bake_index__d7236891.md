---
title: Mastering multi-platform builds, testing, and more with Docker Buildx Bake
linkTitle: Mastering Docker Buildx Bake
description: >
  Learn how to manage simple and complex build configurations with Buildx Bake.
summary: >
  Learn to automate Docker builds and testing with declarative configurations using Buildx Bake.
tags: [devops]
languages: [go]
params:
  time: 30 minutes
  image: /images/guides/bake.webp
---

This guide demonstrates how to simplify and automate the process of building
images, testing, and generating build artifacts using Docker Buildx Bake. By
defining build configurations in a declarative `docker-bake.hcl` file, you can
eliminate manual scripts and enable efficient workflows for complex builds,
testing, and artifact generation.

## Tasks

- [Set up the example project](project-setup.md)
- [Test and lint the project](test-and-lint.md)
- [Build release and debug image variants](image-variants.md)
- [Export local and cross-platform binaries](export-binaries.md)

## Assumptions

See [Assumptions](project-setup.md#assumptions).

## Prerequisites

See [Prerequisites](project-setup.md#prerequisites).

## Introduction

See [Introduction](project-setup.md#introduction).

## Testing and linting

See [Testing and linting](test-and-lint.md).

## Building variants

See [Building variants](image-variants.md).

## Exporting build artifacts

See [Exporting build artifacts](export-binaries.md).

## Conclusion

Docker Buildx Bake streamlines complex build workflows, enabling efficient
multi-platform builds, testing, and artifact export. By integrating Buildx Bake
into your projects, you can simplify your Docker builds, make your build
configuration portable, and wrangle complex configurations more easily.

Experiment with different configurations and extend your Bake files to suit
your project's needs. You might consider integrating Bake into your CI/CD
pipelines to automate builds, testing, and artifact deployment. The flexibility
and power of Buildx Bake can significantly improve your development and
deployment processes.

### Further reading

For more information about how to use Bake, check out these resources:

- [Bake documentation](/manuals/build/bake/_index.md)
- [Matrix targets](/manuals/build/bake/matrices.md)
- [Bake file reference](/manuals/build/bake/reference.md)
- [Bake GitHub Action](https://github.com/docker/bake-action)
