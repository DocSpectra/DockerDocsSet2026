---
title: View and pull Docker Hardened Images by digest
description: Task steps and examples for DHI digests.
---

See [image digests context](../core-concepts/digests.md). For registry access, see [Authenticate to dhi.io](authenticate.md). For attestation verification requirements, see [Retrieve and verify attestations](verify-attestations.md).

## View an image digest

### Use the Docker CLI

To view the image digest of a Docker image, you can use the following command. Replace
`<image-name>:<tag>` with the image name and tag.

```console
$ docker buildx imagetools inspect <image-name>:<tag>
```

### Use the Docker Hub UI

1. Go to [Docker Hub](https://hub.docker.com/) and sign in.
2. Navigate to your organization's namespace and open the mirrored DHI repository.
3. Select the **Tags** tab to view image variants.
4. Each tag in the list includes a **Digest** field showing the image's SHA-256 value.

## Pull an image by digest

Pulling an image by digest ensures that you are pulling the exact image version
identified by the specified digest.

To pull a Docker image using its digest, use the following command. Replace
`<image-name>` with the image name and `<digest>` with the image digest.

```console
$ docker pull <image-name>@sha256:<digest>
```

For example, to pull a `docs/dhi-python:3.13` image using its digest of
`94a00394bc5a8ef503fb59db0a7d0ae9e1110866e8aee8ba40cd864cea69ea1a`, you would
run:

```console
$ docker pull docs/dhi-python@sha256:94a00394bc5a8ef503fb59db0a7d0ae9e1110866e8aee8ba40cd864cea69ea1a
```
