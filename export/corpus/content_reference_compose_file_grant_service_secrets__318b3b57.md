---
title: Grant a service access to a secret
description: Use short or long syntax to mount a service secret.
---

## Secret configuration and caveats

See [secret declarations](secrets.md), [access grants, syntax, permissions, and limitations](services.md#secrets), [build secrets](build.md#secrets), and [using secrets](/manuals/compose/how-tos/use-secrets.md).

## Mount a secret by name

The following example uses the short syntax to grant the `frontend` service
access to the `server-certificate` secret. The value of `server-certificate` is set
to the contents of the file `./server.cert`.

```yml
services:
  frontend:
    image: example/webapp
    secrets:
      - server-certificate
secrets:
  server-certificate:
    file: ./server.cert
```

## Set the target and permissions

Note that support for `uid`, `gid`, and `mode` attributes are not implemented in Docker Compose when the source of the secret is a [`file`](secrets.md). This is because bind-mounts used under the hood don't allow uid remapping.

The following example sets the name of the `server-certificate` secret file to `server.cert`
within the container, sets the mode to `0440` (group-readable), and sets the user and group
to `103`. The value of `server-certificate` is set
to the contents of the file `./server.cert`.

```yml
services:
  frontend:
    image: example/webapp
    secrets:
      - source: server-certificate
        target: server.cert
        uid: "103"
        gid: "103"
        mode: 0o440
secrets:
  server-certificate:
    file: ./server.cert
```

