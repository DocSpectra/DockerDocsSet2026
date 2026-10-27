---
description: Learn about and change Docker Desktop's settings
keywords: settings, preferences, proxy, file sharing, resources, kubernetes, Docker
  Desktop, Linux, Mac, Windows
title: Change your Docker Desktop settings
linkTitle: Change settings
aliases:
 - /desktop/settings/mac/
 - /desktop/settings/windows/
 - /desktop/settings/linux/
 - /desktop/settings/
weight: 10
---

Customize Docker Desktop behavior and optimize performance and resource usage with Docker Desktop's settings.

To open **Settings** either:

- Select the Docker menu {{< inline-image src="../images/whale-x.svg" alt="whale menu" >}} and then **Settings**
- Select the **Settings** icon from the Docker Desktop Dashboard.

You can also locate the `settings-store.json` file at:
 - Mac: `~/Library/Group\ Containers/group.com.docker/settings-store.json`
 - Windows: `C:\Users\[USERNAME]\AppData\Roaming\Docker\settings-store.json`
 - Linux: `~/.docker/desktop/settings-store.json`

For information on enforcing settings at an organization level, see [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/settings-reference.md).

## General

Configure startup behavior, UI appearance, terminal preferences, and feature defaults for Docker Desktop.

| Setting                                                           | Description                                                                | Default            | Platform     | Notes                                 |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------ | ------------ | ------------------------------------- |
| **Start Docker Desktop when you sign in to your computer**        | Automatically start Docker Desktop when you sign in to your machine.        | Disabled           | All          | Recommended for frequent users.        |
| **Open Docker Dashboard when Docker Desktop starts**              | Automatically open the dashboard when starting Docker Desktop.              | Disabled           | All          |                                       |
| **Choose theme for Docker Desktop**                               | Apply a **Light** or **Dark** theme to Docker Desktop. | **Use system settings**. | All |                                   |
| **Configure shell completions**                                  | Edits your shell configuration to enable word completion for commands, flags, and Docker objects when you press `<Tab>` in your terminal. For more information, see [Completion](/manuals/engine/cli/completion.md). | Disabled | All | |
| **Choose container terminal** | Sets which terminal opens when you select a container terminal. Use the integrated terminal to run commands in a running container from the Dashboard. For more information, see [Integrated terminal](/manuals/desktop/use-desktop/terminal.md). | Disabled | All | |
| **Enable Docker terminal**.                                       | Interact with your host machine and execute commands directly from Docker Desktop.  | Disabled | All | |
| **Enable Docker Debug by default**                                | Use Docker Debug by default opening the integrated terminal. For more information, see [Run commands or debug a container](/manuals/desktop/use-desktop/container-debug.md#execdebug).   | Disabled | All | |
| **Include VM in Time Machine backups**                            | Back up the Docker Desktop virtual machine. | Disabled | Mac | |
| **Use containerd for pulling and storing images**     | Uses containerd image store instead of classic image store. For more information, see [containerd image store](/manuals/engine/storage/image-store-capabilities.md).| Enabled  | All   |           |
| **Expose daemon on tcp://localhost:2375 without TLS** | Allow legacy clients to connect to the Docker daemon. Use with caution as exposing the daemon without TLS can result in remote code execution attacks. | Disabled                  | Windows (Hyper-V backend only) | |
| **Use the WSL 2 based engine** | WSL 2 provides better performance than the Hyper-V backend. For more information, see [WSL 2 requirements](/manuals/desktop/features/wsl/requirements.md). | Disabled | Windows | |
| **Add \*.docker.internal to host file**                | Adds internal DNS entries.                                  | Enabled                   | Windows                        | Helps resolve Docker-internal domains |
| **Choose Virtual Machine Manager (VMM)**              | Choose the VMM for creating and managing the Docker Desktop Linux VM. For more information, see [Virtual Machine Manager](/manuals/desktop/features/vmm-reference.md). | | Mac | Select **Docker VMM** for the latest and most performant Hypervisor/Virtual Machine Manager. This option is available only on Apple Silicon Macs and is in Beta.|
| **Choose file sharing implementation for your containers** | Choose whether you want to share files using **VirtioFS**, **gRPC FUSE**, or **osxfs (Legacy)** | **VirtioFS** | Mac | Use VirtioFS for speedy file sharing. VirtioFS has reduced the time taken to complete filesystem operations by [up to 98%](https://github.com/docker/roadmap/issues/7#issuecomment-1044452206). It is the only file sharing implementation supported by Docker VMM. |
|**Use Rosetta for x86_64/amd64 emulation on Apple Silicon** | Accelerate x86/AMD64 binary emulation on Apple Silicon. This option is only available if you have selected **Apple Virtualization framework** as the Virtual Machine Manager. | Disabled | Mac | |
| **Send usage statistics** | Send diagnostics, crash reports, and usage data to Docker to improve and troubleshoot the application. Docker may periodically prompt you for more information. | Enabled | All | |
| **Use Enhanced Container Isolation** | Prevent containers from breaching the Linux VM. For more information, see [Enhanced Container Isolation](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/_index.md). | Disabled | All | Must be signed in and have a Docker Business subscription. |
| **Show CLI hints**                                   | Display helpful CLI suggestions in terminal.               | Enabled                  | All        | Improves discoverability              |
| **Enable Docker Scout image analysis**                | Show a **Start analysis** button when inspecting an image, which analyzes the image with Docker Scout.         | Enabled                   | All   | |
| **Enable background SBOM indexing** | Automatically analyze images that you build or pull. | Disabled | All | |
| **Automatically check configuration** | Regularly check your configuration to ensure no unexpected changes have been made by another application. Notifies you if changes are found with the option to restore the configuration directly from the notification. For more information, see the [FAQs](/manuals/desktop/troubleshoot-and-support/faqs/macfaqs.md#why-do-i-keep-getting-a-notification-telling-me-an-application-has-changed-my-desktop-configurations). | Enabled | Mac | Docker Desktop checks if your setup, configured during installation, has been altered by external apps like Orbstack. Docker Desktop checks the symlinks of Docker binaries to `/usr/local/bin` and the symlink of the default Docker socket. Additionally, Docker Desktop ensures that the context is switched to `desktop-linux` on startup. |

## Resources

Control the CPU, memory, disk, file sharing, proxy, and network resources available to Docker Desktop.

### Advanced

| Setting             | Description                               | Platform | Notes                                 |
| ------------------- | ----------------------------------------- | -------- | ------------------------------------- |
| **CPU limit** | Specify the maximum number of CPUs to be used by Docker Desktop. | Mac, Linux, Windows Hyper-V | |
| **Memory limit** | RAM allocated to the Docker VM | Mac, Linux, Windows Hyper-V | Defaults to 50% of your host's memory. |
| **Swap** | Configure swap file size as needed. | Mac, Linux, Windows Hyper-V | 1 GB default. |
| **Disk usage limit** | Specify the maximum amount of disk space the engine can use. | Mac, Linux, Windows Hyper-V | |
|  **Disk image location** | Specify the location of the Linux volume where containers and images are stored. On the **Advanced** tab, you can limit resources available to the Docker Linux VM. | Mac, Linux, Windows Hyper-V | You can also move the disk image to a different location. If you attempt to move a disk image to a location that already has one, you are asked if you want to use the existing image or replace it. |
| **Resource Saver** | Enable or disable [Resource Saver mode](/manuals/desktop/use-desktop/resource-saving-context.md), which significantly reduces CPU and memory utilization on the host by automatically turning off the Linux VM when Docker Desktop is idle. | Mac, Linux, Windows Hyper-V | Restarts automatically when containers run. Restart may take 3–10 seconds. |

In WSL 2 mode, configure memory, CPU, and swap limits on the [WSL 2 utility VM](https://docs.microsoft.com/en-us/windows/wsl/wsl-config#configure-global-options-with-wslconfig).

> [!TIP]
>
> If you feel Docker Desktop starting to get slow or you're running
> multi-container workloads, increase the memory and disk image space allocation.

### File sharing

Use File sharing to allow local directories on your machine to be shared with
Linux containers. This is especially useful for editing source code in an IDE on
the host while running and testing the code in a container.

| Setting             | Description                               | Platform | Notes                                 |
| ------------------- | ----------------------------------------- | -------- | ------------------------------------- |
| **Synchronized file shares** | Fast and flexible host-to-VM file sharing, enhancing bind mount performance through the use of synchronized filesystem caches. To learn more, see [Synchronized file share](/manuals/desktop/features/file-sharing-context.md). | Mac, Linux, Windows Hyper-V | Available with Pro, Team, and Business subscriptions. |
| **Virtual file shares** | Share local directories with Linux containers. By default the `/Users`, `/Volumes`, `/private`, `/tmp` and `/var/folders` directory are shared. If your project is outside this directory then it must be added to the list, otherwise you may get `Mounts denied` or `cannot start service` errors at runtime. | Mac, Linux, Windows Hyper-V | |


- Share only the directories that you need with the container. File sharing
introduces overhead as any changes to the files on the host need to be notified
to the Linux VM. Sharing too many files can lead to high CPU load and slow
filesystem performance.
- Shared folders are designed to allow application code to be edited
on the host while being executed in containers. For non-code items
such as cache directories or databases, the performance will be much
better if they are stored in the Linux VM, using a [data volume](/manuals/engine/storage/volumes.md)
(named volume) or [data container](/manuals/engine/storage/volumes.md).
- If you share the whole of your home directory into a container, Mac may
prompt you to give Docker access to personal areas of your home directory such as
your Reminders or Downloads.
- By default, Mac file systems are case-insensitive while Linux is case-sensitive.
On Linux, it is possible to create two separate files: `test` and `Test`,
while on Mac these filenames would actually refer to the same underlying
file. This can lead to problems where an app works correctly on a developer's
machine (where the file contents are shared) but fails when run in Linux in
production (where the file contents are distinct). To avoid this, Docker Desktop
insists that all shared files are accessed as their original case. Therefore,
if a file is created called `test`, it must be opened as `test`. Attempts to
open `Test` will fail with the error "No such file or directory". Similarly,
once a file called `test` is created, attempts to create a second file called
`Test` will fail.

For more information, see [Volume mounting requires file sharing for any project directories outside of `/Users`](/manuals/desktop/troubleshoot-and-support/troubleshoot/topics.md).

### Proxies

See [Docker Desktop proxy settings and authentication](proxy-settings.md).

#### Docker Desktop proxy

See [Docker Desktop proxy](proxy-settings.md#docker-desktop-proxy).

#### Containers proxy

See [Containers proxy](proxy-settings.md#containers-proxy).

#### Proxy authentication

See [Proxy authentication](proxy-settings.md#proxy-authentication).

### Network

> [!NOTE]
>
> On Windows, the **Network** tab is not available in Windows container mode because Windows manages networking.

| Setting | Description | Platform |
|---------|-------------|----------|
| **Docker subnet** | Set a custom subnet to avoid conflicts with IPs in your environment. Docker Desktop uses a private IPv4 network for internal services, including a DNS server and HTTP proxy. Default: `192.168.65.0/24`. | All |
| **Use kernel networking for UDP** | Use a more efficient kernel networking path for UDP traffic. May not be compatible with VPN software. | Mac |
| **Enable host networking** | Allows containers started with `--net=host` to use `localhost` to connect to TCP and UDP services on the host. Also allows host software to use `localhost` to connect to TCP and UDP services in the container. | Mac |

On Windows and Mac, you can also set the default networking mode and DNS resolution behavior. For more information, see [Networking](/manuals/desktop/features/networking/network-settings.md).

### WSL integration (Windows only)

| Setting             | Description                               | Notes                               |
| ------------------- | ----------------------------------------- | ------------------------------------- |
| WSL distribution integration| Select which WSL 2 distributions have Docker WSL integration enabled. | Integration is enabled on your default WSL distribution by default. To change your default distribution, run `wsl --set-default <distribution name>`. |

For WSL 2 prerequisites, see
[Docker Desktop WSL 2 backend](/manuals/desktop/features/wsl/requirements.md).

## Docker Engine

Configure the Docker daemon using a JSON configuration file.

The file is located at `$HOME/.docker/daemon.json`. Edit it directly in the Docker Desktop Dashboard or in a text editor.

To see the full list of possible configuration options, see the
[dockerd command reference](/reference/cli/dockerd/).

## Builders

See [Manage builders in Docker Desktop](builders.md).

### Inspect

See [Inspect](builders.md#inspect).

### Select a different builder

See [Select a different builder](builders.md#select-a-different-builder).

### Create a builder

See [Create a builder](builders.md#create-a-builder).

### Remove a builder

See [Remove a builder](builders.md#remove-a-builder).

### Stop and start a builder

See [Stop and start a builder](builders.md#stop-and-start-a-builder).

## Kubernetes

> [!NOTE]
>
> On Windows the **Kubernetes** tab is not available in Windows container mode.

Enable and configure the built-in standalone Kubernetes cluster for testing container deployments.

| Setting             | Description                               |
| ------------------- | ----------------------------------------- |
| **Enable Kubernetes** | Install and run a standalone Kubernetes server as a Docker container for testing deployments. |
| **Cluster provisioning method** | Choose either **Kubeadm**, a single-node cluster with the version set by Docker Desktop, or **Kind**, a multi-node cluster where you can set the version and number of nodes. |
| **Show system containers (advanced)** | Show internal containers when using Docker commands. |
| **Reset Kubernetes cluster** | Delete all stacks and Kubernetes resources. |

For more information about using the Kubernetes integration with Docker Desktop,
see [Kubernetes cluster provisioning methods](/manuals/desktop/use-desktop/kubernetes-provisioning.md).

## Software updates

Manage how and when Docker Desktop checks for and downloads updates.

| Setting             | Description                               | Default                             |
| ------------------- | ----------------------------------------- | ------------------------------------- |
| **Automatically check for updates** | Notifies you of available updates in the Docker menu and Dashboard footer. | Enabled |
| **Always download updates** | Automatically download new versions of Docker Desktop in the background. | Disabled |
| **Automatically update components** | Update Docker Desktop components (such as Docker Compose, Docker Scout, and the Docker CLI) independently, without a full restart. | Enabled |

## Extensions

Enable Docker Extensions and control which extensions are available to install and run.

| Setting             | Description                               |
| ------------------- | ----------------------------------------- |
| **Enable Docker Extensions** | Turn Docker Extensions on or off. |
| **Allow only extensions distributed through the Docker Marketplace** | Restrict extensions to Marketplace-approved sources only. |
| **Show Docker Extensions system containers** | Show containers used by Docker Extensions. |

For more information about Docker extensions, see [Docker Extensions](/manuals/extensions/_index.md).

## Beta features

Beta features provide access to future product functionality.
These features are intended for testing and feedback only as they may change
between releases without warning or remove them entirely from a future
release. Beta features must not be used in production environments.
Docker doesn't offer support for beta features.

You can also sign up to the [Developer Preview program](https://www.docker.com/community/get-involved/developer-preview/) from the **Beta features** tab.

For a list of current experimental features in the Docker CLI, see [Docker CLI Experimental features](https://github.com/docker/cli/blob/master/experimental/README.md).

## Notifications

Choose which types of Docker Desktop notifications you want to receive.

| Notification type | Default|
| ----------------- | ------ |
| Status updates on tasks and processes | Enabled |
| Recommendations from Docker | Enabled |
| Docker announcements | Enabled |
| Docker surveys | Enabled |
| Error notifications | Always Enabled (cannot be changed) |
| New releases | Always Enabled (cannot be changed) |

Notifications appear briefly in the lower-right of the Docker Desktop Dashboard, then move to the **Notifications** drawer, accessible from the top-right of the Dashboard.

## Advanced (Mac only)

Reconfigure CLI tool installation paths and privileged system permissions set during initial install.

| Setting             | Description                               | Notes                               |
| ------------------- | ----------------------------------------- | ------------------------------------- |
| CLI tools installation — **System** | Install Docker CLI tools to `/usr/local/bin`. | |
| CLI tools installation — **User** | Install Docker CLI tools to `$HOME/.docker/bin` | Add `$HOME/.docker/bin` to your PATH by appending `export PATH=$PATH:~/.docker/bin` to `~/.bashrc` or `~/.zshrc`, then restart your shell. |
| **Allow the default Docker socket to be used** | Creates `/var/run/docker.sock` which some third party clients may use to communicate with Docker Desktop. For more information, see [permission requirements for macOS](/manuals/desktop/setup/install/mac-permission-requirements.md#installing-symlinks). | Requires password |
| **Allow privileged port mapping** | Starts the privileged helper process which binds the ports that are between 1 and 1024. For more information, see [permission requirements for macOS](/manuals/desktop/setup/install/mac-permission-requirements.md#binding-privileged-ports). | Requires password |

## Docker Offload

Enable Docker Offload and configure idle timeout and GPU support for cloud-based workloads.

| Setting             | Description                               | Notes                                 |
| ------------------- | ----------------------------------------- | ------------------------------------- |
| **Enable Docker Offload** | Run your containers in the cloud.  | Requires sign-in and an Offload subscription |
| **Idle timeout** | Set the duration of time between no activity and Docker Offload entering idle mode. For details about idle timeout, see [Session management and idle state](../../offload/about.md#session-management-and-idle-state). | |
| **Enable GPU support** | Let your workloads use cloud GPU if available. | |
