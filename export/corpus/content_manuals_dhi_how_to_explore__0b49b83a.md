---
title: Search and evaluate Docker Hardened Images
linktitle: Search and evaluate
description: Learn how to find, compare, and evaluate Docker Hardened Images using the catalog on Docker Hub and Docker Scout comparison tools.
keywords: search docker images, image variants, docker hub catalog, compare docker images, docker scout compare, image comparison, vulnerability comparison
weight: 10
aliases:
  - /dhi/how-to/compare/
---

Docker Hardened Images (DHI) are a curated set of secure, production-ready
container images designed to provide enhanced security, minimized attack
surfaces, and production-ready foundations for your applications.

This page explains how to search available DHI repositories, review image
metadata, examine variant details, and compare images to evaluate security
improvements and differences.

## Search the catalog

You can browse, search, or filter images by category in the [Hardened Image
catalog](https://hub.docker.com/hardened-images/catalog) on Docker Hub.

Alternatively, use the [DHI CLI](/reference/cli/docker/dhi/), included in
[Docker Desktop](/desktop/), to browse the catalog from the command line:

```console
$ docker dhi catalog list
```

Filter by image type, name, or compliance requirements:

```console
$ docker dhi catalog list --type image
$ docker dhi catalog list --filter python
$ docker dhi catalog list --fips
$ docker dhi catalog list --stig
```

### Repository details

When you select a repository from the catalog, the repository details page
provides the following:

 - Overview: A brief explanation of the image.
 - Guides: Several guides on how to use the image and migrate your existing application.
 - Images: Select this option to [view image variants](#image-variants).
 - Security summary: Select a tag name to view a quick security summary,
   including package count, total known vulnerabilities, and Scout health score.
 - Recently pushed tags: A list of recently updated image variants and when they
   were last updated.
 - Use this image: After selecting an image variant, you can select this option to
   view instructions on how to pull and use the image variant.

To view repository details from the command line, use the DHI CLI:

```console
$ docker dhi catalog get python
```

This shows available tags, CVE counts, and other repository metadata.

### Image variants

Tags are used to identify image variants. Image variants are different builds of
the same application or framework tailored for different use-cases.

From the [repository details](#repository-details), select **Images** to view
the available image variants.

The **Images** page provides a table with the following columns:

- Image version: The image name with its base distribution (for example, `debian
  13`) and associated tags.
- Type: The support lifecycle status of the variant.
- Compliance: Relevant compliance designations. For example, `CIS`, `FIPS`, or
  `STIG (100%)`.
- Package manager: Whether a package manager is available. A checkmark indicates
  a package manager is present (for example, `apt` or `apk`), a dash indicates
  none.
- Shell: Whether a shell is available. A checkmark indicates a shell is present
  (for example, `bash` or `busybox`), a dash indicates none.
- User: The user that the container runs as. For example, `root` or `nonroot
  (65532)`.
- Last pushed: When the image variant was last updated.
- Vulnerabilities: Vulnerability counts by severity level.
- Health: The Scout health score. Select the score to view more details.

### Image variant details

On the [**Images** page](#image-variants), select an image version from the
table to view detailed information about that specific variant.

The image variant details page provides the following information:

- Packages: A list of all packages included in the image variant. This section
  includes details about each package, including its name, version,
  distribution, and licensing information.
- Specifications: The specifications for the image variant include the following
  key details:
   - Source & Build Information: The image is built from the Dockerfile found
     here and the Git commit.
   - Build parameters
   - Entrypoint
   - CMD
   - User
   - Working directory
   - Environment Variables
   - Labels
   - Platform
- Vulnerabilities: The vulnerabilities section provides a list of known CVEs for
  the image variant, including:
   - CVE
   - Severity
   - Package
   - Fix version
   - Last detected
   - Status
   - Suppressed CVEs
- Attestations: Variants include comprehensive security attestations to verify
  the image's build process, contents, and security posture. These attestations
  are signed and can be verified using cosign. For a list of available
  attestations, see [Attestations](../core-concepts/attestations.md).

## Compare and evaluate images

[Compare images with Docker Scout](compare-images.md).
