---
title: Find and use STIG images and inspect scan reports
description: Task steps and examples for DHI stig.
---

See [STIG context](../core-concepts/stig.md). For registry access, see [Authenticate to dhi.io](authenticate.md). For attestation verification requirements, see [Retrieve and verify attestations](verify-attestations.md).

## Identify images that include STIG scan results

Docker Hardened Images that include STIG scan results are labeled as **STIG** in
the Docker Hardened Images catalog.

To find DHI repositories with STIG image variants, [explore
images](explore.md#image-variants) and:

- Use the **STIG** filter on the catalog page
- Look for **STIG** labels on individual image listings

To find a STIG image variant within a repository, go to the **Tags** tab in the
repository, and find images labeled with **STIG** in the **Compliance** column.

## Use a STIG variant

To use a STIG variant, you must [mirror](mirror-hub.md) the repository
and then pull the STIG image from your mirrored repository.

## View and verify STIG scan results

Docker provides a signed [STIG scan
attestation](../core-concepts/attestations.md) for each STIG-ready image.
These attestations include:

- A summary of the scan results, including the number of passed, failed, and not
  applicable checks
- The name and version of the STIG profile used
- Full output in both HTML and XCCDF (XML) formats

### View STIG scan attestations

You can retrieve and inspect a STIG scan attestation using the Docker Scout CLI:

```console
$ docker scout attest get \
  --predicate-type https://docker.com/dhi/stig/v0.1 \
  --verify \
  --predicate \
  dhi.io/<image>:<tag>
```

### Extract HTML report

To extract and view the human-readable HTML report:

```console
$ docker scout attest get dhi.io/<image>:<tag> \
  --predicate-type https://docker.com/dhi/stig/v0.1 \
  --verify \
  --predicate \
  | jq -r '.[0].output[] | select(.format == "html").content | @base64d' > stig_report.html
```

### Extract XCCDF report

To extract the XML (XCCDF) report for integration with other tools:

```console
$ docker scout attest get dhi.io/<image>:<tag> \
  --predicate-type https://docker.com/dhi/stig/v0.1 \
  --verify \
  --predicate \
  | jq -r '.[0].output[] | select(.format == "xccdf").content | @base64d' > stig_report.xml
```

### View STIG scan summary

To view just the scan summary without the full reports:

```console
$ docker scout attest get dhi.io/<image>:<tag> \
  --predicate-type https://docker.com/dhi/stig/v0.1 \
  --verify \
  --predicate \
  | jq -r '.[0] | del(.output)'
```
