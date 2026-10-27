---
title: Analyze images locally
---

You can analyze local images with Docker Scout using Docker Desktop or the
`docker scout` commands for the Docker CLI.

## Docker Desktop

> [!NOTE]
>
> Docker Desktop background indexing supports images up to 10 GB in size.
> See [Maximum image size](/manuals/scout/deep-dive/image-analysis.md#maximum-image-size).

To analyze an image locally using the Docker Desktop GUI:

1. Pull or build the image that you want to analyze.
2. Go to the **Images** view in the Docker Dashboard.
3. Select one of your local images in the list.

   This opens the [Image details view](../explore/image-details-view.md), showing a
   breakdown of packages and vulnerabilities found by the Docker Scout analysis
   for the image you selected.

## CLI

For artifact selection and local-versus-registry lookup, see [Artifact types](/manuals/scout/how-tos/artifact-types.md).

The `docker scout` CLI commands provide a command line interface for using Docker
Scout from your terminal.

- `docker scout quickview`: summary of the specified image, see [Quickview](#quickview)
- `docker scout cves`: local analysis of the specified image, see [CVEs](#cves)
- `docker scout compare`: analyzes and compares two images

By default, the results are printed to standard output.
You can also export results to a file in a structured format,
such as Static Analysis Results Interchange Format (SARIF).

### Quickview

The `docker scout quickview` command provides an overview of the
vulnerabilities found in a given image and its base image.

```console
$ docker scout quickview traefik:latest
    ✓ SBOM of image already cached, 311 packages indexed

  Your image  traefik:latest  │    0C     2H     8M     1L
  Base image  alpine:3        │    0C     0H     0M     0L
```

If your the base image is out of date, the `quickview` command also shows how
updating your base image would change the vulnerability exposure of your image.

```console
$ docker scout quickview postgres:13.1
    ✓ Pulled
    ✓ Image stored for indexing
    ✓ Indexed 187 packages

  Your image  postgres:13.1                 │   17C    32H    35M    33L
  Base image  debian:buster-slim            │    9C    14H     9M    23L
  Refreshed base image  debian:buster-slim  │    0C     1H     6M    29L
                                            │    -9    -13     -3     +6
  Updated base image  debian:stable-slim    │    0C     0H     0M    17L
                                            │    -9    -14     -9     -6
```

### CVEs

The `docker scout cves` command gives you a complete view of all the
vulnerabilities in the image. This command supports several flags that lets you
specify more precisely which vulnerabilities you're interested in, for example,
by severity or package type:

```console
$ docker scout cves --format only-packages --only-vuln-packages \
  --only-severity critical postgres:13.1
    ✓ SBOM of image already cached, 187 packages indexed
    ✗ Detected 10 vulnerable packages with a total of 17 vulnerabilities

     Name            Version         Type        Vulnerabilities
───────────────────────────────────────────────────────────────────────────
  dpkg        1.19.7                 deb      1C     0H     0M     0L
  glibc       2.28-10                deb      4C     0H     0M     0L
  gnutls28    3.6.7-4+deb10u6        deb      2C     0H     0M     0L
  libbsd      0.9.1-2                deb      1C     0H     0M     0L
  libksba     1.3.5-2                deb      2C     0H     0M     0L
  libtasn1-6  4.13-3                 deb      1C     0H     0M     0L
  lz4         1.8.3-1                deb      1C     0H     0M     0L
  openldap    2.4.47+dfsg-3+deb10u5  deb      1C     0H     0M     0L
  openssl     1.1.1d-0+deb10u4       deb      3C     0H     0M     0L
  zlib        1:1.2.11.dfsg-1        deb      1C     0H     0M     0L
```

For more information about these commands and how to use them, refer to the CLI
reference documentation:

- [`docker scout quickview`](/reference/cli/docker/scout/quickview/)
- [`docker scout cves`](/reference/cli/docker/scout/cves/)
