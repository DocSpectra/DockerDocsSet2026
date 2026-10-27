---
title: Set up the Bake example project
---

## Assumptions

This guide assumes that you're familiar with:

- Docker
- [Buildx](/manuals/build/concepts/overview.md#buildx)
- [BuildKit](/manuals/build/concepts/overview.md#buildkit)
- [Multi-stage builds](/manuals/build/building/multi-stage.md)
- [Multi-platform builds](/manuals/build/building/multi-platform.md)

## Prerequisites

- You have a recent version of Docker installed on your machine.
- You have Git installed for cloning repositories.
- You're using the [containerd](/manuals/desktop/features/containerd.md) image store.

## Introduction

This guide uses an example project to demonstrate how Docker Buildx Bake can
streamline your build and test workflows. The repository includes both a
Dockerfile and a `docker-bake.hcl` file, giving you a ready-to-use setup to try
out Bake commands.

Start by cloning the example repository:

```bash
git clone https://github.com/dvdksn/bakeme.git
cd bakeme
```

The Bake file, `docker-bake.hcl`, defines the build targets in a declarative
syntax, using targets and groups, allowing you to manage complex builds
efficiently.

Here's what the Bake file looks like out-of-the-box:

```hcl
target "default" {
  target = "image"
  tags = [
    "bakeme:latest",
  ]
  attest = [
    "type=provenance,mode=max",
    "type=sbom",
  ]
  platforms = [
    "linux/amd64",
    "linux/arm64",
    "linux/riscv64",
  ]
}
```

The `target` keyword defines a build target for Bake. The `default` target
defines the target to build when no specific target is specified on the command
line. Here's a quick summary of the options for the `default` target:

- `target`: The target build stage in the Dockerfile.
- `tags`: Tags to assign to the image.
- `attest`: [Attestations](/manuals/build/metadata/attestations/_index.md) to attach to the image.

  > [!TIP]
  > The attestations provide metadata such as build provenance, which tracks
  > the source of the image's build, and an SBOM (Software Bill of Materials),
  > useful for security audits and compliance.

- `platforms`: Platform variants to build.

To execute this build, simply run the following command in the root of the
repository:

```console
$ docker buildx bake
```

With Bake, you avoid long, hard-to-remember command-line incantations,
simplifying build configuration management by replacing manual, error-prone
scripts with a structured configuration file.

For contrast, here's what this build command would look like without Bake:

```console
$ docker buildx build \
  --target=image \
  --tag=bakeme:latest \
  --provenance=true \
  --sbom=true \
  --platform=linux/amd64,linux/arm64,linux/riscv64 \
  .
```


