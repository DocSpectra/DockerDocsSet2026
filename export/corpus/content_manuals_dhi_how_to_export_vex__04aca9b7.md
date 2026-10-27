---
title: Export Docker Hardened Image VEX attestations
description: Retrieve VEX files for scanners with local-file support.
---

## Export VEX attestations

For scanners that need local VEX files (like Grype or Trivy with local files),
you can export the VEX attestations from Docker Hardened Images.

> [!NOTE]
>
> By default, VEX attestations are fetched from `registry.scout.docker.com`. Ensure that you can access this registry
> if your network has outbound restrictions. You can also mirror the attestations to an alternate registry. For more
> details, see [Mirror to a third-party registry](mirror-registry.md).

Export VEX attestations to a JSON file:

```console
$ docker scout vex get dhi.io/<image>:<tag> --output vex.json
```

> [!NOTE]
>
> The `docker scout vex get` command requires [Docker Scout
> CLI](https://github.com/docker/scout-cli/) version 1.18.3 or later.
>
> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use
> `registry://docs/dhi-python:3.13` instead of `docs/dhi-python:3.13`.


## Use VEX to filter known non-exploitable CVEs

Docker Hardened Images include signed [VEX (Vulnerability Exploitability
eXchange)](../core-concepts/vex.md) attestations that identify vulnerabilities not relevant to the image’s
runtime behavior.

When using Docker Scout or Trivy with the VEX-enabled scan examples, these
VEX statements are automatically applied, and no manual configuration is needed.

To manually retrieve the VEX attestation for tools that support it:

```console
$ docker scout vex get dhi.io/<image>:<tag> --output vex.json
```

> [!NOTE]
>
> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use
> `registry://dhi.io/python:3.13` instead of `dhi.io/python:3.13`.

For example:

```console
$ docker scout vex get dhi.io/python:3.13 --output vex.json
```

This creates a `vex.json` file containing the VEX statements for the specified
image. You can then use this file with tools that support VEX to filter out known non-exploitable CVEs.
