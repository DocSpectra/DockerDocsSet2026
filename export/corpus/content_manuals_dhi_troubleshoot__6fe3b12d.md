---
title: Troubleshoot
description: Resolve common issues when building, running, or debugging Docker Hardened Images, such as non-root behavior, missing shells, and port access.
weight: 40
tags: [Troubleshooting]
keywords: troubleshoot hardened image, docker debug container, non-root permission issue, missing shell error, no package manager, debug, hardened images, DHI, troubleshooting, ephemeral container, docker debug, non-root containers, hardened container image, debug secure container
aliases:
- /dhi/how-to/debug/
---

This page covers debugging techniques and common issues you may encounter while
migrating to or using Docker Hardened Images (DHIs).

## General debugging

[Debug locally with Docker Debug, dev variants, or image mounts](how-to/debug.md).

## Common issues

[Resolve permissions, ports, shells, entrypoints, and package manager issues](how-to/runtime-issues.md).

### Permissions

[Check permissions](how-to/runtime-issues.md#permissions).

### Privileged ports

[Check privileged ports](how-to/runtime-issues.md#privileged-ports).

### No shell

[Resolve missing-shell assumptions](how-to/runtime-issues.md#no-shell).

### Entry point differences

[Inspect entrypoints](how-to/runtime-issues.md#entry-point-differences).

### No package manager

[Install packages during the build stage](how-to/runtime-issues.md#no-package-manager).
