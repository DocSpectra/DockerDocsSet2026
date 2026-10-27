---
title: Rootless mode prerequisites and limitations
---

## Prerequisites

-  You must install `newuidmap` and `newgidmap` on the host. These commands
  are provided by the `uidmap` package on most distributions.

- `/etc/subuid` and `/etc/subgid` should contain at least 65,536 subordinate
  UIDs/GIDs for the user. In the following example, the user `testuser` has
  65,536 subordinate UIDs/GIDs (231072-296607).

```console
$ id -u
1001
$ whoami
testuser
$ grep ^$(whoami): /etc/subuid
testuser:231072:65536
$ grep ^$(whoami): /etc/subgid
testuser:231072:65536
```

The `dockerd-rootless-setuptool.sh install` script automatically shows help
when the prerequisites are not satisfied.

## Distribution-specific hint

{{< tabs >}}
{{< tab name="Ubuntu" >}}
- Ubuntu 24.04 and later enables restricted unprivileged user namespaces by
  default, which prevents unprivileged processes in creating user namespaces
  unless an AppArmor profile is configured to allow programs to use
  unprivileged user namespaces.

  If you install `docker-ce-rootless-extras` using the deb package (`apt-get
  install docker-ce-rootless-extras`), then the AppArmor profile for
  `rootlesskit` is already bundled with the `apparmor` deb package. With this
  installation method, you don't need to add any manual the AppArmor
  configuration. If you install the rootless extras using the [installation
  script](https://get.docker.com/rootless), however, you must add an AppArmor
  profile for `rootlesskit` manually:

  1. Create and install the currently logged-in user's AppArmor profile:

     ```console
     $ filename=$(echo $HOME/bin/rootlesskit | sed -e 's@^/@@' -e 's@/@.@g')
     $ [ ! -z "${filename}" ] && sudo cat <<EOF > /etc/apparmor.d/${filename}
     abi <abi/4.0>,
     include <tunables/global>

     "$HOME/bin/rootlesskit" flags=(unconfined) {
       userns,

       include if exists <local/${filename}>
     }
     EOF
     ```
  2. Restart AppArmor.

     ```console
     $ systemctl restart apparmor.service
     ```

{{< /tab >}}
{{< tab name="Arch Linux" >}}
- Add `kernel.unprivileged_userns_clone=1` to `/etc/sysctl.conf` (or
  `/etc/sysctl.d`) and run `sudo sysctl --system`
{{< /tab >}}
{{< tab name="openSUSE and SLES" >}}
- `sudo modprobe ip_tables iptable_mangle iptable_nat iptable_filter` is required.
  This might be required on other distributions as well depending on the configuration.

- Known to work on openSUSE 15 and SLES 15.
{{< /tab >}}
{{< tab name="CentOS, RHEL, and Fedora" >}}
- For RHEL 8 and similar distributions, installing `fuse-overlayfs` is recommended. Run `sudo dnf install -y fuse-overlayfs`.
  This step is not required on RHEL 9 and similar distributions.

- You might need `sudo dnf install -y iptables`.
{{< /tab >}}
{{< /tabs >}}

## Known limitations

- Only the following storage drivers are supported:
  - `overlay2` (only if running with kernel 5.11 or later)
  - `fuse-overlayfs` (only if running with kernel 4.18 or later, and `fuse-overlayfs` is installed)
  - `btrfs` (only if running with kernel 4.18 or later, or `~/.local/share/docker` is mounted with `user_subvol_rm_allowed` mount option)
  - `vfs`
- cgroup is supported only when running with cgroup v2 and systemd. See [Limiting resources](./network-and-resources.md#limiting-resources).
- Following features are not supported:
  - AppArmor
  - Checkpoint
  - Overlay network
  - Exposing SCTP ports
- To use the `ping` command, see [Routing ping packets](./network-and-resources.md#routing-ping-packets).
- To expose privileged TCP/UDP ports (< 1024), see [Exposing privileged ports](./network-and-resources.md#exposing-privileged-ports).
- `IPAddress` shown in `docker inspect` is namespaced inside RootlessKit's network namespace.
  This means the IP address is not reachable from the host without `nsenter`-ing into the network namespace.
- Host network (`docker run --net=host`) is also namespaced inside RootlessKit.
- NFS mounts as the docker "data-root" is not supported. This limitation is not specific to rootless mode.
