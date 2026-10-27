---
title: Docker Hardened Image and chart customizations
description: Customization capabilities, automatic rebuilds, and supply-chain guarantees.
---

{{< summary-bar feature_name="Docker Hardened Images" >}}

When you have a DHI Select or DHI Enterprise subscription, you can customize Docker
Hardened Images (DHI) and charts to suit your specific needs using the Docker
Hub web interface. For images, this lets you select a base image, add packages,
add OCI artifacts (such as custom certificates or additional tools), and
configure settings. For charts, this lets you customize the image references.

Your customizations stay secure automatically. When the base Docker Hardened
Image or chart receives a security patch or your OCI artifacts are updated,
Docker automatically rebuilds your customizations in the background. This
ensures continuous compliance and protection by default, with no manual work
required. The rebuilt artifacts are signed and attested to the same SLSA Build
Level 3 standard as the base images and charts, ensuring a secure and verifiable
supply chain.
