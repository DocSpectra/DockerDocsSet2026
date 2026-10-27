---
title: Inspect and verify hardened packages and package attestations
description: Verify package signatures and trace provenance recursively through package attestations.
---

Before you begin, review [hardened package context](../core-concepts/packages.md) and [image attestation verification](verify-attestations.md).

## Verify packages

Every hardened package is cryptographically signed and includes metadata that
proves its provenance and build integrity. You can verify the signatures and
view the metadata to ensure your packages come from Docker's trusted build
infrastructure.

### View package metadata

To view information about a hardened package, including its provenance:

```console
$ apk info -L <package-name>
```

This shows the files included in the package and its metadata.

### Verify package signatures

Hardened packages are cryptographically signed by Docker. When you install the
signing keys and configure your package manager as described previously, the
package manager automatically verifies signatures during installation.

If a package fails signature verification, the package manager will refuse to
install it, protecting you from tampered or compromised packages.

### Build provenance and cryptographic verification

Docker hardened packages are built by Docker's trusted infrastructure and include
verifiable metadata and cryptographic signatures.

To view this metadata for an installed package:

```console
$ apk info -a <package-name>
```

Or to view metadata for a package before installing:

```console
$ apk fetch --stdout <package-name> | tar -xzO .PKGINFO
```

The package signing keys ensure that packages haven't been tampered with after
being built. When you install the signing key and configure your package manager,
all packages are automatically verified before installation.

### Package attestations

Each hardened package includes its own attestations, similar to [image
attestations](verify-attestations.md). These attestations provide provenance and build
information for individual packages, allowing you to trace the supply chain down
to the package level.

You can retrieve package attestations by first extracting package information
from the image's SLSA provenance, then using the package digest to access its
attestations.

#### Extract package information from image attestations

To get provenance information for a specific package from an image's SLSA
provenance attestation, you first need to retrieve the image's provenance and
then filter for the specific package you're interested in.

The SLSA provenance attestation includes a `materials` array that lists all
build inputs, including packages. You can use `jq` to filter this array for a
specific package:

```console
$ docker scout attest get dhi.io/golang:1.26-alpine3.23 \
    --predicate-type https://slsa.dev/provenance/v0.2 | \
    jq '.predicate.materials[] | select( .uri == "https://dhi.io/apk/alpine/v3.23/main/aarch64/golang-1.26-1.26.0-r0.apk" )'
```

Replace the package URI in the `select()` filter with the specific package
you're looking for. You can find available packages by first running the command
without the `select()` filter to see all materials.

This returns the package URI and its SHA-256 digest:

```json
{
  "uri": "https://dhi.io/apk/alpine/v3.23/main/aarch64/golang-1.26-1.26.0-r0.apk",
  "digest": {
    "sha256": "4082a2500abc2e7b8435f9398d3514d760044fa52ca3d10cf80015469124a838"
  }
}
```

#### List attestations for a package

Using the package digest from the previous section, you can list all available
attestations for that package:

```console
$ curl -s https://dhi.io/apk/alpine/v3.23/main/sha256:4082a2500abc2e7b8435f9398d3514d760044fa52ca3d10cf80015469124a838/attestations/list | jq .
```

This returns information about the package and its available attestations:

```json
{
  "subject": {
    "name": "pkg:apk/alpine/golang-1.26@1.26.0-r0?os_name=&os_version=",
    "digest": {
      "sha256": "4082a2500abc2e7b8435f9398d3514d760044fa52ca3d10cf80015469124a838"
    }
  },
  "attestations": [
    {
      "predicate_type": "https://slsa.dev/provenance/v1",
      "digest": {
        "sha256": "97c919cf0edb27087739bbabeea4c1ef88d069cd41791476ba64b69280d63a32"
      },
      "url": "https://dhi.io/apk/alpine/v3.23/main/sha256:4082a2500abc2e7b8435f9398d3514d760044fa52ca3d10cf80015469124a838/attestations/sha256:97c919cf0edb27087739bbabeea4c1ef88d069cd41791476ba64b69280d63a32"
    }
  ]
}
```

#### Retrieve package attestations

To retrieve the actual attestation content, use the URL provided in the
attestation list:

```console
$ curl -s https://dhi.io/apk/alpine/v3.23/main/sha256:4082a2500abc2e7b8435f9398d3514d760044fa52ca3d10cf80015469124a838/attestations/sha256:97c919cf0edb27087739bbabeea4c1ef88d069cd41791476ba64b69280d63a32 | jq .
```

This returns the full SLSA provenance attestation for the package, which
includes information about how the package was built, its dependencies, and
other build materials.

You can continue this process recursively to trace the supply chain all the way
down to the compiler and other build tools used to create the package.
