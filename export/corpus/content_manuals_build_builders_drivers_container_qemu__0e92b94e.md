---
title: Build non-native platforms with a container builder
---

For shared procedures, see [Select a builder](../selection.md) and
[Load build results](../image-loading.md).

## QEMU

The `docker-container` driver supports using [QEMU](https://www.qemu.org/)
(user mode) to build non-native platforms. Use the `--platform` flag to specify
which architectures that you want to build for.

For example, to build a Linux image for `amd64` and `arm64`:

```console
$ docker buildx build \
  --builder=container \
  --platform=linux/amd64,linux/arm64 \
  -t <registry>/<image> \
  --push .
```

> [!NOTE]
>
> Emulation with QEMU can be much slower than native builds, especially for
> compute-heavy tasks like compilation and compression or decompression.

