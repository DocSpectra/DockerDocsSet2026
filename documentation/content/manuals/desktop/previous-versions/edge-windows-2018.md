---
title: Docker Desktop for Windows Edge 2018 release notes
linkTitle: Windows Edge 2018
toc_max: 3
sitemap: false
---

## Related guidance

- [Historical Edge release caveats and update prerequisites](/manuals/desktop/release-availability.md#historical-edge-releases)
- [Historical upgrade and update procedures](upgrade-guidance.md)

## Edge Releases of 2018

### Docker Community Edition 2.0.0.0-win82 2018-12-07

* Upgrades
  - [Docker compose 1.23.2](https://github.com/docker/compose/releases/tag/1.23.2)

* Bug fixes and minor changes
  - Compose: Fixed a bug where build context URLs would fail to build on Windows. Fixes [docker/for-win#2918](https://github.com/docker/for-win/issues/2918)

### Docker Community Edition 2.0.0.0-win77 2018-11-14

* Upgrades
  - [Docker 18.09.0](https://github.com/docker/docker-ce-packaging/releases/tag/v18.09.0)
  - [Docker compose 1.23.1](https://github.com/docker/compose/releases/tag/1.23.1)
  - [Docker Machine 0.16.0](https://github.com/docker/machine/releases/tag/v0.16.0)
  - [Kitematic 0.17.5](https://github.com/docker/kitematic/releases/tag/v0.17.5)

* Bug fixes and minor changes
  - Windows Containers: Fix group daemon option settings. Fixes [docker/for-win#2647](https://github.com/docker/for-win/issues/2647)
  - Windows Containers: Improve host.docker.internal ip resolution
  - Do not try to update samba share mounts when using Windows containers
  - Improved dns update too verbose in logs
  - VPNKit: Improved scalability of port forwarding.
  - VPNKit: Limit the size of the UDP NAT table. This ensures port forwarding and regular TCP traffic continue even when running very chatty UDP protocols.

### Docker Community Edition 2.0.0.0-beta1-win75 2018-09-14

* Upgrades
  - [Docker 18.09.0-ce-beta1](https://github.com/docker/docker-ce/releases/tag/v18.09.0-ce-beta1)
  - Linux Kernel 4.9.125

* New
  - New version scheme

* Deprecation
  - Removed support of AUFS

* Bug fixes and minor changes
  - LCOW does not anymore need --platform flag on multi-arch images
  - Better WCOW host.docker.internal resolution on host, don't rewrite it if not modified. From [docker/for-win#1976](https://github.com/docker/for-win/issues/1976)
  - Disk size can now be adjusted from 32GiB to drive space.
  - Fix dns update too verbose in logs
  - Fix panic in diagnose

### Docker Community Edition 18.06.1-ce-win74 2018-08-29

* Upgrades
  - [Docker 18.06.1-ce](https://github.com/docker/docker-ce/releases/tag/v18.06.1-ce)

* Bug fixes and minor changes
  - Fix bug in virtual machine activity detection, preventing Docker Desktop from starting. Fixes [docker/for-win#2404](https://github.com/docker/for-win/issues/2404)
  - Fix bug in detection when Windows service is not running, and proposes to restart the service.
  - Fix local DNS failing to resolve inside containers. Fixes [docker/for-win#2301](https://github.com/docker/for-win/issues/2301), [docker/for-win#2304](https://github.com/docker/for-win/issues/2304)
  - Fix Kubernetes status display after reset to factory default
  - Fix bug where `host.docker.internal` is not resolved in some cases. Fixes [docker/for-win#2402](https://github.com/docker/for-win/issues/2402)
  - Use a 1MB vhdx blocksize instead of the default 32MB. See [docker/for-win#244](https://github.com/docker/for-win/issues/244). Also see [Microsoft Best Practices for running Linux on Hyper-V](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/best-practices-for-running-linux-on-hyper-v)
  - Fix diagnostics in specific cases when Windows service is not started.
  - Changed samba default file permissions back to avoid issue with too-open rights. Fixes [docker/for-win#2170](https://github.com/docker/for-win/issues/2170)
  - On RS5 insider, fix wrong detection of missing feature "Containers" requiring to install feature + reboot.

### Docker Community Edition 18.06.0-ce-win71 2018-07-27

* Bug fixes and minor changes
  - Fix bug in automatic feature enabling if "Hyper-V" and "Containers" Windows features are not enabled already when starting Docker Desktop.

### Docker Community Edition 18.06.0-ce-win69 2018-07-25

* Upgrades
  - [Docker 18.06.0-ce](https://github.com/docker/docker-ce/releases/tag/v18.06.0-ce)

### Docker Community Edition 18.06.0-ce-rc3-win68 2018-07-19

* Upgrades
  - [Docker 18.06.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v18.06.0-ce-rc3)
  - [Docker Machine 0.15.0](https://github.com/docker/machine/releases/tag/v0.15.0)
  - [Docker compose 1.22.0](https://github.com/docker/compose/releases/tag/1.22.0)

* New
  - New Kubernetes menu item allowing to switch Kubernetes context & connect to clusters other than the local one.

* Bug fixes and minor changes
  - Before updating from Desktop 18.06.x to the next major update, see [AUFS disk reset requirements](upgrade-guidance.md#aufs-disk-reset-after-desktop-1806).
  - Fix startup issue with AUFS
  - Fix status bug which could prevent the kubernetes cluster from starting.
  - Fix bug which would cause VM logs to be written to RAM rather than disk in some cases, and the VM to hang.
  - Fix security issue with named pipe connection to docker service.

### Docker Community Edition 18.05.0-ce-win67 2018-06-07

* Upgrades
  - [LinuxKit v0.4](https://github.com/linuxkit/linuxkit/releases/tag/v0.4)
  - Linux Kernel 4.9.93 with CEPH, DRBD, RBD, MPLS_ROUTING and MPLS_IPTUNNEL enabled
  - [Kubernetes 1.10.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.10.md#v1103). If Kubernetes is enabled, the upgrade will be performed automatically when starting Docker for Windows.

* Bug fixes and minor changes
  - Fix VPNKit memory leak. Fixes [docker/for-win#2087](https://github.com/docker/for-win/issues/2087), [moby/vpnkit#371](https://github.com/moby/vpnkit/issues/371)
  - Fix potential loss of Kubernetes local cluster certificates on reboot.

### Docker Community Edition 18.05.0-ce-win66 2018-05-17

* Upgrades
  - [Docker 18.05.0-ce](https://github.com/docker/docker-ce/releases/tag/v18.05.0-ce)
  - [Docker compose 1.21.2](https://github.com/docker/compose/releases/tag/1.21.2)

* New
  - Allow orchestrator selection from the UI in the "Kubernetes" pane, to allow "docker stack" commands to deploy to swarm clusters, even if Kubernetes is enabled in Docker for Windows.

* Bug fixes and minor changes
  - Fix restart issue when using Windows fast startup on latest 1709 Windows updates. Fixes [docker/for-win#1741](https://github.com/docker/for-win/issues/1741), [docker/for-win#1741](https://github.com/docker/for-win/issues/1741)
  - DNS name `host.docker.internal` can be used for host resolution from Windows containers.  Fixes [docker/for-win#1976](https://github.com/docker/for-win/issues/1976)
  - Fix broken link in diagnostics window.

### Docker Community Edition 18.05.0-ce-rc1-win63 2018-04-26

* Upgrades
  - [Docker 18.05.0-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v18.05.0-ce-rc1)
  - [Notary 0.6.1](https://github.com/docker/notary/releases/tag/v0.6.1)

* Bug fixes and minor changes
  - Fix startup issue due to incompatibility with other programs (like Razer Synapse 3). Fixes [docker/for-win#1723](https://github.com/docker/for-win/issues/1723)
  - Fix Kubernetes hostPath translation for PersistentVolumeClaim (PVC). Previously failing PVCs must be deleted and recreated. Fixes [docker/for-win#1758](https://github.com/docker/for-win/issues/1758)
  - Fix Kubernetes status when resetting to factory defaults.


### Docker Community Edition 18.04.0-ce-win62 2018-04-12

* Upgrades
  - [Docker 18.04.0-ce](https://github.com/docker/docker-ce/releases/tag/v18.04.0-ce)
  - [Docker compose 1.21.0](https://github.com/docker/compose/releases/tag/1.21.0)

### Docker Community Edition 18.04.0-ce-rc2-win61 2018-04-09

* Upgrades
  - [Docker 18.04.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v18.04.0-ce-rc2)
  - [Kubernetes 1.9.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.9.md#v196). If Kubernetes is enabled, the upgrade will be performed automatically when starting Docker for Windows.

* New
  - Enable ceph & rbd modules in LinuxKit VM.

* Bug fixes and minor changes
  - Fix ApyProxy not starting properly when Docker for Windows is started with the `HOME` environment variable already defined (typically started from the command line). Fixes [docker/for-win#1880](https://github.com/docker/for-win/issues/1880)

### Docker Community Edition 18.03.0-ce-win58 2018-03-26

* Upgrades
  - [Docker 18.03.0-ce](https://github.com/docker/docker-ce/releases/tag/v18.03.0-ce)
  - [Docker compose 1.20.1](https://github.com/docker/compose/releases/tag/1.20.1)

* Bug fixes and minor changes
  - Adding Docker for Windows icon on desktop is optional in the installer. Fixes [docker/for-win#246](https://github.com/docker/for-win/issues/246)

### Docker Community Edition 18.03.0-ce-rc4-win57 2018-03-15

* Upgrades
  - [Docker 18.03.0-ce-rc4](https://github.com/docker/docker-ce/releases/tag/v18.03.0-ce-rc4)
  - AUFS 20180312

* Bug fixes and minor changes
  - Fix support for AUFS. Fixes [docker/for-win#1831](https://github.com/docker/for-win/issues/1831)

### Docker Community Edition 18.03.0-ce-rc3-win56 2018-03-13

* Upgrades
  - [Docker 18.03.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v18.03.0-ce-rc3)
  - [Docker Machine 0.14.0](https://github.com/docker/machine/releases/tag/v0.14.0)
  - [Docker compose 1.20.0-rc2](https://github.com/docker/compose/releases/tag/1.20.0-rc2)
  - [Notary 0.6.0](https://github.com/docker/notary/releases/tag/v0.6.0)
  - Linux Kernel 4.9.87

* Bug fixes and minor changes
  - Fix port Windows Containers port forwarding on windows 10 build 16299 post KB4074588. Fixes [docker/for-win#1707](https://github.com/docker/for-win/issues/1707), [docker/for-win#1737](https://github.com/docker/for-win/issues/1737)
  - Fix for the HTTP/S transparent proxy when using "localhost" names (for example "host.docker.internal", "docker.for.win.host.internal", "docker.for.win.localhost").
  - If Kubernetes is enabled, switch CLI orchestrator option back to "swarm" when switching to Windows Containers.
  - Fix daemon not starting properly when setting TLS-related options.

### Docker Community Edition 18.03.0-ce-rc1-win54 2018-02-27

* Upgrades
  - [Docker 18.03.0-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v18.03.0-ce-rc1)

* New
  - VM Swap size can be changed in settings.
  - Support NFS Volume sharing. Also works in Kubernetes. See [docker/for-win#1700](https://github.com/docker/for-win/issues/1700)
  - Allow users to activate Windows container during installation (avoid vm disk creation and vm boot when working only on win containers). See [docker/for-win#217](https://github.com/docker/for-win/issues/217).

* Bug fixes and minor changes
  - DNS name `host.docker.internal` should be used for host resolution from containers. Older aliases (still valid) are deprecated in favor of this one. (See https://tools.ietf.org/html/draft-west-let-localhost-be-localhost-06).
  - Fix Linuxkit start on Windows Insider. Fixes [docker/for-win#1458](https://github.com/docker/for-win/issues/1458), [docker/for-win#1514](https://github.com/docker/for-win/issues/1514), [docker/for-win#1640](https://github.com/docker/for-win/issues/1640)
  - Fix risk of privilege escalation. (https://www.tenable.com/sc-report-templates/microsoft-windows-unquoted-service-path-vulnerability)
  - All users present in the docker-users group are now able to use docker. Fixes [docker/for-win#1732](https://github.com/docker/for-win/issues/1732)
  - Kubernetes Load balanced services are no longer marked as `Pending`.
  - Fix hostPath mounts in Kubernetes.
  - Update Compose on Kubernetes to v0.3.0 rc4. Existing Kubernetes stacks will be removed during migration and need to be re-deployed on the cluster.


### Docker Community Edition 18.02.0-ce-win52 2018-02-08

* Upgrades
  - [Docker 18.02.0-ce](https://github.com/docker/docker-ce/releases/tag/v18.02.0-ce)
  - [Docker compose 1.19.0](https://github.com/docker/compose/releases/tag/1.19.0)

### Docker Community Edition 18.02.0-ce-rc2-win51 2018-02-02

* Upgrades
  - [Docker 18.02.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v18.02.0-ce-rc2)
  - [Docker compose 1.19.0-rc2](https://github.com/docker/compose/releases/tag/1.19.0-rc2)
  - [Kubernetes 1.9.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.9.md#v192). If you have Kubernetes enabled, the upgrade will be performed automatically when starting Docker for Windows.

* New
  - Virtual machine disk size can be changed in settings. Fixes [docker/for-win#105](https://github.com/docker/for-win/issues/105)
  - New menu item to restart Docker.

* Bug fixes and minor changes
  - Migration of Docker Toolbox images is not proposed anymore in Docker For Windows installer (still possible to migrate Toolbox images manually).

### Docker Community Edition 18.02.0-ce-rc1-win50 2018-01-26

* Upgrades
  - [Docker 18.02.0-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v18.02.0-ce-rc1)

* New
  - Experimental Kubernetes Support. You can now run a single-node Kubernetes cluster from the "Kubernetes" Pane in Docker for Windows settings and use kubectl commands as well as docker commands. See [the Kubernetes section](/manuals/desktop/use-desktop/kubernetes.md).
  - LCOW containers can now be run next to Windows containers (on Windows RS3 build 16299 and later). Use `--platform=linux` in Windows container mode to run Linux Containers On Windows. Note that LCOW is still experimental, and requires daemon `experimental` option.

* Bug fixes and minor changes
  - Better cleanup for Windows containers and images on reset/uninstall. Fixes [docker/for-win#1580](https://github.com/docker/for-win/issues/1580), [docker/for-win#1544](https://github.com/docker/for-win/issues/1544), [docker/for-win#191](https://github.com/docker/for-win/issues/191)
  - Do not recreate Desktop icon on upgrade (effective on next upgrade). Fixes [docker/for-win#246](https://github.com/docker/for-win/issues/246), [docker/for-win#925](https://github.com/docker/for-win/issues/925), [docker/for-win#1551](https://github.com/docker/for-win/issues/1551)
  - Fix proxy for docker.for.win.localhost and docker.for.win.host.internal. Fixes [docker/for-win#1130](https://github.com/docker/for-win/issues/1130)

### Docker Community Edition 18.01.0-ce-win48 2018-01-19

* Upgrades
  - [Docker 18.01.0-ce](https://github.com/docker/docker-ce/releases/tag/v18.01.0-ce)
  - Linux Kernel 4.9.75

* Bug fixes and minor changes
  - Fix linuxKit port-forwarder sometimes not being able to start. Fixes [docker/for-win#1506](https://github.com/docker/for-win/issues/1506)
  - Fix certificate management when connecting to a private registry. Fixes [docker/for-win#1512](https://github.com/docker/for-win/issues/1512)
  - Fix Mount compatibility when mounting drives with `-v //c/...`, now mounted in /host_mnt/c in the LinuxKit VM. Fixes [docker/for-win#1509](https://github.com/docker/for-win/issues/1509), [docker/for-win#1516](https://github.com/docker/for-win/issues/1516), [docker/for-win#1497](https://github.com/docker/for-win/issues/1497)

### Docker Community Edition 17.12.0-ce-win45 2018-01-05

* Upgrades
  - [Docker 17.12.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.12.0-ce)

