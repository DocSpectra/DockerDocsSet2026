---
title: Docker Engine upgrade requirements
linkTitle: Upgrade requirements
description: Package, storage-driver, plugin, and systemd requirements for historical Docker Engine upgrades.
---

Use the section for the version you are upgrading to:

- [Docker 1.13 storage drivers and plugins](#docker-113-storage-drivers-and-plugins)
- [Docker 18.09 packages](#docker-1809-packages)
- [Docker 18.09 systemd mount settings](#docker-1809-systemd-mount-settings)
- [Docker 20.10 HTTPS proxies](#docker-2010-https-proxies)
- [Docker Engine 23.0 packages](#docker-engine-230-packages)

## Docker 1.13 storage drivers and plugins

### Storage driver defaults

> [!IMPORTANT]
>
> On Linux distributions where `devicemapper` was the default storage driver, the `overlay2`, or `overlay` is now used by default (if the kernel supports it). To use devicemapper, you can manually configure the storage driver to use through the `--storage-driver` daemon option, or by setting "storage-driver" in the `daemon.json` configuration file.

### Remove Docker 1.12 plugins before upgrading

> [!IMPORTANT]
>
> In Docker 1.13, the managed plugin api changed, as compared to the experimental version introduced in Docker 1.12. You must **uninstall** plugins which you installed with Docker 1.12 _before_ upgrading to Docker 1.13. You can uninstall plugins using the `docker plugin rm` command.

### Recover if the daemon fails to start

If you have already upgraded to Docker 1.13 without uninstalling
previously-installed plugins, you may see this message when the Docker daemon
starts:

    Error starting daemon: json: cannot unmarshal string into Go value of type types.PluginEnv

To manually remove all plugins and resolve this problem, take the following steps:

1. Remove plugins.json from: `/var/lib/docker/plugins/`.
2. Restart Docker. Verify that the Docker daemon starts with no errors.
3. Reinstall your plugins.

## Docker 18.09 packages

> **Note:**
>
> With this release, the daemon, client and container runtime are now all shipped
> in separate packages. When updating, you need to update all packages at the same
> time to get the latest patch releases for each. For example, on Ubuntu:
> 
> ```console
> $ sudo apt-get install docker-ce docker-ce-cli containerd.io
> ```
> 
> See the [installation instructions](../install/_index.md) for the corresponding
> Linux distribution for details.

## Docker 18.09 systemd mount settings

In Docker versions prior to 18.09, containerd was managed by the Docker engine daemon. In Docker Engine 18.09, containerd is managed by systemd. Since containerd is managed by systemd, any custom configuration to the `docker.service` systemd configuration which changes mount settings (for example, `MountFlags=slave`) breaks interactions between the Docker Engine daemon and containerd, and you will not be able to start containers.

Run the following command to get the current value of the `MountFlags` property for the `docker.service`:

```console
$ sudo systemctl show --property=MountFlags docker.service
MountFlags=
```

Update your configuration if this command prints a non-empty value for `MountFlags`, and restart the docker service.

## Docker 20.10 HTTPS proxies

Release entries: 20.10.8, 20.10.9, 20.10.10, and 20.10.11.

> [!IMPORTANT]
>
> Due to [net/http changes](https://github.com/golang/go/issues/40909) in [Go 1.16](https://golang.org/doc/go1.16#net/http), HTTP proxies configured through the `$HTTP_PROXY` environment variable are no longer used for TLS (`https://`) connections. Make sure you also set an `$HTTPS_PROXY` environment variable for handling requests to `https://` URLs. Refer to [Configure the daemon to use a proxy](/manuals/engine/daemon/proxy.md) to learn how to configure the Docker Daemon to use a proxy server.

## Docker Engine 23.0 packages

> [!NOTE]
>
> From Docker Engine version 23.0.0, Buildx is distributed in a separate package: `docker-buildx-plugin`.
> In earlier versions, Buildx was included in the `docker-ce-cli` package.
> When you upgrade to this version of Docker Engine, make sure you update all
> packages. For example, on Ubuntu:
>
> ```console
> $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
> ```
>
> Refer to the [Docker Engine installation instructions](/manuals/engine/install/_index.md) for your operating system
> for more details on upgrading Docker Engine.
