---
title: Migrate from Ubuntu
description: Step-by-step guide to migrate from Ubuntu-based images to Docker Hardened Images
weight: 25
keywords: ubuntu, migration, dhi, debian, docker hardened images
---

Docker Hardened Images (DHI) come in [Alpine-based and Debian-based
variants](../explore/available.md). When migrating from an Ubuntu-based image,
you should migrate to the Debian-based DHI variant, as both Ubuntu and Debian
share the same package management system (APT) and underlying architecture,
making migration straightforward.

This guide helps you migrate from an existing Ubuntu-based image to DHI.

## Before you begin

Review the [image differences](image-differences.md), [migration checklist](checklist.md), and [Dockerfile migration procedure](dockerfile.md). [Authenticate to dhi.io](../how-to/authenticate.md) before pulling images.

## Migration steps

### Step 1: Update the base image in your Dockerfile

Follow [Update the base image in your Dockerfile](dockerfile.md#update-the-base-image-in-your-dockerfile).

The following example diff snippet from a Dockerfile shows the old Ubuntu-based image
replaced by the new DHI Debian image.

```diff
- ## Original Ubuntu-based image
- FROM ubuntu/go:1.22-24.04

+ ## Updated to use hardened Debian-based image
+ FROM dhi.io/golang:1-debian13-dev
```

To find the right tag, explore the available tags in the [DHI
Catalog](https://hub.docker.com/hardened-images/catalog/).

### Step 2: Update package installation commands

Since Ubuntu and Debian both use APT for package management, most package
installation commands remain similar. However, you need to ensure that package
installations only occur in `dev` or `sdk` images, as runtime images don't
contain package managers.

```diff
- ## Ubuntu: Installing packages
- FROM ubuntu/go:1.22-24.04
- RUN apt-get update && apt-get install -y \
-     git \
-     && rm -rf /var/lib/apt/lists/*

+ ## DHI: Use a language-specific dev image with package manager
+ FROM dhi.io/golang:1-debian13-dev
+ RUN apt-get update && apt-get install -y \
+     git \
+     && rm -rf /var/lib/apt/lists/*
```

Most Ubuntu packages are available in Debian with the same names. If you
encounter missing packages, you can search for equivalent packages using the
[Debian package search](https://packages.debian.org/) website.

### Step 3: Update the runtime image in your Dockerfile

Follow [Update the runtime image in your Dockerfile](dockerfile.md#update-the-runtime-image-in-your-dockerfile).

The following example shows a multi-stage Dockerfile migrating from Ubuntu to DHI Debian:

```dockerfile
# Build stage
FROM dhi.io/golang:1-debian13-dev AS builder
WORKDIR /app

# Install system dependencies (only available in dev images)
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags="-s -w" -o main .

# Runtime stage
FROM dhi.io/golang:1-debian13
WORKDIR /app

# Copy compiled binary from builder
COPY --from=builder /app/main /app/main

# Run the application
ENTRYPOINT ["/app/main"]
```

## Language-specific examples

See the [migration examples index](examples/_index.md).
