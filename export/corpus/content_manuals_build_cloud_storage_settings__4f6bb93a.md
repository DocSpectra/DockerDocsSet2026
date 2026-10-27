---
title: Configure Build Cloud disk allocation and cache space
---

For shared cache lifecycle context, see [Garbage collection](/manuals/build/cache/garbage-collection.md).

## Storage and cache management

### Disk allocation

The **Disk allocation** setting lets you control how much of the available
storage is dedicated to the build cache. A lower allocation increases
storage available for active builds.

To make disk allocation changes, navigate to **Builder settings** in Docker
Build Cloud and then adjust the **Disk allocation** slider to specify the
percentage of storage used for build caching.

Any changes take effect immediately.

### Build cache space

Your subscription includes the following Build cache space:

| Subscription | Build cache space |
|--------------|-------------------|
| Personal     | N/A               |
| Pro          | 50GB              |
| Team         | 100GB             |
| Business     | 200GB             |

### Multi-architecture storage allocation

Docker Build Cloud automatically provisions builders for both amd64 and arm64 architectures. Your total build cache space is split equally between these
two builders:

- Pro (50GB total): 25GB for amd64 builder + 25GB for arm64 builder
- Team (100GB total): 50GB for amd64 builder + 50GB for arm64 builder
- Business (200GB total): 100GB for amd64 builder + 100GB for arm64 builder

> [!IMPORTANT]
>
> If you only build for one architecture, be aware that your effective cache
> space is half of your subscription's total allocation.

### Get more build cache space

To get more Build cache space, [upgrade your subscription](/manuals/subscription/scale.md).

> [!TIP]
>
> If you build large images, consider allocating less storage for caching to
> leave more space for active builds.

