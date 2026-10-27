---
title: Extensions API Reference
linkTitle: Extensions API
description: Docker extension API reference
keywords: Docker, extensions, sdk, API, reference
aliases: 
 - /desktop/extensions-sdk/dev/api/reference/README/
 - /extensions/extensions-sdk/dev/api/reference/README/
---

## Find an API by task

For client setup and examples, start with [Extension UI API](/manuals/extensions/extensions-sdk/dev/api/overview.md).

| Task | Interfaces |
| --- | --- |
| Access extension components | [Extension](Extension.md), [ExtensionVM](ExtensionVM.md), [ExtensionHost](ExtensionHost.md) |
| List containers and images or run Docker commands | [Docker](Docker.md), [DockerCommand](DockerCommand.md) |
| Run extension commands | [ExtensionCli](ExtensionCli.md), [Exec](Exec.md) |
| Configure command execution | [ExecOptions](ExecOptions.md), [SpawnOptions](SpawnOptions.md), [ExecStreamOptions](ExecStreamOptions.md) |
| Read command output or close a streaming process | [ExecResult](ExecResult.md), [RawExecResult](RawExecResult.md), [ExecProcess](ExecProcess.md) |
| Send backend HTTP requests | [HttpService](HttpService.md), [RequestConfig](RequestConfig.md), [ServiceError](ServiceError.md) |
| Use Dashboard UI APIs | [DesktopUI](DesktopUI.md), [Toast](Toast.md), [Dialog](Dialog.md), [OpenDialogResult](OpenDialogResult.md) |
| Navigate within Docker Desktop | [NavigationIntents](NavigationIntents.md) |
| Open URLs or read host information | [Host](Host.md) |

## Compatibility interfaces

- [DockerDesktopClient](DockerDesktopClient.md)
- [BackendV0](BackendV0.md)
- [ExecResultV0](ExecResultV0.md)
- [RequestConfigV0](RequestConfigV0.md)
