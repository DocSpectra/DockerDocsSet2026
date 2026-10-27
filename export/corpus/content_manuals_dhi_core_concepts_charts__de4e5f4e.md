---
title: Docker Hardened Image Helm charts
description: Chart compatibility, signed metadata, and customization guarantees.
---

Docker Hardened Image (DHI) charts are Docker-provided [Helm
charts](https://helm.sh/docs/) built from upstream sources, designed for
compatibility with Docker Hardened Images. These charts are available as OCI
artifacts within the DHI catalog on Docker Hub.

DHI charts incorporate multiple layers of supply chain security that aren't present in upstream charts:

- SLSA Level 3 compliance: Each chart is built with SLSA Build Level 3 standards, including detailed build provenance
- Software Bill of Materials (SBOMs): Comprehensive SBOMs detail all components referenced within the chart
- Cryptographic signing: All associated metadata is cryptographically signed by Docker for integrity and authenticity
- Hardened configuration: Charts automatically reference Docker Hardened Images for secure deployments
- Tested compatibility: Charts are robustly tested to work out-of-the-box with Docker Hardened Images

You can use a DHI chart like any other Helm chart stored in an OCI registry.
When you have a Docker Hardened Images subscription, you can also customize DHI
charts to reference customized images and mirrored repositories. The customized
chart build pipeline ensures that your customizations are built securely, use
the latest base charts, and include attestations.
