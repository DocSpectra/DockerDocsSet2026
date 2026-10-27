---
title: Scan Docker Hardened Images with Wiz
description: Scanner-specific steps for Wiz.
---

Shared guidance: [scanner integrations](../explore/scanner-integrations.md) and [DHI registry authentication](authenticate.md).

## Wiz

[Wiz](https://www.wiz.io/) is a cloud security platform that includes container
image scanning capabilities with support for DHI VEX attestations. Wiz CLI
automatically consumes VEX statements from Docker Hardened Images to provide
accurate vulnerability assessments.

### Scan a DHI using Wiz CLI

After acquiring a Wiz subscription and installing the Wiz CLI, you can scan a
Docker Hardened Image by pulling the image and running the scan command:

```console
$ docker login dhi.io
$ docker pull dhi.io/<image>:<tag>
$ wizcli scan container-image dhi.io/<image>:<tag>
```
