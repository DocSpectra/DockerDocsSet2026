---
title: Build a Debian Redis definition with third-party repositories
description: Task-specific definition steps and examples.
---

Before you begin, review [image definitions](../core-concepts/definitions.md), the [field reference](definition-reference.md), and the [shared build and verification procedure](build-definition.md).

## Use a Debian base with third-party repositories

For applications that require Debian packages or third-party APT repositories,
use the Debian syntax directive. The following example builds a Redis image
from the official Redis APT repository.

Create a file called `redis.yaml`:

```yaml
# syntax=dhi.io/build:2-debian13

name: Redis 8.0.x
image: my-registry/my-redis
variant: runtime
tags:
  - "8.0"
  - "8.0.5"
platforms:
  - linux/amd64
  - linux/arm64

contents:
  repositories:
    - deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb trixie main
  keyring:
    - https://packages.redis.io/gpg
  packages:
    - '!libelogind0'
    - '!mawk'
    - '!original-awk'
    - base-files
    - libpcre2-8-0
    - libssl3t64
    - libstdc++6
    - libsystemd0
    - redis=6:8.0.5-1rl1~trixie1
    - redis-server=6:8.0.5-1rl1~trixie1
    - redis-tools=6:8.0.5-1rl1~trixie1
    - tini
  mappings:
    redis: pkg:deb/redis/redis@6:8.0.5-1rl1~trixie1?os_name=debian&os_version=13
    redis-server: pkg:deb/redis/redis-server@6:8.0.5-1rl1~trixie1?os_name=debian&os_version=13
    redis-tools: pkg:deb/redis/redis-tools@6:8.0.5-1rl1~trixie1?os_name=debian&os_version=13

accounts:
  run-as: nonroot
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
  name: Docker Hardened Images (Debian)
  id: debian
  version-id: "13"
  version-codename: trixie
  pretty-name: Docker Hardened Images/Debian GNU/Linux 13 (trixie)
  home-url: https://docker.com/products/hardened-images/
  bug-report-url: https://docker.com/support/

work-dir: /data

environment:
  REDIS_VERSION: 8.0.5

annotations:
  org.opencontainers.image.description: A minimal Redis image
  org.opencontainers.image.licenses: AGPL-3.0-only

entrypoint:
  - /usr/bin/tini
  - --

cmd:
  - redis-server
  - /etc/redis/redis.conf
  - --include
  - /etc/redis/conf.d/*.conf
```

This example introduces several patterns:

- **Third-party repositories**: The `repositories` field uses the Debian
  `deb [signed-by=...] URL suite component` format for APT sources.
- **Keyring**: The `keyring` field downloads the GPG key used to verify packages
  from the third-party repository.
- **Package exclusions**: Prefix a package name with `!` to explicitly exclude
  it. This prevents unwanted dependencies from being installed. In this case,
  `!libelogind0`, `!mawk`, and `!original-awk` are excluded.
- **Debian version pinning**: Use the full epoch format,
  `redis-server=6:8.0.5-1rl1~trixie1`, to pin exact package versions.
- **SBOM mappings**: The `mappings` field provides Package URL (purl) metadata
  so that Docker Scout can accurately identify the software in the SBOM.
- **Init process**: The `entrypoint` uses `tini` as a lightweight init process
  (PID 1) to handle signal forwarding and zombie process reaping.
- **Config includes**: The `cmd` uses `--include /etc/redis/conf.d/*.conf` so
  that configuration files created in the `paths` section are loaded at startup.

## Create paths

Use the `paths` field to create directories, files with inline content, and
symlinks inside the image. The following example extends the Redis definition
with the paths required for operation:

```yaml
paths:
  - type: directory
    path: /var/lib/redis
    uid: 65532
    gid: 65532
    mode: "0755"
  - type: directory
    path: /var/log/redis
    uid: 65532
    gid: 65532
    mode: "0755"
  - type: directory
    path: /run/redis/
    uid: 65532
    gid: 65532
    mode: "0755"
  - type: directory
    path: /data
    uid: 65532
    gid: 65532
    mode: "0755"
  - type: file
    path: /etc/redis/conf.d/docker.conf
    content: |
      daemonize no
      bind 0.0.0.0 -::1
      logfile ""
    uid: 0
    gid: 0
    mode: "0555"
  - type: symlink
    path: /usr/bin/redis-sentinel
    uid: 0
    gid: 0
    source: /usr/bin/redis-check-rdb
```

Three path types are available:

| Type        | Required fields                  | Description                          |
|-------------|----------------------------------|--------------------------------------|
| `directory` | `path`, `uid`, `gid`, `mode`     | Creates an empty directory.          |
| `file`      | `path`, `content`, `uid`, `gid`, `mode` | Creates a file with inline content. |
| `symlink`   | `path`, `source`, `uid`, `gid`   | Creates a symbolic link.             |

The `mode` field uses a string representation of the octal permission bits,
such as `"0755"` for read-write-execute by owner or `"0555"` for read-execute
by all. Note that the `file` type supports inline `content` using a YAML
multi-line string.
