---
title: View and verify DHI test attestations
description: Retrieve scan or test results and verify the signed attestation.
---

See [image testing context](../explore/test.md). Before you begin, [authenticate to dhi.io](authenticate.md) and review the [shared attestation verification procedure](verify-attestations.md).

## Testing attestation

Docker provides a test attestation that details the testing and validation
processes each DHI has undergone.

### View and verify the test attestation

You can view and verify this attestation using the Docker Scout CLI.

1. Use the `docker scout attest get` command with the test predicate type:

   ```console
   $ docker scout attest get \
     --predicate-type https://scout.docker.com/tests/v0.1 \
     --predicate \
     dhi.io/<image>:<tag>
   ```

   > [!NOTE]
   >
   > If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use
   > `registry://dhi.io/python` instead of `dhi.io/python`.

   For example:

   ```console
   $ docker scout attest get \
     --predicate-type https://scout.docker.com/tests/v0.1 \
     --predicate \
     dhi.io/python:3.13
   ```

   This contains a list of tests and their results.

   Example output:

    ```console
        v SBOM obtained from attestation, 101 packages found
        v Provenance obtained from attestation
        {
          "reportFormat": "CTRF",
          "results": {
            "summary": {
              "failed": 0,
              "passed": 1,
              "skipped": 0,
              "start": 1749216533,
              "stop": 1749216574,
              "tests": 1
            },
            "tests": [
              {
                ...
   ```

2. Verify the test attestation signature. To ensure the attestation is authentic
   and signed by Docker, run:

   ```console
   docker scout attest get \
     --predicate-type https://scout.docker.com/tests/v0.1 \
     --verify \
     dhi.io/<image>:<tag> --platform <platform>
   ```

   Example output:
   
   ```console
    v SBOM obtained from attestation, 101 packages found
    v Provenance obtained from attestation
    v cosign verify registry.scout.docker.com/docker/dhi-python@sha256:70c8299c4d3cb4d5432734773c45ae58d8acc2f2f07803435c65515f662136d5 \
        --key https://registry.scout.docker.com/keyring/dhi/latest.pub --experimental-oci11

      Verification for registry.scout.docker.com/docker/dhi-python@sha256:70c8299c4d3cb4d5432734773c45ae58d8acc2f2f07803435c65515f662136d5 --
      The following checks were performed on each of these signatures:
        - The cosign claims were validated
        - Existence of the claims in the transparency log was verified offline
        - The signatures were verified against the specified public key

    i Signature payload
    ...
    ```

If the attestation is valid, Docker Scout will confirm the signature and show
the matching `cosign verify` command.

To view other attestations, such as SBOMs or vulnerability reports, see [Verify
an image](verify-attestations.md).
