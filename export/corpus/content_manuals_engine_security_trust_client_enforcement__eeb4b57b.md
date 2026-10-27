---
title: Require trusted image tags in the Docker client
---

See [Docker Content Trust concepts and scope](context.md), including the Docker Official Images retirement notice.

## Client enforcement with Docker Content Trust

Content trust is disabled by default in the Docker Client. To enable
it, set the `DOCKER_CONTENT_TRUST` environment variable to `1`. This prevents
users from working with tagged images unless they contain a signature.

When DCT is enabled in the Docker client, `docker` CLI commands that operate on
tagged images must either have content signatures or explicit content hashes.
The commands that operate with DCT are:

* `push`
* `build`
* `create`
* `pull`
* `run`

For example, with DCT enabled a `docker pull someimage:latest` only
succeeds if `someimage:latest` is signed. However, an operation with an explicit
content hash always succeeds as long as the hash exists:

```console
$ docker pull registry.example.com/user/image:1
Error: remote trust data does not exist for registry.example.com/user/image: registry.example.com does not have trust data for registry.example.com/user/image

$ docker pull registry.example.com/user/image@sha256:d149ab53f8718e987c3a3024bb8aa0e2caadf6c0328f1d9d850b2a2a67f2819a
sha256:ee7491c9c31db1ffb7673d91e9fac5d6354a89d0e97408567e09df069a1687c1: Pulling from user/image
ff3a5c916c92: Pull complete
a59a168caba3: Pull complete
Digest: sha256:ee7491c9c31db1ffb7673d91e9fac5d6354a89d0e97408567e09df069a1687c1
Status: Downloaded newer image for registry.example.com/user/image@sha256:ee7491c9c31db1ffb7673d91e9fac5d6354a89d0e97408567e09df069a1687c1
```
