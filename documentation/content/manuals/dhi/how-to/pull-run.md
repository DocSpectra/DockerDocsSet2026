---
title: Pull, run, and reference Docker Hardened Images
description: Image references and standard Docker commands for DHI.
---

You can use a Docker Hardened Image (DHI) just like any other image on Docker
Hub. DHIs follow the same familiar usage patterns. Pull them with `docker pull`,
reference them in your Dockerfile, and run containers with `docker run`.

The key difference is that DHIs are security-focused and intentionally minimal
to reduce the attack surface. This means some variants don't include a shell or
package manager, and may run as a non-root user by default.

> [!IMPORTANT]
>
> Before pulling images, follow [Authenticate to dhi.io](authenticate.md).

## Considerations when adopting DHIs

Docker Hardened Images are intentionally minimal to improve security. If you're
updating existing Dockerfiles or frameworks to use DHIs, keep in mind that
runtime images don't include shells or package managers, run as non-root users
by default, and may have different configurations than images you're familiar
with.

For a comprehensive checklist of migration considerations and detailed guidance,
see [Migrate to Docker Hardened Images](../migration/checklist.md).

## Pull, run, and reference DHIs

Docker Hardened Images use different image references depending on your
subscription:

| Subscription        | Image reference            | Authentication        |
|---------------------|----------------------------|-----------------------|
| Community           | `dhi.io/<image>:<tag>`     | `docker login dhi.io` |
| Select & Enterprise | `<your-org>/<image>:<tag>` | `docker login`        |

Select and Enterprise users should [mirror](mirror-hub.md) repositories to their
Docker Hub organization to access compliance variants and customization
features.

After authenticating, use the image reference in standard Docker commands and
Dockerfiles. For example:

```console
$ docker pull dhi.io/python:3.13
$ docker run --rm dhi.io/python:3.13 python -c "print('Hello from DHI')"
```

```dockerfile
FROM dhi.io/python:3.13
COPY . /app
CMD ["python", "/app/main.py"]
```

For multi-stage builds:

- Use a `-dev` tag for build stages that need a shell or package manager. See
  [Use dev variants for framework-based
  applications](build-app-images.md#use-dev-variants-for-framework-based-applications).
- Use the `static` image for compiled executables with minimal runtime
  dependencies. See [Use a static image for compiled
  executables](build-app-images.md#use-a-static-image-for-compiled-executables).

To learn how to search for available variants, see [Search and evaluate
images](./explore.md).
