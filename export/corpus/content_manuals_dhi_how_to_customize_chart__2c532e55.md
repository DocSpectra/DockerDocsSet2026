---
title: Customize a Docker Hardened Image Helm chart
description: Customize chart image references in Docker Hub.
---

Before you begin, review [customization capabilities](../core-concepts/customizations.md), [mirroring requirements](../core-concepts/mirroring.md), and [CLI setup](cli.md).

## Customize a DHI Helm chart

You can customize DHI Helm charts to meet your organization's specific needs.
Via the Docker Hub web interface, you can modify the image references to
reference mirrored images or customized images you've created. This lets you
create a custom, securely-built chart with references to images stored in Docker
Hub or other private registries. DHI securely packages customized Helm charts
that reference your repositories, wherever they are stored, by default.

To customize image references, an organization owner must [mirror](mirror-hub.md)
the DHI chart repository to your organization on Docker Hub.

You can create one chart customization per Helm chart repository. This is
different from image customizations, where you can create multiple
customizations per repository. If you need to make changes, you can edit your
existing customization. Alternatively, you can mirror the same Helm chart
repository again and add a new customization to the new mirror.

> [!NOTE]
>
> You can customize Docker Hardened Image charts like any other Helm chart using
> standard Helm tools and practices, such as a `values.yaml` file, outside of
> Docker Hub. The following instructions describe how to customize image
> references for the chart using the Docker Hub web interface.

To customize a Docker Hardened Image Helm chart after it has been mirrored:

1. Sign in to [Docker Hub](https://hub.docker.com).
1. Select **My Hub**.
1. In the namespace drop-down, select your organization that has a mirrored DHI
   repository.
1. Select **Hardened Images** > **Manage** > **Mirrored Helm charts**.
1. For the mirrored DHI repository you want to customize, select the **Name**.
1. Select the **Customizations** tab.
1. Select **Create customization**.

   At this point, the on-screen instructions will guide you through the
   customization process.
