---
title: Switch Docker Desktop image stores
linkTitle: containerd image store
weight: 80
description: Learn about the containerd image store in Docker Desktop and how it extends image management capabilities.
keywords: Docker, containerd, engine, image store, lazy-pull
toc_max: 3
aliases:
  - /desktop/containerd/
---

Docker Desktop uses containerd as its image store by default. The image store
is the component responsible for pushing, pulling, and storing images on your
filesystem. The containerd image store supports features like multi-platform
images, image attestations, and alternative snapshotters.

## What is `containerd`?

See [Container runtime and image store capabilities](/manuals/engine/storage/image-store-capabilities.md#what-is-containerd).

## What is the `containerd` image store?

See [Image store capabilities](/manuals/engine/storage/image-store-capabilities.md#what-is-the-containerd-image-store).

## Classic image store

See [Classic image store capabilities](/manuals/engine/storage/image-store-capabilities.md#classic-image-store).

## Switch image stores

The containerd image store is enabled by default in Docker Desktop version 4.34
and later. To switch between image stores:

1. Navigate to **Settings** in Docker Desktop.
2. In the **General** tab, check or clear the **Use containerd for pulling and storing images** option.
3. Select **Apply**.

> [!NOTE]
>
> Docker Desktop maintains separate image stores for the classic and containerd image stores.
> When switching between them, images and containers from the inactive store remain on disk but are hidden until you switch back.

## Build multi-platform images

See [Build multi-platform images](/manuals/engine/storage/image-store-capabilities.md#build-multi-platform-images).
