---
description: Install Docker Desktop for Mac to get started. This guide covers system requirements,
  where to download, and instructions on how to install and update.
keywords: docker for mac, install docker macos, docker mac, docker mac install, docker
  install macos, install docker on mac, install docker macbook, docker desktop for
  mac, how to install docker on mac, setup docker on mac
title: Install Docker Desktop on Mac
linkTitle: Mac
weight: 10
aliases:
- /desktop/mac/install/
- /docker-for-mac/install/
- /engine/installation/mac/
- /installation/mac/
- /docker-for-mac/apple-m1/
- /docker-for-mac/apple-silicon/
- /desktop/mac/apple-silicon/
- /desktop/install/mac-install/
- /desktop/install/mac/
---

> **Docker Desktop terms**
>
> Commercial use of Docker Desktop in larger enterprises (more than 250
> employees or more than $10 million USD in annual revenue) requires a [paid
> subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopMacInstall).

This page provides download links, system requirements, and step-by-step installation instructions for Docker Desktop on Mac.

{{< button text="Docker Desktop for Mac with Apple silicon" url="https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64" >}}
{{< button text="Docker Desktop for Mac with Intel chip" url="https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-amd64" >}}

*For checksums, see [Release notes](/manuals/desktop/release-notes.md).*

## System requirements

Review [Docker Desktop for Mac requirements](mac-requirements.md), including the macOS support window, memory, and Apple silicon Rosetta guidance.

## Before you install or update

Review [Prepare to install or update Docker Desktop on Mac](mac-preparation.md) before either installation route.

If you encounter a "Docker.app is damaged" dialog, see [Recover a partial Docker Desktop installation on Mac](mac-reinstall.md).

## Install and run Docker Desktop on Mac

> [!TIP]
>
> See the [FAQs](/manuals/desktop/troubleshoot-and-support/faqs/general.md#how-do-I-run-docker-desktop-without-administrator-privileges) on how to install and run Docker Desktop without needing administrator privileges.

### Install interactively

Follow [Install Docker Desktop on Mac interactively](mac-interactive.md).

### Install from the command line

Follow [Install Docker Desktop on Mac from the command line](mac-command-line.md).

#### Installer flags

See [Mac installer flags](installer-options.md#mac-installer-flags).

##### Installation behavior

See [Mac installation behavior](installer-options.md#mac-installation-behavior), including `--user` and license acceptance.

##### Security and access

See [Mac security and access](installer-options.md#mac-security-and-access). The [`--user` flag](installer-options.md#mac-installation-behavior) is listed under installation behavior.

##### Proxy configuration

See [Mac proxy configuration](installer-options.md#mac-proxy-configuration).

###### Example of specifying PAC file

See the [Mac PAC file example](installer-options.md#mac-pac-file).

###### Example of specifying PAC script

See the [Mac PAC script example](installer-options.md#mac-pac-script).

## Inventory installations

See [Inventory Docker Desktop installations](inventory.md) for endpoint management resources and license reporting.

## Where to go next

- Explore [Docker's subscriptions](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopMacInstall) to see what Docker can offer you.
- [Get started with Docker](/get-started/introduction/_index.md).
- [Explore Docker Desktop](/manuals/desktop/use-desktop/_index.md) and all its features.
- [Troubleshooting](/manuals/desktop/troubleshoot-and-support/troubleshoot/_index.md) describes common problems, workarounds, how
  to run and submit diagnostics, and submit issues.
- [FAQs](/manuals/desktop/troubleshoot-and-support/faqs/general.md) provide answers to frequently asked questions.
- [Release notes](/manuals/desktop/release-notes.md) lists component updates, new features, and improvements associated with Docker Desktop releases.
- [Back up and restore data](/manuals/desktop/settings-and-maintenance/backup-and-restore.md) provides instructions
  on backing up and restoring data related to Docker.
