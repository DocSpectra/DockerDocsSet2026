---
title: Migrate from Alpine or Debian
description: Step-by-step guide to migrate from Docker Official Images to Docker Hardened Images
weight: 20
keywords: docker official images, doi, migration, dhi, alpine, debian
---

Docker Hardened Images (DHI) come in both [Alpine-based and Debian-based
variants](../explore/available.md). In many cases, migrating from another image
based on these distributions is as simple as changing the base image in your
Dockerfile.

This guide helps you migrate from an existing Alpine-based or Debian-based
Docker Official Image (DOI) to DHI.

If you're currently using a Debian-based Docker Official Image, migrate to the
Debian-based DHI variant. If you're using an Alpine-based image, migrate to the
Alpine-based DHI variant. This minimizes changes to package management and
dependencies during migration.

## Before you begin

Review the [image differences](image-differences.md), [migration checklist](checklist.md), and [Dockerfile migration procedure](dockerfile.md). [Authenticate to dhi.io](../how-to/authenticate.md) before pulling images.

## Migration steps

### Step 1: Update the base image in your Dockerfile

Follow [Update the base image in your Dockerfile](dockerfile.md#update-the-base-image-in-your-dockerfile).

The following example diff snippet from a Dockerfile shows the old base image
replaced by the new hardened image.

```diff
- ## Original base image
- FROM golang:1.25

+ ## Updated to use hardened base image
+ FROM dhi.io/golang:1.25-debian12-dev
```

For version and distribution tags, see [Select a version and distribution tag](dockerfile.md#select-a-version-and-distribution-tag).

### Step 2: Update the runtime image in your Dockerfile

Follow [Update the runtime image in your Dockerfile](dockerfile.md#update-the-runtime-image-in-your-dockerfile).

The following example shows a multi-stage Dockerfile with a build stage and runtime stage:

```dockerfile
# Build stage
FROM dhi.io/golang:1.25-debian12-dev AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

# Runtime stage
FROM dhi.io/golang:1.25-debian12
WORKDIR /app
COPY --from=builder /app/myapp .
ENTRYPOINT ["/app/myapp"]
```

For build and test guidance, see the [Dockerfile migration procedure](dockerfile.md).

## Language-specific examples

See the [migration examples index](examples/_index.md).
