---
title: Sign application images built from DHI
description: Sign derivative images with Cosign.
---

See [why to sign your own images](../core-concepts/signatures.md#why-sign-your-own-images).

## Sign images

To sign a Docker image, use [Cosign](https://docs.sigstore.dev/). Replace
`<image-name>:<tag>` with the image name and tag.

```console
$ cosign sign <image-name>:<tag>
```

This command will prompt you to authenticate via an OIDC provider (such as
GitHub, Google, or Microsoft). Upon successful authentication, Cosign will
generate a short-lived certificate and sign the image. The signature will be
stored in a transparency log and associated with the image in the registry.
