---
title: Manage Docker Build Cloud cache
---

Before following this task, see [Docker Build Cloud setup](setup.md).

## Managing build cache

You don't need to manage Docker Build Cloud cache manually.
The system manages it for you through [garbage collection](/build/cache/garbage-collection/).

Old cache is automatically removed if you hit your storage limit.
You can check your current cache state using the
[`docker buildx du` command](/reference/cli/docker/buildx/du/).

To clear the builder's cache manually,
use the [`docker buildx prune` command](/reference/cli/docker/buildx/prune/).
This works like pruning the cache for any other builder.

> [!WARNING]
>
> Pruning a cloud builder's cache also removes the cache for other team members
> using the same builder.


