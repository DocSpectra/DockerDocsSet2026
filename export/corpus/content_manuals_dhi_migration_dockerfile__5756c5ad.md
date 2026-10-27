---
title: Update Dockerfile build and runtime stages for DHI
description: Shared Dockerfile migration steps and build-stage considerations.
---

## Before you begin

See [Authenticate to dhi.io](../how-to/authenticate.md), [image differences](image-differences.md), and the [migration checklist](checklist.md).

## Update the base image in your Dockerfile

Update the base image in your application's Dockerfile to a hardened image. This
is typically going to be an image tagged as `dev` or `sdk` because it has the tools
needed to install packages and dependencies.

## Select a version and distribution tag

Note that DHI does not have a `latest` tag in order to promote best practices
around image versioning. Ensure that you specify the appropriate version tag for
your image. To find the right tag, explore the available tags in the [DHI
Catalog](https://hub.docker.com/hardened-images/catalog/). In addition, the
distribution base is specified in the tag (for example, `-alpine3.22` or
`-debian12`), so be sure to select the correct variant for your application.

## Update the runtime image in your Dockerfile

> [!NOTE]
>
> Multi-stage builds are recommended to keep your final image minimal and
> secure. Single-stage builds are supported, but they include the full `dev` image
> and therefore result in a larger image with a broader attack surface.

To ensure that your final image is as minimal as possible, you should use a
[multi-stage build](/manuals/build/building/multi-stage.md). All stages in your
Dockerfile should use a hardened image. While intermediary stages will typically
use images tagged as `dev` or `sdk`, your final runtime stage should use a runtime image.

Use the build stage to compile your application, install dependencies, and
prepare your application, then copy the resulting artifacts to the final runtime
stage. This ensures that your final image is minimal and secure.

After updating your Dockerfile, build and test your application. If you encounter
issues, see the [Troubleshoot](/manuals/dhi/troubleshoot.md) guide for common
problems and solutions.
