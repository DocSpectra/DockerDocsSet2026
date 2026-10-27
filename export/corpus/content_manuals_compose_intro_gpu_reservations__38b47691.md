---
title: GPU reservations in Compose
description: Device reservation properties, requirements, and mutually exclusive options.
---

## Prerequisites

Compose services can define GPU device reservations if the Docker host contains such devices and the Docker Daemon is set accordingly. For this, make sure you install the [prerequisites](/manuals/engine/containers/resource_constraints.md#gpu) if you haven't already done so.

## Device properties

GPUs are referenced in a `compose.yaml` file using the [device](/reference/compose-file/deploy.md#devices) attribute from the Compose Deploy specification, within your services that need them.

This provides more granular control over a GPU reservation as custom values can be set for the following device properties: 

- `capabilities`. This value is specified as a list of strings. For example, `capabilities: [gpu]`. You must set this field in the Compose file. Otherwise, it returns an error on service deployment.
- `count`. Specified as an integer or the value `all`, represents the number of GPU devices that should be reserved (providing the host holds that number of GPUs). If `count` is set to `all` or not specified, all GPUs available on the host are used by default.
- `device_ids`. This value, specified as a list of strings, represents GPU device IDs from the host. You can find the device ID in the output of `nvidia-smi` on the host. If no `device_ids` are set, all GPUs available on the host are used by default.
- `driver`. Specified as a string, for example `driver: 'nvidia'`
- `options`. Key-value pairs representing driver specific options.


> [!IMPORTANT]
>
> You must set the `capabilities` field. Otherwise, it returns an error on service deployment.

> [!NOTE]
>
> `count` and `device_ids` are mutually exclusive. You must only define one field at a time.

For more information on these properties, see the [Compose Deploy Specification](/reference/compose-file/deploy.md#devices).
