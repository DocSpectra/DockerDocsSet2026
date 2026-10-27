---
title: "Interface: RawExecResult"
description: Docker extension API reference
keywords: Docker, extensions, sdk, API, reference
aliases:
 - /desktop/extensions-sdk/dev/api/reference/interfaces/RawExecResult/
 - /extensions/extensions-sdk/dev/api/reference/interfaces/RawExecResult/
---

For command contexts, results, streaming, and command chaining limits, see [Extension service and command execution](/manuals/extensions/extensions-sdk/dev/api/backend.md).

**`Since`**

0.2.0

## Hierarchy

- **`RawExecResult`**

  ↳ `ExecResult`

## Properties

### cmd

• `Optional` `Readonly` **cmd**: `string`

___

### killed

• `Optional` `Readonly` **killed**: `boolean`

___

### signal

• `Optional` `Readonly` **signal**: `string`

___

### code

• `Optional` `Readonly` **code**: `number`

___

### stdout

• `Readonly` **stdout**: `string`

___

### stderr

• `Readonly` **stderr**: `string`
