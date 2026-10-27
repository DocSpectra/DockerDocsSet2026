---
title: View and verify DHI code signatures
description: Inspect signature metadata and validate signed DHI attestations.
---

Before you begin, review [code signing](../core-concepts/signatures.md), [authenticate to dhi.io](authenticate.md), and see the [shared attestation verification procedure](verify-attestations.md).

## How to view and use code signatures

### View signatures

You can verify that a Docker Hardened Image is signed and trusted using either Docker Scout or Cosign.

To lists all attestations, including signature metadata, attached to the image, use the following command:

```console
$ docker scout attest list <image-name>:<tag>
```

> [!NOTE]
>
> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use
> `registry://dhi.io/python` instead of `dhi.io/python`.

To verify a specific signed attestation (e.g., SBOM, VEX, provenance):

```console
$ docker scout attest get \
  --predicate-type <predicate-uri> \
  --verify \
  <image-name>:<tag>
```

> [!NOTE]
>
> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use
> `registry://dhi.io/python:3.13` instead of `dhi.io/python:3.13`.

For example:

```console
$ docker scout attest get \
  --predicate-type https://openvex.dev/ns/v0.2.0 \
  --verify \
  dhi.io/python:3.13
```

If valid, Docker Scout will confirm the signature and display signature payload, as well as the equivalent Cosign command to verify the image.
