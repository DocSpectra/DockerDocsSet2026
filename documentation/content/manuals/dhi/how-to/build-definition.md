---
title: Build, inspect, and publish a DHI definition
description: Shared local build, verification, debugging, and push procedure.
---

> [!IMPORTANT]
>
> The DHI build system pulls base images and build tools from `dhi.io`, so you
> must authenticate to that registry before building a definition file. Use your
> Docker ID credentials (the same username and password you use for Docker Hub)
> when signing in.
>
> Run `docker login dhi.io` to authenticate.

## Build and verify

### Build the image

Build a single-platform image for local testing:

```console
$ docker buildx build . -f my-image.yaml \
    --sbom=generator=dhi.io/scout-sbom-indexer:1 \
    --provenance=1 \
    --tag my-image:latest \
    --load
```

### Inspect the SBOM

View the generated Software Bill of Materials:

```console
$ docker scout sbom my-image:latest
```

### Scan for vulnerabilities

Check the image against known CVE databases:

```console
$ docker scout cves my-image:latest
```

### Compare with a non-hardened image

Measure the security improvement against an equivalent non-hardened image:

```console
$ docker scout compare my-image:latest \
    --to <non-hardened-equivalent>:<tag> \
    --platform linux/amd64
```

Replace `<non-hardened-equivalent>` with the Docker Official Image or
community image you're comparing against.

### Inspect with Docker Debug

Verify the os-release and entrypoint configuration:

```console
$ docker debug my-image:latest
```

The output shows the detected distribution name from your `os-release`
configuration and runs an entrypoint lint check.

## Push to a registry

Tag and push the image to your container registry:

```console
$ docker tag my-image:latest <your-namespace>/my-image:latest
```

```console
$ docker push <your-namespace>/my-image:latest
```

Replace `<your-namespace>` with your Docker Hub username or organization
namespace.
