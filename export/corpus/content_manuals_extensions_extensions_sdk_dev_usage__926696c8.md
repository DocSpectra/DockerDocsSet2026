---
title: CLI reference
description: Docker extension CLI
keywords: Docker, extensions, sdk, CLI
aliases:
 - /desktop/extensions-sdk/dev/cli/usage/
 - /desktop/extensions-sdk/dev/usage/
weight: 30
---

The Extensions CLI is an extension development tool that is used to manage Docker extensions. Actions include install, list, remove, and validate extensions.

## Turn extensions on or off

- `docker extension enable` turns on Docker extensions.
- `docker extension disable` turns off Docker extensions.

## Create and develop an extension

- `docker extension init` creates a new Docker extension.
- `docker extension dev` commands for extension development.
- `docker extension validate` validates the extension metadata file against the JSON schema.

For development steps, see [Quickstart](../quickstart.md), [Test and debug](test-debug.md), and [Validate your extension](../extensions/validate.md).

## Manage installed extensions

- `docker extension install` installs a Docker extension with the specified image.
- `docker extension ls` list installed Docker extensions.
- `docker extension rm` removes a Docker extension.
- `docker extension update` removes and re-installs a Docker extension.

See also [Marketplace extensions](../../marketplace.md) and [non-Marketplace extensions](../../non-marketplace.md).
