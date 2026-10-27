---
description: Instructions for installing Docker Desktop on Fedora
keywords: fedora, rpm, update install, uninstall, upgrade, update, linux, desktop,
  docker desktop, docker desktop for linux, dd4l
title: Install Docker Desktop on Fedora
linkTitle: Fedora
weight: 30
toc_max: 4
aliases:
- /desktop/linux/install/fedora/
- /desktop/install/fedora/
- /desktop/install/linux/fedora/
---

> **Docker Desktop terms**
>
> Commercial use of Docker Desktop in larger enterprises (more than 250
> employees OR more than $10 million USD in annual revenue) requires a [paid
> subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopFedoraInstall).

This page contains information on how to install, launch and upgrade Docker Desktop on a Fedora distribution.

## Prerequisites

Review the [Docker Desktop license agreement](/manuals/subscription/desktop-license.md) and [Docker Desktop/Engine coexistence and contexts](engine-context.md).

To install Docker Desktop successfully, you must:

- Meet the [general system requirements](requirements.md#general-system-requirements).
- Have a 64-bit version of Fedora 42 or Fedora 43.
- For a GNOME desktop environment you must install AppIndicator and KStatusNotifierItem [GNOME extensions](https://extensions.gnome.org/extension/615/appindicator-support/).
- If you're not using GNOME, you must install `gnome-terminal` to enable terminal access from Docker Desktop:

   ```console
   $ sudo dnf install gnome-terminal
   ```

## Install Docker Desktop

To install Docker Desktop on Fedora:

1. Set up [Docker's package repository](/manuals/engine/install/fedora.md#set-up-the-repository).

2. Download the latest [RPM package](https://desktop.docker.com/linux/main/amd64/docker-desktop-x86_64.rpm?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64). For checksums, see the [Release notes](/manuals/desktop/release-notes.md).

3. Install the package with dnf as follows:

   ```console
   $ sudo dnf install ./docker-desktop-x86_64.rpm
   ```

   By default, Docker Desktop is installed at `/opt/docker-desktop`.

See [Linux DEB and RPM post-install setup](package-installation.md) for the automatic capability, DNS, and Docker CLI symlink changes.

## Launch Docker Desktop

Follow [Start, verify, and stop Docker Desktop on Linux](/manuals/desktop/setup/linux-start.md) for launch and agreement acceptance, binary version checks, starting on sign in, and stopping Docker Desktop.

## Upgrade Docker Desktop

Once a new version for Docker Desktop is released, the Docker UI shows a notification.
You need to first remove the previous version and then download the new package each time you want to upgrade Docker Desktop. Run:

```console
$ sudo dnf remove docker-desktop
$ sudo dnf install ./docker-desktop-x86_64.rpm
```

## Next steps

- Explore [Docker's subscriptions](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopFedoraInstall) to see what Docker can offer you.
- Take a look at the [Docker workshop](/get-started/workshop/_index.md) to learn how to build an image and run it as a containerized application.
- [Explore Docker Desktop](/manuals/desktop/use-desktop/_index.md) and all its features.
- [Troubleshooting](/manuals/desktop/troubleshoot-and-support/troubleshoot/_index.md) describes common problems, workarounds, how to run and submit diagnostics, and submit issues.
- [FAQs](/manuals/desktop/troubleshoot-and-support/faqs/general.md) provide answers to frequently asked questions.
- [Release notes](/manuals/desktop/release-notes.md) lists component updates, new features, and improvements associated with Docker Desktop releases.
- [Back up and restore data](/manuals/desktop/settings-and-maintenance/backup-and-restore.md) provides instructions
  on backing up and restoring data related to Docker.
