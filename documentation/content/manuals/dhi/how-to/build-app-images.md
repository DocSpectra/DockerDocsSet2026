---
title: Build application images with DHI variants
description: Use dev stages and static or minimal runtime images.
---

Before pulling images, [authenticate to dhi.io](authenticate.md). Review the [migration checklist](../migration/checklist.md).

## Use a static image for compiled executables

Docker Hardened Images include a `static` image repository designed specifically
for running compiled executables in an extremely minimal and secure runtime.
Unlike a non-hardened `FROM scratch` image, the DHI `static` image includes
attestations and essential packages like `ca-certificates`.

Use a `-dev` or other builder image to compile your binary, then copy the output
into a `static` image:

```dockerfile
FROM dhi.io/golang:1.22-dev AS build
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o myapp

FROM dhi.io/static:20230311
COPY --from=build /app/myapp /myapp
ENTRYPOINT ["/myapp"]
```

For multi-stage build patterns, see [Multi-stage builds](/manuals/build/building/multi-stage.md).

## Use dev variants for framework-based applications

If you're building applications with frameworks that require package managers or
build tools (such as Python, Node.js, or Go), use a `-dev` variant during the
development or build stage. These variants include essential utilities like
shells, compilers, and package managers to support local iteration and CI
workflows.

Use `-dev` images in your inner development loop or in isolated CI stages to
maximize productivity. Once you're ready to produce artifacts for production,
switch to a smaller runtime variant to reduce the attack surface and image size.

For the build and runtime stage procedure, see [Update Dockerfile stages for DHI](../migration/dockerfile.md).
