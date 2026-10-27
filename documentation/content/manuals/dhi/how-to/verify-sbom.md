---
title: View and verify a DHI SBOM
description: Task steps and examples for DHI sbom.
---

See [SBOM context](../core-concepts/sbom.md). For registry access, see [Authenticate to dhi.io](authenticate.md). For attestation verification requirements, see [Retrieve and verify attestations](verify-attestations.md).

## View SBOMs in Docker Hardened Images

To view the SBOM of a Docker Hardened Image, you can use the `docker scout sbom`
command. Replace `<image-name>:<tag>` with the image name and tag.

```console
$ docker scout sbom dhi.io/<image-name>:<tag>
```

## Verify the SBOM of a Docker Hardened Image

Since Docker Hardened Images come with signed SBOMs, you can use Docker Scout to
verify the authenticity and integrity of the SBOM attached to the image. This
ensures that the SBOM has not been tampered with and that the image's contents
are trustworthy.

To verify the SBOM of a Docker Hardened Image using Docker Scout, use the following command:

```console
$ docker scout attest get dhi.io/<image-name>:<tag> \
   --predicate-type https://scout.docker.com/sbom/v0.1 --verify --platform <platform>
```

For example, to verify the SBOM attestation for the `node:20.19-debian12` image:

```console
$ docker scout attest get dhi.io/node:20.19-debian12 \
   --predicate-type https://scout.docker.com/sbom/v0.1 --verify --platform linux/amd64
```

## Resources

For more details about SBOM attestations and Docker Build, see [SBOM
attestations](/build/metadata/attestations/sbom/).

To learn more about Docker Scout and working with SBOMs, see [Docker Scout SBOMs](../../scout/how-tos/view-create-sboms.md).
