---
title: GitHub Actions attestation defaults and output requirements
---

For shared concepts, see [SBOMs](/manuals/security/sbom.md) and
[Image attestations and provenance](/manuals/security/image-attestations.md).



Software Bill of Material (SBOM) and provenance
[attestations](../../metadata/attestations/_index.md) add metadata about the contents of
your image, and how it was built.

Attestations are supported with version 4 and later of the
`docker/build-push-action`.

## Default provenance

The `docker/build-push-action` GitHub Action automatically adds provenance
attestations to your image, with the following conditions:

- If the GitHub repository is public, provenance attestations with `mode=max`
  are automatically added to the image.
- If the GitHub repository is private, provenance attestations with `mode=min`
  are automatically added to the image.
- If you're using the [`docker` exporter](../../exporters/oci-docker.md), or
  you're loading the build results to the runner with `load: true`, no
  attestations are added to the image. These output formats don't support
  attestations.

> [!WARNING]
>
> If you're using `docker/build-push-action` to build images for code in a
> public GitHub repository, the provenance attestations attached to your image
> by default contains the values of build arguments. If you're misusing build
> arguments to pass secrets to your build, such as user credentials or
> authentication tokens, those secrets are exposed in the provenance
> attestation. Refactor your build to pass those secrets using
> [secret mounts](/reference/cli/docker/buildx/build/#secret)
> instead. Also remember to rotate any secrets you may have exposed.

## Output requirements

For image-store context, see [Image store capabilities](/manuals/engine/storage/image-store-capabilities.md#build-images-with-attestations).

Note that adding attestations to an image means you must push the image to a
registry directly, as opposed to loading the image to the local image store of
the runner. This is because the local image store doesn't support loading
images with attestations.


