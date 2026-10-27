---
description: Turn on the Docker WSL 2 backend and get to work using best practices,
  GPU support, and more in this thorough guide.
keywords: wsl, wsl2, installing wsl2, wsl installation, docker wsl2, wsl docker, wsl2
  tech preview, wsl install docker, install docker wsl, how to install docker in wsl
title: Docker Desktop WSL 2 backend on Windows
linkTitle: WSL
weight: 120
aliases:
- /docker-for-windows/wsl/
- /docker-for-windows/wsl-tech-preview/
- /desktop/windows/wsl/
- /desktop/wsl/
---

Windows Subsystem for Linux (WSL) 2 is a full Linux kernel built by Microsoft that lets Linux distributions run without managing virtual machines. With Docker Desktop running on WSL 2, users can leverage Linux workspaces and avoid maintaining both Linux and Windows build scripts. In addition, WSL 2 provides improvements to file system sharing, faster cold-start times, and dynamic resource allocation.

Because WSL 2 uses dynamic memory allocation, Docker Desktop requests only the CPU and memory it actually needs — freeing resources for the rest of your system, while still letting memory-intensive tasks such as multi-stage image builds run at full speed.

## Prerequisites

See [WSL 2 requirements and memory reclamation](requirements.md).

## Turn on Docker Desktop WSL 2

See [Turn on the Docker Desktop WSL 2 backend](enable-wsl.md).

## Enable Docker in a WSL 2 distribution

See [Enable Docker in a WSL 2 distribution](integration.md).

## WSL 2 security in Docker Desktop

See [WSL 2 security in Docker Desktop](security.md).

## Additional resources

- [Explore best practices](best-practices.md)
- [Understand how to develop with Docker and WSL 2](use-wsl.md)
- [Learn about GPU support with WSL 2](/manuals/desktop/features/gpu.md)
- [Custom kernels on WSL](custom-kernels.md)
