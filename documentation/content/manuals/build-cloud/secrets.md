---
title: Use secrets with Docker Build Cloud
---

Before following this task, see [Docker Build Cloud setup](setup.md).

For shared procedures and context, see [Build secrets](/manuals/build/building/secrets.md).

## Use secrets with Docker Build Cloud

To use build secrets with Docker Build Cloud,
such as authentication credentials or tokens,
use the `--secret` and `--ssh` CLI flags for the `docker buildx` command.
The traffic is encrypted and secrets are never stored in the build cache.

> [!WARNING]
>
> If you're misusing build arguments to pass credentials, authentication
> tokens, or other secrets, you should refactor your build to pass the secrets using
> [secret mounts](/reference/cli/docker/buildx/build/#secret) instead.
> Build arguments are stored in the cache and their values are exposed through attestations.
> Secret mounts don't leak outside of the build and are never included in attestations.

For more information, refer to:

- [`docker buildx build --secret`](/reference/cli/docker/buildx/build/#secret)
- [`docker buildx build --ssh`](/reference/cli/docker/buildx/build/#ssh)

