---
title: Choose a Virtual Machine Manager for Docker Desktop on Mac
linkTitle: Virtual Machine Manager
keywords: virtualization software, resource allocation, mac, docker desktop, vm monitoring, vm performance, apple silicon
description: Discover Docker Desktop for Mac's Virtual Machine Manager (VMM) options, including Docker VMM for Apple Silicon, offering enhanced performance and efficiency
weight: 110
aliases:
  - /desktop/vmm/
---

Docker Desktop supports multiple Virtual Machine Managers (VMMs) to power the Linux VM that runs containers. You can choose the most suitable option based on your system architecture (Intel or Apple Silicon), performance needs, and feature requirements. This page provides an overview of the available options.

## Options and limitations

Before changing the VMM, see [Virtual Machine Manager options and limitations](vmm-reference.md), including Docker VMM memory requirements and known issues.

## Change the VMM

To change the VMM, go to **Settings** > **General** > **Virtual Machine Manager**.

## Docker VMM

See [Docker VMM](vmm-reference.md#docker-vmm).

### Known issues

See [Docker VMM known issues](vmm-reference.md#known-issues).

## Apple Virtualization framework

See [Apple Virtualization framework](vmm-reference.md#apple-virtualization-framework).

## QEMU (Legacy) for Apple Silicon

See [QEMU deprecation and scope](vmm-reference.md#qemu-legacy-for-apple-silicon).

## HyperKit (Legacy) for Intel-based Macs

See [HyperKit deprecation](vmm-reference.md#hyperkit-legacy-for-intel-based-macs).
