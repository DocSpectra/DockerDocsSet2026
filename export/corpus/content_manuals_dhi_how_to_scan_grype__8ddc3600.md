---
title: Scan Docker Hardened Images with Grype
description: Scanner-specific steps for Grype.
---

Shared guidance: [scanner integrations](../explore/scanner-integrations.md) and [DHI registry authentication](authenticate.md). For VEX file retrieval requirements, see [Export VEX attestations](export-vex.md).

## Grype

[Grype](https://github.com/anchore/grype) is an open-source scanner that checks
container images against vulnerability databases like the NVD and distro
advisories.

### Scan a DHI using Grype

After installing Grype, you can scan a Docker Hardened Image by pulling
the image and running the scan command. Grype requires you to export the VEX
attestation to a file first:

To scan a Docker Hardened Image using Grype with VEX filtering, first export
the VEX attestation and then scan with the `--vex` flag:

```console
$ docker login dhi.io
$ docker pull dhi.io/<image>:<tag>
$ docker scout vex get dhi.io/<image>:<tag> --output vex.json
$ grype dhi.io/<image>:<tag> --vex vex.json
```

The `--vex` flag applies VEX statements during the scan, filtering out known
non-exploitable CVEs for accurate results.

For more information on exporting VEX attestations, see [Export VEX
attestations](export-vex.md).


Example output:

```plaintext
NAME               INSTALLED              FIXED-IN     TYPE  VULNERABILITY     SEVERITY    EPSS%  RISK
libperl5.36        5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1
perl               5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1
perl-base          5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1
...
```
