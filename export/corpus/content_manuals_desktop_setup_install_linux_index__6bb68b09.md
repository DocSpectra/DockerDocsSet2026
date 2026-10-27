---
description:
  Install Docker on Linux with ease using our step-by-step installation
  guide covering system requirements, supported platforms, and where to go next.
keywords:
  linux, docker linux install, docker linux, linux docker installation, docker
  for linux, docker desktop for linux, installing docker on linux, docker download
  linux, how to install docker on linux, linux vs docker engine, switch docker contexts
title: Install Docker Desktop on Linux
linkTitle: Linux
weight: 60
aliases:
  - /desktop/linux/install/
  - /desktop/install/linux-install/
  - /desktop/install/linux/
---

> **Docker Desktop terms**
>
> Commercial use of Docker Desktop in larger enterprises (more than 250
> employees or more than $10 million USD in annual revenue) requires a [paid
> subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopLinuxInstall).

This page contains information about general system requirements, supported platforms, and instructions on how to install Docker Desktop for Linux.

## Docker Desktop and Docker Engine

See [Use Docker Desktop and Docker Engine on Linux](engine-context.md) for the VM and storage separation, port conflicts, service commands, and context switching.

### Installing Docker Desktop and Docker Engine

See [Installing Docker Desktop and Docker Engine](engine-context.md#installing-docker-desktop-and-docker-engine).

### Switching between Docker Desktop and Docker Engine

See [Switching between Docker Desktop and Docker Engine](engine-context.md#switching-between-docker-desktop-and-docker-engine).

## Supported platforms

Docker provides `.deb` and `.rpm` packages for the following Linux distributions
and architectures:

| Platform                                   | x86_64 / amd64 |
| :----------------------------------------- | :------------: |
| [Ubuntu](ubuntu.md)                        |       ✅       |
| [Debian](debian.md)                        |       ✅       |
| [Red Hat Enterprise Linux (RHEL)](rhel.md) |       ✅       |
| [Fedora](fedora.md)                        |       ✅       |

An experimental package is available for [Arch](archlinux.md)-based distributions. Docker has not tested or verified the installation.

Docker supports Docker Desktop on the current and previous LTS releases of the aforementioned distributions, as well as the most recent version.

## System requirements

See [General system requirements](#general-system-requirements).

## General system requirements

Before installing, review [Linux requirements](requirements.md#general-system-requirements), including virtualization, memory, desktop environments, and version-specific file-sharing requirements.

### KVM virtualization support

Follow [KVM virtualization support](requirements.md#kvm-virtualization-support), including [KVM device user permissions](requirements.md#set-up-kvm-device-user-permissions).

#### Set up KVM device user permissions

Follow [Set up KVM device user permissions](requirements.md#set-up-kvm-device-user-permissions).

## Using Docker SDKs with Docker Desktop

See [Using Docker SDKs with Docker Desktop](requirements.md#using-docker-sdks-with-docker-desktop) for the per-user socket and `DOCKER_HOST` requirement.

## Where to go next

- Install Docker Desktop for Linux for your specific Linux distribution:
  - [Install on Ubuntu](ubuntu.md)
  - [Install on Debian](debian.md)
  - [Install on Red Hat Enterprise Linux (RHEL)](rhel.md)
  - [Install on Fedora](fedora.md)
  - [Install on Arch](archlinux.md)
