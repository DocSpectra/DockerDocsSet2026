---
description:
  Find the latest recommended version of the Docker Compose file format
  for defining multi-container applications.
keywords:
  docker compose file, docker compose yml, docker compose reference, docker
  compose cmd, docker compose user, docker compose image, yaml spec, docker compose
  syntax, yaml specification, docker compose specification
title: Compose file reference
toc_max: 4
toc_min: 1
grid:
  - title: Version and name top-level element
    description: Understand version and name attributes for Compose.
    icon: text_snippet
    link: /reference/compose-file/version-and-name/
  - title: Services top-level element
    description: Explore all services attributes for Compose.
    icon: construction
    link: /reference/compose-file/services/
  - title: Networks top-level element
    description: Find all networks attributes for Compose.
    icon: lan
    link: /reference/compose-file/networks/
  - title: Volumes top-level element
    description: Explore all volumes attributes for Compose.
    icon: database
    link: /reference/compose-file/volumes/
  - title: Configs top-level element
    description: Find out about configs in Compose.
    icon: settings
    link: /reference/compose-file/configs/
  - title: Secrets top-level element
    description: Learn about secrets in Compose.
    icon: lock
    link: /reference/compose-file/secrets/
aliases:
  - /compose/yaml/
  - /compose/compose-file/compose-file-v1/
  - /compose/compose-file/
  - /compose/reference/overview/
---

> **New to Docker Compose?**
>
> Find more information about the [key features and use cases of Docker Compose](/manuals/compose/intro/features-uses.md) or [try the quickstart guide](/manuals/compose/gettingstarted.md).

The Compose Specification is the latest and recommended version of the Compose file format. It helps you define a [Compose file](/manuals/compose/intro/compose-application-model.md) which is used to configure your Docker application’s services, networks, volumes, and more.

Legacy versions 2.x and 3.x of the Compose file format were merged into the Compose Specification. It is implemented in versions 1.27.0 and above (also known as Compose v2) of the Docker Compose CLI.

The Compose Specification on Docker Docs is the Docker Compose implementation. If you wish to implement your own version of the Compose Specification, see the [Compose Specification repository](https://github.com/compose-spec/compose-spec).

## Find a task

| Task | Reference |
| --- | --- |
| Define services and their runtime settings | [Services](services.md#find-a-service-setting) |
| Set a project name or check the obsolete version field | [Version and name](version-and-name.md) |
| Build and publish service images | [Build](build.md#find-a-build-setting) |
| Configure deployment, resources, and updates | [Deploy](deploy.md#find-a-deployment-setting) |
| Update services while developing | [Develop and Watch](develop.md#find-a-watch-setting) |
| Connect services and configure networks | [Networks](networks.md) and [service network attachments](services.md#networks) |
| Declare persistent volumes and configure mounts | [Volumes](volumes.md) and [service mounts](services.md#volumes) |
| Provide configuration files to services | [Configs](configs.md) and [service access](services.md#configs) |
| Provide sensitive data to services or builds | [Secrets](secrets.md), [service access](services.md#secrets), and [build access](build.md#secrets) |
| Declare AI models and connect services to them | [Models](models.md) and [service model references](services.md#models) |
| Reuse configuration within a file | [Fragments](fragments.md) and [extensions](extension.md) |
| Substitute variables | [Interpolation](interpolation.md) |
| Combine or override Compose files | [Merge](merge.md) and [include](include.md) |
| Select services for different uses | [Profiles](profiles.md) |
| Find the older file formats | [Legacy versions](legacy-versions.md) |

## Find prerequisites and caveats

- Images: [build and pull precedence](build.md#using-build-and-image), [publishing requirements](build.md#publishing-built-images), and [target platforms](build.md#platforms).
- Startup: [dependency conditions](services.md#depends_on), [healthchecks](services.md#healthcheck), and [profile dependencies](profiles.md#references-and-dependencies).
- Networks and ports: [network mode conflicts](services.md#network_mode), [port publishing warnings](services.md#ports), and [external networks](networks.md#external).
- Files and data: [external configs](configs.md#external-config-restrictions), [secret permissions and file-source limitations](services.md#secrets), and [mount path caveats](services.md#volumes).
- Development: [Develop availability](develop.md), [Watch actions and their version requirements](develop.md#action), and [watch pattern quoting](develop.md#include).

## Browse top-level elements

Use the following links to navigate key sections of the Compose Specification.

> [!TIP]
>
> Want a better editing experience for Compose files in VS Code?
> Check out the [Docker DX](https://marketplace.visualstudio.com/items?itemName=docker.docker) extension for linting, code navigation, and vulnerability scanning.

{{< grid >}}
