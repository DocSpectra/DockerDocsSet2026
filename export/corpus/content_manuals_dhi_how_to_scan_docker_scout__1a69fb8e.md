---
title: Scan Docker Hardened Images with Docker Scout
description: Scanner-specific steps for Docker Scout.
---

Shared guidance: [scanner integrations](../explore/scanner-integrations.md) and [DHI registry authentication](authenticate.md).

## Docker Scout

Docker Scout is integrated into Docker Desktop and the Docker CLI. It provides
vulnerability insights, CVE summaries, and direct links to remediation guidance.

### Scan a DHI using Docker Scout

To scan a Docker Hardened Image using Docker Scout, run the following
command:

```console
$ docker login dhi.io
$ docker scout cves dhi.io/<image>:<tag> --platform <platform>
```

Example output:

```plaintext
    v SBOM obtained from attestation, 101 packages found
    v Provenance obtained from attestation
    v VEX statements obtained from attestation
    v No vulnerable package detected
    ...
```

For more detailed filtering and JSON output, see [Docker Scout CLI reference](/reference/cli/docker/scout/).
