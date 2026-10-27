---
title: Use Hardened System Packages
linkTitle: Use hardened packages
weight: 32
keywords: hardened images, DHI, hardened packages, packages, alpine
description: Learn how to use and verify Docker's hardened system packages in your images.
---

Choose a package task. Review [hardened package access and built-in packages](../core-concepts/packages.md) for context.

## Built-in packages

[Read about built-in packages](../core-concepts/packages.md#built-in-packages).

## Add hardened packages to your images

### Add packages through image customization

{{< summary-bar feature_name="Docker Hardened Images" >}}

When customizing Docker Hardened Images with DHI Select or DHI Enterprise, you
can add hardened packages for Alpine-based images through the customization
interface. Follow the steps to [create an image
customization](customize-image.md#customize-a-docker-hardened-image) and select hardened
packages during the customization process.

### Configure the package manager

- [Configure the public repository](packages-public.md)
- [Configure the enterprise repository](packages-enterprise.md)

#### Public repository

[Public repository setup and verification](packages-public.md).

#### Enterprise repository

[Enterprise repository setup and build secrets](packages-enterprise.md).

## Verify packages

[Inspect metadata and verify packages](verify-packages.md).

### Package attestations

[Retrieve package attestations and trace the supply chain](verify-packages.md#package-attestations).
