---
title: Resolve common DHI runtime and build issues
description: Check permissions, privileged ports, missing shells, entrypoints, and package managers.
---

See [image hardening](../core-concepts/hardening.md) and the [migration checklist](../migration/checklist.md) for shared adoption context.

## Common issues

The following are specific issues you may encounter when working with Docker
Hardened Images, along with recommended solutions.

### Permissions

DHIs run as a nonroot user by default for enhanced security. This can result in
permission issues when accessing files or directories. Ensure your application
files and runtime directories are owned by the expected UID/GID or have
appropriate permissions.

To find out which user a DHI runs as, check the repository page for the image on
Docker Hub. See [View image variant
details](explore.md#image-variant-details) for more information.

### Privileged ports

Nonroot containers cannot bind to ports below 1024 by default. This is enforced
by both the container runtime and the kernel (especially in Kubernetes and
Docker Engine < 20.10).

Inside the container, configure your application to listen on an unprivileged
port (1025 or higher). For example `docker run -p 80:8080 my-image` maps
port 8080 in the container to port 80 on the host, allowing you to access it
without needing root privileges.

### No shell

Runtime DHIs omit interactive shells like `sh` or `bash`. If your build or
tooling assumes a shell is present (e.g., for `RUN` instructions), use a `dev`
variant of the image in an earlier build stage and copy the final artifact into
the runtime image.

To find out which shell, if any, a DHI has, check the repository page for the
image on Docker Hub. See [View image variant
details](explore.md#image-variant-details) for more information.

Also, use Docker Debug when you need shell access to a running container. For
more details, see [General debugging](debug.md#general-debugging).

### Entry point differences

DHIs may define different entry points compared to Docker Official Images (DOIs)
or other community images.

To find out the ENTRYPOINT or CMD for a DHI, check the repository page for the
image on Docker Hub. See [View image variant
details](explore.md#image-variant-details) for more information.

### No package manager

Runtime Docker Hardened Images are stripped down for security and minimal attack
surface. As a result, they don't include a package manager such as `apk` or
`apt`. This means you can't install additional software directly in the runtime
image.

If your build or application setup requires installing packages (for example, to
compile code, install runtime dependencies, or add diagnostic tools), use a `dev`
variant of the image in a build stage. Then, copy only the necessary artifacts
into the final runtime image.
