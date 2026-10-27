---
title: Use a Docker Hardened Image chart
linktitle: Use a Helm chart
description: Learn how to use a Docker Hardened Image chart.
keywords: use hardened image, helm, k8s, kubernetes, dhi chart, chart
weight: 31
---

See [Docker Hardened Image Helm charts](../core-concepts/charts.md) for chart compatibility, security metadata, and customization context.

## Find a Docker Helm chart

To find a Docker Helm chart for DHI:

1. Go to the Hardened Images catalog in [Docker Hub](https://hub.docker.com/hardened-images/catalog) and sign in.
2. In the left sidebar, select **Hardened Images** > **Catalog**.
3. Select **Filter by** for **Helm Charts**.
4. Select a Helm chart repository to view its details.

## Mirror a Helm chart and/or its images to a third-party registry

Follow [Mirror images, charts, and attestations to another registry](mirror-registry.md).

## Create a Kubernetes secret for pulling images

Follow [Create a Kubernetes secret for Helm chart image pulls](kubernetes.md#create-a-kubernetes-secret-for-helm-chart-image-pulls).

## Install a Helm chart

To install a Helm chart from Docker Hardened Images:

1. Sign in to the registry using Helm:

   ```console
   $ echo $ACCESS_TOKEN | helm registry login dhi.io --username <your-username> --password-stdin
   ```

    Replace `<your-username>` and set `$ACCESS_TOKEN`.

2. Install the chart using `helm install`. Optionally, you can also use the `--dry-run` flag to test the installation without
   actually installing anything.


   ```console
   $ helm install <release-name> oci://dhi.io/<helm-chart-repository> --version <chart-version> \
     --set "imagePullSecrets[0].name=<your-secret-name>"
   ```

   Replace `<helm-chart-repository>` and `<chart-version>` accordingly. If the
   chart is in your own registry or another repository, replace
   `dhi.io/<helm-chart-repository>` with your own location. Replace
   `<your-secret-name>` with the name of the image pull secret created
   from [Create a Kubernetes secret for pulling images](#create-a-kubernetes-secret-for-pulling-images).

## Customize a Helm chart

You can customize Docker Hardened Image Helm charts to reference customized
images and mirrored repositories. For more details, see [Customize Docker
Hardened Images and charts](customize-chart.md).

## Verify a Helm chart and view its attestations

You can verify Helm charts. For more details, see [Verify Helm chart attestations](verify-charts.md).
