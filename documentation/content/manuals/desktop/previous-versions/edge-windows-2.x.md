---
title: Docker Desktop for Windows Edge 2.x release notes
linkTitle: Windows Edge 2.x
toc_max: 3
sitemap: false
---

## Related guidance

- [Historical Edge release caveats and update prerequisites](/manuals/desktop/release-availability.md#historical-edge-releases)
- [Historical upgrade and update procedures](upgrade-guidance.md)

## Docker Desktop Community 2.5.4
2020-12-07


### Upgrades

- [Docker Engine 20.10.0-rc2](https://github.com/docker/docker-ce/blob/master/CHANGELOG.md#20100)
- [Go 1.15.6](https://github.com/golang/go/issues?q=milestone%3AGo1.15.6+label%3ACherryPickApproved+)

### Bug fixes and minor changes

- Fixed an issue causing the background update to fail when the current user is not an administrator.
- Downgraded the kernel to [4.19.121](https://hub.docker.com/layers/docker/for-desktop-kernel/4.19.121-2a1dbedf3f998dac347c499808d7c7e029fbc4d3-amd64/images/sha256-4e7d94522be4f25f1fbb626d5a0142cbb6e785f37e437f6fd4285e64a199883a?context=repo) to reduce the CPU usage of hyperkit. Fixes [docker/for-mac#5044](https://github.com/docker/for-mac/issues/5044)

## Docker Desktop Community 2.5.3
2020-11-30


### Upgrades

- [Compose CLI v1.0.3](https://github.com/docker/compose-cli/releases/tag/v1.0.3)

## Docker Desktop Community 2.5.2
2020-11-26


### New

- Use of three digit version number.
- Starting with Docker Desktop 2.5.2, updates will be much smaller as they will be applied using delta patches.

### Bug fixes and minor changes

- Fixed an unexpected EOF error when trying to start a non-existing container with `-v /var/run/docker.sock:`. See [docker/for-mac#5025](https://github.com/docker/for-mac/issues/5025).

## Docker Desktop Community 2.5.1.0
2020-11-18


This release contains a Kubernetes upgrade. Note that your local Kubernetes cluster will be reset after installing Docker Desktop.

### Upgrades

- [Docker Engine 20.10.0-rc1](https://github.com/docker/docker-ce/blob/master/CHANGELOG.md#20100)
- [Compose CLI v1.0.2](https://github.com/docker/compose-cli/releases/tag/v1.0.2)
- [Snyk v1.424.4](https://github.com/snyk/snyk/releases/tag/v1.424.4)
- [Kubernetes 1.19.3](https://github.com/kubernetes/kubernetes/releases/tag/v1.19.3)

### Bug fixes and minor changes

- Renamed 'Run Diagnostics' to 'Get support'.
- Fixed an issue with the WSL 2 backend where some network plugins may fail to load, provoking a crash of the Docker daemon.
- Fixed an unexpected EOF error when trying to start a non-existing container. See [docker/for-mac#5025](https://github.com/docker/for-mac/issues/5025).

## Docker Desktop Community 2.4.2.0
2020-10-19


### New

- If you have enabled [Vulnerability Scanning](../../docker-hub/repos/manage/vulnerability-scanning.md) in Docker Hub, the scan results will now appear in Docker Desktop.

### Upgrades

- [Docker Engine 20.10.0 beta1](https://github.com/docker/docker-ce/blob/0fc7084265b3786a5867ec311d3f916af7bf7a23/CHANGELOG.md)
- [Docker Compose CLI - 0.1.22](https://github.com/docker/compose-cli/releases/tag/v0.1.22)
- [Linux kernel 5.4.39](https://hub.docker.com/layers/linuxkit/kernel/5.4.39-f39f83d0d475b274938c86eaa796022bfc7063d2/images/sha256-8614670219aca0bb276d4749e479591b60cd348abc770ac9ecd09ee4c1575405?context=explore)
- [Kubernetes 1.19.2](https://github.com/kubernetes/kubernetes/releases/tag/v1.19.2)
- [Go 1.15.2](https://github.com/golang/go/issues?q=milestone:Go1.15.2+label:CherryPickApproved)

* Deprecation
  - Docker Desktop cannot be installed on Windows 1703 (build 15063) anymore.

### Bug fixes and minor changes

- Fixed an issue that can intermittently cause the WSL 2 backend to fail to start.
- Fixed an issue related to NFS mounting. See [docker/for-mac#4958](https://github.com/docker/for-mac/issues/4958).
- Fixed an issue with http proxy exclude lists containing entries such as `localhost` or `127.0.0.1`. Fixes [docker/for-win#8750](https://github.com/docker/for-win/issues/8750).
- When WSL integration process unexpectedly stops, the user is now notified and can decide to restart it or not, instead of always try to restart it in a loop. fixes [docker/for-win#8968](https://github.com/docker/for-win/issues/8968).
- Fixed an issue related to container logs that lag under heavy load. Fixes [docker/for-win#8216](https://github.com/docker/for-win/issues/8216).
- Diagnostics: avoid hanging when Kubernetes is in a broken state.
- When sharing a file into a container (e.g. `docker run -v ~/.gitconfig`) Docker Desktop does not watch the parent directory. Fixes [docker/for-mac#4981](https://github.com/docker/for-mac/issues/4981).
- Always flush file system caches synchronously on container start. See [docker/for-mac#4943](https://github.com/docker/for-mac/issues/4943).

## Docker Desktop Community 2.4.1.0
2020-10-01


### Upgrades

- [Docker Compose CLI - 0.1.18](https://github.com/docker/compose-cli)
- [Docker Compose 1.27.4](https://github.com/docker/compose/releases/tag/1.27.4)
- [Snyk v1.399.1](https://github.com/snyk/snyk/releases/tag/v1.399.1)
- [Docker Engine 19.03.13](https://github.com/docker/docker-ce/releases/tag/v19.03.13)

### Bug fixes and minor changes

- Fixed the path to the installer log file default location when the username contains a space. Fixes [docker/for-win#7941](https://github.com/docker/for-win/issues/7941).

## Docker Desktop Community 2.3.7.0
2020-09-17


### New

- [Amazon ECR Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper/releases/tag/v0.4.0)

### Upgrades

- [Docker ACI integration 0.1.15](https://github.com/docker/aci-integration-beta/releases/tag/v0.1.15)
- [Snyk v0.393.0](https://github.com/snyk/snyk/releases/tag/v1.393.0)

### Bug fixes and minor changes

**WSL 2**

  - Fixed an issue that intermittently made the backend fail to start.
  - Fixed a proxy crash that happened when glibc was not compatible. See [docker/for-win#8183](https://github.com/docker/for-win/issues/8183).
  - Fixed an issue where restarting Docker Desktop may delete files mounted in a container.
  - Fixed an issue where restarting Docker Desktop truncates files when a single file is mounted in a container. See [docker/for-win#8439](https://github.com/docker/for-win/issues/8439).

**Other fixes**

- Fixed the VM debug shell used for low-level debugging.
- Fixed compatibility with Go 1.15 clients. See [docker/for-mac#4855](https://github.com/docker/for-mac/issues/4855).
- Avoid exposing `/host_mnt` paths in `docker container inspect` and `docker volume inspect`. Fixes [docker/for-mac#4859](https://github.com/docker/for-mac/issues/4859).
- Fixed container logs lagging under heavy load. See [docker/for-win#8216](https://github.com/docker/for-win/issues/8216).

### Known issues

- The `clock_gettime64` system call returns `EPERM` rather than `ENOSYS`
in i386 images. To work around this issue, disable `seccomp` by using
the `--privileged` flag. See [docker/for-win#8326](https://github.com/docker/for-win/issues/8326).

## Docker Desktop Community 2.3.6.2
2020-09-09


### Upgrades

- [Docker Compose 1.27.0](https://github.com/docker/compose/releases/tag/1.27.0)

### Bug fixes and minor changes

- Fixed an issue with mount shadowing in WSL 2. See [docker/for-win#8183](https://github.com/docker/for-win/issues/8183) and [docker/for-win#8316](https://github.com/docker/for-win/issues/8316).

## Docker Desktop Community 2.3.6.0
2020-09-01


### New

- In partnership with Snyk, Docker Desktop launches vulnerability scanning for Docker local images.
- Docker ECS plugin has been replaced by ECS cloud integration
- Docker UI:
  - The Images view now has search and filter options.
  - You can now push an image to Docker Hub using the Remote repositories drop-down menu.

### Upgrades

- [Alpine 3.12](https://alpinelinux.org/posts/Alpine-3.12.0-released.html)
- [Kubernetes 1.18.8](https://github.com/kubernetes/kubernetes/releases/tag/v1.18.8)

### Bug fixes and minor changes

- Fixed an issue with Docker Desktop integration with other WSL 2 distributions. See [docker/for-win#6894](https://github.com/docker/for-win/issues/6894)
- Fixed DNS resolution of short names. See [docker/for-win#4425](https://github.com/docker/for-win/issues/4425)

## Docker Desktop Community 2.3.5.1
2020-08-25


### Bug fixes and minor changes

- Fixed an issue which broke WSL 2 integration when stopping Docker Desktop while containers with bind mounts are present. See [docker/for-win#8164](https://github.com/docker/for-win/issues/8164)

## Docker Desktop Community 2.3.5.0
2020-08-20


### New

- The **Images** view on the Dashboard now allows you to interact with images on Docker Hub. You can now pull a remote repository with specific tags from Docker Hub, or view the details of the repository on the Docker Hub page. To access the new Images view, from the Docker menu, select **Dashboard** > **Images**.

- Docker Desktop now enables BuildKit by default after a reset to factory defaults. To revert to the old docker build experience, go to **Preferences** > **Docker Engine** and then disable the BuildKit feature.

- Docker Desktop now supports running on WSL 2 on the latest updates of Windows 10 versions 1903 and 1909 (in addition to the existing support for version 2004). This also means that Docker Desktop can be installed on those builds of Windows 10 Home.

### Upgrades

- [Go 1.14.7](https://github.com/golang/go/issues?q=milestone:Go1.14.7+label:CherryPickApproved)
- [Docker ECS integration v1.0.0-beta.5](https://github.com/docker/ecs-plugin/releases/tag/v1.0.0-beta.5)
- [Docker Engine 19.03.13-beta2](https://github.com/docker/docker-ce/releases/tag/v19.03.13-beta2)
- [Docker ACI integration 0.1.12](https://github.com/docker/aci-integration-beta/releases/tag/v0.1.12)

### Bug fixes and minor changes

- Moved **Dashboard** to the top of the whale menu.
- The systray icon now responds to dark or light mode. See [docker/for-win#4113](https://github.com/docker/for-win/issues/4113)
- Improved the error handling when `dockerd` crashes.
- Fixed minor bugs in the **Images** view.

## Docker Desktop Community 2.3.4.0
2020-07-28


### New

- Docker Desktop introduces the new **Images** view to the Docker Dashboard. The Images view allows users to view a list of Docker images on the disk, run an image as a container, pull the latest version of an image from Docker Hub, inspect images, and remove any unwanted images from the disk.

  To access the new Images view, from the Docker menu, select **Dashboard** > **Images**.

### Upgrades

- [Docker ECS integration v1.0.0-beta.4](https://github.com/docker/ecs-plugin/releases/tag/v1.0.0-beta.4)
- [Kubernetes 1.18.6](https://github.com/kubernetes/kubernetes/releases/tag/v1.18.6)

### Bug fixes and minor changes

- UI changes to dark or light theme depending on Windows default app mode.
- Copying the container logs from the dashboard does not copy the ANSI color codes to the clipboard anymore.

## Docker Desktop Community 2.3.3.2
2020-07-21


### Upgrades

- [Docker ECS integration v1.0.0-beta.2](https://github.com/docker/ecs-plugin/releases/tag/v1.0.0-beta.2)
- [Docker ACI integration 0.1.10](https://github.com/docker/aci-integration-beta/releases/tag/v0.1.10)

## Docker Desktop Community 2.3.3.1
2020-07-10


### Bug fixes and minor changes

- Fixed a bug where the ECS plugin was not visible from WSL 2.

## Docker Desktop Community 2.3.3.0
2020-07-09


### Upgrades

- Beta release of Docker ECS integration v1.0.0-beta.1.
- [Docker ACI integration v0.1.7](https://github.com/docker/aci-integration-beta/releases/tag/v0.1.7)
- [Docker Compose 1.26.2](https://github.com/docker/compose/releases/tag/1.26.2)

### Bug fixes and minor changes

- Compose-on-Kubernetes is no longer included in the Docker Desktop installer. You can download it separately from the compose-on-kubernetes [release page](https://github.com/docker/compose-on-kubernetes/releases).

## Docker Desktop Community 2.3.2.1
2020-06-29


### Security

- Fixed a regression in Docker Desktop Edge 2.3.2.0 on Windows where the Docker API was exposed by default on a random port on all interfaces.

## Docker Desktop Community 2.3.2.0
2020-06-25

### Upgrades

- [Docker 19.03.12](https://github.com/docker/docker-ce/releases/tag/v19.03.12)
- [Docker Compose 1.26.0](https://github.com/docker/compose/releases/tag/1.26.0)
- [Kubernetes 1.18.3](https://github.com/kubernetes/kubernetes/releases/tag/v1.18.3)
- Beta release of the [Docker ACI integration](/engine/context/aci-integration/)

### Bug fixes and minor changes

- Fixed application startup if `hosts` is specified inside the Docker `daemon.json`. See [docker/for-win#6895](https://github.com/docker/for-win/issues/6895#issuecomment-637429117).
- Fixed opening a CLI from the dashboard for Windows containers. See [docker/for-win#7079](https://github.com/docker/for-win/issues/7079).
- Fixed an issue where adding a folder on a non-existing drive in the settings would create an empty entry. See [docker/for-win#6797](https://github.com/docker/for-win/issues/6797).
- Fixed an issue when updating Windows to a WSL 2 capable version, where a configuration file is locked by the old Hyper-V VM.
- Pinning the application to the taskbar and clicking on it will launch the container view if Docker is already running.
- Left-clicking on the Docker icon in the system tray now launches the container view Dashboard. See [docker/for-win#6650](https://github.com/docker/for-win/issues/6650).
- Fixed an issue which blocks Docker Desktop startup if `localhost:2375` is used by another program. See [docker/for-win#6929](https://github.com/docker/for-win/issues/6929) and [docker/for-win#6961](https://github.com/docker/for-win/issues/6961).
- Docker contexts are now synced between Windows and WSL 2 distributions.
- Docker Desktop now prompts users to share drives for paths like `////c/Users/foo`, rather than only paths like `C:\Users\foo` and `C:/Users/foo`.
- The installer now returns a non-zero exit code on error or when the user cancels the installation.
- Avoid failing withFixed an issue which caused Docker Desktop to fail with `Function not implemented` error during file I/O on shared volumes. See [docker/for-win#5955](https://github.com/docker/for-win/issues/5955).
- Fixed an issue when bind mounting a mounted host directory inside a container. See [docker/for-win#5089](https://github.com/docker/for-win/issues/5089).
- Removed the legacy Kubernetes context `docker-for-desktop`. The context `docker-desktop` should be used instead. See [docker/for-win#5089](https://github.com/docker/for-win/issues/5089).

## Docker Desktop Community 2.3.1.0
2020-05-20


### Upgrades

- [Docker Compose 1.26.0-rc4](https://github.com/docker/compose/releases/tag/1.26.0-rc4)
- Upgrade to Qemu 4.2.0, add Risc-V support

### Bug fixes and minor changes

**Hyper-V**

- Create drive symlinks in VM at startup to avoid breaking setup that was using them. Fixes [docker/for-win#6628](https://github.com/docker/for-win/issues/6628).
- Implement `fallocate` for shared filesystems. See [docker/for-win#6658](https://github.com/docker/for-win/issues/6658#issuecomment-627736820).

**WSL 2**

- Configure CLI to use Docker Desktop credential store.
- Adds a restart button to the popup prompting the user to install the Linux kernel.
- More reliable bootstrap, do not rely on `wslpath` for path translation, retry mounts on errors at startup.

**Dashboard**

- Fixed containers logs which were sometimes truncated. Fixes [docker/for-win#5954](https://github.com/docker/for-win/issues/5954)
- Fixed `open with vs code` button for compose app deployed from a WSL 2 Linux Workspace.

**Other fixes**

- Fixed an installer crash when an old and/or partially uninstalled version of Docker Desktop was present on the system. [Fixes docker/for-win/6536](https://github.com/docker/for-win/issues/6536).
- Fixed home expansion when using tilde in bind mounts source (for example, `-v ~/dir:/vm-dir`)
- `localhost` and `127.0.0.1` can both be used in the proxy settings to redirect to a proxy on the host. Fixes [docker/for-win#5715](https://github.com/docker/for-win/issues/5715).
- Fixed a typo in the backend destroy notification. Fixes [docker/for-win#6739](https://github.com/docker/for-win/issues/6739).
- Fixed a crash which sometimes occurred when Docker Desktop loads a corrupted Docker CLI configuration file. Fixes [docker/for-win#6657](https://github.com/docker/for-win/issues/6657).
- Fixed a delay when opening the systray menu. Fixes [docker/for-win#1011](https://github.com/docker/for-win/issues/1011).

### Known issues

**WSL 2**

- Swarm service bind mounts are not always restored correctly.
- Bind mounts of files living outside of the root mount point (files within `/mnt/c`, `/tmp`, `/run...`) don't work correctly when multiple containers mount them.

## Docker Desktop Community 2.3.0.1
2020-04-28



### Bug fixes and minor changes

- Fixed an upgrade bug where users on versions still using the PowerShell-based VM management experience a silent un-installation crash leading to Docker Desktop being uninstalled instead of upgraded.
- Fixed a crash when failing to login due to no Internet connection.
- Fixed bug in handling shared volume paths with `..` characters. Fixes [docker/for-win#5375](https://github.com/docker/for-win/issues/5375).
- WSL 2: Docker Desktop detects when the wsl-distribution is stopped and displays an actionable error message.
- Fixed a bug in `ftruncate` which prevented [libgit2sharp](https://github.com/libgit2/libgit2sharp) from cloning repositories on shared volumes. See [docker/for-win#5808](https://github.com/docker/for-win/issues/5808#issuecomment-610996272).
- Fixed a bug that caused starting and stopping of a Compose application from the UI to fail when the path contains whitespace.

## Docker Desktop Community 2.3.0.0
2020-04-20



### Upgrades

- [Docker Compose 1.25.5](https://github.com/docker/compose/releases/tag/1.25.5)
- [Go 1.13.10](https://github.com/golang/go/issues?q=milestone%3AGo1.13.10+label%3ACherryPickApproved)
- [Linux kernel 4.19.76](https://hub.docker.com/layers/docker/for-desktop-kernel/4.19.76-ce15f646db9b062dc947cfc0c1deab019fa63f96-amd64/images/sha256-6c252199aee548e4bdc8457e0a068e7d8e81c2649d4c1e26e4150daa253a85d8?context=repo)
- LinuxKit [init](https://hub.docker.com/layers/linuxkit/init/1a80a9907b35b9a808e7868ffb7b0da29ee64a95/images/sha256-64cc8fa50d63940dbaa9979a13c362c89ecb4439bcb3ab22c40d300b9c0b597e?context=explore), [runc](https://hub.docker.com/layers/linuxkit/runc/69b4a35eaa22eba4990ee52cccc8f48f6c08ed03/images/sha256-57e3c7cbd96790990cf87d7b0f30f459ea0b6f9768b03b32a89b832b73546280?context=explore), and [containerd](https://hub.docker.com/layers/linuxkit/containerd/09553963ed9da626c25cf8acdf6d62ec37645412/images/sha256-866be7edb0598430709f88d0e1c6ed7bfd4a397b5ed220e1f793ee9067255ff1?context=explore)

### Bug fixes and minor changes

> Docker Desktop Edge 2.3.0.0 fixes 10 issues reported on the [docker/for-win](https://github.com/docker/for-win/issues) GitHub repository.

**WSL 2**

- Detect when the WSL 2 backend stops and allow the user to restart it.
- Added support for chmod/chown on WSL 2 bind mounts. Fixed [docker/for-win#6284](https://github.com/docker/for-win/issues/6284).
- Fixed a race condition when exposing ports.
- Prevent the WSL 2 dialog from blocking other windows.
- Added a check that virtualization is enabled in the BIOS.

**Filesharing**

- Fixed a bug when parent directories of shared folders are renamed, leading to spurious `File not found` errors. Fixes [docker/for-win#6200](https://github.com/docker/for-win/issues/6200).
- Fixed bug where a letter and two digit root folder name causes Docker Compose to fail creating directories inside the volume. Fixes [docker/for-win#6248](https://github.com/docker/for-win/issues/6248).
- Fixed a bug which prevented containers from seeing file updates on shared volumes, when under load and a container restarts. Fixes [docker/for-win#5530](https://github.com/docker/for-win/issues/5530#issuecomment-608804192)
- Fixed a bug where host paths are incorrectly translated into VM paths. Fixes [docker/for-win#6209](https://github.com/docker/for-win/issues/6209).
- Fixed bug receiving file events on long paths (> 260 characters). Fixes [docker/for-win#6337](https://github.com/docker/for-win/issues/6337).

**Other fixes**

- Fixed a bug where containers disappeared from the UI when Kubernetes context is invalid. Fixes [docker/for-win#6037](https://github.com/docker/for-win/issues/6037).
- Fixed Windows event logs filtering when copying them to the Docker Desktop log files. Fixes [docker/for-win#6258](https://github.com/docker/for-win/issues/6258).
- Fixed a handle leak in `vpnkit-bridge`. Fixed [docker/for-win#5841](https://github.com/docker/for-win/issues/5841)
- Fixed a bug when removing Docker Desktop virtual switch.
- Added a link to the Stable channel from the Docker Desktop UI.
- IPv6 has been re-enabled in the embedded Linux kernel, so listening on IPv6 addresses works again. Fixed [docker/for-win#6206](https://github.com/docker/for-win/issues/6206) and [docker/for-mac#4415](https://github.com/docker/for-mac/issues/4415).
- Made the embedded terminal resizable.
- Fixed a bug which only respected the "expose on TCP" Docker engine API setting on application restart. Setting will now take effect when the Apply button is clicked.
- Fixed a bug where diagnostic upload would fail if the username contained spaces.

## Docker Desktop Community 2.2.3.0
2020-04-02



### Upgrades

- [Docker 19.03.8](https://github.com/docker/docker-ce/releases/tag/v19.03.8)
- [Docker Compose 1.26.0-rc3](https://github.com/docker/compose/releases/tag/1.26.0-rc3)
- [Linux 4.19.76](https://hub.docker.com/layers/docker/for-desktop-kernel/4.19.76-4e5d9e5f3bde0abf236f97e4a81b029ae0f5f6e7-amd64/images/sha256-11dc0f6ee3187088219ba1463ebb378f5093a7d98f176ddfd62dd6b741c2dd2d?context=repo)

### New

- Docker Desktop introduces a new onboarding tutorial upon first startup. The Quick Start tutorial guides users to get started with Docker in a few easy steps. It includes a simple exercise to build an example Docker image, run it as a container, push and save the image to Docker Hub.

### Bug fixes and minor changes

> Docker Desktop Edge 2.2.3.0 fixes 28 issues reported on the [docker/for-win](https://github.com/docker/for-win/issues) GitHub repository.

**WSL 2**
- Docker Desktop only exposes host ports in Linux if the Windows port is available.
- Docker Desktop now allows users to refresh the list of Linux distributions.
- Docker Desktop defaults to WSL 2 on install on compatible OS versions.
- Docker Desktop detects missing Linux kernel and adds a pointer to the Microsoft documentation to download the kernel.

**File sharing**
- Kubernetes: Persistent volumes created by claims are now stored in the virtual machine. Fixes [for-win/issues/5665](https://github.com/docker/for-win/issues/5665).
- Docker Desktop ensures that host paths accessed by containers are within the shared folders list.
- Fixed a bug where opening a read-only file would fail with an `Operation not permitted error`. Fixes [docker/for-win#6016](https://github.com/docker/for-win/issues/6016) and [docker/for-win#6017](https://github.com/docker/for-win/issues/6017).
- Fixed path handling for `docker volume create -o type=none -o o=bind -o device=C:\Some\Windows\path`.
- Fixed a bug which prevented open files from being deleted. Fixes [docker/for-win#5565](https://github.com/docker/for-win/issues/5565).
- Docker Desktop now avoids locking files on the host which are open in containers.
- Docker Desktop generates `fsnotify.WRITE` events in Linux containers when files are changed on the host. [docker/for-win#5530](https://github.com/docker/for-win/issues/5530#issuecomment-585572414)
- Docker Desktop now displays hidden files on shared volumes. Fixes [docker/for-win#5808](https://github.com/docker/for-win/issues/5808).
- Fixed cache invalidation and event injection for shared volumes with long paths.
- Docker Desktop now handles case-insensitivity correctly during file creation.
- Docker Desktop represents valid directory junctions as directories (rather than symlinks) and handles cache invalidation and event injection properly. Fixes [docker/for-win#5582](https://github.com/docker/for-win/issues/5582).
- Fixed a race condition in `readlink` on shared volumes using "mfsymlinks". Fixes [docker/for-win#5793](https://github.com/docker/for-win/issues/5793)
- Fixed a bug where files did not change in shared volumes when using `volumes_from` in docker-compose.yml. Fixes [docker/for-win#5530](https://github.com/docker/for-win/issues/5530).

**Other fixes**
- Reduced the size of the Docker Desktop installer from 960 MB to 400 MB.
- Added an option to delete container and image data from the **Troubleshoot** screen.
- Docker Desktop now reads the Hyper-V VM disk max size on startup and uses it as the value to display in the Settings.
- Fixed the Hyper-V used disk image size being reported incorrectly.
- Fixed the Hyper-V VM disk size increase. Fixes [docker/for-win#5881](https://github.com/docker/for-win/issues/5881).
- Fixed container time drift when system hibernates. Fixes [docker/for-win#4526](https://github.com/docker/for-win/issues/4526).
- Fixed a bug where the Docker Desktop UI could be started without the engine. Fixes [docker/for-win#5376](https://github.com/docker/for-win/issues/5376).
- Docker Desktop now uses the least possible privilege for querying the `Server service`. Fixes [docker/for-win#5150](https://github.com/docker/for-win/issues/5150).
- Fixed a bug where diagnostics upload could fail silently.
- Capturing diagnostics is now faster and easier.
- Fixed an issue where a container port could not be exposed on a specific host IP. See [docker/for-win#5546](https://github.com/docker/for-mac/issues/5546).
- Removed port probing from dashboard, just unconditionally showing links to ports that should be available. Fixes [docker/for-win#5903](https://github.com/docker/for-win/issues/5903).

### Known issues

- Loopback and unspecified IPv6 addresses (`::` and `::1`) within a container do not currently work. Some web servers and other programs may be using these addresses in their configuration files.

## Docker Desktop Community 2.2.2.0
2020-03-02



This release contains a Kubernetes upgrade. Note that your local Kubernetes cluster will be reset after installing Docker Desktop.

### Upgrades

- [Kubernetes 1.16.5](https://github.com/kubernetes/kubernetes/releases/tag/v1.16.5)
- [Go 1.13.8](https://golang.org/doc/devel/release.html#go1.13)

### New

- Windows 10 Home users can now use Docker Desktop through the experimental WSL 2 support. This requires Windows Insider Preview Build 19018 or later.
- Docker Desktop now allows sharing individual folders, rather than whole drives, giving more control to users over what is being shared.

### Bug fixes and minor changes

- Added a prerequisite check in the installer for the `LanmanServer` service. Fixes [docker/for-win#5150](https://github.com/docker/for-win/issues/5150).
- DockerNAT has been removed from Docker Desktop as using an IP address to communicate from the host to a container is not a supported feature. To communicate from a container to the host, you must use the special DNS name `host.docker.internal`. We also recommend using ports to communicate from the host to a container. For more information, see [Networking](/manuals/desktop/features/networking.md).
- Ceph support has been removed from Docker Desktop to save disk space.
- Fixed an issue that caused the Windows log file archive to grow indefinitely. Fixes [docker/for-win#5113](https://github.com/docker/for-win/issues/5113).

## Docker Desktop Community 2.2.1.0
2020-02-12



### Upgrades

- [Docker Compose 1.25.4](https://github.com/docker/compose/releases/tag/1.25.4)
- [Go 1.12.16](https://golang.org/doc/devel/release.html#go1.12)

### Bug fixes and minor changes

- Fixed an issue that prevented users from creating files with special characters in the filenames within a shared volume. Fixes [docker/for-win#5520](https://github.com/docker/for-win/issues/5520).
- Fixed handling of shared volumes with relative paths in `docker-compose.yml`. Fixes [docker/for-win#5516](https://github.com/docker/for-win/issues/5516).
- Fixed handling of shared volumes where the path case (uppercase / lowercase) did not exactly match the host. Fixes [docker/for-win#5516](https://github.com/docker/for-win/issues/5516).
- Fixed an issue where changing a file in the Windows file system did not update the file within the container. Fixes [docker/for-win#5530](https://github.com/docker/for-win/issues/5530), [docker/for-win#5550](https://github.com/docker/for-win/issues/5550), and [docker/for-win#5318](https://github.com/docker/for-win/issues/5318).
- Fixed an issue that prevented users from sharing drives and sometimes incorrectly prompted users to enter file system credentials. Fixes [docker/for-win#5567](https://github.com/docker/for-win/issues/5567).
- Fixed an issue which prevented users from mounting nested volumes. Fixes [docker/for-win#5540](https://github.com/docker/for-win/issues/5540).
- Fixed a file synchronization issue on bind mounts. Fixes [docker/for-win#5533](https://github.com/docker/for-win/issues/5533).
- Fixed an issue where timestamps were reset to zero on files within shared volumes. Fixes [docker/for-win#5528](https://github.com/docker/for-win/issues/5528) and [docker/for-win#5543](https://github.com/docker/for-win/issues/5543).
- Fixed a bug which caused Docker Desktop to fail when sharing file paths longer than 260 characters. Fixes [docker/for-win#5572](https://github.com/docker/for-win/issues/5572).
- Fixed an issue where some users were unable to start a container if there is a symlink in a shared volume. Fixes [docker/for-win#5582](https://github.com/docker/for-win/issues/5582).
- Fixed a bug where users were unable to modify the **Manual proxy configuration** settings through the Docker Desktop UI. Fixes [docker/for-win#5606](https://github.com/docker/for-win/issues/5606) and [docker/for-win#5548](https://github.com/docker/for-win/issues/5548).
- Fixed an issue where the Docker Desktop UI failed to start if the `no_proxy` environment variable has an entry that starts with a dot (.). Fixes [docker/for-win/5551](https://github.com/docker/for-win/issues/5551).
- Fixed a bug that did not allow users to access the Docker Desktop UI on machines with a policy preventing access to the Windows registry. Fixes [docker/for-win#5536](https://github.com/docker/for-win/issues/5536).
- Fixed an issue where disabling the WSL2 integration and re-enabling it later resulted in broken symlinks. Fixes [docker/for-win#5613](https://github.com/docker/for-win/issues/5613).
- Fixed a race condition when starting the WSL engine which caused Docker Desktop to incorrectly report that the containers have exited. Fixes [docker/for-win#5607](https://github.com/docker/for-win/issues/5607).
- Fixed an issue where editing code inside a container resulted in an error. Fixes [docker/for-win#5528](https://github.com/docker/for-win/issues/5528).
- Fixed a bug where running the command `DockerCli.exe -SharedDrives` failed to display a list of drives that are shared. Fixes [docker/for-win#5625](https://github.com/docker/for-win/issues/5625).

### Known issues

- DockerNAT has been removed from Docker Desktop 2.2.0.0 as using an IP address to communicate from the host to a container is not a supported feature. To communicate from a container to the host, you must use the special DNS name `host.docker.internal`. We also recommend using ports to communicate from the host to a container. For more information, see [Networking](/manuals/desktop/features/networking.md).

  However, if your current setup relies on IP addresses for communication, you can use a temporary workaround to reinstate DockerNAT. To do this, open
`C:\Program Files\Docker\Docker\resources\MobyLinux.ps1` and add `$SwitchName = "DockerNAT"` between line 175 and 176. Note that the temporary workaround to reinstate DockerNAT may be removed from future releases.
- Directory junctions in shared volumes pointing outside the shared volume do not work.
- It is currently not possible to rename open files within shared volumes.
- In some cases, Docker containers do not synchronize time with the host when the host machine is put to sleep.
- It is not possible to use `localhost` in the proxy settings. You can instead use `host.docker.internal` to work around this issue.

## Docker Desktop Community 2.1.7.0
2019-12-11



> [!NOTE]
>
> Docker Desktop Edge 2.1.7.0 is the release candidate for the upcoming major Stable release. Please help us test this version before the wider release and report any issues in the [docker/for-win](https://github.com/docker/for-win/issues) GitHub repository.

### Upgrades

- [Docker Compose 1.25.1-rc1](https://github.com/docker/compose/releases/tag/1.25.1-rc1)

### New

- Added the **WSL Integration** option in **Settings** > **Resources** to select WSL 2 distributions. This option will be visible only after enabling WSL 2 on your machine.
- File sharing: The new gRPC FUSE system is no longer experimental and is enabled by default even when experimental features are turned off.

### Bug fixes and minor changes

- The Docker Desktop Dashboard now displays port information inline with the container status.
- Fixed an issue which caused the 'back' button on the Dashboard UI to behave inconsistently when repeatedly switching between container details and the Settings window.
- Various minor improvements to the Dashboard UI.
- Fixed a bug that caused a rare crash when uninstalling Docker Desktop.
- Fixed an issue when overwriting existing files with the WSL 2 CLI bundle, such as kubectl.
- Fixed an issue where WSL 2 failed to start when the distribution directory is compressed or encrypted. Fixes [docker/for-win#5256](https://github.com/docker/for-win/issues/5256).
- Fixed an issue that caused Docker Desktop to fail on startup when there is an incomplete Kubernetes config file.
- Fixed various stability issues.

### Known issues

- The Dashboard stops updating when you switch the container mode between Linux and Windows. To work around this issue, close and reopen the Dashboard.
- The new gRPC FUSE file sharing implementation does not support connecting to new drives after Docker Desktop starts (for example, a USB drive). If you would like to share the new drive in Docker Desktop, you must quit Docker Desktop and then start the application to refresh the list of drives in Settings.

## Docker Desktop Community 2.1.6.1
2019-11-20



### Bug fixes and minor changes

- Fixed an issue that prevented Kubernetes to start with WSL 2 on machines with multiple CPU cores.
- Fixed a rare issue that caused to Docker Desktop to crash with the error `Unable to stop Hyper-V VM: Cannot validate argument on parameter 'SwitchName'. The argument is null or empty.`

### Known issue

Windows Insider Preview Slow Ring users running OS builds older than 19025 cannot run WSL 2 following upgrade to Docker Desktop Edge 2.1.6.1. WSL 2 requires Windows 10 Insider Preview build 19018 or greater.

### Docker Desktop Community 2.1.6.0
2019-11-18



### Upgrades

- [Docker 19.03.5](https://github.com/docker/docker-ce/releases/tag/v19.03.5)
- [Go 1.12.13](https://golang.org/doc/devel/release.html#go1.12)

### New

Added the ability to start and stop Compose-based applications and view combined logs in the Docker Desktop **Dashboard** UI.

### Bug fixes and minor changes

- Docker Desktop now automatically restarts after an update.
- Fixed an issue where Docker Desktop auto-start was not being disabled properly on some machines.
- Fixed a container start error when a container has more than one port with an arbitrary or not-yet-configured external port number. For example, `docker run -p 80 -p 443 nginx`). Fixes [docker/for-win#4935](https://github.com/docker/for-win/issues/4935) and [docker/compose#6998](https://github.com/docker/compose/issues/6998).
- Fixed an issue which caused Docker Desktop to crash when resetting to factory defaults while running Windows containers.
- Fixed multiple issues related to Fast Startup.
- Injected Docker CLI, CLI plugins, Docker Compose, Notary, and kubectl into WSL distributions when Docker Desktop WSL integration is enabled.
- Fixed an issue where bind mounts created with Docker Compose from a WSL distribution were incorrectly translated. Fixes [docker/for-win#5084](https://github.com/docker/for-win/issues/5084).
- Docker Desktop now supports inotify events on shared filesystems for Windows file sharing.
- Fixed a cache invalidation bug when a file in a shared volume is renamed on the host for Windows file sharing.
- Fixed a handle leak when calling `Mknod` on a shared volume for Windows file sharing.
- To make VM startup more reliable, Docker Desktop now avoids adding a Hyper-V NIC to the Windows VM when using Hypervisor sockets for Windows file sharing (rather than Samba).

### Known issue

Windows Insider Preview Slow Ring users running OS builds older than 19025 cannot run WSL 2 following upgrade to Docker Desktop Edge 2.1.6.0. WSL 2 requires Windows 10 Insider Preview build 19018 or greater.

## Docker Desktop Community 2.1.5.0
2019-11-04



This release contains a Kubernetes upgrade. Note that your local Kubernetes cluster will be reset after installation.

### Upgrades

- [Kubernetes 1.15.5](https://github.com/kubernetes/kubernetes/releases/tag/v1.15.5)
- [Docker Compose 1.25.0-rc4](https://github.com/docker/compose/releases/tag/1.25.0-rc4)
- Linux kernel 4.19.76

### New

- **Docker Desktop Dashboard:** The new Docker Desktop **Dashboard** provides a user-friendly interface which enables you to interact with containers and applications, and manage the lifecycle of your applications directly from the UI. In addition, it allows you to access the logs, view container details, and monitor resource utilization to explore the container behavior.

  To access the Dashboard UI, select the Docker menu from the system tray and then click **Dashboard**.

- **WSL 2 backend:** The new Docker Desktop WSL 2 backend replaces the Docker Desktop WSL 2 Tech Preview. The WSL 2 backend architecture introduces support for Kubernetes, provides an updated Docker daemon, offers VPN-friendly networking, and additional features. For more information, see [Docker Desktop WSL 2 backend](/manuals/desktop/features/wsl/_index.md).

- **New file sharing implementation:** Docker Desktop introduces a new file sharing implementation which uses gRPC, FUSE, and Hypervisor sockets instead of Samba, CIFS, and Hyper-V networking. The new implementation  offers improved I/O performance. Additionally, when using the new file system:

  - Users don't have to expose the Samba port, and therefore do not experience issues related to IT firewall or the drive-sharing policy.
  - There is no need to provide user credentials to Docker Desktop. File access rights are automatically enforced when accessing mounted folders through containers.

  > To switch back to the Samba file system:
  >
  > From the Docker menu, select **Settings** > **Command line**, and then clear the **Enable experimental features** check box. Alternatively, install a Docker Desktop Stable release.

### Known issues

- When you start a Docker Compose application and then start a Docker App which has the same name as the Compose application, Docker Desktop displays only one application on the Dashboard. However, when you expand the application, containers that belong to both applications are displayed on the Dashboard.

- When you deploy a Docker App with multiple containers on Kubernetes, Docker Desktop displays each Pod as an application on the Dashboard.

## Docker Desktop Community 2.1.4.0
2019-10-15



### Upgrades

- [Docker 19.03.3](https://github.com/docker/docker-ce/releases/tag/v19.03.3)
- [Kubernetes 1.15.4](https://github.com/kubernetes/kubernetes/releases/tag/v1.15.4)
- [Go 1.12.10](https://github.com/golang/go/issues?q=milestone%3AGo1.12.10+label%3ACherryPickApproved) for [CVE-2019-16276](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16276)
- [Kitematic 0.17.9](https://github.com/docker/kitematic/releases/tag/v0.17.9)

### Bug fixes and minor changes

- Improved the navigation in **Settings** and **Troubleshoot** UI.
- Fixed a bug that prevented users from accessing WSL 2 Tech Preview. Fixes [docker/for-win#4734](https://github.com/docker/for-win/issues/4734).
- Docker Machine is no longer included in the Docker Desktop installer. You can download it separately from the [Docker Machine releases](https://github.com/docker/machine/releases) page.

## Docker Desktop Community 2.1.3.0
2019-09-16



### Bug fixes and minor changes

- Added a loading overlay to the **Settings** and **Troubleshoot** windows to prevent editing conflicts.
- Deactivated the **Reset Kubernetes** button when Kubernetes is not activated.

## Docker Desktop Community 2.1.2.0
2019-09-09



#### Upgrades

- [Docker 19.03.2](https://github.com/docker/docker-ce/releases/tag/v19.03.2)
- [Kubernetes 1.14.6](https://github.com/kubernetes/kubernetes/releases/tag/v1.14.6)
- [Go 1.12.9](https://github.com/golang/go/issues?q=milestone%3AGo1.12.9+label%3ACherryPickApproved)
- [Qemu 4.0.1](https://github.com/docker/binfmt)
- [Docker Machine 0.16.2](https://github.com/docker/machine/releases/tag/v0.16.2)
- [Kitematic 0.17.8](https://github.com/docker/kitematic/releases/tag/v0.17.8)

#### Bug fixes and minor changes

- Reduced the Virtual Machine (VM) startup time.
- Added support for `Expect: 100-continue` headers in the Docker API proxy. Some HTTP clients such as `curl` send this header when the payload is large, for example, when creating containers. Fixes [moby/moby#39693](https://github.com/moby/moby/issues/39693).

## Docker Desktop Community 2.1.1.0
2019-08-12



#### Upgrades

- Linux Kernel 4.14.131

#### New

- [Docker Desktop WSL 2 Tech Preview](/manuals/desktop/features/wsl/_index.md)

#### Bug fixes and minor changes

- Fixed a PowerShell script signing issue that caused `AuthorizationManager check failed` errors on machines with strict group policies on PowerShell script signing. [docker/for-win#4376](https://github.com/docker/for-win/issues/4376)
- Fixed an issue where attempts to upgrade Docker Desktop to version 2.1.0.0 sometimes failed with the error value cannot be null. [docker/for-win#3375](https://github.com/docker/for-win/issues/3375), [docker/for-win#4381](https://github.com/docker/for-win/issues/4381), [docker/for-win#4343](https://github.com/docker/for-win/issues/4343), [docker/for-win#4359](https://github.com/docker/for-win/issues/4359)
- Fixed an issue to ensure Docker Desktop Community installer does not prompt for UAC when UAC is disabled.
- Improved the error messages displayed during VM lifecycle operations. [docker/for-win#4348](https://github.com/docker/for-win/issues/4348)
- Docker Desktop now supports a configurable user timeout for VMs on slower machines. [docker/for-win#4393](https://github.com/docker/for-win/issues/4393)
- Enabled Windows features such as Hyper-V and Containers during installation, thereby reducing the need for another restart after installation.

## Docker Desktop Community 2.1.0.0
2019-07-30



This release contains Kubernetes security improvements. Note that your local Kubernetes PKI and cluster will be reset after installation.

#### Upgrades

 - [Docker 19.03.1](https://github.com/docker/docker-ce/releases/tag/v19.03.1)
 - [Docker Compose 1.24.1](https://github.com/docker/compose/releases/tag/1.24.1)
 - [Alpine 3.10](https://alpinelinux.org/posts/Alpine-3.10.0-released.html)
 - Linux Kernel 4.9.184
 - [Docker Credential Helpers 0.6.3](https://github.com/docker/docker-credential-helpers/releases/tag/v0.6.3)

#### New

 - Introduced a new user interface for the Docker Desktop **Settings** menu.
 - The **Restart** and **Reset** options are now available on the **Troubleshoot** menu.

#### Bug fixes and minor changes

 - Changed the host's kubernetes context to ensure `docker run -v .kube:kube ... kubectl` works.
 - Restricted the `cluster-admin` role on local Kubernetes cluster to `kube-system` namespace.
 - Fixed Kubernetes installation with VPNkit subnet.
 - Fixed an issue where Docker Desktop restarts when a user logs out of Windows and logs back in, which results in retaining the
   exported ports on containers.
 - Reduced the VM startup time. `swap` is not created every time a virtual machine boots.
 - Fixed a bug which caused Docker Desktop to crash when a user cancels switching the version using Windows User Account Control (UAC)    settings.
 - Fixed a bug where the process output was not redirected to stdout when gathering diagnostics on Windows, which sometimes resulted in    a crash.


## Docker Community Edition 2.0.5.0 2019-06-12



This is the Edge channel, which gives you early access to our newest features. Be aware that some of them may be experimental, and some of them may not ever reach the Stable release.

This release contains a Kubernetes upgrade. Note that your local Kubernetes cluster will be reset after installation.

* Upgrades
  - [Docker 19.03.0-rc2](https://github.com/docker/docker-ce/releases/tag/v19.03.0-rc2)
  - [Kubernetes 1.14.3](https://github.com/kubernetes/kubernetes/releases/tag/v1.14.3)
  - [Compose on Kubernetes 0.4.23](https://github.com/docker/compose-on-kubernetes/releases/tag/v0.4.23)
  - [linuxkit v0.7](https://github.com/linuxkit/linuxkit/releases/tag/v0.7)
  - [Qemu 4.0.0](https://github.com/docker/binfmt) for cross compiling for ARM

* New
  - Docker Desktop includes the `buildx` plugin (currently experimental).
  - Selecting the `Experimental features` checkbox on the Docker Desktop settings Daemon page enables experimental features in the Docker daemon and the Docker CLI.
  - Docker Desktop now checks for stored credentials at startup before attempting to mount any shared drives. This prompts users to reenter the credentials if they are invalid.

* Bug fixes and minor changes
  - Fixed race condition where Kubernetes sometimes fails to start after the app is restarted.
  - The system tray icon now opens the Docker Desktop menu with left or right mouse button.
  - When displaying the crash report window, Docker Desktop does not send a bugsnag crash report unless the user needs the report to upload diagnostics.
  - Docker Desktop has removed the ability to log in using email address as a username as the Docker command line does not support this.
  - For Linux containers on Windows (LCOW), at least one physical computer running Windows 10 Professional or Windows 10 Enterprise version 1809 or later is required.
  - The `Send usage statistics` checkbox is selected by default in Docker Desktop for Windows (Community). This option cannot be modified.
  - Docker Desktop has added a new dialog box during startup which allows users to retry mounting a shared drive or remove it from the shared drives list after a failed attempt.


* Known issues
  - Windows containers networking does not work properly on Windows 1903.

## Docker Community Edition 2.0.4.1 2019-05-07



* Bug fixes and minor changes
  - Upgrade QEMU from 2.8.0 to 3.1.0 to fix an emulation issue when building and running Java applications on Arm64 devices.

## Docker Community Edition 2.0.4.0 2019-04-30



* Upgrades
  - [Docker 19.03.0-beta3](https://github.com/docker/docker-ce/releases/tag/v19.03.0-beta3)
  - [Docker Compose 1.24.0](https://github.com/docker/compose/releases/tag/1.24.0)
  - [Compose on Kubernetes 0.4.22](https://github.com/docker/compose-on-kubernetes/releases/tag/v0.4.22)
  - [Kubernetes 1.14.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.14.md#changelog-since-v1141)

* New

  - App: Docker CLI plugin to configure, share, and install applications

    - Extend Compose files with metadata and parameters
    - Reuse the same application across multiple environments (Development/QA/Staging/Production)
    - Multi-orchestrator installation (Swarm or Kubernetes)
    - Push/Pull/Promotion/Signing supported for application, with the same workflow as images
    - Fully CNAB compliant
    - Full support for Docker Contexts

  - Buildx (Tech Preview): Docker CLI plugin for extended build capabilities with BuildKit

    - Familiar UI from docker build
    - Full BuildKit capabilities with container driver
    - Multiple builder instance support
    - Multi-node builds for cross-platform images (out-of-the-box support for linux/arm/v7 and linux/arm64)
    - Concurrent building of compose files
    - High-level build constructs with `bake`

* Bug fixes and minor changes

  - Fix `Delete` of persistent volume claims
  - Truncate UDP DNS responses which are over 512 bytes in size

## Docker Community Edition 2.0.3.0 2019-03-05



* Upgrades
  - [Docker 18.09.3](https://github.com/docker/docker-ce/releases/tag/v18.09.3)

* Bug fixes and minor changes
  - Fixed docker not added to PATH after install in some cases
  - Fixed port 8080 that was used on localhost when starting Kubernetes.
  - Fixed "create issue" link in diagnostics windows.

## Docker Community Edition 2.0.2.1 2019-02-15



* Upgrades
  - [Docker 18.09.2](https://github.com/docker/docker-ce/releases/tag/v18.09.2), fixes [CVE-2019-5736](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736)

## Docker Community Edition 2.0.2.0 2019-02-06



* Upgrades
  - [Docker Compose 1.24.0-rc1](https://github.com/docker/compose/releases/tag/1.24.0-rc1)
  - [Docker Machine 0.16.1](https://github.com/docker/machine/releases/tag/v0.16.1)
  - [Compose on Kubernetes 0.4.18](https://github.com/docker/compose-on-kubernetes/releases/tag/v0.4.18)

* New
  - Rebranded UI

* Bug fixes and minor changes
  - Kubernetes: use default maximum number of pods for kubelet. [docker/for-mac#3453](https://github.com/docker/for-mac/issues/3453)

## Docker Community Edition 2.0.1.0 2019-01-11



* Upgrades
  - [Docker 18.09.1](https://github.com/docker/docker-ce/releases/tag/v18.09.1)
  - [Kubernetes 1.13.0](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.13.md#v1130)
  - [Kitematic 0.17.6](https://github.com/docker/kitematic/releases/tag/v0.17.6)
  - Golang 1.10.6, fixes CVEs: [CVE-2018-16875](https://www.cvedetails.com/cve/CVE-2018-16875), [CVE-2018-16873](https://www.cvedetails.com/cve/CVE-2018-16873) and [CVE-2018-16874](https://www.cvedetails.com/cve/CVE-2018-16874)

  WARNING: If you have an existing Kubernetes cluster created with Docker Desktop, this upgrade will reset the cluster. If you need to back up your Kubernetes cluster or persistent volumes you can use [Ark](https://github.com/heptio/ark).

* Bug fixes and minor changes
  - Fix service log collection in diagnostics
  - Gather /etc/hosts to help diagnostics
  - Add 18.09 missing daemon options
  - Rename Docker for Windows to Docker Desktop
  - Partially open services ports if possibles
  - Quit will not check if service is running anymore
  - Fix UI lock when changing kubernetes state

