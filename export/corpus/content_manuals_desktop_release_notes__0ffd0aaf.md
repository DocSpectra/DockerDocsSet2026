---
description: Find the Docker Desktop release notes for Mac, Linux, and Windows.
keywords: Docker desktop, release notes, linux, mac, windows
title: Docker Desktop release notes
linkTitle: Release notes
tags: [Release notes]
toc_max: 2
aliases:
- /docker-for-mac/release-notes/
- /docker-for-mac/edge-release-notes/
- /desktop/mac/release-notes/
- /docker-for-windows/edge-release-notes/
- /docker-for-windows/release-notes/
- /desktop/windows/release-notes/
- /desktop/linux/release-notes/
- /mackit/release-notes/
weight: 220
---
<!-- vale off -->

This page contains information about the new features, improvements, known issues, and bug fixes in Docker Desktop releases.

Before updating, see [release availability and update prerequisites](release-availability.md).

## Find an earlier release

- [Docker Desktop 4.60-4.69](previous-versions/4.60-4.69.md)
- [Docker Desktop 4.50-4.59](previous-versions/4.50-4.59.md)
- [Docker Desktop 4.40-4.49](previous-versions/4.40-4.49.md)
- [Docker Desktop 4.30-4.39](previous-versions/4.30-4.39.md)
- [Docker Desktop 4.20-4.29](previous-versions/4.20-4.29.md)
- [Docker Desktop 4.10-4.19](previous-versions/4.10-4.19.md)
- [Docker Desktop 4.0-4.9](previous-versions/4.0-4.9.md)
- [Mac and Windows releases before 4.x](previous-versions/_index.md)

## 4.71.0

{{< release-date date="2026-04-27" >}}

{{< desktop-install-v2 all=true win_arm_release="Early Access" version="4.71.0" build_path="/225177/" >}}

> [!IMPORTANT]
>
> Support for RHEL 8 has ended. Installing Docker Desktop will require RHEL 9 or RHEL 10 in the next release.

### Updates

- [Docker Model Runner v1.1.36](https://github.com/docker/model-runner/releases/tag/v1.1.36)
- [containerd to v2.2.3](https://github.com/containerd/containerd/releases/tag/v2.2.3)
- [Runc v1.3.5](https://github.com/opencontainers/runc/releases/tag/v1.3.5)
- [Docker Compose v5.1.3](https://github.com/docker/compose/releases/tag/v5.1.3)
- [Docker Agent v1.44.0](https://github.com/docker/docker-agent/releases/tag/v1.44.0)
- [Docker Engine v29.4.1](/manuals/engine/release-notes/29.md#2941)

### Bug fixes and enhancements

#### For all platforms

- Docker Model Runner is now disabled by default and must be explicitly enabled in **Settings**. When enabled, TCP host-side support is automatically active.
- Fixed an issue where downloading a Docker Desktop update would fail without a clear error if the disk had insufficient free space.
- Fixed an issue where Docker Scout tag recommendations, when inspecting an image, failed when the base image digest or repository name was empty.
- Added a **Switch to local Docker context** button on the sign-in screen, allowing users in a cloud context to switch back to their local context without signing in.
- Added a dedicated **Stopped** status screen for the cloud engine so users see a clear stopped state instead of an error screen when transitioning away from Docker Offload.

#### For Mac

- Fixed an issue where error tracking would temporarily continue sending session data directly after a user disabled analytics. Fixes [docker/for-mac#7768](https://github.com/docker/for-mac/issues/7768).

#### For Windows

- Fixed a critical issue where Docker Desktop Dashboard failed to open with `ERR_FAILED` errors caused by process hardening policies conflicting with Chromium.
- Fixed a bug where Kubernetes could fail to start on WSL 2 when `HTTP_PROXY` environment variables are set in WSL 2 itself.
- Fixed a bug in Enhanced Container Isolation (ECI) that was causing loss of container `rootfs` persistence across Docker Desktop restarts, when using WSL.

## 4.70.0

{{< release-date date="2026-04-20" >}}

{{< desktop-install-v2 all=true win_arm_release="Early Access" version="4.70.0" build_path="/224270/" >}}

### New

- Added a CLI hint that surfaces the **Logs** view when running `logs`, `compose logs`, `compose attach`, or `compose up` commands, giving you quick access to logs across all running containers. Available with the **Logs** (Beta) feature enabled.

### Updates

- [Docker Compose v5.1.2](https://github.com/docker/compose/releases/tag/v5.1.2)
- [Docker Engine v29.4.0](/manuals/engine/release-notes/29.md#2940)
- [Docker Agent v1.43.0](https://github.com/docker/docker-agent/releases/tag/v1.43.0)
- [Docker Model Runner v1.1.33](https://github.com/docker/model-runner/releases/tag/v1.1.33)
- [Docker Scout CLI v1.20.4](https://github.com/docker/scout-cli/releases/tag/v1.20.4)

### Bug fixes and enhancements

#### For all platforms

- Fixed a bug where `docker login` could fail silently in CI environments due to slow Docker Hub responses causing credential store update timeouts.
- Fixed an issue where disabling Beta features also disabled Docker Model Runner.
- Fixed `docker desktop start` causing the Docker AI agent API daemon to fail due to an inherited CLI plugin environment variable.

#### For Mac

- Fixed a crash loop where Docker Desktop repeatedly failed to start with exit status `42` after an update due to a corrupted `DockerAppLaunchPath` setting.
- Fixed an issue where a failed update could leave Docker Desktop in a broken state. The installer now automatically reverts to the previous version and shows a clear error message.
- Fixed a bug where stopping one container could disrupt active Unix socket forwards belonging to other running containers.

#### For Windows

- Fixed an issue where a failed update could leave Docker Desktop in a broken state. The installer now automatically reverts to the previous version and shows a clear error message.
- Fixed a bug where a failed switch to Windows containers could leave Docker Desktop in a broken state, requiring a restart.
- Fixed an issue where Docker Desktop failed to launch for users with `DEVHOME` set in their environment.
- Temporarily rolled back process hardening that caused Electron crashes on Windows. Fixes [docker/desktop-feedback#245](https://github.com/docker/desktop-feedback/issues/245).

## 4.69.0

See [Docker Desktop 4.69.0 release notes](previous-versions/4.60-4.69.md#4690).

## 4.68.0

See [Docker Desktop 4.68.0 release notes](previous-versions/4.60-4.69.md#4680).

## 4.67.0

See [Docker Desktop 4.67.0 release notes](previous-versions/4.60-4.69.md#4670).

## 4.66.1

See [Docker Desktop 4.66.1 release notes](previous-versions/4.60-4.69.md#4661).

## 4.66.0

See [Docker Desktop 4.66.0 release notes](previous-versions/4.60-4.69.md#4660).

## 4.65.0

See [Docker Desktop 4.65.0 release notes](previous-versions/4.60-4.69.md#4650).

## 4.64.0

See [Docker Desktop 4.64.0 release notes](previous-versions/4.60-4.69.md#4640).

## 4.63.0

See [Docker Desktop 4.63.0 release notes](previous-versions/4.60-4.69.md#4630).

## 4.62.0

See [Docker Desktop 4.62.0 release notes](previous-versions/4.60-4.69.md#4620).

## 4.61.0

See [Docker Desktop 4.61.0 release notes](previous-versions/4.60-4.69.md#4610).

## 4.60.1

See [Docker Desktop 4.60.1 release notes](previous-versions/4.60-4.69.md#4601).

## 4.60.0

See [Docker Desktop 4.60.0 release notes](previous-versions/4.60-4.69.md#4600).

## 4.59.1

See [Docker Desktop 4.59.1 release notes](previous-versions/4.50-4.59.md#4591).

## 4.59.0

See [Docker Desktop 4.59.0 release notes](previous-versions/4.50-4.59.md#4590).

## 4.58.1

See [Docker Desktop 4.58.1 release notes](previous-versions/4.50-4.59.md#4581).

## 4.58.0

See [Docker Desktop 4.58.0 release notes](previous-versions/4.50-4.59.md#4580).

## 4.57.0

See [Docker Desktop 4.57.0 release notes](previous-versions/4.50-4.59.md#4570).

## 4.56.0

See [Docker Desktop 4.56.0 release notes](previous-versions/4.50-4.59.md#4560).

## 4.55.0

See [Docker Desktop 4.55.0 release notes](previous-versions/4.50-4.59.md#4550).

## 4.54.0

See [Docker Desktop 4.54.0 release notes](previous-versions/4.50-4.59.md#4540).

## 4.53.0

See [Docker Desktop 4.53.0 release notes](previous-versions/4.50-4.59.md#4530).

## 4.52.0

See [Docker Desktop 4.52.0 release notes](previous-versions/4.50-4.59.md#4520).

## 4.51.0

See [Docker Desktop 4.51.0 release notes](previous-versions/4.50-4.59.md#4510).

## 4.50.0

See [Docker Desktop 4.50.0 release notes](previous-versions/4.50-4.59.md#4500).

## 4.49.0

See [Docker Desktop 4.49.0 release notes](previous-versions/4.40-4.49.md#4490).

## 4.48.0

See [Docker Desktop 4.48.0 release notes](previous-versions/4.40-4.49.md#4480).

## 4.47.0

See [Docker Desktop 4.47.0 release notes](previous-versions/4.40-4.49.md#4470).

## 4.46.0

See [Docker Desktop 4.46.0 release notes](previous-versions/4.40-4.49.md#4460).

## 4.45.0

See [Docker Desktop 4.45.0 release notes](previous-versions/4.40-4.49.md#4450).

## 4.44.3

See [Docker Desktop 4.44.3 release notes](previous-versions/4.40-4.49.md#4443).

## 4.44.2

See [Docker Desktop 4.44.2 release notes](previous-versions/4.40-4.49.md#4442).

## 4.44.1

See [Docker Desktop 4.44.1 release notes](previous-versions/4.40-4.49.md#4441).

## 4.44.0

See [Docker Desktop 4.44.0 release notes](previous-versions/4.40-4.49.md#4440).

## 4.43.2

See [Docker Desktop 4.43.2 release notes](previous-versions/4.40-4.49.md#4432).

## 4.43.1

See [Docker Desktop 4.43.1 release notes](previous-versions/4.40-4.49.md#4431).

## 4.43.0

See [Docker Desktop 4.43.0 release notes](previous-versions/4.40-4.49.md#4430).

## 4.42.1

See [Docker Desktop 4.42.1 release notes](previous-versions/4.40-4.49.md#4421).

## 4.42.0

See [Docker Desktop 4.42.0 release notes](previous-versions/4.40-4.49.md#4420).

## 4.41.2

See [Docker Desktop 4.41.2 release notes](previous-versions/4.40-4.49.md#4412).

## 4.41.1

See [Docker Desktop 4.41.1 release notes](previous-versions/4.40-4.49.md#4411).

## 4.41.0

See [Docker Desktop 4.41.0 release notes](previous-versions/4.40-4.49.md#4410).

## 4.40.0

See [Docker Desktop 4.40.0 release notes](previous-versions/4.40-4.49.md#4400).

## 4.39.0

See [Docker Desktop 4.39.0 release notes](previous-versions/4.30-4.39.md#4390).

## 4.38.0

See [Docker Desktop 4.38.0 release notes](previous-versions/4.30-4.39.md#4380).

## 4.37.2

See [Docker Desktop 4.37.2 release notes](previous-versions/4.30-4.39.md#4372).

## 4.37.1

See [Docker Desktop 4.37.1 release notes](previous-versions/4.30-4.39.md#4371).

## 4.37.0

See [Docker Desktop 4.37.0 release notes](previous-versions/4.30-4.39.md#4370).

## 4.36.1

See [Docker Desktop 4.36.1 release notes](previous-versions/4.30-4.39.md#4361).

## 4.36.0

See [Docker Desktop 4.36.0 release notes](previous-versions/4.30-4.39.md#4360).

## 4.35.2

See [Docker Desktop 4.35.2 release notes](previous-versions/4.30-4.39.md#4352).

## 4.35.1

See [Docker Desktop 4.35.1 release notes](previous-versions/4.30-4.39.md#4351).

## 4.35.0

See [Docker Desktop 4.35.0 release notes](previous-versions/4.30-4.39.md#4350).

## 4.34.4

See [Docker Desktop 4.34.4 release notes](previous-versions/4.30-4.39.md#4344).

## 4.34.3

See [Docker Desktop 4.34.3 release notes](previous-versions/4.30-4.39.md#4343).

## 4.34.2

See [Docker Desktop 4.34.2 release notes](previous-versions/4.30-4.39.md#4342).

## 4.34.1

See [Docker Desktop 4.34.1 release notes](previous-versions/4.30-4.39.md#4341).

## 4.34.0

See [Docker Desktop 4.34.0 release notes](previous-versions/4.30-4.39.md#4340).

## 4.33.2

See [Docker Desktop 4.33.2 release notes](previous-versions/4.30-4.39.md#4332).

## 4.33.1

See [Docker Desktop 4.33.1 release notes](previous-versions/4.30-4.39.md#4331).

## 4.33.0

See [Docker Desktop 4.33.0 release notes](previous-versions/4.30-4.39.md#4330).

## 4.32.1

See [Docker Desktop 4.32.1 release notes](previous-versions/4.30-4.39.md#4321).

## 4.32.0

See [Docker Desktop 4.32.0 release notes](previous-versions/4.30-4.39.md#4320).

## 4.31.1

See [Docker Desktop 4.31.1 release notes](previous-versions/4.30-4.39.md#4311).

## 4.31.0

See [Docker Desktop 4.31.0 release notes](previous-versions/4.30-4.39.md#4310).

## 4.30.0

See [Docker Desktop 4.30.0 release notes](previous-versions/4.30-4.39.md#4300).

## 4.29.0

See [Docker Desktop 4.29.0 release notes](previous-versions/4.20-4.29.md#4290).

## 4.28.0

See [Docker Desktop 4.28.0 release notes](previous-versions/4.20-4.29.md#4280).

## 4.27.2

See [Docker Desktop 4.27.2 release notes](previous-versions/4.20-4.29.md#4272).

## 4.27.1

See [Docker Desktop 4.27.1 release notes](previous-versions/4.20-4.29.md#4271).

## 4.27.0

See [Docker Desktop 4.27.0 release notes](previous-versions/4.20-4.29.md#4270).

## 4.26.1

See [Docker Desktop 4.26.1 release notes](previous-versions/4.20-4.29.md#4261).

## 4.26.0

See [Docker Desktop 4.26.0 release notes](previous-versions/4.20-4.29.md#4260).

## 4.25.2

See [Docker Desktop 4.25.2 release notes](previous-versions/4.20-4.29.md#4252).

## 4.25.1

See [Docker Desktop 4.25.1 release notes](previous-versions/4.20-4.29.md#4251).

## 4.25.0

See [Docker Desktop 4.25.0 release notes](previous-versions/4.20-4.29.md#4250).

## 4.24.2

See [Docker Desktop 4.24.2 release notes](previous-versions/4.20-4.29.md#4242).

## 4.24.1

See [Docker Desktop 4.24.1 release notes](previous-versions/4.20-4.29.md#4241).

## 4.24.0

See [Docker Desktop 4.24.0 release notes](previous-versions/4.20-4.29.md#4240).

## 4.23.0

See [Docker Desktop 4.23.0 release notes](previous-versions/4.20-4.29.md#4230).

## 4.22.1

See [Docker Desktop 4.22.1 release notes](previous-versions/4.20-4.29.md#4221).

## 4.22.0

See [Docker Desktop 4.22.0 release notes](previous-versions/4.20-4.29.md#4220).

## 4.21.1

See [Docker Desktop 4.21.1 release notes](previous-versions/4.20-4.29.md#4211).

## 4.21.0

See [Docker Desktop 4.21.0 release notes](previous-versions/4.20-4.29.md#4210).

## 4.20.1

See [Docker Desktop 4.20.1 release notes](previous-versions/4.20-4.29.md#4201).

## 4.20.0

See [Docker Desktop 4.20.0 release notes](previous-versions/4.20-4.29.md#4200).

## 4.19.0

See [Docker Desktop 4.19.0 release notes](previous-versions/4.10-4.19.md#4190).

## 4.18.0

See [Docker Desktop 4.18.0 release notes](previous-versions/4.10-4.19.md#4180).

## 4.17.1

See [Docker Desktop 4.17.1 release notes](previous-versions/4.10-4.19.md#4171).

## 4.17.0

See [Docker Desktop 4.17.0 release notes](previous-versions/4.10-4.19.md#4170).

## 4.16.3

See [Docker Desktop 4.16.3 release notes](previous-versions/4.10-4.19.md#4163).

## 4.16.2

See [Docker Desktop 4.16.2 release notes](previous-versions/4.10-4.19.md#4162).

## 4.16.1

See [Docker Desktop 4.16.1 release notes](previous-versions/4.10-4.19.md#4161).

## 4.16.0

See [Docker Desktop 4.16.0 release notes](previous-versions/4.10-4.19.md#4160).

## 4.15.0

See [Docker Desktop 4.15.0 release notes](previous-versions/4.10-4.19.md#4150).

## 4.14.1

See [Docker Desktop 4.14.1 release notes](previous-versions/4.10-4.19.md#4141).

## 4.14.0

See [Docker Desktop 4.14.0 release notes](previous-versions/4.10-4.19.md#4140).

## 4.13.1

See [Docker Desktop 4.13.1 release notes](previous-versions/4.10-4.19.md#4131).

## 4.13.0

See [Docker Desktop 4.13.0 release notes](previous-versions/4.10-4.19.md#4130).

## 4.12.0

See [Docker Desktop 4.12.0 release notes](previous-versions/4.10-4.19.md#4120).

## 4.11.1

See [Docker Desktop 4.11.1 release notes](previous-versions/4.10-4.19.md#4111).

## 4.11.0

See [Docker Desktop 4.11.0 release notes](previous-versions/4.10-4.19.md#4110).

## 4.10.1

See [Docker Desktop 4.10.1 release notes](previous-versions/4.10-4.19.md#4101).

## 4.10.0

See [Docker Desktop 4.10.0 release notes](previous-versions/4.10-4.19.md#4100).

## 4.9.1

See [Docker Desktop 4.9.1 release notes](previous-versions/4.0-4.9.md#491).

## 4.9.0

See [Docker Desktop 4.9.0 release notes](previous-versions/4.0-4.9.md#490).

## 4.8.2

See [Docker Desktop 4.8.2 release notes](previous-versions/4.0-4.9.md#482).

## 4.8.1

See [Docker Desktop 4.8.1 release notes](previous-versions/4.0-4.9.md#481).

## 4.8.0

See [Docker Desktop 4.8.0 release notes](previous-versions/4.0-4.9.md#480).

## 4.7.1

See [Docker Desktop 4.7.1 release notes](previous-versions/4.0-4.9.md#471).

## 4.7.0

See [Docker Desktop 4.7.0 release notes](previous-versions/4.0-4.9.md#470).

## 4.6.1

See [Docker Desktop 4.6.1 release notes](previous-versions/4.0-4.9.md#461).

## 4.6.0

See [Docker Desktop 4.6.0 release notes](previous-versions/4.0-4.9.md#460).

## 4.5.1

See [Docker Desktop 4.5.1 release notes](previous-versions/4.0-4.9.md#451).

## 4.5.0

See [Docker Desktop 4.5.0 release notes](previous-versions/4.0-4.9.md#450).

## 4.4.4

See [Docker Desktop 4.4.4 release notes](previous-versions/4.0-4.9.md#444).

## 4.4.3

See [Docker Desktop 4.4.3 release notes](previous-versions/4.0-4.9.md#443).

## 4.4.2

See [Docker Desktop 4.4.2 release notes](previous-versions/4.0-4.9.md#442).

## 4.3.2

See [Docker Desktop 4.3.2 release notes](previous-versions/4.0-4.9.md#432).

## 4.3.1

See [Docker Desktop 4.3.1 release notes](previous-versions/4.0-4.9.md#431).

## 4.3.0

See [Docker Desktop 4.3.0 release notes](previous-versions/4.0-4.9.md#430).

## 4.2.0

See [Docker Desktop 4.2.0 release notes](previous-versions/4.0-4.9.md#420).

## 4.1.1

See [Docker Desktop 4.1.1 release notes](previous-versions/4.0-4.9.md#411).

## 4.1.0

See [Docker Desktop 4.1.0 release notes](previous-versions/4.0-4.9.md#410).

## 4.0.1

See [Docker Desktop 4.0.1 release notes](previous-versions/4.0-4.9.md#401).

## 4.0.0

See [Docker Desktop 4.0.0 release notes](previous-versions/4.0-4.9.md#400).

