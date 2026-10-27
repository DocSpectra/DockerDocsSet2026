---
title: Use compliance and ELS variants
description: Access FIPS, STIG, and Extended Lifecycle Support image variants.
---

## Use compliance and ELS variants

{{< summary-bar feature_name="Docker Hardened Images" >}}

With a DHI Select or DHI Enterprise subscription, you can access additional
image variants:

- Compliance variants: FIPS-enabled and STIG-ready images for regulatory
  requirements
- ELS (Extended Lifecycle Support) variants (requires add-on): Security patches
  for end-of-life image versions

To access these variants, [mirror](./mirror.md) the repository to your Docker
Hub organization. For ELS, enable **Mirror end-of-life images** when setting up
mirroring. Once mirrored, use the compliance or EOL tags like any other image
tag.
