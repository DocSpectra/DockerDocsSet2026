---
title: Scan Docker Hardened Images with Mend.io
description: Scanner-specific steps for Mend.io.
---

Shared guidance: [scanner integrations](../explore/scanner-integrations.md) and [DHI registry authentication](authenticate.md).

## Mend.io

[Mend.io](https://www.mend.io/) is an application security platform that
includes container image scanning with support for DHI VEX attestations.
Mend Container automatically retrieves and applies VEX statements from Docker
Hardened Images and combines them with Mend's reachability analysis for
comprehensive vulnerability assessment.

### Scan a DHI using Mend.io

After acquiring a Mend.io subscription and configuring
[Mend Container](https://docs.mend.io/container/latest/), Mend automatically
detects Docker Hardened Images and applies their VEX data without requiring any
additional configuration. When you scan a Docker Hardened Image through the Mend
AppSec Platform, VEX statements are automatically retrieved and attached as risk
factors to each finding.

You can view and filter DHI-specific findings in the Mend AppSec Platform under
**Security > Containers > Packages**, where a Docker badge identifies hardened
image packages. Use the **Risk Factors** column to filter by VEX statuses such
as Not Affected, Fixed, or Under Investigation.

For more information, see the [Mend.io Docker Hardened Images
documentation](https://docs.mend.io/platform/latest/docker-hardened-images).
