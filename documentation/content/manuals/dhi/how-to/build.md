---
title: Create and build a Docker Hardened Image
linktitle: Create and build an image
description: Learn how to write a DHI definition file and build your own Docker Hardened Image from the declarative YAML schema.
keywords: hardened images, DHI, build, yaml, security, sbom, provenance, declarative, catalog, definition file
weight: 26
---

See [DHI image definitions](../core-concepts/definitions.md) for the build model and catalog layout. Before building, review the [field reference](definition-reference.md) and [authentication requirements](build-definition.md).

## Try it: build a catalog image

Before writing your own definition, try building an existing catalog image
directly from GitHub:

```console
$ docker buildx build \
    https://raw.githubusercontent.com/docker-hardened-images/catalog/refs/heads/main/image/alpine-base/alpine-3.23/3.23.yaml \
    --sbom=generator=dhi.io/scout-sbom-indexer:1 \
    --provenance=1 \
    --tag my-alpine-base:3.23 \
    --load
```

This downloads the definition file directly from GitHub and builds it locally.
After the build completes, verify the image:

```console
$ docker images my-alpine-base
```

To modify an image, clone the catalog and edit the YAML files locally:

```console
$ git clone https://github.com/docker-hardened-images/catalog.git
$ cd catalog
```

## Create a minimal image

Start with the simplest possible definition: an Alpine base image with a
non-root user.

Create a directory for your project and add a file called `base.yaml`:

```yaml
# syntax=dhi.io/build:2-alpine3.23

name: My Base Image
image: my-registry/my-base
variant: runtime
tags:
  - "1.0.0"
  - "1.0"
platforms:
  - linux/amd64
  - linux/arm64

contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/v3.23/main
    - https://dl-cdn.alpinelinux.org/alpine/v3.23/community
  packages:
    - alpine-baselayout-data
    - busybox
    - ca-certificates-bundle

accounts:
  run-as: nonroot
  users:
    - name: nonroot
      uid: 65532
      gid: 65532
  groups:
    - name: nonroot
      gid: 65532
      members:
        - nonroot

os-release:
  name: Docker Hardened Images (Alpine)
  id: alpine
  version-id: "3.23"
  pretty-name: My Hardened Image
  home-url: https://docker.com/products/hardened-images/
  bug-report-url: https://docker.com/support/

environment:
  SSL_CERT_FILE: /etc/ssl/certs/ca-certificates.crt

annotations:
  org.opencontainers.image.description: A minimal Alpine base image

cmd:
  - /bin/sh
```

In this definition:

- `contents.repositories` uses full URLs to Alpine package mirrors.
- `contents.packages` lists exact Alpine package names.
- The `accounts` block creates a `nonroot` user (UID 65532) and sets it as the
  default user for the container.
- The `os-release` block defines what appears in `/etc/os-release`. Always
  include `bug-report-url` alongside `home-url`.
- The `annotations` block adds OCI metadata visible in registries and Docker
  Scout reports.

Build the image:

```console
$ docker buildx build . -f base.yaml \
    --sbom=generator=dhi.io/scout-sbom-indexer:1 \
    --provenance=1 \
    --tag my-base:latest \
    --load
```
> [!NOTE]
>
> The `tags` field in the spec file defines the image metadata (variant and
> version labels embedded in the image manifest). The `--tag` flag on the CLI
> sets the OCI image reference used to push or load the image. These serve
> different purposes - the spec file tags describe *what the image is*, while
> the CLI tag determines *where it's stored*.


For inspection, verification, and publishing, follow [Build, inspect, and publish a definition](build-definition.md).

## How DHI builds differ from Dockerfiles

[DHI image definitions](../core-concepts/definitions.md#how-dhi-builds-differ-from-dockerfiles).

## Explore the catalog for reference

[Catalog layout](../core-concepts/definitions.md#explore-the-catalog-for-reference).

## YAML schema reference

[Definition field reference](definition-reference.md).

## Use a Debian base with third-party repositories

[Build a Debian Redis image](build-debian.md).

## Create paths

[Create paths in the Redis definition](build-debian.md#create-paths).

## Add build stages

[Build Nginx with shell pipeline stages](build-nginx.md).

## Use OCI artifacts as package sources

[OCI artifact field reference](definition-reference.md#use-oci-artifacts-as-package-sources).

## Create a dev variant

[Create dev variants](build-variants.md#create-a-dev-variant).

## Create a compatibility variant

[Create compatibility variants](build-variants.md#create-a-compatibility-variant).

## Set ports and volumes

[Ports and volumes reference](definition-reference.md#set-ports-and-volumes).

## Set annotations

[Annotations reference](definition-reference.md#set-annotations).

## Build and verify

[Shared build and verification procedure](build-definition.md#build-and-verify).

## Push to a registry

[Shared publishing procedure](build-definition.md#push-to-a-registry).

## Contribute to the catalog

[Contribute a definition](contribute-definitions.md).
