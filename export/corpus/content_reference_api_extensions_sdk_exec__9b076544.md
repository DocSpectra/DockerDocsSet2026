---
title: "Interface: Exec"
description: Docker extension API reference
keywords: Docker, extensions, sdk, API, reference
aliases: 
 - /desktop/extensions-sdk/dev/api/reference/interfaces/Exec/
 - /extensions/extensions-sdk/dev/api/reference/interfaces/Exec/
---

## Choose a call form

- [Execute a command and wait for its result](#exec)
- [Stream command output](#stream-command-output)

See also [Docker command examples](/manuals/extensions/extensions-sdk/dev/api/docker.md#docker-commands), [backend and host command examples](/manuals/extensions/extensions-sdk/dev/api/backend.md), and the [API task index](_index.md).

## Callable

### Exec

▸ **Exec**(`cmd`, `args`, `options?`): `Promise`<[`ExecResult`](ExecResult.md)\>

Executes a command.

**`Since`**

0.2.0

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cmd` | `string` | The command to execute. |
| `args` | `string`[] | The arguments of the command to execute. |
| `options?` | [`ExecOptions`](ExecOptions.md) | The list of options. |

#### Returns

`Promise`<[`ExecResult`](ExecResult.md)\>

A promise that will resolve once the command finishes.

## Stream command output

### Exec

▸ **Exec**(`cmd`, `args`, `options`): [`ExecProcess`](ExecProcess.md)

Streams the result of a command if `stream` is specified in the `options` parameter.

Specify the `stream` if the output of your command is too long or if you need to stream things indefinitely (for example container logs).

**`Since`**

0.2.2

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cmd` | `string` | The command to execute. |
| `args` | `string`[] | The arguments of the command to execute. |
| `options` | [`SpawnOptions`](SpawnOptions.md) | The list of options. |

#### Returns

[`ExecProcess`](ExecProcess.md)

The spawned process.
