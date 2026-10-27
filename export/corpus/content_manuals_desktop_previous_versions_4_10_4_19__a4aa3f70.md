---
title: Docker Desktop 4.10-4.19 release notes
linkTitle: Desktop 4.10-4.19
description: Docker Desktop release notes for versions 4.10-4.19.
toc_max: 2
sitemap: false
---
<!-- vale off -->

Before updating, see [release availability and update prerequisites](/manuals/desktop/release-availability.md).

## Find a release

- [4.19.0](#4190)
- [4.18.0](#4180)
- [4.17.1](#4171)
- [4.17.0](#4170)
- [4.16.3](#4163)
- [4.16.2](#4162)
- [4.16.1](#4161)
- [4.16.0](#4160)
- [4.15.0](#4150)
- [4.14.1](#4141)
- [4.14.0](#4140)
- [4.13.1](#4131)
- [4.13.0](#4130)
- [4.12.0](#4120)
- [4.11.1](#4111)
- [4.11.0](#4110)
- [4.10.1](#4101)
- [4.10.0](#4100)

## Check known issues

- [4.18.0](#4180)
- [4.17.1](#4171)
- [4.16.0](#4160)
- [4.14.0](#4140)
- [4.10.0](#4100)

## 4.19.0

{{< release-date date="2023-04-27" >}}

### New

- Docker Engine and CLI updated to [Moby 23.0](https://github.com/moby/moby/releases/tag/v23.0.0).
- The **Learning Center** now supports in-product walkthroughs.
- Docker init (Beta) now supports Node.js and Python.
- Faster networking between VM and host on macOS.
- You can now inspect and analyze remote images from Docker Desktop without pulling them.
- Usability and performance improvements to the **Artifactory images** view.

### Removed

- Removed `docker scan` command. To continue learning about the vulnerabilities of your images, and many other features, use the new `docker scout` command. Run `docker scout --help`, or [read the docs to learn more](/reference/cli/docker/scout/).

### Upgrades

- [Docker Engine v23.0.5](https://docs.docker.com/engine/release-notes/23.0/#2305)
- [Compose 2.17.3](https://github.com/docker/compose/releases/tag/v2.17.3)
- [Containerd v1.6.20](https://github.com/containerd/containerd/releases/tag/v1.6.20)
- [Kubernetes v1.25.9](https://github.com/kubernetes/kubernetes/releases/tag/v1.25.9)
- [runc v1.1.5](https://github.com/opencontainers/runc/releases/tag/v1.1.5)
- [Go v1.20.3](https://github.com/golang/go/releases/tag/go1.20.3)

### Bug fixes and enhancements

#### For all platforms

- Improved `docker scout compare` command to compare two images, now also aliased under `docker scout diff`.
- Added more details to dashboard errors when a `docker-compose` action fails ([docker/for-win#13378](https://github.com/docker/for-win/issues/13378)).
- Added support for setting HTTP proxy configuration during installation. This can be done via the `--proxy-http-mode`, `--overrider-proxy-http`, `--override-proxy-https` and `--override-proxy-exclude` installer flags in the case of installation from the CLI on [Mac](/manuals/desktop/setup/install/mac-install.md#install-from-the-command-line) and [Windows](/manuals/desktop/setup/install/windows-install.md#install-from-the-command-line), or alternatively by setting the values in the `install-settings.json` file.
- Docker Desktop now stops overriding .docker/config.json `credsStore` keys on application start. Note that if you use a custom credential helper then the CLI `docker login` and `docker logout` does not affect whether the UI is signed in to Docker or not. In general, it is better to sign into Docker via the UI since the UI supports multi-factor authentication.
- Added a warning about the forthcoming removal of Compose V1 from Docker Desktop. Can be suppressed with `COMPOSE_V1_EOL_SILENT=1`.
- In the Compose config, boolean fields in YAML should be either `true` or `false`. Deprecated YAML 1.1 values such as “on” or “no” now produce a warning.
- Improved UI for image table, allowing rows to use more available space.
- Fixed various bugs in port-forwarding.
- Fixed a HTTP proxy bug where an HTTP request without a Server Name Indication record would be rejected with an error.

#### For Windows

- Reverted to fully patching etc/hosts on Windows (includes `host.docker.internal` and `gateway.docker.internal` again). For WSL, this behavior is controlled by a new setting in the **General** tab. Fixes [docker/for-win#13388](https://github.com/docker/for-win/issues/13388) and [docker/for-win#13398](https://github.com/docker/for-win/issues/13398).
- Fixed a spurious `courgette.log` file appearing on the Desktop when updating Docker Desktop. Fixes [docker/for-win#12468](https://github.com/docker/for-win/issues/12468).
- Fixed the "zoom in" shortcut (ctrl+=). Fixes [docker/for-win#13392](https://github.com/docker/for-win/issues/13392).
- Fixed a bug where the tray menu would not correctly update after second container type switch. Fixes [docker/for-win#13379](https://github.com/docker/for-win/issues/13379).

#### For Mac

- Increased the performance of VM networking when using the Virtualization framework on macOS Ventura and above. Docker Desktop for Mac now uses gVisor instead of VPNKit. To continue using VPNKit, add `"networkType":"vpnkit"` to your `settings.json` file located at `~/Library/Group Containers/group.com.docker/settings.json`.
- Fixed a bug where an error window is displayed on uninstall.
- Fixed a bug where the setting `deprecatedCgroupv1` was ignored. Fixes [docker/for-mac#6801](https://github.com/docker/for-mac/issues/6801).
- Fixed cases where `docker pull` would return `EOF`.

#### For Linux

- Fixed a bug where the VM networking crashes after 24h. Fixes [docker/desktop-linux#131](https://github.com/docker/desktop-linux/issues/131).

### Security

#### For all platforms

- Fixed a security issue allowing users to bypass Image Access Management (IAM) restrictions configured by their organisation by avoiding `registry.json` enforced login via deleting the `credsStore` key from their Docker CLI configuration file. Only affects Docker Business customers.
- Fixed [CVE-2023-24532](https://github.com/advisories/GHSA-x2w5-7wp4-5qff).
- Fixed [CVE-2023-25809](https://github.com/advisories/GHSA-m8cg-xc2p-r3fc).
- Fixed [CVE-2023-27561](https://github.com/advisories/GHSA-vpvm-3wq2-2wvm).
- Fixed [CVE-2023-28642](https://github.com/advisories/GHSA-g2j6-57v7-gm8c).
- Fixed [CVE-2023-28840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28840).
- Fixed [CVE-2023-28841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28841).
- Fixed [CVE-2023-28842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28842).

## 4.18.0

{{< release-date date="2023-04-03" >}}

### New

- Initial beta release of `docker init` as per [the roadmap](https://github.com/docker/roadmap/issues/453).
- Added a new **Learning Center** tab to help users get started with Docker.
- Added an experimental file-watch command to Docker Compose that automatically updates your running Compose services as you edit and save your code.

### Upgrades

- [Buildx v0.10.4](https://github.com/docker/buildx/releases/tag/v0.10.4)
- [Compose 2.17.2](https://github.com/docker/compose/releases/tag/v2.17.2)
- [Containerd v1.6.18](https://github.com/containerd/containerd/releases/tag/v1.6.18), which includes fixes for [CVE-2023-25153](https://github.com/advisories/GHSA-259w-8hf6-59c2) and [CVE-2023-25173](https://github.com/advisories/GHSA-hmfx-3pcx-653p).
- [Docker Engine v20.10.24](https://docs.docker.com/engine/release-notes/20.10/#201024), which contains fixes for [CVE-2023-28841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28841),
  [CVE-2023-28840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28840), and
  [CVE-2023-28842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28842).

### Bug fixes and enhancements

#### For all platforms

- [Docker Scout CLI](/manuals/scout/_index.md#docker-scout-cli) can now compare two images and display packages and vulnerabilities differences. This command is in [Early Access](/manuals/release-lifecycle.md) and might change in the future.
- [Docker Scout CLI](/manuals/scout/_index.md#docker-scout-cli) now displays base image update and remediation recommendations using `docker scout recommendations`. It also displays a short overview of an image using `docker scout quickview` commands.
- You can now search for extensions direct from the Marketplace, as well as using **Global Search**.
- Fixed a bug where `docker buildx` container builders would lose access to the network after 24hrs.
- Reduced how often users are prompted for feedback on Docker Desktop.
- Removed minimum VM swap size.
- Added support for subdomain match, CIDR match, `.` and `_.` in HTTP proxy exclude lists.
- Fixed a bug in the transparent TLS proxy when the Server Name Indication field is not set.
- Fixed a grammatical error in Docker Desktop engine status message.

### For Windows

- Fixed a bug where `docker run --gpus=all` hangs. Fixes [docker/for-win#13324](https://github.com/docker/for-win/issues/13324).
- Fixed a bug where Registry Access Management policy updates were not downloaded.
- Docker Desktop now allows Windows containers to work when BitLocker is enabled on `C:`.
- Docker Desktop with the WSL backend no longer requires the `com.docker.service` privileged service to run permanently. For more information see [Permission requirements for Windows](https://docs.docker.com/desktop/windows/permission-requirements/).

### For Mac

- Fixed a performance issue where attributes stored on the host would not be cached for VirtioFS users.
- The first time Docker Desktop for Mac is launched, the user is presented with an installation window to confirm or adjust the configuration that requires privileged access. For more information see [Permission requirements for Mac](https://docs.docker.com/desktop/mac/permission-requirements/).
- Added the **Advanced** tab in **Settings**, where users can adjust the settings which require privileged access.

### For Linux

- Fixed a bug where the VM networking crashes after 24h. [docker/for-linux#131](https://github.com/docker/desktop-linux/issues/131)

### Security

#### For all platforms

- Fixed [CVE-2023-1802](https://www.cve.org/cverecord?id=CVE-2023-1802) where a security issue with the Artifactory Integration would cause it to fall back to sending registry credentials over plain HTTP if HTTPS check failed. Only users who have `Access experimental features` enabled are affected. Fixes [docker/for-win#13344](https://github.com/docker/for-win/issues/13344).

#### For Mac

- Removed the `com.apple.security.cs.allow-dyld-environment-variables` and `com.apple.security.cs.disable-library-validation` entitlements which allow an arbitrary dynamic library to be loaded with Docker Desktop via the `DYLD_INSERT_LIBRARIES` environment variable.

### Known Issues

- Uninstalling Docker Desktop on Mac from the **Troubleshoot** page might trigger an unexpected fatal error popup.

## 4.17.1

{{< release-date date="2023-03-20" >}}

### Bug fixes and enhancements

#### For Windows

- Docker Desktop now allows Windows containers to work when BitLocker is enabled on C:
- Fixed a bug where `docker buildx` container builders would lose access to the network after 24hrs.
- Fixed a bug where Registry Access Management policy updates were not downloaded.
- Improved debug information to better characterise failures under WSL 2.

### Known Issues

- Running containers with `--gpus` on Windows with the WSL 2 backend does not work. This will be fixed in future releases. See [docker/for-win/13324](https://github.com/docker/for-win/issues/13324).

## 4.17.0

{{< release-date date="2023-02-27" >}}

### New

- Docker Desktop now ships with Docker Scout. Pull and view analysis for images from Docker Hub and Artifactory repositories, get base image updates and recommended tags and digests, and filter your images on vulnerability information. To learn more, see [Docker Scout](/manuals/scout/_index.md).
- `docker scan` has been replaced by `docker scout`. See [Docker Scout CLI](/manuals/scout/_index.md#docker-scout-cli), for more information.
- You can now discover extensions that have been autonomously published in the Extensions Marketplace. For more information on self-published extensions, see [Marketplace Extensions](/manuals/extensions/marketplace.md).
- **Container File Explorer** is available as an experimental feature. Debug the filesystem within your containers straight from the GUI.
- You can now search for volumes in **Global Search**.

### Upgrades

- [Containerd v1.6.18](https://github.com/containerd/containerd/releases/tag/v1.6.18), which includes fixes for [CVE-2023-25153](https://github.com/advisories/GHSA-259w-8hf6-59c2) and [CVE-2023-25173](https://github.com/advisories/GHSA-hmfx-3pcx-653p).
- [Docker Engine v20.10.23](https://docs.docker.com/engine/release-notes/20.10/#201023).
- [Go 1.19.5](https://github.com/golang/go/releases/tag/go1.19.5)

### Bug fixes and enhancements

#### For all platforms

- Fixed a bug where diagnostic gathering could hang waiting for a subprocess to exit.
- Prevented the transparent HTTP proxy from mangling requests too much. Fixes Tailscale extension login, see [tailscale/docker-extension#49](https://github.com/tailscale/docker-extension/issues/49).
- Fixed a bug in the transparent TLS proxy where the Server Name Indication field is not set.
- Added support for subdomain match, CIDR match, `.` and `*.` in HTTP proxy exclude lists.
- Ensured HTTP proxy settings are respected when uploading diagnostics.
- Fixed fatal error when fetching credentials from the credential helper.
- Fixed fatal error related to concurrent logging.
- Improved the UI for Extension actions in the Marketplace.
- Added new filters in the Extensions Marketplace. You can now filter extensions by category and reviewed status.
- Added a way to report a malicious extension to Docker.
- Updated Dev Environments to v0.2.2 with initial set up reliability & security fixes.
- Added a whalecome survey for new users only.
- The confirmation dialogs on the troubleshooting page are now consistent in style with other similar dialogs.
- Fixed fatal error caused by resetting the Kubernetes cluster before it has started.
- Implemented `docker import` for the containerd integration.
- Fixed image tagging with an existing tag with the containerd integration.
- Implemented the dangling filter on images for the containerd integration.
- Fixed `docker ps` failing with containers whose images are no longer present with the containerd integration.

#### For Mac

- Fixed download of Registry Access Management policy on systems where the privileged helper tool `com.docker.vmnetd` is not installed.
- Fixed a bug where `com.docker.vmnetd` could not be installed if `/Library/PrivilegedHelperTools` does not exist.
- Fixed a bug where the "system" proxy would not handle "autoproxy" / "pac file" configurations.
- Fixed a bug where vmnetd installation fails to read `Info.Plist` on case-sensitive file systems. The actual filename is `Info.plist`. Fixes [docker/for-mac#6677](https://github.com/docker/for-mac/issues/6677).
- Fixed a bug where user is prompted to create the docker socket symlink on every startup. Fixes [docker/for-mac#6634](https://github.com/docker/for-mac/issues/6634).
- Fixed a bug that caused the **Start Docker Desktop when you log in** setting not to work. Fixes [docker/for-mac#6723](https://github.com/docker/for-mac/issues/6723).
- Fixed UDP connection tracking and `host.docker.internal`. Fixes [docker/for-mac#6699](https://github.com/docker/for-mac/issues/6699).
- Improved kubectl symlink logic to respect existing binaries in `/usr/local/bin`. Fixes [docker/for-mac#6328](https://github.com/docker/for-mac/issues/6328).
- Docker Desktop now automatically installs Rosetta when you opt-in to use it but have not already installed it.

### For Windows

- Added statical linking of WSL integration tools against `musl` so there is no need to install `alpine-pkg-glibc` in user distributions.
- Added support for running under cgroupv2 on WSL 2. This is activated by adding `kernelCommandLine = systemd.unified_cgroup_hierarchy=1 cgroup_no_v1=all` to your `%USERPROFILE%\.wslconfig` file in the `[wsl2]` section.
- Fixed an issue that caused Docker Desktop to get stuck in the "starting" phase when in WSL 2 mode (introduced in 4.16).
- Fixed Docker Desktop failing to start the WSL 2 backend when file system compression or encryption is enabled on `%LOCALAPPDATA%`.
- Fixed Docker Desktop failing to report a missing or outdated (incapable of running WSL version 2 distributions) WSL installation when starting.
- Fixed a bug where opening in Visual Studio Code fails if the target path has a space.
- Fixed a bug that causes `~/.docker/context` corruption and the error message "unexpected end of JSON input". You can also remove `~/.docker/context` to work around this problem.
- Ensured the credential helper used in WSL 2 is properly signed. Related to [docker/for-win#10247](https://github.com/docker/for-win/issues/10247).
- Fixed an issue that caused WSL integration agents to be terminated erroneously. Related to [docker/for-win#13202](https://github.com/docker/for-win/issues/13202).
- Fixed corrupt contexts on start. Fixes [docker/for-win#13180](https://github.com/docker/for-win/issues/13180) and [docker/for-win#12561](https://github.com/docker/for-win/issues/12561).

### For Linux

- Added Docker Buildx plugin for Docker Desktop for Linux.
- Changed compression algorithm to `xz` for RPM and Arch Linux distribution.
- Fixed a bug that caused leftover files to be left in the root directory of the Debian package. Fixes [docker/for-linux#123](https://github.com/docker/desktop-linux/issues/123).

### Security

#### For all platforms

- Fixed [CVE-2023-0628](https://www.cve.org/cverecord?id=CVE-2023-0628), which allows an attacker to execute an arbitrary command inside a Dev Environments container during initialization by tricking a user to open a crafted malicious `docker-desktop://` URL.
- Fixed [CVE-2023-0629](https://www.cve.org/cverecord?id=CVE-2023-0629), which allows an unprivileged user to bypass Enhanced Container Isolation (ECI) restrictions by setting the Docker host to `docker.raw.sock`, or `npipe:////.pipe/docker_engine_linux` on Windows, via the `-H` (`--host`) CLI flag or the `DOCKER_HOST` environment variable and launch containers without the additional hardening features provided by ECI. This does not affect already running containers, nor containers launched through the usual approach (without Docker's raw socket).

## 4.16.3

{{< release-date date="2023-01-30" >}}

### Bug fixes and enhancements

#### For Windows

- Fixed Docker Desktop failing to start the WSL 2 backend when file system compression or encryption is enabled on `%LOCALAPPDATA%`. Fixes [docker/for-win#13184](https://github.com/docker/for-win/issues/13184).
- Fixed Docker Desktop failing to report a missing or outdated WSL installation when starting. Fixes [docker/for-win#13184](https://github.com/docker/for-win/issues/13184).

## 4.16.2

{{< release-date date="2023-01-19" >}}

### Bug fixes and enhancements

#### For all platforms

- Fixed an issue where `docker build` and `docker tag` commands produced an `image already exists` error if the containerd integration feature is enabled.
- Fixed a regression introduced with Docker Desktop 4.16 breaking networking from containers with target platform linux/386 on amd64 systems. Fixes [docker/for-mac/6689](https://github.com/docker/for-mac/issues/6689).

#### For Mac

- Fixed the capitalization of `Info.plist` which caused `vmnetd` to break on case-sensitive file systems. Fixes [docker/for-mac/6677](https://github.com/docker/for-mac/issues/6677).

#### For Windows

- Fixed a regression introduced with Docker Desktop 4.16 causing it to get stuck in the "starting" phase when in WSL2 mode. Fixes [docker/for-win/13165](https://github.com/docker/for-win/issues/13165)

## 4.16.1

{{< release-date date="2023-01-13" >}}

### Bug fixes and enhancements

#### For all platforms

- Fixed `sudo` inside a container failing with a security related error for some images. Fixes [docker/for-mac/6675](https://github.com/docker/for-mac/issues/6675) and [docker/for-win/13161](https://github.com/docker/for-win/issues/13161).

## 4.16.0

{{< release-date date="2023-01-12" >}}

### New

- Extensions have moved from Beta to GA.
- Quick Search has moved from experimental to GA.
- Extensions are now included in Quick Search.
- Analyzing large images is now up to 4x faster.
- New local images view has moved from experimental to GA.
- New Beta feature for MacOS 13, Rosetta for Linux, has been added for faster emulation of Intel-based images on Apple Silicon.

### Upgrades

- [Compose v2.15.1](https://github.com/docker/compose/releases/tag/v2.15.1)
- [Containerd v1.6.14](https://github.com/containerd/containerd/releases/tag/v1.6.14)
- [Docker Engine v20.10.22](https://docs.docker.com/engine/release-notes/20.10/#201022)
- [Buildx v0.10.0](https://github.com/docker/buildx/releases/tag/v0.10.0)
- [Docker Scan v0.23.0](https://github.com/docker/scan-cli-plugin/releases/tag/v0.23.0)
- [Go 1.19.4](https://github.com/golang/go/releases/tag/go1.19.4)

### Bug fixes and enhancements

#### For all platforms

- Fixed `docker build --quiet` not outputting the image identifier with the `containerd` integration.
- Fixed image inspect not showing image labels with the `containerd` integration.
- Increased the contrast between running and stopped container icons to make it easier for colorblind people to scan the containers list.
- Fixed a bug where the user is prompted for new HTTP proxy credentials repeatedly until Docker Desktop is restarted.
- Added a diagnostics command `com.docker.diagnose login` to check HTTP proxy configuration.
- Fixed actions on compose stack not working properly. Fixes [docker/for-mac#6566](https://github.com/docker/for-mac/issues/6566).
- Fixed the Docker Desktop Dashboard trying at startup to get disk usage information and display an error banner before the engine was running.
- Added an informational banner with instructions on how to opt-out of experimental feature access next to all experimental features.
- Docker Desktop now supports downloading Kubernetes images via an HTTP proxy.
- Fixed tooltips to not block action buttons. Fixes [docker/for-mac#6516](https://github.com/docker/for-mac/issues/6516).
- Fixed the blank "An error occurred" container list on the **Container** view.

#### For Mac

- Minimum OS version to install or update Docker Desktop on macOS is now macOS Big Sur (version 11) or later.
- Fixed the Docker engine not starting when Enhanced Container Isolation is enabled if the legacy `osxfs` implementation is used for file sharing.
- Fixed files created on VirtioFS having the executable bit set. Fixes [docker/for-mac#6614](https://github.com/docker/for-mac/issues/6614).
- Added back a way to uninstall Docker Desktop from the command line. Fixes [docker/for-mac#6598](https://github.com/docker/for-mac/issues/6598).
- Fixed hardcoded `/usr/bin/kill`. Fixes [docker/for-mac#6589](https://github.com/docker/for-mac/issues/6589).
- Fixed truncation (for example with the `truncate` command) of very large files (> 38GB) shared on VirtioFS with an incorrect size.
- Changed the disk image size in **Settings** to use the decimal system (base 10) to coincide with how Finder displays disk capacity.
- Fixed Docker crash under network load. Fixes [docker/for-mac#6530](https://github.com/docker/for-mac/issues/6530).
- Fixed an issue causing Docker to prompt the user to install the `/var/run/docker.sock` symlink after every reboot.
- Ensured the Login Item which installs the `/var/run/docker.sock` symlink is signed.
- Fixed bug where `$HOME/.docker` was removed on factory reset.

### For Windows

- Fixed `docker build` hanging while printing "load metadata for". Fixes [docker/for-win#10247](https://github.com/docker/for-win/issues/10247).
- Fixed typo in diagnose.exe output Fixes [docker/for-win#13107](https://github.com/docker/for-win/issues/13107).
- Added support for running under cgroupv2 on WSL 2. This is activated by adding `kernelCommandLine = systemd.unified_cgroup_hierarchy=1 cgroup_no_v1=all` to your `%USERPROFILE%\.wslconfig` file in the `[wsl2]` section.

### Known Issues

- Calling `sudo` inside a container fails with a security related error for some images. See [docker/for-mac/6675](https://github.com/docker/for-mac/issues/6675) and [docker/for-win/13161](https://github.com/docker/for-win/issues/13161).

## 4.15.0

{{< release-date date="2022-12-01" >}}

### New

- Substantial performance improvements for macOS users with the option of enabling the new VirtioFS file sharing technology. Available for macOS 12.5 and above.
- Docker Desktop for Mac no longer needs to install the privileged helper process `com.docker.vmnetd` on install or on the first run. For more information see [Permission requirements for Mac](https://docs.docker.com/desktop/mac/permission-requirements/).
- Added [WebAssembly capabilities](/manuals/desktop/features/wasm.md). Use with the [containerd integration](/manuals/desktop/features/containerd.md).
- Improved the descriptions for beta and experimental settings to clearly explain the differences and how people can access them.
- Available disk space of VM now displays in the footer of Docker Desktop Dashboard for Mac and Linux.
- A disk space warning now displays in the footer if available space is below 3GB.
- Changes to Docker Desktop's interface as we become more ADA accessible and visually unified.
- Added a **Build** tab inside **Extensions** which contains all the necessary resources to build an extension.
- Added the ability to share extensions more easily, either with `docker extension share` CLI or with the share button in the extensions **Manage** tab.
- Extensions in the Marketplace now display the number of installs. You can also sort extensions by the number of installs.
- Dev Environments allow cloning a Git repository to a local bind mount, so you can use any local editor or IDE.
- More Dev Environments improvements: custom names, better private repo support, improved port handling.

### Upgrades

- [Compose v2.13.0](https://github.com/docker/compose/releases/tag/v2.13.0)
- [Containerd v1.6.10](https://github.com/containerd/containerd/releases/tag/v1.6.10)
- [Docker Hub Tool v0.4.5](https://github.com/docker/hub-tool/releases/tag/v0.4.5)
- [Docker Scan v0.22.0](https://github.com/docker/scan-cli-plugin/releases/tag/v0.22.0)

### Bug fixes and enhancements

#### For all platforms

- Containers are now restored on restart with the containerd integration.
- Fixed listing multi-platform images with the containerd integration.
- Better handling of dangling images with the containerd integration.
- Implement "reference" filter for images with the containerd integration.
- Added support for selecting upstream HTTP/HTTPS proxies automatically via `proxy.pac` in containers, `docker pull` etc.
- Fixed regressions when parsing image references on pull. Fixes [docker/for-win#13053](https://github.com/docker/for-win/issues/13053), [docker/for-mac#6560](https://github.com/docker/for-mac/issues/6560), and [docker/for-mac#6540](https://github.com/docker/for-mac/issues/6540).

#### For Mac

- Improved the performance of `docker pull`.

#### For Windows

- Fixed an issue where the system HTTP proxies were not used when Docker starts and the developer logs in.
- When Docker Desktop is using "system" proxies and if the Windows settings change, Docker Desktop now uses the new Windows settings without a restart.

#### For Linux

- Fixed hot-reload issue on Linux. Fixes [docker/desktop-linux#30](https://github.com/docker/desktop-linux/issues/30).
- Disabled tray icon animations on Linux which fixes crashes for some users.

## 4.14.1

{{< release-date date="2022-11-17" >}}

### Bug fixes and enhancements

#### For all platforms

- Fixed container DNS lookups when using Registry Access Management.

#### For Mac

- Fixed an issue preventing the **Analyze Image** button on the **Images** tab from working.
- Fixed a bug causing symlinks to not be created for the user if `/usr/local/lib` doesn't already exist. Fixes [docker/for-mac#6569](https://github.com/docker/for-mac/issues/6569)

## 4.14.0

{{< release-date date="2022-11-10" >}}

### New

- Set Virtualization framework as the default hypervisor for macOS >= 12.5.
- Migrate previous install to Virtualization framework hypervisor for macOS >= 12.5.
- The Enhanced Container Isolation feature, available to Docker Business users, can now be enabled from the General Settings.

### Updates

- [Docker Engine v20.10.21](/manuals/engine/release-notes/20.10.md#201021),
  which contains mitigations against a Git vulnerability, tracked in [CVE-2022-39253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39253),
  and updates the handling of `image:tag@digest` image references.
- [Docker Compose v2.12.2](https://github.com/docker/compose/releases/tag/v2.12.2)
- [Containerd v1.6.9](https://github.com/containerd/containerd/releases/tag/v1.6.9)
- [Go 1.19.3](https://github.com/golang/go/releases/tag/go1.19.3)

### Bug fixes and enhancements

#### For all platforms

- Docker Desktop now requires an internal network subnet of size /24. If you were previously using a /28, it is automatically expanded to /24. If you experience networking issues, check to see if you have a clash between the Docker subnet and your infrastructure. Fixes [docker/for-win#13025](https://github.com/docker/for-win/issues/13025).
- Fixed an issue that prevents users from creating Dev Environments when the Git URL has upper-case characters.
- Fix the `vpnkit.exe is not running` error reported in diagnostics.
- Reverted qemu to 6.2.0 to fix errors like `PR_SET_CHILD_SUBREAPER is unavailable` when running emulated amd64 code.
- Enabled [contextIsolation](https://www.electronjs.org/docs/latest/tutorial/context-isolation) and [sandbox](https://www.electronjs.org/docs/latest/tutorial/sandbox) mode inside Extensions. Now Extensions run in a separate context and this limits the harm that malicious code can cause by limiting access to most system resources.
- Included `unpigz` to allow parallel decompression of pulled images.
- Fixed issues related to performing actions on selected containers. [Fixes https://github.com/docker/for-win/issues/13005](https://github.com/docker/for-win/issues/13005)
- Added functionality that allows you to display timestamps for your container or project view.
- Fixed a possible segfault when interrupting `docker pull` with Control+C.
- Increased the default DHCP lease time to avoid the VM's network glitching and dropping connections every two hours.
- Removed the infinite spinner on the containers list. [Fixes https://github.com/docker/for-mac/issues/6486](https://github.com/docker/for-mac/issues/6486)
- Fixed bug which showed incorrect values on used space in **Settings**.
- Fixed a bug that caused Kubernetes not to start with the containerd integration.
- Fixed a bug that caused `kind` not to start with the containerd integration.
- Fixed a bug that caused Dev Environments to not work with the containerd integration.
- Implemented `docker diff` in the containerd integration.
- Implemented `docker run —-platform` in the containerd integration.
- Fixed a bug that caused insecure registries not to work with the containerd integration.

#### For Mac

- Fixed a startup failure for users of Virtualization framework.
- Re-added the `/var/run/docker.sock` on Mac by default, to increase compatibility with tooling like `tilt` and `docker-py.`
- Fixed an issue that prevented the creation of Dev Environments on new Mac installs (error "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?").

#### For Windows

- Re-added `DockerCli.exe -SharedDrives`. Fixes [docker/for-win#5625](https://github.com/docker/for-win#5625).
- Docker Desktop now allows Docker to function on machines where PowerShell is disabled.
- Fixed an issue where Compose v2 was not always enabled by default on Windows.
- Docker Desktop now deletes the `C:\Program Files\Docker` folder at uninstall.

### Known Issues

- For some users on Mac OS there is a known issue with the installer that prevents the installation of a new helper tool needed for the experimental vulnerability and package discovery feature in Docker Desktop. To fix this, a symlink is needed that can be created with the following command: `sudo ln -s /Applications/Docker.app/Contents/Resources/bin/docker-index /usr/local/bin/docker-index`

## 4.13.1

{{< release-date date="2022-10-31" >}}

### Updates

- [Docker Compose v2.12.1](https://github.com/docker/compose/releases/tag/v2.12.1)

### Bug fixes and enhancements

#### For all platforms

- Fixed a possible segfault when interrupting `docker pull` with `Control+C` or `CMD+C`.
- Increased the default DHCP lease time to avoid the VM's network glitching and dropping connections every two hours.
- Reverted `Qemu` to `6.2.0` to fix errors like `PR_SET_CHILD_SUBREAPER is unavailable` when running emulated amd64 code.

#### For Mac

- Added back the `/var/run/docker.sock` symlink on Mac by default, to increase compatibility with tooling like `tilt` and `docker-py`. Fixes [docker/for-mac#6529](https://github.com/docker/for-mac/issues/6529).
- Fixed an issue preventing the creation of Dev Environments on new Mac installs and causing `error "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?")`

#### For Windows

- Docker Desktop now functions on machines where PowerShell is disabled.

## 4.13.0

{{< release-date date="2022-10-19" >}}

### New

- Two new security features have been introduced for Docker Business users, Settings Management and Enhanced Container Isolation. Read more about Docker Desktop’s new [Hardened Docker Desktop security model](/manuals/enterprise/security/hardened-desktop/_index.md).
- Added the new Dev Environments CLI `docker dev`, so you can create, list, and run Dev Envs via command line. Now it's easier to integrate Dev Envs into custom scripts.
- Docker Desktop can now be installed to any drive and folder using the `--installation-dir`. Partially addresses [docker/roadmap#94](https://github.com/docker/roadmap/issues/94).

### Updates

- [Docker Scan v0.21.0](https://github.com/docker/scan-cli-plugin/releases/tag/v0.21.0)
- [Go 1.19.2](https://github.com/golang/go/releases/tag/go1.19.2) to address [CVE-2022-2879](https://www.cve.org/CVERecord?id=CVE-2022-2879), [CVE-2022-2880](https://www.cve.org/CVERecord?id=CVE-2022-2880) and [CVE-2022-41715](https://www.cve.org/CVERecord?id=CVE-2022-41715)
- Updated Docker Engine and Docker CLI to [v20.10.20](/manuals/engine/release-notes/20.10.md#201020),
  which contain mitigations against a Git vulnerability, tracked in [CVE-2022-39253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39253),
  and updated handling of `image:tag@digest` image references, as well as a fix for [CVE-2022-36109](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36109).
- [Docker Credential Helpers v0.7.0](https://github.com/docker/docker-credential-helpers/releases/tag/v0.7.0)
- [Docker Compose v2.12.0](https://github.com/docker/compose/releases/tag/v2.12.0)
- [Kubernetes v1.25.2](https://github.com/kubernetes/kubernetes/releases/tag/v1.25.2)
- [Qemu 7.0.0](https://wiki.qemu.org/ChangeLog/7.0) used for cpu emulation, inside the Docker Desktop VM.
- [Linux kernel 5.15.49](https://hub.docker.com/layers/docker/for-desktop-kernel/5.15.49-13422a825f833d125942948cf8a8688cef721ead/images/sha256-ebf1f6f0cb58c70eaa260e9d55df7c43968874d62daced966ef6a5c5cd96b493?context=explore)

### Bug fixes and enhancements

#### For all platforms

- Docker Desktop now allows the use of TLS when talking to HTTP and HTTPS proxies to encrypt proxy usernames and passwords.
- Docker Desktop now stores HTTP and HTTPS proxy passwords in the OS credential store.
- If Docker Desktop detects that the HTTP or HTTPS proxy password has changed then it will prompt developers for the new password.
- The **Bypass proxy settings for these hosts and domains** setting now handles domain names correctly for HTTPS.
- The **Remote Repositories** view and Tip of the Day now works with HTTP and HTTPS proxies which require authentication
- We’ve introduced dark launch for features that are in early stages of the product development lifecycle. Users that are opted in can opt out at any time in the settings under the “beta features” section.
- Added categories to the Extensions Marketplace.
- Added an indicator in the whale menu and on the **Extension** tab on when extension updates are available.
- Fixed failing uninstalls of extensions with image names that do not have a namespace, as in 'my-extension'.
- Show port mapping explicitly in the **Container** tab.
- Changed the refresh rate for disk usage information for images to happen automatically once a day.
- Made the tab style consistent for the **Container** and **Volume** tabs.
- Fixed Grpcfuse filesharing mode enablement in **Settings**. Fixes [docker/for-mac#6467](https://github.com/docker/for-mac/issues/6467)
- Virtualization Framework and VirtioFS are disabled for users running macOS < 12.5.
- Ports on the **Containers** tab are now clickable.
- The Extensions SDK now allows `ddClient.extension.vm.cli.exec`, `ddClient.extension.host.cli.exec`, `ddClient.docker.cli.exec` to accept a different working directory and pass environment variables through the options parameters.
- Added a small improvement to navigate to the Extensions Marketplace when clicking on **Extensions** in the sidebar.
- Added a badge to identify new extensions in the Marketplace.
- Fixed kubernetes not starting with the containerd integration.
- Fixed `kind` not starting with the containerd integration.
- Fixed dev environments not working with the containerd integration.
- Implemented `docker diff` in the containerd integration.
- Implemented `docker run —-platform` in the containerd integration.
- Fixed insecure registries not working with the containerd integration.
- Fixed a bug that showed incorrect values on used space in **Settings**.
- Docker Desktop now installs credential helpers from Github releases. See [docker/for-win#10247](https://github.com/docker/for-win/issues/10247), [docker/for-win#12995](https://github.com/docker/for-win/issues/12995).
- Fixed an issue where users were logged out of Docker Desktop after 7 days.

#### For Mac

- Added **Hide**, **Hide others**, **Show all** menu items for Docker Desktop. See [docker/for-mac#6446](https://github.com/docker/for-mac/issues/6446).
- Fixed a bug which caused the application to be deleted when running the install utility from the installed application. Fixes [docker/for-mac#6442](https://github.com/docker/for-mac/issues/6442).
- By default Docker will not create the /var/run/docker.sock symlink on the host and use the docker-desktop CLI context instead.

#### For Linux

- Fixed a bug that prevented pushing images from the Dashboard

## 4.12.0

{{< release-date date="2022-09-01" >}}

### New

- Added the ability to use containerd for pulling and storing images. This is an experimental feature.
- Docker Desktop now runs untagged images. Fixes [docker/for-mac#6425](https://github.com/docker/for-mac/issues/6425).
- Added search capabilities to Docker Extension's Marketplace. Fixes [docker/roadmap#346](https://github.com/docker/roadmap/issues/346).
- Added the ability to zoom in, out or set Docker Desktop to Actual Size. This is done by using keyboard shortcuts ⌘ + / CTRL +, ⌘ - / CTRL -, ⌘ 0 / CTRL 0 on Mac and Windows respectively, or through the View menu on Mac.
- Added compose stop button if any related container is stoppable.
- Individual compose containers are now deletable from the **Container** view.
- Removed the workaround for virtiofsd <-> qemu protocol mismatch on Fedora 35, as it is no longer needed. Fedora 35 users should upgrade the qemu package to the most recent version (qemu-6.1.0-15.fc35 as of the time of writing).
- Implemented an integrated terminal for containers.
- Added a tooltip to display the link address for all external links by default.

### Updates

- [Docker Compose v2.10.2](https://github.com/docker/compose/releases/tag/v2.10.2)
- [Docker Scan v0.19.0](https://github.com/docker/scan-cli-plugin/releases/tag/v0.19.0)
- [Kubernetes v1.25.0](https://github.com/kubernetes/kubernetes/releases/tag/v1.25.0)
- [Go 1.19](https://github.com/golang/go/releases/tag/go1.19)
- [cri-dockerd v0.2.5](https://github.com/Mirantis/cri-dockerd/releases/tag/v0.2.5)
- [Buildx v0.9.1](https://github.com/docker/buildx/releases/tag/v0.9.1)
- [containerd v1.6.8](https://github.com/containerd/containerd/releases/tag/v1.6.8)
- [containerd v1.6.7](https://github.com/containerd/containerd/releases/tag/v1.6.7)
- [runc v1.1.4](https://github.com/opencontainers/runc/releases/tag/v1.1.4)
- [runc v1.1.3](https://github.com/opencontainers/runc/releases/tag/v1.1.3)

### Security

#### For all platforms

- Fixed [CVE-2023-0626](https://www.cve.org/cverecord?id=CVE-2023-0626) which allows RCE via query parameters in the message-box route in the Electron client.
- Fixed [CVE-2023-0625](https://www.cve.org/cverecord?id=CVE-2023-0625) which allows RCE via extension description/changelog which could be abused by a malicious extension.

#### For Windows

- Fixed [CVE-2023-0627](https://www.cve.org/cverecord?id=CVE-2023-0627) which allows to bypass for the `--no-windows-containers` installation flag which was introduced in version 4.11. This flag allows administrators to disable the use of Windows containers.
- Fixed [CVE-2023-0633](https://www.cve.org/cverecord?id=CVE-2023-0633) in which an argument injection to the Docker Desktop installer which may result in local privilege escalation.

### Bug fixes and minor enhancements

#### For all platforms

- Compose V2 is now enabled after factory reset.
- Compose V2 is now enabled by default on new installations of Docker Desktop.
- Precedence order of environment variables in Compose is more consistent, and clearly [documented](/manuals/compose/how-tos/environment-variables/envvars-precedence.md).
- Upgraded kernel to 5.10.124.
- Improved overall performance issues caused by calculating disk size. Related to [docker/for-win#9401](https://github.com/docker/for-win/issues/9401).
- Docker Desktop now prevents users on ARM macs without Rosetta installed from switching back to Compose V1, which has only intel binaries.
- Changed the default sort order to descending for volume size and the **Created** column, along with the container's **Started** column.
- Re-organized container row actions by keeping only the start/stop and delete actions visible at all times, while allowing access to the rest via the row menu item.
- The Quickstart guide now runs every command immediately.
- Defined the sort order for container/compose **Status** column to running > some running > paused > some paused > exited > some exited > created.
- Fixed issues with the image list appearing empty in Docker Desktop even though there are images. Related to [docker/for-win#12693](https://github.com/docker/for-win/issues/12693) and [docker/for-mac#6347](https://github.com/docker/for-mac/issues/6347).
- Defined what images are "in use" based on whether or not system containers are displayed. If system containers related to Kubernetes and Extensions are not displayed, the related images are not defined as "in use."
- Fixed a bug that made Docker clients in some languages hang on `docker exec`. Fixes [https://github.com/apocas/dockerode/issues/534](https://github.com/apocas/dockerode/issues/534).
- A failed spawned command when building an extension no longer causes Docker Desktop to unexpectedly quit.
- Fixed a bug that caused extensions to be displayed as disabled in the left menu when they are not.
- Fixed `docker login` to private registries when Registry Access Management is enabled and access to Docker Hub is blocked.
- Fixed a bug where Docker Desktop fails to start the Kubernetes cluster if the current cluster metadata is not stored in the `.kube/config` file.
- Updated the tooltips in Docker Desktop and MUI theme package to align with the overall system design.
- Copied terminal contents do not contain non-breaking spaces anymore.

#### For Mac

- Minimum version to install or update Docker Desktop on macOS is now 10.15. Fixes [docker/for-mac#6007](https://github.com/docker/for-mac/issues/6007).
- Fixed a bug where the Tray menu incorrectly displays "Download will start soon..." after downloading the update. Fixes some issue reported in [for-mac/issues#5677](https://github.com/docker/for-mac/issues/5677)
- Fixed a bug that didn't restart Docker Desktop after applying an update.
- Fixed a bug that caused the connection to Docker to be lost when the computer sleeps if a user is using virtualization.framework and restrictive firewall software.
- Fixed a bug that caused Docker Desktop to run in the background even after a user had quit the application. Fixes [docker/for-mac##6440](https://github.com/docker/for-mac/issues/6440)
- Disabled both Virtualization Framework and VirtioFS for users running macOS < 12.5

#### For Windows

- Fixed a bug where versions displayed during an update could be incorrect. Fixes [for-win/issues#12822](https://github.com/docker/for-win/issues/12822).

## 4.11.1

{{< release-date date="2022-08-05" >}}

### Bug fixes and enhancements

#### For all platforms

- Fixed regression preventing VM system locations (e.g. /var/lib/docker) from being bind mounted [for-mac/issues#6433](https://github.com/docker/for-mac/issues/6433)

#### For Windows

- Fixed `docker login` to private registries from WSL2 distribution [docker/for-win#12871](https://github.com/docker/for-win/issues/12871)

## 4.11.0

{{< release-date date="2022-07-28" >}}

### New

- Docker Desktop is now fully supported for Docker Business customers inside VMware ESXi and Azure VMs. For more information, see [Run Docker Desktop inside a VM or VDI environment](/manuals/desktop/setup/vm-vdi.md)
- Added two new extensions ([vcluster](https://hub.docker.com/extensions/loftsh/vcluster-dd-extension) and [PGAdmin4](https://hub.docker.com/extensions/mochoa/pgadmin4-docker-extension)) to the Extensions Marketplace.
- The ability to sort extensions has been added to the Extensions Marketplace.
- Fixed a bug that caused some users to be asked for feedback too frequently. You'll now only be asked for feedback twice a year.
- Added custom theme settings for Docker Desktop. This allows you to specify dark or light mode for Docker Desktop independent of your device settings. Fixes [docker/for-win#12747](https://github.com/docker/for-win/issues/12747)
- Added a new flag for Windows installer. `--no-windows-containers` disables the Windows containers integration.
- Added a new flag for Mac install command. `--user <username>` sets up Docker Desktop for a specific user, preventing them from needing an admin password on first run.

### Updates

- [Docker Compose v2.7.0](https://github.com/docker/compose/releases/tag/v2.7.0)
- [Docker Compose "Cloud Integrations" v1.0.28](https://github.com/docker/compose-cli/releases/tag/v1.0.28)
- [Kubernetes v1.24.2](https://github.com/kubernetes/kubernetes/releases/tag/v1.24.2)
- [Go 1.18.4](https://github.com/golang/go/releases/tag/go1.18.4)

### Bug fixes and enhancements

#### For all platforms

- Added the Container / Compose icon as well as the exposed port(s) / exit code to the Containers screen.
- Updated the Docker theme palette colour values to match our design system.
- Improved an error message from `docker login` if Registry Access Management is blocking the Docker engine's access to Docker Hub.
- Increased throughput between the Host and Docker. For example increasing performance of `docker cp`.
- Collecting diagnostics takes less time to complete.
- Selecting or deselecting a compose app on the containers overview now selects/deselects all its containers.
- Tag names on the container overview image column are visible.
- Added search decorations to the terminal's scrollbar so that matches outside the viewport are visible.
- Fixed an issue with search which doesn't work well on containers page [docker/for-win#12828](https://github.com/docker/for-win/issues/12828).
- Fixed an issue which caused infinite loading on the **Volume** screen [docker/for-win#12789](https://github.com/docker/for-win/issues/12789).
- Fixed a problem in the Container UI where resizing or hiding columns didn't work. Fixes [docker/for-mac#6391](https://github.com/docker/for-mac/issues/6391).
- Fixed a bug where the state of installing, updating, or uninstalling multiple extensions at once was lost when leaving the Marketplace screen.
- Fixed an issue where the compose version in the about page would only get updated from v2 to v1 after restarting Docker Desktop.
- Fixed an issue where users cannot see the log view because their underlying hardware didn't support WebGL2 rendering. Fixes [docker/for-win#12825](https://github.com/docker/for-win/issues/12825).
- Fixed a bug where the UI for Containers and Images got out of sync.
- Fixed a startup race when the experimental virtualization framework is enabled.

#### For Mac

- Fixed an issue executing Compose commands from the UI. Fixes [docker/for-mac#6400](https://github.com/docker/for-mac/issues/6400).

#### For Windows

- Fixed horizontal resizing issue. Fixes [docker/for-win#12816](https://github.com/docker/for-win/issues/12816).
- If an HTTP/HTTPS proxy is configured in the UI, then it automatically sends traffic from image builds and running containers to the proxy. This avoids the need to separately configure environment variables in each container or build.
- Added the `--backend=windows` installer option to set Windows containers as the default backend.

#### For Linux

- Fixed bug related to setting up file shares with spaces in their path.

## 4.10.1

{{< release-date date="2022-07-05" >}}

### Bug fixes and enhancements

#### For Windows

- Fixed a bug where actions in the UI failed with Compose apps that were created from WSL. Fixes [docker/for-win#12806](https://github.com/docker/for-win/issues/12806).

#### For Mac

- Fixed a bug where the install command failed because paths were not initialized. Fixes [docker/for-mac#6384](https://github.com/docker/for-mac/issues/6384).

## 4.10.0

{{< release-date date="2022-06-30" >}}

### New

- You can now add environment variables before running an image in Docker Desktop.
- Added features to make it easier to work with a container's logs, such as regular expression search and the ability to clear container logs while the container is still running.
- Implemented feedback on the containers table. Added ports and separated container and image names.
- Added two new extensions, Ddosify and Lacework, to the Extensions Marketplace.

### Removed

- Removed Homepage while working on a new design. You can provide [feedback here](https://docs.google.com/forms/d/e/1FAIpQLSfYueBkJHdgxqsWcQn4VzBn2swu4u_rMQRIMa8LExYb_72mmQ/viewform?entry.1237514594=4.10).

### Updates

- [Docker Engine v20.10.17](/manuals/engine/release-notes/20.10.md#201017)
- [Docker Compose v2.6.1](https://github.com/docker/compose/releases/tag/v2.6.1)
- [Kubernetes v1.24.1](https://github.com/kubernetes/kubernetes/releases/tag/v1.24.1)
- [cri-dockerd to v0.2.1](https://github.com/Mirantis/cri-dockerd/releases/tag/v0.2.1)
- [CNI plugins to v1.1.1](https://github.com/containernetworking/plugins/releases/tag/v1.1.1)
- [containerd to v1.6.6](https://github.com/containerd/containerd/releases/tag/v1.6.6)
- [runc to v1.1.2](https://github.com/opencontainers/runc/releases/tag/v1.1.2)
- [Go 1.18.3](https://github.com/golang/go/releases/tag/go1.18.3)

### Bug fixes and enhancements

#### For all platforms

- Added additional bulk actions for starting/pausing/stopping selected containers in the **Containers** tab.
- Added pause and restart actions for compose projects in the **Containers** tab.
- Added icons and exposed ports or exit code information in the **Containers** tab.
- External URLs can now refer to extension details in the Extension Marketplace using links such as `docker-desktop://extensions/marketplace?extensionId=docker/logs-explorer-extension`.
- The expanded or collapsed state of the Compose apps is now persisted.
- `docker extension` CLI commands are available with Docker Desktop by default.
- Increased the size of the screenshots displayed in the Extension marketplace.
- Fixed a bug where a Docker extension fails to load if its backend container(s) are stopped. Fixes [docker/extensions-sdk#16](https://github.com/docker/extensions-sdk/issues/162).
- Fixed a bug where the image search field is cleared without a reason. Fixes [docker/for-win#12738](https://github.com/docker/for-win/issues/12738).
- Fixed a bug where the license agreement does not display and silently blocks Docker Desktop startup.
- Fixed the displayed image and tag for unpublished extensions to actually display the ones from the installed unpublished extension.
- Fixed the duplicate footer on the Support screen.
- Dev Environments can be created from a subdirectory in a GitHub repository.
- Removed the error message if the tips of the day cannot be loaded when using Docker Desktop offline. Fixes [docker/for-mac#6366](https://github.com/docker/for-mac/issues/6366).

#### For Mac

- Fixed a bug with location of bash completion files on macOS. Fixes [docker/for-mac#6343](https://github.com/docker/for-mac/issues/6343).
- Fixed a bug where Docker Desktop does not start if the username is longer than 25 characters. Fixes [docker/for-mac#6122](https://github.com/docker/for-mac/issues/6122).
- Fixed a bug where Docker Desktop was not starting due to invalid system proxy configuration. Fixes some issues reported in [docker/for-mac#6289](https://github.com/docker/for-mac/issues/6289).
- Fixed a bug where Docker Desktop failed to start when the experimental virtualization framework is enabled.
- Fixed a bug where the tray icon still displayed after uninstalling Docker Desktop.

#### For Windows

- Fixed a bug which caused high CPU usage on Hyper-V. Fixes [docker/for-win#12780](https://github.com/docker/for-win/issues/12780).
- Fixed a bug where Docker Desktop for Windows would fail to start. Fixes [docker/for-win#12784](https://github.com/docker/for-win/issues/12784).
- Fixed the `--backend=wsl-2` installer flag which did not set the backend to WSL 2. Fixes [docker/for-win#12746](https://github.com/docker/for-win/issues/12746).

#### For Linux

- Fixed a bug when settings cannot be applied more than once.
- Fixed Compose version displayed in the `About` screen.

### Known Issues

- Occasionally the Docker engine will restart during a `docker system prune`. This is a [known issue](https://github.com/moby/buildkit/pull/2177) in the version of buildkit used in the current engine and will be fixed in future releases.

