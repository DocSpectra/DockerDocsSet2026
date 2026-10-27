---
title: Building
weight: 20
---

## Choose a build task

| Task | Guide | Sections to consult |
| --- | --- | --- |
| Separate build stages | [Multi-stage builds](./multi-stage.md) | [Select a target stage](./multi-stage.md#stop-at-a-specific-build-stage), [builder differences](./multi-stage.md#differences-between-legacy-builder-and-buildkit) |
| Configure build values | [Build variables](./variables.md) | [ARG and ENV](./variables.md#similarities-and-differences), [scope](./variables.md#scoping) |
| Pass credentials to a build | [Build secrets](./secrets.md) | [Secret types](./secrets.md#types-of-build-secrets), [pass and consume secrets](./secrets.md#using-build-secrets) |
| Build for multiple platforms | [Multi-platform builds](./multi-platform.md) | [Prerequisites](./multi-platform.md#prerequisites), [strategies](./multi-platform.md#strategies), [examples](./multi-platform.md#examples) |
| Export executable files | [Export binaries](./export.md) | [Single build](./export.md#export-binaries-from-a-build), [multiple platforms](./export.md#exporting-multi-platform-builds) |
| Use devices during a build | [Container Device Interface](./cdi.md) | [Setup](./cdi.md#getting-started), [GPU builder](./cdi.md#set-up-a-container-builder-with-gpu-support) |
| Review a Dockerfile | [Building best practices](./best-practices.md) | [Base images](./best-practices.md#choose-the-right-base-image), [instructions](./best-practices.md#dockerfile-instructions) |
| Create a base image | [Base images](./base-images.md) | [Scratch](./base-images.md#create-a-minimal-base-image-using-scratch), [tar](./base-images.md#create-a-full-image-using-tar) |

## Related tasks

- [Choose build inputs](../concepts/context.md).
- [Check build configuration](../checks.md).
- [Optimize cache usage](../cache/optimize.md).
- [Choose an exporter](../exporters/_index.md).
- Follow the [Building Container Images lab](/guides/lab-building-images.md).
