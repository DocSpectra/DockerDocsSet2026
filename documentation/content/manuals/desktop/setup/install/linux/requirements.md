---
title: Docker Desktop for Linux requirements
---

## General system requirements

To install Docker Desktop successfully, your Linux host must meet the following general requirements:

- 64-bit kernel and CPU support for virtualization.
- KVM virtualization support. Follow the [KVM virtualization support instructions](#kvm-virtualization-support) to check if the KVM kernel modules are enabled and how to provide access to the KVM device.
- QEMU must be version 5.2 or later. We recommend upgrading to the latest version.
- systemd init system.
- GNOME, KDE, or MATE desktop environments are supported but others may work.
  - For many Linux distributions, the GNOME environment does not support tray icons. To add support for tray icons, you need to install a GNOME extension. For example, [AppIndicator](https://extensions.gnome.org/extension/615/appindicator-support/).
- At least 4 GB of RAM.
- Enable configuring ID mapping in user namespaces, see [File sharing](/manuals/desktop/troubleshoot-and-support/faqs/linuxfaqs.md#how-do-i-enable-file-sharing). Note that for Docker Desktop version 4.35 and later, this is not required anymore.
- Recommended: [Initialize `pass`](/manuals/desktop/setup/linux-credentials.md) for credentials management.

Docker Desktop for Linux runs a Virtual Machine (VM). For more information on why, see [Why Docker Desktop for Linux runs a VM](/manuals/desktop/troubleshoot-and-support/faqs/linuxfaqs.md#why-does-docker-desktop-for-linux-run-a-vm).

> [!NOTE]
>
> Docker does not provide support for running Docker Desktop for Linux in nested virtualization scenarios. We recommend that you run Docker Desktop for Linux natively on supported distributions.

### KVM virtualization support

Docker Desktop runs a VM that requires [KVM support](https://www.linux-kvm.org).

The `kvm` module should load automatically if the host has virtualization support. To load the module manually, run:

```console
$ modprobe kvm
```

Depending on the processor of the host machine, the corresponding module must be loaded:

```console
$ modprobe kvm_intel  # Intel processors

$ modprobe kvm_amd    # AMD processors
```

If the above commands fail, you can view the diagnostics by running:

```console
$ kvm-ok
```

To check if the KVM modules are enabled, run:

```console
$ lsmod | grep kvm
kvm_amd               167936  0
ccp                   126976  1 kvm_amd
kvm                  1089536  1 kvm_amd
irqbypass              16384  1 kvm
```

#### Set up KVM device user permissions

To check ownership of `/dev/kvm`, run :

```console
$ ls -al /dev/kvm
```

Add your user to the kvm group in order to access the kvm device:

```console
$ sudo usermod -aG kvm $USER
```

Sign out and sign back in so that your group membership is re-evaluated.

## Using Docker SDKs with Docker Desktop

Docker Desktop for Linux uses a per-user socket instead of the system-wide `/var/run/docker.sock`. Docker SDKs and tools that connect directly to the Docker daemon need the `DOCKER_HOST` environment variable set to connect to Docker Desktop. For configuration details, see [How do I use Docker SDKs with Docker Desktop for Linux?](/manuals/desktop/troubleshoot-and-support/faqs/linuxfaqs.md#how-do-i-use-docker-sdks-with-docker-desktop-for-linux).
