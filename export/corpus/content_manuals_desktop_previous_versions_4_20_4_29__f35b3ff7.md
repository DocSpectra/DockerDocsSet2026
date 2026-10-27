---
title: Docker Desktop 4.20-4.29 release notes
linkTitle: Desktop 4.20-4.29
description: Docker Desktop release notes for versions 4.20-4.29.
toc_max: 2
sitemap: false
---
<!-- vale off -->

Before updating, see [release availability and update prerequisites](/manuals/desktop/release-availability.md).

## Find a release

- [4.29.0](#4290)
- [4.28.0](#4280)
- [4.27.2](#4272)
- [4.27.1](#4271)
- [4.27.0](#4270)
- [4.26.1](#4261)
- [4.26.0](#4260)
- [4.25.2](#4252)
- [4.25.1](#4251)
- [4.25.0](#4250)
- [4.24.2](#4242)
- [4.24.1](#4241)
- [4.24.0](#4240)
- [4.23.0](#4230)
- [4.22.1](#4221)
- [4.22.0](#4220)
- [4.21.1](#4211)
- [4.21.0](#4210)
- [4.20.1](#4201)
- [4.20.0](#4200)

## Check known issues

- [4.29.0](#4290)
- [4.28.0](#4280)
- [4.27.0](#4270)
- [4.26.0](#4260)
- [4.25.0](#4250)
- [4.24.0](#4240)
- [4.23.0](#4230)

## 4.29.0

{{< release-date date="2024-04-08" >}}

### New

- You can now enforce Rosetta usage via [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md).
- [Docker socket mount restrictions](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/config.md) with ECI is now generally available.
- Docker Engine and CLI updated to [Moby 26.0](https://github.com/moby/moby/releases/tag/v26.0.0). This includes Buildkit 0.13, sub volumes mounts, networking updates, and improvements to the containerd multi-platform image store UX.
- New and improved Docker Desktop error screens: swift troubleshooting, easy diagnostics uploads, and actionable remediation.
- Compose supports [Synchronized file shares (experimental)](/manuals/desktop/features/synchronized-file-sharing.md).
- New [interactive Compose CLI (experimental)](/manuals/compose/how-tos/environment-variables/envvars.md#compose_menu).
- Beta release of:
  - Air-Gapped Containers with [Settings Management](/manuals/enterprise/security/hardened-desktop/air-gapped-containers.md).
  - [Host networking](/manuals/engine/network/drivers/host.md#docker-desktop) in Docker Desktop.
  - [Docker Debug](/manuals/desktop/use-desktop/container.md#integrated-terminal) for running containers.
  - [Volumes Backup & Share extension](/manuals/desktop/use-desktop/volumes.md) functionality available in the **Volumes** tab.

### Upgrades

- [Docker Compose v2.26.1](https://github.com/docker/compose/releases/tag/v2.26.1)
- [Docker Scout CLI v1.6.3](https://github.com/docker/scout-cli/releases/tag/v1.6.3)
- [Docker Engine v26.0.0](https://docs.docker.com/engine/release-notes/26.0/#2600)
- [Buildx v0.13.1](https://github.com/docker/buildx/releases/tag/v0.13.1)
- [Kubernetes v1.29.2](https://github.com/kubernetes/kubernetes/releases/tag/v1.29.2)
- [cri-dockerd v0.3.11](https://github.com/Mirantis/cri-dockerd/releases/tag/v0.3.11)
- Docker Debug v0.0.27

### Bug fixes and enhancements

#### For all platforms

- Fixed an issue with dropdown menu opening beyond the application window.
- Docker Init:
  - Updated the formatting of CLI output to improve legibility.
  - Fixed an issue with `.dockerignore` to avoid ignoring application files that start with "compose".
  - Improved how Java applications are started based on Spring Boot version. Fixes [docker/for-mac#7171](https://github.com/docker/for-mac/issues/7171).
  - Removed non-official Docker image used for Rust cross-compilation.
- The maximum number of files per [Synchronized file share](/manuals/desktop/features/synchronized-file-sharing.md) now exceeds 2 million.
- Fixed an issue that caused the warning: "_The value provided to Autocomplete is invalid._" when selecting the **Export to local image** field.
- **Run Cloud** can now be accessed from the Docker Desktop Dashboard.
- Opting out from sending analytics will now also disable collecting data for bug reports.
- You can now share and unshare a port to the Cloud Engine in the **Containers** view.
- Shared cloud can now be accessed from the footer in the right-hand side of the **Dashboard**.
- Added beta support for host networking on macOS, Windows and Docker Desktop for Linux  [docker#238](https://github.com/docker/roadmap/issues/238).
- Added a timestamp to new unread notifications.
- Fixed typo in the virtualization support error message. Fixes [docker/desktop-linux#197](https://github.com/docker/desktop-linux/issues/197).
- Docker Desktop now allows connections to `host.docker.internal` to be blocked by a rule in a PAC file.
- Fixed the placement of the secondary menu in the **Images** and **Containers** lists.
- Fixed a race condition that occurred when starting Docker Desktop with QEMU.
- Improved the error message when an image pull is blocked by Registry Access Management policy.
- Re-add `CONFIG_BONDING=y` in the kernel config.

#### For Mac

- Fixed Kubernetes not starting successfully. Fixes [docker/for-mac#7136](https://github.com/docker/for-mac/issues/7136) and [docker/for-mac#7031](https://github.com/docker/for-mac/issues/7031).
- Fixed a bug when the browser was not able to send back authentication information to Docker Desktop. Fixes [docker/for-mac/issues#7160](https://github.com/docker/for-mac/issues/7160).

#### For Windows

- Fixed a bug where `docker run -v` would fail after switching between WSL 2 and Hyper-V.
- Fixed a bug where Docker Desktop was not stopping its WSL distributions (`docker-desktop` and `docker-desktop-data`) when it was shutdown. Fixes [docker/for-win/issues/13443](https://github.com/docker/for-win/issues/13443) and [docker/for-win/issues/13938](https://github.com/docker/for-win/issues/13938).

#### For Linux

- Fixed an issue that caused the list of available experimental features in the UI to become out-of-sync with the backend data.

#### Security

- Disabled Electron `runAsNode` fuse to improve security hardening. For more info, see [Electron's documentation.](https://www.electronjs.org/blog/statement-run-as-node-cves).
- Fixed [CVE-2024-6222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6222) which allows an attacker who has gained access to the Docker Desktop VM through a container breakout to further escape to the host by passing extensions and dashboard related IPC messages. Reported by Billy Jheng Bing-Jhong, Đỗ Minh Tuấn, Muhammad Alifa Ramdhan working with Trend Micro Zero Day Initiative.

### Known issues

#### For Mac

- Docker Desktop on Apple Silicon doesn't start if Rosetta is not installed. This will be fixed in future releases. See [docker/for-mac#7243](https://github.com/docker/for-mac/issues/7243).

## 4.28.0

{{< release-date date="2024-02-26" >}}

### New

- [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md) now allows admins to set the default file-sharing implementation and specify which paths developer can add file shares to.
- Added support for `socks5://` HTTP and HTTPS proxy URLs when the [`SOCKS` proxy support beta feature](/manuals/desktop/features/networking.md) is enabled.
- Users can now filter volumes to see which ones are in use in the **Volumes** tab.

### Upgrades

- [Compose v2.24.6](https://github.com/docker/compose/releases/tag/v2.24.6)
- [Docker Engine v25.0.3](https://docs.docker.com/engine/release-notes/25.0/#2503)
- [Docker Scout CLI v1.5.0](https://github.com/docker/scout-cli/releases/tag/v1.5.0)
- [Qemu 8.1.5](https://wiki.qemu.org/ChangeLog/8.1)
- [Wasm](/manuals/desktop/features/wasm.md) runtimes:
  - Updated runwasi shims to `v0.4.0`, including:
    - wasmtime `v17.0`, with initial support for WASI preview 2
    - wasmedge `v0.13.5`
    - wasmer `v4.1.2`
  - Updated deislabs shims to `v0.11.1`, including:
    - lunatic `v0.13.2`
    - slight `v0.5.1`
    - spin `v2.2.0`
    - wws `v1.7.0`

### Bug fixes and enhancements

#### For all platforms

- Fixed `postgis` with `Qemu`. Fixes [docker/for-mac#7172](https://github.com/docker/for-mac/issues/7172).
- Re added `CONFIG_BLK_DEV_DM` kernel config for `kpartx`. Fixes [docker/for-mac#7197](https://github.com/docker/for-mac/issues/7197).
- Allow `SOCKS` proxies to be set via a proxy autoconfig `pac file`.
- Re added `CONFIG_AUDIT` kernel config.
- Fixed a bug with the Rust build on `virtiofs`. See [rust-lang/docker-rust#161](https://github.com/rust-lang/docker-rust/issues/161).
- Fixed an issue that caused the `missing registry authentication` error when pulling Kubernetes images.
- Fixed an issue that caused Docker Compose commands to hang.
- Fixed a bug in `docker build` that caused Docker Desktop to crash. Fixes [docker/for-win#13885](https://github.com/docker/for-win/issues/13885), [docker/for-win#13896](https://github.com/docker/for-win/issues/13896), [docker/for-win#13899](https://github.com/docker/for-win/issues/13899), [docker/for-mac#7164](https://github.com/docker/for-mac/issues/7164), [docker/for-mac#7169](https://github.com/docker/for-mac/issues/7169)
- Docker Init:
  - Improved how Java applications are started based on Spring Boot version. Fixes [docker/for-mac#7171](https://github.com/docker/for-mac/issues/7171).
  - Removed non-official Docker image used for Rust cross-compilation
- Builds view:
  - Active and completed builds can be found in dedicated tabs.
  - Build details now displays build duration and cache steps.
  - OpenTelemetry traces are now displayed in the build results.
  - Fixed an issue where context builders events were not always triggered.
  - Restyle the empty state view to make the dashboard clearer.

#### For Mac

- Fix `httpd` issue with Rosetta. [docker/for-mac#7182](https://github.com/docker/for-mac/issues/7182)
- Fixed a bug that caused a crash on the `virtualization.framework`. Fixes [docker/for-mac#7024](https://github.com/docker/for-mac/issues/7024)

#### For Windows

- Fixed an issue with DNS timeouts on Windows.
- Added support for Enhanced Container Isolation Docker socket mount permission on WSL user distributions.
- Fixed an issue that caused the `failed to get console mode` error when redirecting output from the CLI.
- Fixed an issue with the engine socket permissions when mounted inside containers. Fixes [docker/for-win#13898](https://github.com/docker/for-win/issues/13898)

### Known Issues

#### For Windows

- In dark mode, the **Disk image location** in **Resources**>**Advanced** settings is not visible. As a workaround, change to light mode.

## 4.27.2

{{< release-date date="2024-02-08" >}}

### Upgrades

- [Compose v2.24.5](https://github.com/docker/compose/releases/tag/v2.24.5)
- [Docker Scout CLI v1.4.1](https://github.com/docker/scout-cli/releases/tag/v1.4.1)
- Docker Debug v0.0.24

### Bug fixes and enhancements

#### For all platforms

- Fixed a bug where the diagnostics ID would not print correctly when uploading diagnostics from the terminal.
- Fixed a bug where the default settings values were being reset to default on startup, when using Settings Management.
- Fixed a bug with the dashboard being shown at startup even though the **Open Docker Dashboard when Docker Desktop starts** option was disabled. Fixes [docker/for-win#13887](https://github.com/docker/for-win/issues/13887).
- Fixed a bug in the build backend service that caused Docker Desktop to crash. Fixes [docker/for-win#13885](https://github.com/docker/for-win/issues/13885), [docker/for-win#13896](https://github.com/docker/for-win/issues/13896), [docker/for-win#13899](https://github.com/docker/for-win/issues/13899), [docker/for-mac#7164](https://github.com/docker/for-mac/issues/7164), [docker/for-mac#7169](https://github.com/docker/for-mac/issues/7169).
- Fixed the Docker Engine socket permissions when mounted inside containers. Fixes [docker/for-win#13898](https://github.com/docker/for-win/issues/13898).
- Docker Scout:
  - Updated dependencies to address Leaky Vessels series of CVEs ([CVE-2024-21626](https://github.com/advisories/GHSA-xr7r-f8xq-vfvv), [CVE-2024-24557](https://github.com/advisories/GHSA-xw73-rw38-6vjc))
  - Added initial VEX document to document false positive [CVE-2020-8911](https://github.com/advisories/GHSA-f5pg-7wfw-84q9) and [CVE-2020-8912](https://github.com/advisories/GHSA-7f33-f4f5-xwgw)
  - Added support for cosign SBOM attestations
  - Added support for VEX in-toto attestations
- Docker Debug:
  - Fixed a bug when pulling the image behind resource accesses management
  - Fixed connection issues

#### For Mac

- Re-added kernel modules needed by `Istio`. Fixes [docker/for-mac#7148](https://github.com/docker/for-mac/issues/7148).
- Node now uses all the cores available under Rosetta.
- Fixed an issue with `php-fpm`. Fixes [docker/for-mac#7037](https://github.com/docker/for-mac/issues/7037).

## 4.27.1

{{< release-date date="2024-02-01" >}}

### Upgrades

- [Docker Engine v25.0.2](https://docs.docker.com/engine/release-notes/25.0/#2502) which contains a fix for [CVE-2024-24557](https://scout.docker.com/vulnerabilities/id/CVE-2024-24557), [CVE-2024-23650](https://scout.docker.com/vulnerabilities/id/CVE-2024-23650), [CVE-2024-23651](https://scout.docker.com/vulnerabilities/id/CVE-2024-23651), [CVE-2024-23652](https://scout.docker.com/vulnerabilities/id/CVE-2024-23652) and [CVE-2024-23653](https://scout.docker.com/vulnerabilities/id/CVE-2024-23653)
- [Containerd v1.6.28](https://github.com/containerd/containerd/releases/tag/v1.6.28)
- [Runc v1.1.12](https://github.com/opencontainers/runc/releases/tag/v1.1.12) which contains a fix for [CVE-2024-21626](https://scout.docker.com/vulnerabilities/id/CVE-2024-21626)

### Bug fixes and enhancements

#### For Mac

- Fixed a bug that caused Docker Desktop to hang when applying an update.

## 4.27.0

{{< release-date date="2024-01-25" >}}

### New

- Docker init now supports Java and is generally available to all users.
- [Synchronized File Shares](/manuals/desktop/features/synchronized-file-sharing.md) provides fast and flexible host-to-VM file sharing within Docker Desktop. Utilizing the technology behind [Docker’s acquisition of Mutagen](https://www.docker.com/blog/mutagen-acquisition/), this feature provides an alternative to virtual bind mounts that uses synchronized filesystem caches, improving performance for developers working with large codebases.
- Organization admins can now [configure Docker socket mount permissions](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/config.md) when ECI is enabled.
- [Containerd Image Store](/manuals/desktop/features/containerd.md) support is now generally available to all users.
- Get a debug shell into any container or image with the new [`docker debug` command](/reference/cli/docker/debug/) (Beta).
- Organization admins, with a Docker Business subscription, can now configure a custom list of extensions with [Private Extensions Marketplace](/manuals/extensions/private-marketplace.md) enabled (Beta)

### Upgrades

- [Amazon ECR Credential Helper v0.7.1](https://github.com/awslabs/amazon-ecr-credential-helper/releases/tag/v0.7.1)
- [Buildx v0.12.1](https://github.com/docker/buildx/releases/tag/v0.12.1)
- [Containerd v1.6.27](https://github.com/containerd/containerd/releases/tag/v1.6.27)
- [Compose v2.24.3](https://github.com/docker/compose/releases/tag/v2.24.3)
- [Docker Credential Helpers v0.8.1](https://github.com/docker/docker-credential-helpers/releases/tag/v0.8.1)
- [Runc v1.1.11](https://github.com/opencontainers/runc/releases/tag/v1.1.11)
- [Docker Engine v25.0.0](https://docs.docker.com/engine/release-notes/25.0/)
- [Kubernetes v1.29.1](https://github.com/kubernetes/kubernetes/releases/tag/v1.29.1)
- [Docker Scout v1.3.0](https://github.com/docker/scout-cli/releases/tag/v1.3.0)

### Bug fixes and enhancements

#### For all platforms

- The `docker scan` command has been removed. To continue learning about the vulnerabilities of your images, and many other features, use the [`docker scout` command](/reference/cli/docker/scout/).
- Fixed a bug where automatic updates would not download when the **Always download updates** checkbox was selected.
- Fixed typo in the dashboard tooltip. Fixes [docker/for-mac#7132](https://github.com/docker/for-mac/issues/7132)
- Improved signal handling behavior (e.g. when pressing Ctrl-C in the terminal while running a `docker` command).
- Re-added kernel modules required by `minikube start --cni=cilium`.
- Fixed a bug that caused the installation screen to appear again when admin controls are enabled after sign in.
- Fixed a bug where Docker would not start if a shared folder is no longer present.
- Fixed the number of available CPUs displayed in the **Containers** section of the Dashboard.
- Re-added kernel modules for `btrfs`, `xfs`, `vfat`, `exfat`, `ntfs3`, `f2fs`, `squashfs`, `udf`, `9p` and `autofs`.
- Container usage charts have been moved to a vertical **Resource usage** side panel to allow for more space in the containers list. Accessing the usage charts remains the same via the **Show charts** button.
- Fixed a bug where selecting **Close Application** at sign-in was leaving behind a hung backend process.
- Fixed a bug which caused Docker Desktop to become unresponsive when analytics is disabled through Settings Management.
- Docker init:
  - Added support for containerizing a Java server
  - Various fixes on Windows
- Builder settings:
  - You can now refresh storage data for your builder at any point in time.
  - You can now delete the build history for a builder.
- Builds view:
  - An error message is now shown when a build record cannot be removed.
  - Fixed an issue where a cloud builder could not be created in rootless mode on macOS.
  - Inline cache and Git source are now properly handled in the **Build timing** section of the **Info** tab.
  - The Builder used and the author invoking the build is now displayed in past builds on the **History** tab.
  - Several improvements made to better link past builds on the **History** tab.
  - Several improvements to make the build name more accurate.
  - Fixed stuck builds in the **Active builds** list when a builder cannot be reached.
  - Fixed an issue preventing the build record from being deleted in some circumstances.
  - Fixed an issue where build names could be empty.
  - Fixed a general issue with the Builds view when Resource saver mode is enabled.

#### For Mac

- Enabled `Huge Pages` and fixed PHP segmentation fault with Rosetta. Fixes [docker/for-mac#7117](https://github.com/docker/for-mac/issues/7117).
- Fixed `xvfb` under Rosetta. Fixes [docker/for-mac#7122](https://github.com/docker/for-mac/issues/7122)
- Fixed `ERR_WORKER_INVALID_EXEC_ARGV` error under Rosetta. [docker/for-mac#6998](https://github.com/docker/for-mac/issues/6998).
- Fixed a bug where Docker Desktop could deadlock if `admin-settings.json` was syntactically invalid.

#### For Windows

- Fixed a bug that prevented UTF-16 strings from being encoded to UTF-8 for some locales. Fixes [docker/for-win#13868](https://github.com/docker/for-win/issues/13868).
- Fixed a bug where the credentials store configuration would reset on app restart with the WSL integration. Fixes [docker/for-win#13529](https://github.com/docker/for-win/issues/13529).
- Fixed an issue that prevented the correct WSL engine errors from propagating to the user.
- Fixed an issue that would cause Docker Desktop to hang when quitting from Windows Containers mode.

### Security

#### For Windows

- Mitigated several DLL side-loading vulnerabilities in the Docker Desktop installer on Windows, reported by Suman Kumar Chakraborty ([@Hijack-Everything](https://github.com/Hijack-Everything))

### Known issues

#### For all platforms

- When using Setting Management, the settings that are not set in the `admin-settings.json` will be reset to default when Docker Desktop starts.

#### For Mac

- Updating to 4.27.0 from the **Software updates** sometimes hangs. As a workaround, use the 4.27.0 installer from this page.

## 4.26.1

{{< release-date date="2023-12-14" >}}

### Bug fixes and enhancements

#### For all platforms

- Updated feedback links inside Docker Desktop to ensure they continue to work correctly

#### For Windows

- Switch the CLI binaries to a version compatible with older versions of glibc, such as used in Ubuntu 20.04 fixes [docker/for-win#13824](https://github.com/docker/for-win/issues/13824)

## 4.26.0

{{< release-date date="2023-12-04" >}}

### New

- Administrators can now control access to beta and experimental features in the **Features in development** tab with [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md).
- Introduced four new version update states in the footer.
- `docker init` (Beta) now supports PHP with Apache + Composer.
- The [**Builds** view](/manuals/desktop/use-desktop/builds.md) is now GA. You can now inspect builds, troubleshoot errors, and optimize build speed.

### Upgrades

- [Compose v2.23.3](https://github.com/docker/compose/releases/tag/v2.23.3)
- [Docker Scout CLI v1.2.0](https://github.com/docker/scout-cli/releases/tag/v1.2.0).
- [Buildx v0.12.0](https://github.com/docker/buildx/releases/tag/v0.12.0)
- [Wasm](/manuals/desktop/features/wasm.md) runtimes:
  - wasmtime, wasmedge and wasmer `v0.3.1`.
  - lunatic, slight, spin, and wws `v0.10.0`.
  - Wasmtime is now based on wasmtime `v14.0` and supports wasi preview-2 components
  - Wasmedge is now based on WasmEdge `v0.13.5`
  - Spin is now based on Spin `v2.0.1`
  - wws is now based on wws `v1.7.0`
- [Docker Engine v24.0.7](https://docs.docker.com/engine/release-notes/24.0/#2407)
- [Containerd v1.6.25](https://github.com/containerd/containerd/releases/tag/v1.6.25)
- [runc v1.1.10](https://github.com/opencontainers/runc/releases/tag/v1.1.10)

### Bug fixes and enhancements

#### For all platforms

- You can now provide feedback from the commandline by using `docker feedback`.
- Improved the text and position of the startup options in the **General** settings tab.
- Redesigned the dashboard's header bar, added links to other Docker resources, improved display of account information.
- Fixed a bug  where enabling the containerd image store and Wasm simultaneously would not enable Wasm.
- containerd integration:
  - Fixed `docker push/pull` authentication not being sent to non-DockerHub registries in cases where `ServerAddress` is not provided.
  - Fixed `docker history` reporting wrong IDs and tags.
  - Fixed `docker tag` not preserving internal metadata.
  - Fixed `docker commit` when the daemon configured with `--userns-remap`.
  - Fixed `docker image list` to show real image creation date.
  - Added support for `-a` flag to `docker pull` (pull all remote repository tags).
  - Added support for `--group-add` flag to `docker run` (append extra groups).
  - Adjusted some errors reported by `docker push/pull`.
- Docker Init:
  - Improved cross-compilation in Dockerfiles for Golang and Rust.
  - Improved caching in Dockerfile for ASP.NET Core.
- Docker Desktop now gives more detailed information about pending updates in the dashboard footer.
- Fixed a bug in Enhanced Container Isolation mode where `docker run --init` was failing.
- Fixed a bug where a notification prompting the user to download a new version of Docker Desktop remained visible after the user started downloading the new version.
- Added a notification that indicates when Docker Desktop is installing a new version.
- Fixed a bug where the cursor changed to a pointer when the user hovered over a notification that has no call to action.

#### For Mac

- Fixed an issue where Rosetta would not work with PHP. Fixes [docker/for-mac#6773](https://github.com/docker/for-mac/issues/6773)  and [docker/for-mac#7037](https://github.com/docker/for-mac/issues/7037).
- Fixed several issues related to Rosetta not working. Fixed [[docker/for-mac#6973](https://github.com/docker/for-mac/issues/6973), [[docker/for-mac#7009](https://github.com/docker/for-mac/issues/7009), [[docker/for-mac#7068](https://github.com/docker/for-mac/issues/7068) and [[docker/for-mac#7075](https://github.com/docker/for-mac/issues/7075)
- Improved the performance of NodeJS under Rosetta.
- Fixed the **Unable to open /proc/self/exe** Rosetta errors.
- Fixed a bug were the setting **Start Docker Desktop when you sign in** would not work. Fixes [docker/for-mac#7052](https://github.com/docker/for-mac/issues/7052).
- You can now enable the use of Kernel networking path for UDP through the UI. Fixes [docker/for-mac#7008](https://github.com/docker/for-mac/issues/7008).
- Fixed a regression where the `uninstall` CLI tool was missing.
- Addressed an issue which caused Docker Desktop to become unresponsive when analytics were disabled with Settings Management.

#### For Windows

- Added support for WSL mirrored mode networking (requires WSL `v2.0.4` and up).
- Added missing signatures on DLL and VBS files.

### Known issues

#### For Windows

- Docker CLI doesn’t work when using WSL 2 integration on an older Linux distribution (for example, Ubuntu 20.04) which uses a `glibc` version older than `2.32`. This will be fixed in future releases. See [docker/for-win#13824](https://github.com/docker/for-win/issues/13824).

## 4.25.2

{{< release-date date="2023-11-21" >}}

### Bug fixes and enhancements

#### For all platforms

- Fixed a bug where a blank UI would appear after submitting a response in the **Welcome Survey**.

#### For Windows

- Fixed a bug where Docker Desktop on WSL 2 would shut down dockerd unexpectedly when idle. Fixes [docker/for-win#13789](https://github.com/docker/for-win/issues/13789)

## 4.25.1

{{< release-date date="2023-11-13" >}}

### Bug fixes and enhancements

#### For all platforms

- Fixed a regression in 4.25 where Docker would not start if the swap file was corrupt. Corrupt swap files will be re-created on next boot.
- Fixed a bug when swap is disabled. Fixes [docker/for-mac#7045](https://github.com/docker/for-mac/issues/7045), [docker/for-mac#7044](https://github.com/docker/for-mac/issues/7044) and [docker/for-win#13779](https://github.com/docker/for-win/issues/13779).
- The `sysctl vm.max_map_count` is now set to 262144. See [docker/for-mac#7047](https://github.com/docker/for-mac/issues/7047)

#### For Windows

- Fixed an issue where **Switch to Windows Containers** would not appear on the tray menu for some users. See [docker/for-win#13761](https://github.com/docker/for-win/issues/13761).
- Fixed a bug where the WSL integration would not work for users using a shell other than `sh`. See [docker/for-win#13764](https://github.com/docker/for-win/issues/13764).
- Re-added `DockerCli.exe`.

## 4.25.0

{{< release-date date="2023-10-26" >}}

### New

- Rosetta is now Generally Available for all users on macOS 13 or later. It provides faster emulation of Intel-based images on Apple Silicon. To use Rosetta, see [Settings](/manuals/desktop/settings-and-maintenance/settings.md). Rosetta is enabled by default on macOS 14.1 and later.
- Docker Desktop now detects if a WSL version is out of date. If an out dated version of WSL is detected, you can allow Docker Desktop to automatically update the installation or you can manually update WSL outside of Docker Desktop.
- New installations of Docker Desktop for Windows now require a Windows version of 19044 or later.
- Administrators now have the ability to control Docker Scout image analysis in [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md).

### Upgrades

- [Compose v2.23.0](https://github.com/docker/compose/releases/tag/v2.23.0)
- [Docker Scout CLI v1.0.9](https://github.com/docker/scout-cli/releases/tag/v1.0.9).
- [Kubernetes v1.28.2](https://github.com/kubernetes/kubernetes/releases/tag/v1.28.2)
  - [cri-dockerd v0.3.4](https://github.com/Mirantis/cri-dockerd/releases/tag/v0.3.4)
  - [CNI plugins v1.3.0](https://github.com/containernetworking/plugins/releases/tag/v1.3.0)
  - [cri-tools v1.28.0](https://github.com/kubernetes-sigs/cri-tools/releases/tag/v1.28.0)

### Bug fixes and enhancements

#### For all platforms

- Fixed a spacing problem in the `Accept License` pop-up.
- Fixed a bug where the **Notifications drawer** changed size when navigating between **Notifications list** and **Notification details** view.
- containerd integration:
  - `docker push` now supports `Layer already exists` and `Mounted from` progress statuses.
  - `docker save` is now able to export images from all tags of the repository.
  - Hide push upload progress of manifests, configs and indexes (small json blobs) to match the original push behavior.
  - Fixed `docker diff` containing extra differences.
  - Fixed `docker history` not showing intermediate image IDs for images built with the classic builder.
  - Fixed `docker load` not being able to load images from compressed tar archives.
  - Fixed registry mirrors not working.
  - Fixed `docker diff` not working correctly when called multiple times concurrently for the same container.
  - Fixed `docker push` not reusing layers when pushing layers to different repositories on the same registry.
- Docker Init:
  - Fixed outdated links to Docker documentation included in generated files
  - Add support for ASP.NET Core 8 (in addition to 6 and 7)
- Fixed a bug that caused a failure when installing Wasm shims.
- Fixed a bug where Docker Desktop exits the [Resource Saver mode](https://docs.docker.com/desktop/use-desktop/resource-saver/) every 15 minutes, or, if the timer is set above 15 minutes, the resource saver mode never kicks in.
- Promoted the **Enable background SBOM indexing** option to **General settings**.

#### For Mac

- Minimum OS version to install or update Docker Desktop on macOS is now macOS Monterey (version 12) or later.
- Enhanced error messaging when an update cannot be completed if the user doesn't match the owner of `Docker.app`. Fixes [docker/for-mac#7000](https://github.com/docker/for-mac/issues/7000).
- Fixed a bug where **Re-apply configuration** might not work when `/var/run/docker.sock` is mis-configured.
- Docker Desktop doesn't overwrite `ECRCredentialHelper` if already present in `/usr/local/bin`.

#### For Windows

- Fixed an issue where **Switch to Windows Containers** would show in the tray menu on Windows Home Editions. Fixes [docker/for-win#13715](https://github.com/docker/for-win/issues/13715)

#### For Linux

- Fixed a bug in `docker login`. Fixes  [docker/docker-credential-helpers#299](https://github.com/docker/docker-credential-helpers/issues/299)

### Known Issues

#### For Mac

- Upgrading to MacOS 14 can cause Docker Desktop to also update to a latest version even if the auto update option is disabled.
- Uninstalling Docker Desktop from the command line is not available. As a workaround, you can [uninstall Docker Desktop from the Dashboard](https://docs.docker.com/desktop/uninstall/).

#### For Windows

- **Switch to Windows containers** option in the tray menu may not show up on Windows. As a workaround, edit the [`settings.json` file](/manuals/desktop/settings-and-maintenance/settings.md) and set `"displaySwitchWinLinContainers": true`.

#### For all platforms

- Docker operations, such as pulling images or logging in, fail with 'connection refused' or 'timeout' errors if the Swap file size is set to 0MB. As a workaround, configure the swap file size to a non-zero value in the **Resources** tab in **Settings**.

## 4.24.2

{{< release-date date="2023-10-12" >}}

### Bug fixes and enhancements

#### For all platforms

- Fixed a bug where Docker Desktop would send multiple requests to `notify.bugsnag.com`. Fixes [docker/for-win#13722](https://github.com/docker/for-win/issues/13722).
- Fixed a performance regression for PyTorch.

## 4.24.1

{{< release-date date="2023-10-04" >}}

### Bug fixes and enhancements

#### For Windows

- Fixed a bug on Docker Desktop for Windows where the Docker Desktop Dashboard wouldn't display container logs correctly. Fixes [docker/for-win#13714](https://github.com/docker/for-win/issues/13714).

## 4.24.0

{{< release-date date="2023-09-28" >}}

### New

- The new Notification center is now available to all users so you can be notified of new releases, installation progress updates, and more. Select the bell icon in the bottom-right corner of the Docker Desktop Dashboard to access the notification center.
- Compose Watch is now available to all users. For more information, see [Use Compose Watch](/manuals/compose/how-tos/file-watch.md).
- Resource Saver is now available to all users and is enabled by default. To configure this feature, navigate to the **Resources** tab in **Settings**. For more information see [Docker Desktop's Resource Saver mode](/manuals/desktop/use-desktop/resource-saver.md).
- You can now view and manage the Docker Engine state, with pause, stop, and resume, directly from the Docker Desktop Dashboard.

### Upgrades

- [Compose v2.22.0](https://github.com/docker/compose/releases/tag/v2.22.0)
- [Go 1.21.1](https://github.com/golang/go/releases/tag/go1.21.1)
- [Wasm](/manuals/desktop/features/wasm.md) runtimes:
  - wasmtime, wasmedge `v0.2.0`.
  - lunatic, slight, spin, and wws`v0.9.1`.
  - Added wasmer wasm shims.


### Bug fixes and enhancements

#### For all platforms

- Docker Init:
  - Fixed an issue formatting Dockerfile file paths for ASP.NET projects on Windows.
  - Improved performance on language detection for large directories with lots of files.
- Added a timeout to polling for resource usage stats used by the **Containers** view. Fixes [docker/for-mac#6962](https://github.com/docker/for-mac/issues/6962).
- containerd integration:
  - Implemented push/pull/save image events.
  - Implemented pulling legacy schema1 images.
  - Implemented `docker push --all-tags`.
  - Implemented counting containers using a specific image (visible for example in `docker system df -v`).
  - Validated pulled image names are not reserved.
  - Handle `userns-remap` daemon setting.
  - Fixed legacy builder build errors when multiple COPY/ADD instructions are used.
  - Fixed `docker load` causing pool corruption which could some subsequent image related operations.
  - Fixed not being able to reference images via truncated digest with a `sha256:` prefix.
  - Fixed `docker images` (without `--all`) showing intermediate layers (created by the legacy classic builder).
  - Fixed `docker diff` containing extra differences.
  - Changed `docker pull` output to match the output with containerd integration disabled.
- Fixed a grammatical error in Kubernetes status message. See [docker/for-mac#6971](https://github.com/docker/for-mac/issues/6971).
- Docker containers now use all host CPU cores by default.
- Improved inter-process security in dashboard UI.

#### For Mac

- Fixed a kernel panic on Apple Silicon Macs with macOS version earlier than 12.5. Fixes [docker/for-mac#6975](https://github.com/docker/for-mac/issues/6975).
- Fixed a bug where Docker Desktop failed to start if invalid directories were included in `filesharingDirectories`. Fixes [docker/for-mac#6980](https://github.com/docker/for-mac/issues/6980).
- Fixed a bug where installer is creating root-owned directories. Fixes [docker/for-mac#6984](https://github.com/docker/for-mac/issues/6984).
- Fixed a bug where installer is failing on setting up the docker socket when missing `/Library/LaunchDaemons`. Fixes [docker/for-mac#6967](https://github.com/docker/for-mac/issues/6967).
- Fixed a permission denied error when binding a privileged port to a non-localhost IP on macOS. Fixes [docker/for-mac#697](https://github.com/docker/for-mac/issues/6977).
- Fixed a resource leak introduced in 4.23. Related to [docker/for-mac#6953](https://github.com/docker/for-mac/issues/6953).

#### For Windows

- Fixed a bug where a "Docker Desktop service not running" popup appeared when service is already running. See [docker/for-win#13679](https://github.com/docker/for-win/issues/13679).
- Fixed a bug that caused Docker Desktop fail to start on Windows hosts. Fixes [docker/for-win#13662](https://github.com/docker/for-win/issues/13662).
- Modified the Docker Desktop resource saver feature to skip reducing kernel memory on WSL when no containers are running, as this was causing timeouts in some cases. Instead, users are encouraged to enable "autoMemoryReclaim" on WSL directly via the .wslconfig file (available since WSL 1.3.10).

### Known issues

#### For Mac

- Creating a container with the port 53 fails with the error address `already in use`. As a workaround, deactivate network acceleration by adding `"kernelForUDP": false`, in the `settings.json` file located at `~/Library/Group Containers/group.com.docker/settings.json`.

## 4.23.0

{{< release-date date="2023-09-11" >}}

### Upgrades

- [Compose v2.21.0](https://github.com/docker/compose/releases/tag/v2.21.0)
- [Docker Engine v24.0.6](https://docs.docker.com/engine/release-notes/24.0/#2406)
- [Docker Scout CLI v0.24.1](https://github.com/docker/scout-cli/releases/tag/v0.24.1).
- [Wasm](/manuals/desktop/features/wasm.md) runtimes:
  - wasmtime, wasmedge revision `d0a1a1cd`.
  - slight and spin wasm `v0.9.0`.

### New

- Added support for new Wasm runtimes: wws and lunatic.
- [`docker init`](/reference/cli/docker/init/) now supports ASP.NET
- Increased performance of exposed ports on macOS, for example with `docker run -p`.

### Removed

- Removed Compose V1 from Docker Desktop as it has stopped receiving updates.  Compose V2 has replaced it and is now integrated into all current Docker Desktop versions.

### Bug fixes and enhancements

#### For all platforms

- With [Docker Scout](/manuals/scout/_index.md), you can now:
  - Manage temporary and cached files with `docker scout cache`.
  - Manage environments with `docker scout environment`.
  - Configure the default organization with `docker scout config`.
  - List packages of an image with their vulnerabilities with `docker scout cves --format only-packages`.
  - Enroll an organization with Docker scout with `docker scout enroll`.
  - Stop, analyze, and compare local file systems with `docker scout cves --type fs`.
- Fixed a bug where `docker stats` would hang when Docker Desktop was in Resource Saver mode.
- Fixed a bug where turning off experimental features via **Settings** in the Docker Desktop Dashboard would not fully turn off Resource Saver mode.
- Fixed a bug where the **Containers list** action button was clipped.
- containerd image store:
  - Fixed `failed to read config content` error when interacting with some images.
  - Fixed building Dockerfiles with `FROM scratch` instruction when using the legacy classic builder (`DOCKER_BUILDKIT=0`).
  - Fixed `mismatched image rootfs errors` when building images with legacy classic builder (`DOCKER_BUILDKIT=0`).
  - Fixed `ONBUILD` and `MAINTAINER` Dockerfile instruction
  - Fixed healthchecks.

#### For Mac

- All users on macOS 12.5 or greater now have VirtioFS turned on by default. You can revert this in **Settings** in the **General** tab.
- Improved single-stream TCP throughput.
- Reinstated the health check for macOS that notifies you if there has been a change on your system which might cause problems running Docker binaries.

#### For Linux

- Fixed a bug where the GUI is killed when opening the Docker Desktop app twice. See [docker/desktop-linux#148](https://github.com/docker/desktop-linux/issues/148).

#### For Windows

- Fixed a bug where non-admin users would get prompted for credentials when switching to Windows Containers or after disabling WSL and switching to the Hyper-V engine.
  This issue would occur after an OS restart, or on a cold start of Docker Desktop.

### Security

#### For all platforms

- Fixed [CVE-2023-5165](https://www.cve.org/cverecord?id=CVE-2023-5165) which allows Enhanced Container Isolation bypass via debug shell. The affected functionality is available for Docker Business customers only and assumes an environment where users are not granted local root or Administrator privileges.
- Fixed [CVE-2023-5166](https://www.cve.org/cverecord?id=CVE-2023-5166) which allows Access Token theft via a crafted extension icon URL.

### Known Issues

- Binding a privileged port on Docker Desktop does not work on macOS. As a workaround you can expose the port on all interfaces (using `0.0.0.0`) or using localhost (using `127.0.0.1`).

## 4.22.1

{{< release-date date="2023-08-24" >}}

### Bug fixes and enhancements

#### For all platforms

- Mitigated several issues impacting Docker Desktop startup and Resource Saver mode. [docker/for-mac#6933](https://github.com/docker/for-mac/issues/6933)

#### For Windows

- Fixed `Clean / Purge data` troubleshoot option on Windows. [docker/for-win#13630](https://github.com/docker/for-win/issues/13630)

## 4.22.0

{{< release-date date="2023-08-03" >}}

### Upgrades

- [Buildx v0.11.2](https://github.com/docker/buildx/releases/tag/v0.11.2)
- [Compose v2.20.2](https://github.com/docker/compose/releases/tag/v2.20.2)
- [Docker Engine v24.0.5](https://docs.docker.com/engine/release-notes/24.0/#2405)

> [!NOTE]
>
> In this release, the bundled Docker Compose and Buildx binaries show a different version string. This relates to our efforts to test new features without causing backwards compatibility issues.
>
> For example, `docker buildx version` outputs `buildx v0.11.2-desktop.1`.

### New

- [Resource Usage](/manuals/desktop/use-desktop/container.md) has moved from experimental to GA.
- You can now split large Compose projects into multiple sub-projects with [`include`](/manuals/compose/how-tos/multiple-compose-files/include.md).

### Bug fixes and enhancements

#### For all platforms

- [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md) now lets you turn off Docker Extensions for your organisation.
- Fixed a bug where turning on Kubernetes from the UI failed when the system was paused.
- Fixed a bug where turning on Wasm from the UI failed when the system was paused.
- Bind mounts are now shown when you [inspect a container](/manuals/desktop/use-desktop/container.md).
- You can now download Wasm runtimes when the containerd image store is enabled.
- With [Quick Search](/manuals/desktop/use-desktop/_index.md#quick-search), you can now:
  - Find any container or Compose app residing on your local system. In
    addition, you can access environment variables and perform essential actions
    such as starting, stopping, or deleting containers.
  - Find public Docker Hub images, local images, or images from remote
    repositories.
  - Discover more about specific extensions and install them.
  - Navigate through your volumes and gain insights about the associated
    containers.
  - Search and access Docker's documentation.

#### For Mac

- Fixed a bug that prevented Docker Desktop from starting. [docker/for-mac#6890](https://github.com/docker/for-mac/issues/6890)
- Resource Saver is now available on Mac. It optimises Docker Desktop's usage of your system resources when no containers are running. To access this feature, make sure you have [turned on access to experimental features](/manuals/desktop/settings-and-maintenance/settings.md) in settings.

#### For Windows

- Fixed a bug where the self-diagnose tool showed a false-positive failure when vpnkit is expected to be not running. Fixes [docker/for-win#13479](https://github.com/docker/for-win/issues/13479).
- Fixed a bug where an invalid regular expression in the search bar caused an error. Fixes [docker/for-win#13592](https://github.com/docker/for-win/issues/13592).
- Resource Saver is now available on Windows Hyper-V. It optimises Docker Desktop's usage of your system resources when no containers are running. To access this feature, make sure you have [turned on access to experimental features](/manuals/desktop/settings-and-maintenance/settings.md) in settings.

## 4.21.1

{{< release-date date="2023-07-03" >}}

#### For all platforms

- Fixed connection leak for Docker contexts using SSH ([docker/for-mac#6834](https://github.com/docker/for-mac/issues/6834) and [docker/for-win#13564](https://github.com/docker/for-win/issues/13564))

#### For Mac

- Removed configuration health check for further investigation and addressing specific setups.

## 4.21.0

{{< release-date date="2023-06-29" >}}

### New

- Added support for new Wasm runtimes: slight, spin, and wasmtime. Users can download Wasm runtimes on demand when the containerd image store is enabled.
- Added Rust server support to Docker init.
- Beta release of the [**Builds** view](/manuals/desktop/use-desktop/builds.md) that lets you inspect builds and manage builders. This can be found in the **Features in Development** tab in **Settings**.

### Upgrades

- [Buildx v0.11.0](https://github.com/docker/buildx/releases/tag/v0.11.0)
- [Compose v2.19.0](https://github.com/docker/compose/releases/tag/v2.19.0)
- [Kubernetes v1.27.2](https://github.com/kubernetes/kubernetes/releases/tag/v1.27.2)
- [cri-tools v1.27.0](https://github.com/kubernetes-sigs/cri-tools/releases/tag/v1.27.0)
- [cri-dockerd v0.3.2](https://github.com/Mirantis/cri-dockerd/releases/tag/v0.3.2)
- [coredns v1.10.1](https://github.com/coredns/coredns/releases/tag/v1.10.1)
- [cni v1.2.0](https://github.com/containernetworking/plugins/releases/tag/v1.2.0)
- [etcd v3.5.7](https://github.com/etcd-io/etcd/releases/tag/v3.5.7)

### Bug fixes and enhancements

#### For all platforms

- Docker Desktop now automatically pauses the Docker Engine when it is not in use and wakes up again on demand.
- VirtioFS is now the default file sharing implementation for new installations of Docker Desktop on macOS 12.5 and higher.
- Improved product usage reporting using OpenTelemetry (experimental).
- Fixed Docker socket permissions. Fixes [docker/for-win#13447](https://github.com/docker/for-win/issues/13447) and [docker/for-mac#6823](https://github.com/docker/for-mac/issues/6823).
- Fixed an issue which caused Docker Desktop to hang when quitting the application whilst paused.
- Fixed a bug which caused the **Logs** and **Terminal** tab content in the **Container** view to be covered by a fixed toolbar [docker/for-mac#6814](https://github.com/docker/for-mac/issues/6814).
- Fixed a bug which caused input labels to overlap with input values on the container run dialog. Fixes [docker/for-win#13304](https://github.com/docker/for-win/issues/13304).
- Fixed a bug which meant users couldn't select the Docker Extension menu. Fixes [docker/for-mac#6840](https://github.com/docker/for-mac/issues/6840) and [docker/for-mac#6855](https://github.com/docker/for-mac/issues/6855)

#### For Mac

- Added a health check for macOS that notifies users if there has been a change on their system which might cause problems running Docker binaries.

#### For Windows

- Fixed a bug on WSL 2 where if Desktop is paused, killed, and then restarted, the startup hangs unless WSL is shut down first with `wsl --shutdown`.
- Fixed the WSL engine in cases where wsl.exe is not on the PATH [docker/for-win#13547](https://github.com/docker/for-win/issues/13547).
- Fixed the WSL engine's ability to detect cases where one of the Docker Desktop distributions' drive is missing [docker/for-win#13554](https://github.com/docker/for-win/issues/13554).
- A slow or unresponsive WSL integration no longer prevents Docker Desktop from starting. Fixes [docker/for-win#13549](https://github.com/docker/for-win/issues/13549).
- Fixed a bug that caused Docker Desktop to crash on startup [docker/for-win#6890](https://github.com/docker/for-mac/issues/6890).
- Added the following installer flags:
  - `--hyper-v-default-data-root` which specifies the default location for Hyper-V VM disk.
  - `--windows-containers-default-data-root` which specifies the default data root for Windows Containers.
  - `--wsl-default-data-root` which specifies the default location for WSL distribution disks.

## 4.20.1

{{< release-date date="2023-06-05" >}}

### Bug fixes and enhancements

#### For all platforms

- containerd image store: Fixed a bug that caused `docker load` to fail when loading an image that contains attestations.
- containerd image store: Fixed the default image exporter during build.

#### For Windows

- Fixed a bug that made it difficult to parse the WSL version on the host in non-western locales. Fixes [docker/for-win#13518](https://github.com/docker/for-win/issues/13518) and [docker/for-win#13524](https://github.com/docker/for-win/issues/13524).

## 4.20.0

{{< release-date date="2023-05-30" >}}

### Upgrades

- [Buildx v0.10.5](https://github.com/docker/buildx/releases/tag/v0.10.5)
- [Compose v2.18.1](https://github.com/docker/compose/releases/tag/v2.18.1)
- [Docker Engine v24.0.2](https://docs.docker.com/engine/release-notes/24.0/#2402)
- [Containerd v1.6.21](https://github.com/containerd/containerd/releases/tag/v1.6.21)
- [runc v1.1.7](https://github.com/opencontainers/runc/releases/tag/v1.1.5)

### Bug fixes and enhancements

#### For all platforms

- [Docker Scout CLI](https://docs.docker.com/scout/#docker-scout-cli) now finds the most recently built image if it is not provided as an argument.
- Improved the [Docker Scout CLI](https://docs.docker.com/scout/#docker-scout-cli) `compare` command.
- Added a warning about the [retirement of Docker Compose ECS/ACS integrations in November 2023](https://docs.docker.com/go/compose-ecs-eol/). Can be suppressed with `COMPOSE_CLOUD_EOL_SILENT=1`.
- Fixed an HTTP proxy bug where an HTTP 1.0 client could receive an HTTP 1.1 response.
- Enabled Docker Desktop's Enhanced Container Isolation (ECI) feature on WSL-2. This is available with a Docker Business subscription.
- Fixed a bug on the **Containers** table where previously hidden columns were displayed again after a fresh installation of Docker Desktop.

#### For Mac

- You can now reclaim disk space more quickly when files are deleted in containers. Related to [docker/for-mac#371](https://github.com/docker/for-mac/issues/371).
- Fixed a bug that prevented containers accessing 169.254.0.0/16 IPs. Fixes [docker/for-mac#6825](https://github.com/docker/for-mac/issues/6825).
- Fixed a bug in `com.docker.diagnose check` where it would complain about a missing vpnkit even when vpnkit is not expected to be running. Related to [docker/for-mac#6825](https://github.com/docker/for-mac/issues/6825).

#### For Windows

- Fixed a bug that meant WSL data could not be moved to a different disk. Fixes [docker/for-win#13269](https://github.com/docker/for-win/issues/13269).
- Fixed a bug where Docker Desktop was not stopping its WSL distributions (docker-desktop and docker-desktop-data) when it was shutdown, consuming host memory unnecessarily.
- Added a new setting that allows the Windows Docker daemon to use Docker Desktop's internal proxy when running Windows containers. See [Windows proxy settings](/manuals/desktop/settings-and-maintenance/settings.md#proxies).

#### For Linux

- Fixed an issue with the Docker Compose V1/V2 compatibility setting.

