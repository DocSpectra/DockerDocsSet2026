---
title: DHI definition field reference
description: Required fields, metadata, container configuration, OCI artifact sources, ports, and annotations.
---

See [DHI image definitions](../core-concepts/definitions.md) for the declarative-build model and distribution syntax directives.

## YAML schema reference

The following sections describe the fields available in a DHI definition file.

### Required fields

Every definition must include these top-level fields:

| Field       | Description                                                         |
|-------------|---------------------------------------------------------------------|
| `name`      | Human-readable name for the image.                                  |
| `image`     | Full registry path, such as `dhi.io/my-image`.                      |
| `variant`   | Image variant type: `runtime` or `dev`.                             |
| `tags`      | List of image tags.                                                 |
| `platforms`  | Target architectures, such as `linux/amd64` and `linux/arm64`.     |
| `contents`  | Package repositories and packages to install.                       |

### Image metadata

These fields add metadata to the image:

| Field         | Description                                                       |
|---------------|-------------------------------------------------------------------|
| `os-release`  | Defines the `/etc/os-release` contents inside the image.          |
| `annotations` | OCI image annotations such as description and license.            |
| `dates`       | Release date and end-of-life date.                                |
| `vars`        | Build-time variables for templating.                              |
| `flavor`      | Image flavor modifier, such as `compat` for compatibility images.|

### Container configuration

These fields control how the container runs:

| Field         | Description                                                       |
|---------------|-------------------------------------------------------------------|
| `accounts`    | Users, groups, and the `run-as` user.                             |
| `environment` | Environment variables.                                            |
| `entrypoint`  | Container entrypoint command.                                     |
| `cmd`         | Default command arguments.                                        |
| `work-dir`    | Working directory inside the container.                           |
| `volumes`     | Volume mount points.                                              |
| `ports`       | Exposed network ports.                                            |
| `paths`       | Directories, files, and symlinks to create.                       |

### Advanced fields

These fields support more complex build patterns:

| Field                | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `contents.builds`    | Build stages with shell pipelines.                           |
| `contents.keyring`   | Signing keys for third-party package repositories.           |
| `contents.artifacts` | Pre-built OCI artifacts to include.                          |
| `contents.mappings`  | Package URL (purl) mappings for SBOM accuracy.               |
| `contents.files`     | Source files fetched from Git URLs with checksums.            |

## Use OCI artifacts as package sources

Instead of installing packages from Alpine or Debian repositories, you can pull
pre-built binaries from DHI package artifacts. This is how the catalog builds
images like Python and Node.js — the runtime is compiled separately and
published as an OCI artifact, then referenced by digest in the image definition.

Add the `artifacts` field under `contents`:

```yaml
contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/v3.23/main
    - https://dl-cdn.alpinelinux.org/alpine/v3.23/community
  packages:
    - alpine-baselayout-data
    - bzip2
    - ca-certificates-bundle
    - expat
    - gdbm
    - libffi
    - mpdecimal
    - musl
    - ncurses
    - openssl
    - readline
    - sqlite-libs
    - tzdata
    - zlib
  artifacts:
    - name: dhi.io/pkg-python:3.13.12-alpine3.23@sha256:052b3b915055006a27c42470eed5c65d7ee92d2c3de47ecaedcc6bbd36077b95
      includes:
        - opt/**
      uid: 0
      gid: 0
```

| Field      | Description                                                                  |
|------------|------------------------------------------------------------------------------|
| `name`     | Full OCI reference with digest pin. Always use `@sha256:` for reproducibility. |
| `includes` | Glob patterns for files to extract from the artifact. Paths are resolved from the filesystem root; `opt/**` includes everything under the `/opt` path. |
| `excludes` | Glob patterns for files to skip. Useful for removing headers, docs, or unused binaries. |
| `uid`, `gid` | Ownership for extracted files.                                             |

Available DHI packages are in the
[`package/`](https://github.com/docker-hardened-images/catalog/tree/main/package)
directory of the catalog repository.

## Set ports and volumes

Use the `ports` field to declare which ports the container exposes. Always use
unprivileged ports (higher than 1024) when the container runs as a non-root
user.

```yaml
ports:
  - 8080/tcp
```

Use the `volumes` field to declare volume mount points:

```yaml
volumes:
  - /data
```

## Set annotations

OCI annotations add machine-readable metadata to the image. Use the
`annotations` field:

```yaml
annotations:
  org.opencontainers.image.description: A minimal hardened application image
  org.opencontainers.image.licenses: Apache-2.0
```

These annotations appear in Docker Scout reports and container registry
interfaces.
