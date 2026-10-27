---
title: Create OCI artifact images for DHI customization
description: Prepare minimal artifacts, publish all target platforms, and select file paths.
---

See [customization context](../core-concepts/customizations.md) and [multi-stage builds](/manuals/build/building/multi-stage.md).

## Create an OCI artifact image for image customization

An OCI artifact image is a Docker image that contains files or directories that
you want to include in your customized Docker Hardened Image (DHI). This can
include additional tools, libraries, or configuration files.

When creating an image to use as an OCI artifact, it should ideally be as
minimal as possible and contain only the necessary files.

For example, to distribute a custom root CA certificate as part of a trusted CA
bundle, you can use a multi-stage build. This approach registers your
certificate with the system and outputs an updated CA bundle, which can be
extracted into a minimal final image:

```dockerfile
# syntax=docker/dockerfile:1

FROM dhi.io/bash:5-dev AS certs

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /usr/local/share/ca-certificates/my-rootca
COPY certs/rootCA.crt /usr/local/share/ca-certificates/my-rootca

RUN update-ca-certificates

FROM scratch
COPY --from=certs /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
```

You can follow this pattern to create other OCI artifacts, such as images
containing tools or libraries that you want to include in your customized DHI.
Install the necessary tools or libraries in the first stage, and then copy the
relevant files to the final stage that uses `FROM scratch`. This ensures that
your OCI artifact is minimal and contains only the necessary files.

In order for the OCI artifact to be available in a DHI customization, it must be built and
pushed to a repository in the same namespace as the mirrored DHI repository.

If you're customizing a DHI for multiple platforms (such as `linux/amd64` and
`linux/arm64`), build your OCI artifact for all the platforms using the
`--platform` flag:

```console
$ docker buildx build --platform linux/amd64,linux/arm64 \
  -t <your-namespace>/my-oci-artifact:latest \
  --push .
```

This creates a single image manifest that you can use for each platform. The
customization build system automatically selects the correct platform variant
when building each customized image.

> [!IMPORTANT]
>
> The customization UI will only allow you to select platforms that are
> available in all OCI artifacts you've added. If a platform is missing from
> any OCI artifact, you won't be able to select that platform for your
> customization.

Once pushed to a repository in your organization's namespace, the OCI artifact
automatically appears in the customization workflow when you select OCI
artifacts to add to your customized Docker Hardened Image.

### Best practices for OCI artifacts

Follow these best practices when creating OCI artifacts for DHI customizations:

- Use multi-stage builds: Build or install dependencies in a builder stage,
  then copy only the necessary files to a `FROM scratch` final stage. This keeps
  the OCI artifact minimal and free of unnecessary build tools.

- Include only essential files: OCI artifacts should contain only the files
  you need to add to the customized image. Avoid including package managers,
  shells, or other utilities that won't be used in the final image.

- Match target platforms: Build your OCI artifact for all platforms you plan
  to use in your customizations. Use `docker buildx build --platform` to create
  multi-platform images when needed.

- Use specific tags: Tag your OCI artifacts with specific versions or dates
  (like `v1.0` or `20250101`) rather than relying solely on `latest`. This
  ensures reproducible builds and makes it easier to track which artifacts are
  used in which customizations.

- Enable immutable tags: Consider enabling [immutable
  tags](../../docker-hub/repos/manage/hub-images/immutable-tags.md) for your
  OCI artifact repositories. This prevents accidental overwrites and ensures that
  each version of your OCI artifact remains unchanged, improving reproducibility
  and reliability of your customizations.
