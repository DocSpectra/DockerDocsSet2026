---
description: Extensions
keywords: Docker Extensions, Docker Desktop, Linux, Mac, Windows,
title: Install non-marketplace extensions
weight: 20
aliases:
 - /desktop/extensions/non-marketplace/
---

## Install an extension not available in the Marketplace

> [!WARNING]
>
> Extensions installed outside the Marketplace have not gone through Docker's review process. Like all Docker extensions, they run with host-level privileges. They can install binaries, access Docker Engine, invoke commands, and access files on your machine. Install only if you trust the publisher and have verified the source.

The Extensions Marketplace is the trusted and official place to install extensions from within Docker Desktop. These extensions have gone through a review process by Docker. However, other extensions can also be installed in Docker Desktop if you trust the extension author.

Given the nature of a Docker Extension (i.e. a Docker image) you can find other places where users have their extension's source code published. For example on GitHub, GitLab or even hosted in image registries like DockerHub or GHCR.
You can install an extension that has been developed by the community or internally at your company from a teammate. You are not limited to installing extensions just from the Marketplace.

> [!NOTE]
>
> Ensure the option **Allow only extensions distributed through the Docker Marketplace** is disabled. Otherwise, this prevents any extension not listed in the Marketplace, via the Extension SDK tools from, being installed.
> You can change this option in **Settings**. See [Allow extensions not available in the Marketplace](settings.md#turn-on-or-turn-off-extensions-not-available-in-the-marketplace). 

To install an extension which is not present in the Marketplace, you can use the Extensions CLI that is bundled with Docker Desktop.

In a terminal, type `docker extension install IMAGE[:TAG]` to install an extension by its image reference and optionally a tag. Use the `-f` or `--force` flag to avoid interactive confirmation.

Go to the Docker Desktop Dashboard to see the new extension installed.

## Manage installed extensions

See [List installed extensions](manage-extensions.md#list-installed-extensions-with-the-cli) and [Update and uninstall non-marketplace extensions](manage-extensions.md#update-and-uninstall-non-marketplace-extensions-with-the-cli).
