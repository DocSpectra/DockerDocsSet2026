---
title: Find and use FIPS images and inspect their attestations
description: Task steps and examples for DHI fips.
---

See [FIPS context](../core-concepts/fips.md). For registry access, see [Authenticate to dhi.io](authenticate.md). For attestation verification requirements, see [Retrieve and verify attestations](verify-attestations.md).

## Identify images that support FIPS

Docker Hardened Images that support FIPS are marked as **FIPS** compliant
in the Docker Hardened Images catalog.

To find DHI repositories with FIPS image variants, [search the catalog](explore.md) and:

- Use the **FIPS** filter on the catalog page
- Look for **FIPS** compliant on individual image listings

These indicators help you quickly locate repositories that support FIPS-based
compliance needs. Image variants that include FIPS support will have a tag
ending with `-fips`, such as `3.13-fips`.

## Use a FIPS variant

To use a FIPS variant, you must [mirror](mirror-hub.md) the repository
and then pull the FIPS image from your mirrored repository.

## View the FIPS attestation

The FIPS variants of Docker Hardened Images contain a FIPS attestation that
lists the actual cryptographic modules included in the image.

You can retrieve and inspect the FIPS attestation using the Docker Scout CLI:

```console
$ docker scout attest get \
  --predicate-type https://docker.com/dhi/fips/v0.1 \
  --predicate \
  dhi.io/<image>:<tag>
```

For example:

```console
$ docker scout attest get \
  --predicate-type https://docker.com/dhi/fips/v0.1 \
  --predicate \
  dhi.io/python:3.13-fips
```

The attestation output is a JSON array describing the cryptographic modules
included in the image and their compliance status. For example:

```json
[
  {
    "certification": "CMVP #4985",
    "certificationUrl": "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4985",
    "name": "OpenSSL FIPS Provider",
    "package": "pkg:dhi/openssl-provider-fips@3.1.2",
    "standard": "FIPS 140-3",
    "status": "active",
    "sunsetDate": "2030-03-10",
    "version": "3.1.2"
  }
]
```
