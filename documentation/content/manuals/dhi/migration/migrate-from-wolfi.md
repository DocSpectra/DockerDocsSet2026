---
title: Migrate from Wolfi
description: Step-by-step guide to migrate from Wolfi distribution images to Docker Hardened Images
weight: 30
keywords: wolfi, chainguard, migration, dhi
---

This guide helps you migrate from Wolfi-based images to Docker Hardened
Images (DHI). Generally, the migration process is straightforward since Wolfi is
Alpine-like and DHI provides an Alpine-based hardened image.

Like other hardened images, DHI provides comprehensive
[attestations](/dhi/core-concepts/attestations/) including SBOMs and provenance,
allowing you to [verify](/manuals/dhi/how-to/verify.md) image signatures and
[scan](/manuals/dhi/how-to/scan.md) for vulnerabilities to ensure the security
and integrity of your images.

## Before you begin

Review the [migration checklist](checklist.md) and [Dockerfile migration procedure](dockerfile.md). [Authenticate to dhi.io](../how-to/authenticate.md) before pulling images.

## Migration steps

The following example demonstrates how to migrate a Dockerfile from a
Wolfi-based image to an Alpine-based Docker Hardened Image.

### Step 1: Update the base image in your Dockerfile

Follow [Update the base image in your Dockerfile](dockerfile.md#update-the-base-image-in-your-dockerfile).

The following example diff snippet from a Dockerfile shows the old base image
replaced by the new hardened image.

```diff
- ## Original base image
- FROM cgr.dev/chainguard/go:latest-dev

+ ## Updated to use hardened base image
+ FROM dhi.io/golang:1.25-alpine3.22-dev
```

For version tags, see [Select a version and distribution tag](dockerfile.md#select-a-version-and-distribution-tag).

### Step 2: Update the runtime image in your Dockerfile

Follow [Update the runtime image in your Dockerfile](dockerfile.md#update-the-runtime-image-in-your-dockerfile).

The following example shows a multi-stage Dockerfile with a build stage and runtime stage:

```dockerfile
# Build stage
FROM dhi.io/golang:1.25-alpine3.22-dev AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

# Runtime stage
FROM dhi.io/golang:1.25-alpine3.22
WORKDIR /app
COPY --from=builder /app/myapp .
ENTRYPOINT ["/app/myapp"]
```

For build and test guidance, see the [Dockerfile migration procedure](dockerfile.md).

## Language-specific examples

See the [migration examples index](examples/_index.md).
