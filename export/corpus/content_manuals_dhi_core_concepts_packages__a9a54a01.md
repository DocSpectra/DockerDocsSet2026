---
title: Hardened system packages and subscription access
description: Source-built packages, built-in support, and Community, Select, and Enterprise access.
---

Docker Hardened System Packages are built from source by Docker. This ensures
supply chain integrity throughout your entire image stack by eliminating risks
from potentially compromised public packages.

Access to hardened packages varies by subscription:

- **DHI Community**: Includes hardened packages in base images. Can configure the
  public package repository to access the same packages in custom images.
- **DHI Select**: Includes all Community packages, plus access to additional
  compliance-specific packages (such as FIPS variants) and Docker-patched
  packages through the image customization UI.
- **DHI Enterprise**: Includes all Select packages, plus the ability to configure
  the enterprise package repository directly in your own images for full access
  to compliance and security-patched packages.

## Built-in packages

Supported distributions of Docker Hardened Images (DHI) automatically include
hardened system packages. No additional configuration is required. Simply pull
and use the images as normal.

All packages in these images are built by Docker from source, maintaining
the same security standards as the base images themselves.
