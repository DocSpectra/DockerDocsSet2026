---
title: Container runtime and image store capabilities
---

## What is `containerd`?

`containerd` is a container runtime that provides a lightweight, consistent
interface for container lifecycle and image management. It is used under the
hood by Docker Engine for creating, starting, and stopping containers.

## What is the `containerd` image store?

The image store is the component responsible for pushing, pulling,
and storing images on the filesystem.

The containerd image store extends the range of image types
that the Docker Engine can natively interact with.
While this is a low-level architectural change,
it's a prerequisite for unlocking a range of new use cases, including:

- Build multi-platform images and images with attestations
- Support for using containerd snapshotters with unique characteristics,
  such as [stargz][1] for lazy-pulling images on container startup,
  or [nydus][2] and [dragonfly][3] for peer-to-peer image distribution.
- Ability to run Wasm containers

> [!IMPORTANT]
>
> Wasm workloads are deprecated and will be removed in a future Docker Desktop release. This feature is no longer actively maintained.

[1]: https://github.com/containerd/stargz-snapshotter
[2]: https://github.com/containerd/nydus-snapshotter
[3]: https://github.com/dragonflyoss/image-service

## Classic image store

The classic image store is Docker's legacy storage backend, replaced by the
containerd image store. It doesn't support image indices or manifest lists, so
you can't load multi-platform images locally or build images with attestations.

Most users have no reason to use the classic image store. It's available for
cases where you need to match older behavior or have compatibility
requirements.


## Build multi-platform images

The containerd image store lets you build multi-platform images
and load them to your local image store:

<script async id="asciicast-ZSUI4Mi2foChLjbevl2dxt5GD" src="https://asciinema.org/a/ZSUI4Mi2foChLjbevl2dxt5GD.js"></script>

Building multi-platform images with the classic image store is not supported:

```console
$ docker build --platform=linux/amd64,linux/arm64 .
[+] Building 0.0s (0/0)
ERROR: Multi-platform build is not supported for the docker driver.
Switch to a different driver, or turn on the containerd image store, and try again.
Learn more at https://docs.docker.com/go/build-multi-platform/
```

## Build images with attestations

To build images with SBOM attestations, you must use either the [containerd
image store](#what-is-the-containerd-image-store), or use a `docker-container`
builder together with the `--push` flag to push the image (with attestations)
directly to a registry. The classic image store doesn't support manifest lists
or image indices, which is required for adding attestations to an image.

