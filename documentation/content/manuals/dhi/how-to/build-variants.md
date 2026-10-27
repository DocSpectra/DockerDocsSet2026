---
title: Create DHI dev and compatibility variants
description: Task-specific definition steps and examples.
---

Before you begin, review [image definitions](../core-concepts/definitions.md), the [field reference](definition-reference.md), and the [shared build and verification procedure](build-definition.md).

## Create a dev variant

A dev variant of an image adds a shell, package manager, and development tools.
This is useful for debugging and for use as a build stage in multi-stage
workflows.

To create a dev variant, change the `variant` field and enable root access:

```yaml
# syntax=dhi.io/build:2-alpine3.23

name: Alpine 3.23 Base (dev)
image: my-registry/my-base
variant: dev
tags:
  - "1.0-dev"
platforms:
  - linux/amd64
  - linux/arm64

contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/v3.23/main
    - https://dl-cdn.alpinelinux.org/alpine/v3.23/community
  packages:
    - alpine-baselayout-data
    - apk-tools
    - busybox
    - ca-certificates-bundle

accounts:
  root: true
  run-as: root
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
  pretty-name: Docker Hardened Images/Alpine Linux v3.23
  home-url: https://docker.com/products/hardened-images/
  bug-report-url: https://docker.com/support/

environment:
  SSL_CERT_FILE: /etc/ssl/certs/ca-certificates.crt

annotations:
  org.opencontainers.image.description: A minimal Alpine base image

cmd:
  - /bin/sh
```

The key differences from a runtime variant:

- `variant: dev` instead of `variant: runtime`.
- `accounts.root: true` enables the root account.
- `run-as: root` sets root as the default user.
- `apk-tools` is added to packages, giving the image a package manager.
- The `nonroot` user is still defined so that applications can switch to an
  unprivileged user at runtime.

For Debian-based dev variants, add `apt` instead of `apk-tools` and include the
`DEBIAN_FRONTEND: noninteractive` environment variable.

## Create a compatibility variant

A compatibility variant includes common shell utilities for use with
scripts and automation tools that expect a standard Linux userland. Compatibility
images use the `flavor` field:

```yaml
variant: runtime
flavor: compat
```

A compatibility variant adds packages such as `bash`, `coreutils`, `findutils`,
`grep`, `hostname`, `openssl`, `procps`, and `sed` alongside the application
packages. A compatibility-dev variant combines both the compatibility packages
and the dev tools:

```yaml
variant: dev
flavor: compat
```

Refer to the Redis compatibility images in the catalog for a complete example of
the compatibility pattern.
