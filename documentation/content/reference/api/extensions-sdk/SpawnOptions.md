---
title: "Interface: SpawnOptions"
description: Docker extension API reference
keywords: Docker, extensions, sdk, API, reference
aliases:
 - /desktop/extensions-sdk/dev/api/reference/interfaces/SpawnOptions/
 - /extensions/extensions-sdk/dev/api/reference/interfaces/SpawnOptions/
---

For command contexts, results, streaming, and command chaining limits, see [Extension service and command execution](/manuals/extensions/extensions-sdk/dev/api/backend.md).

**`Since`**

0.3.0

## Hierarchy

- [`ExecOptions`](ExecOptions.md)

  ↳ **`SpawnOptions`**

## Properties

### cwd

• `Optional` **cwd**: `string`

#### Inherited from

[ExecOptions](ExecOptions.md).[cwd](ExecOptions.md#cwd)

___

### env

• `Optional` **env**: `ProcessEnv`

#### Inherited from

[ExecOptions](ExecOptions.md).[env](ExecOptions.md#env)

___

### stream

• **stream**: [`ExecStreamOptions`](ExecStreamOptions.md)
