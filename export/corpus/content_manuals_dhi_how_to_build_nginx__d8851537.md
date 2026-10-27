---
title: Build an Nginx definition with shell pipeline stages
description: Task-specific definition steps and examples.
---

Before you begin, review [image definitions](../core-concepts/definitions.md), the [field reference](definition-reference.md), and the [shared build and verification procedure](build-definition.md).

## Add build stages

For images that need to run shell commands during the build, such as
configuring files, creating symlinks, or adjusting permissions, use the
`contents.builds` field. Each build stage has its own packages, a pipeline
of named steps, and output mappings.

The following example configures Nginx during the build to run on an
unprivileged port and disable server tokens:

```yaml
# syntax=dhi.io/build:2-alpine3.23

name: Nginx mainline
image: my-registry/my-nginx
variant: runtime
tags:
  - "1.29"
platforms:
  - linux/amd64
  - linux/arm64

contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/v3.23/main
    - https://dl-cdn.alpinelinux.org/alpine/v3.23/community
    - http://nginx.org/packages/mainline/alpine/v3.23/main
  keyring:
    - https://nginx.org/keys/nginx_signing.rsa.pub
  packages:
    - alpine-baselayout-data
    - busybox
    - musl-utils
    - nginx=1.29.5-r1
  builds:
    - name: nginx
      contents:
        repositories:
          - https://dl-cdn.alpinelinux.org/alpine/v3.23/main
          - https://dl-cdn.alpinelinux.org/alpine/v3.23/community
          - http://nginx.org/packages/mainline/alpine/v3.23/main
        keyring:
          - https://nginx.org/keys/nginx_signing.rsa.pub
        packages:
          - alpine-baselayout-data
          - bash
          - musl-utils
          - nginx=1.29.5-r1
      pipeline:
        - name: install
          runs: |
            set -eux -o pipefail

            ln -sf /dev/stdout /var/log/nginx/access.log
            ln -sf /dev/stderr /var/log/nginx/error.log

            sed -i "s,listen       80;,listen       8080;," /etc/nginx/conf.d/default.conf
            sed -i "/user  nginx;/d" /etc/nginx/nginx.conf
            sed -i "s,pid        /run/nginx.pid;,pid        /var/run/nginx.pid;," /etc/nginx/nginx.conf
            sed -i '/^http {$/a\    server_tokens off;' /etc/nginx/nginx.conf

            chown -R 65532:65532 /var/cache/nginx
            chmod -R g+w /var/cache/nginx
            chown -R 65532:65532 /etc/nginx
            chmod -R g+w /etc/nginx
            chown -R 65532:65532 /run
            chown -R 65532:65532 /run/lock
            chown -R 65532:65532 /var/run
            chown -R 65532:65532 /var/log/nginx
      outputs:
        - source: /
          target: /
          uid: 0
          gid: 0
          diff: true

accounts:
  run-as: nginx
  users:
    - name: nginx
      uid: 65532
      gid: 65532
  groups:
    - name: nginx
      gid: 65532
      members:
        - nginx
    - name: www-data
      gid: 82

os-release:
  name: Docker Hardened Images (Alpine)
  id: alpine
  version-id: "3.23"
  pretty-name: Docker Hardened Images/Alpine Linux v3.23
  home-url: https://docker.com/products/hardened-images/
  bug-report-url: https://docker.com/support/

environment:
  NGINX_VERSION: 1.29.5-r1

annotations:
  org.opencontainers.image.description: A minimal Nginx image
  org.opencontainers.image.licenses: BSD-2-Clause

entrypoint:
  - nginx

cmd:
  - -g
  - daemon off;

ports:
  - 8080/tcp
```

Key patterns in this definition:

| Element     | Description                                                                |
|-------------|----------------------------------------------------------------------------|
| `contents`  | Each build stage has its own `contents` section. Include packages needed only during the build, such as `bash`. |
| `pipeline`  | Contains named steps that run shell commands. Always start scripts with `set -eux -o pipefail`. |
| `outputs`   | Copies results from the build stage into the final image. Setting `diff: true` copies only files that changed, keeping the image minimal. |
| `accounts`  | Nginx uses a dedicated `nginx` user (UID 65532) instead of `nonroot`. The `www-data` group (GID 82) is also created for web server compatibility. |
| `musl-utils` | Required in both the main and build packages for Alpine-based Nginx images. |
