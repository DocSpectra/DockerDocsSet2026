---
title: Prepare DHI file permissions for OpenShift
description: Use dev build stages and root-group ownership for runtime files.
---

Before you begin, review [OpenShift security constraints](../core-concepts/openshift.md) and [DHI registry authentication](authenticate.md).

## Build OpenShift-compatible images from DHI

DHI runtime images are distroless — they contain no shell, no package manager,
and no `RUN`-capable environment. This means you **cannot use `RUN` commands in
the runtime stage** of your Dockerfile. All file permission adjustments for
OpenShift must happen in the `-dev` build stage, and the results must be copied
into the runtime stage using `COPY --chown`.

The core pattern for OpenShift compatibility:

1. Use a DHI `-dev` variant as the build stage (it has a shell).
1. Build your application and set GID 0 ownership in the build stage.
1. Copy the results into the DHI runtime image using `COPY --chown=<UID>:0`.

> [!IMPORTANT]
> 
> Always use `--chown=<UID>:0` (user:root-group) when copying files into the
> runtime stage. This ensures the arbitrary UID that OpenShift assigns can
> access the files through root group membership. Never use `RUN` in the runtime
> stage — distroless DHI images have no shell.

> [!NOTE]
> 
> The UID for DHI images varies by image. Most use 65532 (`nonroot`), but some
> (like the Node.js image) may use a different UID. Verify with:
> `docker inspect dhi.io/<image>:<tag> --format '{{.Config.User}}'`
