---
title: Docker Desktop for Mac Edge 2017 release notes
linkTitle: Mac Edge 2017
toc_max: 3
sitemap: false
---

## Related guidance

- [Historical Edge release caveats and update prerequisites](/manuals/desktop/release-availability.md#historical-edge-releases)
- [Historical upgrade and update procedures](upgrade-guidance.md)

## Edge Releases of 2017

### Docker Community Edition 17.12.0-ce-rc4-mac44 2017-12-21

- Upgrades
  - [Docker 17.12.0-ce-rc4](https://github.com/docker/docker-ce/releases/tag/v17.12.0-ce-rc4)
  - [Docker compose 1.18.0](https://github.com/docker/compose/releases/tag/1.18.0)

- Bug fixes and minor changes
  - Display actual size used by the virtual machine disk, especially useful for disks using raw format. See [docker/for-mac#2297](https://github.com/docker/for-mac/issues/2297).
  - Fix more specific edge cases in filesharing settings migration.

### Docker Community Edition 17.12.0-ce-rc3-mac43 2017-12-15

- Upgrades
  - [Docker 17.12.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v17.12.0-ce-rc3)

- Bug fixes and minor changes
  - Fix filesharing migration issue ([docker/for-mac#2317](https://github.com/docker/for-mac/issues/2317))

### Docker Community Edition 17.12.0-ce-rc2-mac41 2017-12-13

- Upgrades
  - [Docker 17.12.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v17.12.0-ce-rc2)
  - [Docker compose 1.18.0-rc2](https://github.com/docker/compose/releases/tag/1.18.0-rc2)

- New
  - Virtual machine disk size can be changed in settings. (See [docker/for-mac#1037](https://github.com/docker/for-mac/issues/1037)).

- Bug fixes and minor changes
  - Avoid virtual machine reboot when changing host proxy settings.
  - Don't break HTTP traffic between containers by forwarding them through the external proxy [docker/for-mac#981](https://github.com/docker/for-mac/issues/981)
  - Filesharing settings are now stored in settings.json
  - Daemon restart button has been moved to settings / Reset Tab
  - Display various component versions in About box
  - Better virtual machine state handling and error messages in case of virtual machine crashes

### Docker Community Edition 17.11.0-ce-mac40 2017-11-22

- Upgrades
  - [Docker 17.11.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.11.0-ce)

### Docker Community Edition 17.11.0-ce-rc4-mac39 2017-11-17

- Upgrades
  - [Docker 17.11.0-ce-rc4](https://github.com/docker/docker-ce/releases/tag/v17.11.0-ce-rc4)
  - [Docker compose 1.17.1](https://github.com/docker/compose/releases/tag/1.17.1)
  - Linux kernel 4.9.60

- Bug fixes and minor changes
  - Fix login into private repository with certificate issue. [docker/for-mac#2201](https://github.com/docker/for-mac/issues/2201)

- New
  - For systems running APFS on SSD on High Sierra, use `raw` format virtual machine disks by default. This increases disk throughput (from 320MiB/sec to 600MiB/sec in `dd` on a 2015 MacBook Pro) and disk space handling.
    Existing disks are kept in qcow format, if you want to switch to raw format you need to "Reset to factory defaults". To query the space usage of the file, use a command like:
    `$ cd ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/`
    `$ ls -ls Docker.raw`
    `3944768 -rw-r--r--@ 1 user  staff  68719476736 Nov 16 11:19 Docker.raw`
    The first number (`3944768`) is the allocated space in blocks; the larger number `68719476736` is the maximum total amount of space the file may consume in future in bytes.

### Docker Community Edition 17.11.0-ce-rc3-mac38 2017-11-09

- Upgrades
  - [Docker 17.11.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v17.11.0-ce-rc3)

- Bug fixes and minor changes
  - Fix Docker build exits successfully but fails to build image [moby/#35413](https://github.com/moby/moby/issues/35413).

### Docker Community Edition 17.11.0-ce-rc2-mac37 2017-11-02

- Upgrades
  - [Docker 17.11.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v17.11.0-ce-rc2)
  - [Docker compose 1.17.0](https://github.com/docker/compose/releases/tag/1.17.0)
  - Linuxkit blueprint updated to [linuxkit/linuxkit#2633](https://github.com/linuxkit/linuxkit/pull/2633), fixes CVE-2017-15650

- Bug fixes and minor changes
  - Fix centos:5 & centos:6 images not starting properly with LinuxKit virtual machine (fixes [docker/for-mac#2169](https://github.com/docker/for-mac/issues/2169)).

### Docker Community Edition 17.10.0-ce-mac36 2017-10-24

- Upgrades
  - [Docker 17.10.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.10.0-ce)
  - [Docker Machine 0.13.0](https://github.com/docker/machine/releases/tag/v0.13.0)
  - [Docker compose 1.17.0-rc1](https://github.com/docker/compose/releases/tag/1.17.0-rc1)

- New
  - Virtual machine entirely built with Linuxkit

### Docker Community Edition 17.09.0-ce-mac34 2017-10-06

- Bug fixes and minor changes
  - Fix Docker For Mac unable to start in some cases : removed use of libgmp sometimes causing the vpnkit process to die.

### Docker Community Edition 17.09.0-ce-mac31 2017-09-29

- Upgrades
  - [Docker 17.09.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.09.0-ce)
  - DataKit update (fix instability on High Sierra)

- Bug fixes and minor changes
  - Fix password encoding/decoding. May require to re-login to docker cloud after this version is installed. (Fixes:docker/for-mac#2008, docker/for-mac#2016, docker/for-mac#1919, docker/for-mac#712, docker/for-mac#1220).

### Docker Community Edition 17.09.0-ce-rc3-mac30 2017-09-22

- Upgrades
  - [Docker 17.09.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v17.09.0-ce-rc3)

### Docker Community Edition 17.09.0-ce-rc2-mac29 2017-09-19

- Upgrades
  - [Docker 17.09.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v17.09.0-ce-rc2)
  - Linux Kernel 4.9.49
  - AUFS 20170911

- Bug fixes and minor changes
  - Kernel: Enable TASK_XACCT and TASK_IO_ACCOUNTING [docker/for-mac#1608](https://github.com/docker/for-mac/issues/1608)
  - Rotate logs in the virtual machine more often

### Docker Community Edition 17.09.0-ce-rc1-mac28 2017-09-07

- Upgrades
  - [Docker 17.09.0-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v17.09.0-ce-rc1)
  - [Docker compose 1.16.1](https://github.com/docker/compose/releases/tag/1.16.1)
  - Linux Kernel 4.9.46

- Bug fixes and minor changes
  - VPNKit: change protocol to support error messages reported back from the server

### Docker Community Edition 17.07.0-ce-mac26, 2017-09-01

- Upgrades
  - [Docker 17.07.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce)
  - [Docker compose 1.16.0](https://github.com/docker/compose/releases/tag/1.16.0)
  - [Docker Credential Helpers 0.6.0](https://github.com/docker/docker-credential-helpers/releases/tag/v0.6.0)

### Docker Community Edition 17.07.0-ce-rc4-mac25, 2017-08-24

**Upgrades**

- [Docker 17.07.0-ce-rc4](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce-rc4)
- [Docker compose 1.16.0-rc1](https://github.com/docker/compose/releases/tag/1.16.0-rc1)

**Bug fixes and minor changes**

- Fixed string validation in daemon options (related to [docker/for-mac#1971](https://github.com/docker/for-mac/issues/1971))
- VPNKit: Fixed a bug which causes a socket to leak if the corresponding
  TCP connection is idle for more than five minutes (related to
  [docker/for-mac#1374](https://github.com/docker/for-mac/issues/1374))

### Docker Community Edition 17.07.0-ce-rc3-mac23, 2017-08-21

**Upgrades**

- [Docker 17.07.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce-rc3)

**New**

- VPNKit: Added support for ping!
- VPNKit: Added `slirp/port-max-idle-timeout` to allow the timeout to be adjusted or even disabled
- VPNKit: Bridge mode is default everywhere now

**Bug fixes and minor changes**

- VPNKit: Improved the logging around the UNIX domain socket connections
- VPNKit: Automatically trim whitespace from `int` or `bool` database keys

### Docker Community Edition 17.07.0-ce-rc2-mac22, 2017-08-11

**Upgrades**

- [Docker 17.07.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce-rc2)
- Linux Kernel 4.9.41

### Docker Community Edition 17.07.0-ce-rc1-mac21, 2017-07-31

**Upgrades**

- [Docker 17.07.0-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce-rc1)
- [Docker compose 1.15.0](https://github.com/docker/compose/releases/tag/1.15.0)
- [Docker Machine 0.12.2](https://github.com/docker/machine/releases/tag/v0.12.2)
- Linux Kernel 4.9.38

**New**

- Transparent proxy using macOS system proxies (if defined) directly
- GUI settings are now stored in `~/Library/Group\ Containers/group.com.docker/settings.json`. `daemon.json` in now a file in `~/.docker/`
- You can now change the default IP address used by Hyperkit if it collides with your network

**Bug fixes and minor changes**

- Add daemon options validation
- Diagnose can be cancelled & Improved help information. Fixes [docker/for-mac#1134](https://github.com/docker/for-mac/issues/1134), [docker/for-mac#1474](https://github.com/docker/for-mac/issues/1474)
- Support paging of Docker Cloud [repositories](../../docker-hub/repos/_index.md) and [organizations](../../admin/organization/setup/orgs.md). Fixes [docker/for-mac#1538](https://github.com/docker/for-mac/issues/1538)

### Docker Community Edition 17.06.1-ce-mac20, 2017-07-18

**Upgrades**

- [Docker 17.06.1-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v17.06.1-ce-rc1)
- Linux Kernel 4.9.36
- AUFS 20170703

### Docker Community Edition 17.06.0-ce-mac17, 2017-06-28

**Upgrades**

- [Docker 17.06.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce)

### Docker Community Edition 17.06.0-rc5-ce-mac16, 2017-06-21

**Upgrades**

- [Docker 17.06.0-ce-rc5](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce-rc5)
- [Docker compose 1.14.0](https://github.com/docker/compose/releases/tag/1.14.0)

### Docker Community Edition 17.06.0-rc4-ce-mac15, 2017-06-16

**Upgrades**

- [Docker 17.06.0-rc4-ce](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce-rc4)
- [Docker Credential Helpers 0.5.2](https://github.com/docker/docker-credential-helpers/releases/tag/v0.5.2)
- Linux Kernel 4.9.31

### Docker Community Edition 17.06.0-rc2-ce-mac14, 2017-06-08

**Upgrades**

- [Docker 17.06.0-rc2-ce](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce-rc2)
- [Docker Machine 0.12.0](https://github.com/docker/machine/releases/tag/v0.12.0)
- [Docker compose 1.14.0-rc2](https://github.com/docker/compose/releases/tag/1.14.0-rc2)

### Docker Community Edition 17.06.0-rc1-ce-mac13, 2017-06-01

**Upgrades**

- [Docker 17.06.0-rc1-ce](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce-rc1)
- [Docker Credential Helpers 0.5.1](https://github.com/docker/docker-credential-helpers/releases/tag/v0.5.1)
- `qcow-tool` v0.10.0 (improve the performance of `compact`: `mirage/ocaml-qcow#94`)
- OS X Yosemite 10.10 is marked as deprecated
- Linux Kernel 4.9.30

**New**

- GUI option to opt out of credential store
- GUI option to reset docker data without losing all settings (fixes [docker/for-mac#1309](https://github.com/docker/for-mac/issues/1309))
- Add an experimental DNS name for the host: `docker.for.mac.localhost`
- Support for client (such as "login") certificates for authenticating registry access (fixes [docker/for-mac#1320](https://github.com/docker/for-mac/issues/1320))

**Bug fixes and minor changes**

- Resync HTTP(S) proxy settings on application start
- Interpret system proxy setting of localhost correctly (see [docker/for-mac#1511](https://github.com/docker/for-mac/issues/1511))
- All docker binaries bundled with Docker for Mac are now signed
- Display all docker cloud organizations and repositories in the whale menu (fixes [docker/for-mac#1538](https://github.com/docker/for-mac/issues/1538))
- OSXFS: improved latency for many common operations, such as read and write by approximately 25%

### Docker Community Edition 17.05.0-ce-mac11, 2017-05-12

**Upgrades**

- Security fix for CVE-2017-7308

### Docker Community Edition 17.05.0-ce-mac9, 2017-05-09

**Upgrades**

- [Docker 17.05.0-ce](https://github.com/docker/docker/releases/tag/v17.05.0-ce)
- [Docker Compose 1.13.0](https://github.com/docker/compose/releases/tag/1.13.0)
- [Docker Machine 1.11.0](https://github.com/docker/machine/releases/tag/v0.11.0)

**Bug fixes and minor changes**

- Fixed GUI crash when text table view was selected and windows re-opened (fixes [docker/for-mac#1477](https://github.com/docker/for-mac/issues/1477))
- Reset to default / uninstall also remove `config.json` and `osxkeychain` credentials
- More detailed VirtualBox uninstall requirements ( [docker/for-mac#1343](https://github.com/docker/for-mac/issues/1343))
- You are now prompted for your password, if you changed it in Docker Cloud.
- Request time sync after waking up to improve [docker/for-mac#17](https://github.com/docker/for-mac/issues/17)

### Docker Community Edition 17.05.0-ce-rc1-mac8, 2017-04-13

**Upgrades**

- [Docker 17.05.0-ce-rc1](https://github.com/docker/docker/releases/tag/v17.05.0-ce-rc1)

### Docker Community Edition 17.04.0-ce-mac7, 2017-04-06

**New**

- OSXFS: support for `cached` mount flag to improve performance of macOS mounts when strict consistency is not necessary

**Upgrades**

- [Docker 17.04.0-ce](https://github.com/docker/docker/releases/tag/v17.04.0-ce)
- [Docker Compose 1.12.0](https://github.com/docker/compose/releases/tag/1.12.0)
- Linux Kernel 4.9.19

**Bug fixes and minor changes**

- VPNKit: Improved DNS timeout handling (fixes [docker/for-mac#202](https://github.com/docker/vpnkit/issues/202))
- VPNKit: Use DNSServiceRef API by default (only enabled for new installs or after factory reset)
- Add a reset to factory defaults button when application crashes
- Toolbox import dialog now defaults to "Skip"

### Docker Community Edition 17.04.0-ce-rc2-mac6, 2017-04-03

**Upgrades**

- [Docker 17.04.0-ce-rc2](https://github.com/docker/docker/releases/tag/v17.04.0-ce-rc2)
- [Docker Compose 1.12.0-rc2](https://github.com/docker/compose/releases/tag/1.12.0-rc2)
- Linux Kernel 4.9.18

**Bug fixes and minor changes**

- Buffered data should be treated correctly when Docker client requests are upgraded to raw streams
- Removed an error message from the output related to experimental features handling
- `vmnetd` should not crash when user home directory is on an external drive
- Improved settings database schema handling
- Disk trimming should work as expected
- Diagnostics now contains more settings data

### Docker Community Edition 17.03.1-ce-rc1-mac3, 2017-03-28

**Upgrades**

- [Docker 17.03.1-ce-rc1](https://github.com/docker/docker/releases/tag/v17.03.1-ce-rc1)
- [Docker Credential Helpers 0.5.0](https://github.com/docker/docker-credential-helpers/releases/tag/v0.5.0)
- Linux Kernel 4.9.14

**Bug fixes and minor changes**

- Use `fsync` rather than `fcntl`(`F_FULLFSYNC`)
- Update max-connections to 2000 ([docker/for-mac#1374](https://github.com/docker/for-mac/issues/1374) and [docker/for-mac#1132](https://github.com/docker/for-mac/issues/1132))
- VPNKit: capture up to 64KiB of NTP traffic for diagnostics, better handling of DNS
- UI: fix edge cases which crash the application
- QCOW: numerous bugfixes
- osxfs: buffer readdir

### Docker Community Edition 17.03.0-ce-mac2, 2017-03-06

**Hotfixes**

- Set the ethernet MTU to 1500 to prevent a hyperkit crash
- Fix Docker build on private images

**Upgrades**

- [Docker Credential Helpers 0.4.2](https://github.com/docker/docker-credential-helpers/releases/tag/v0.4.2)

### Docker Community Edition 17.03.0-ce-mac1, 2017-03-02

**New**

- Renamed to Docker Community Edition
- Integration with Docker Cloud: control remote Swarms from the local CLI and view your repositories. This feature is going to be rolled out to all users progressively
- Docker will now securely store your IDs in the macOS keychain

**Upgrades**

- [Docker 17.03.0-ce](https://github.com/docker/docker/releases/tag/v17.03.0-ce)
- [Docker Compose 1.11.2](https://github.com/docker/compose/releases/tag/1.11.2)
- [Docker Machine 0.10.0](https://github.com/docker/machine/releases/tag/v0.10.0)
- Linux Kernel 4.9.12

**Bug fixes and minor changes**

- VPNKit: fix unmarshalling of DNS packets containing pointers to pointers to labels
- osxfs: catch EPERM when reading extended attributes of non-files
- Add page_poison=1 to boot args
- Add a new disk flushing option

### Docker Community Edition 17.03.0 RC1 Release Notes (2017-02-22 17.03.0-ce-rc1-mac1)

**New**

- Introduce Docker Community Edition
- Integration with Docker Cloud to control remote Swarms from the local CLI and view your repositories. This feature will be rolled out to all users progressively
- Docker will now use keychain access to secure your IDs

**Upgrades**

- Docker 17.03.0-ce-rc1
- Linux Kernel 4.9.11

**Bug fixes and minor changes**

- VPNKit: fixed unmarshalling of DNS packets containing pointers to pointers to labels
- osxfs: catch EPERM when reading extended attributes of non-files
- Added `page_poison=1` to boot args
- Added a new disk flushing option

### Beta 42 Release Notes (2017-02-09 1.13.1-beta42)

**Upgrades**

- [Docker 1.13.1](https://github.com/docker/docker/releases/tag/v1.13.1)
- [Docker Compose 1.11.1](https://github.com/docker/compose/releases/tag/1.11.1)

### Beta 41 Release Notes (2017-02-07-2017-1.13.1-rc2-beta41)

**Upgrades**

- Docker 1.13.1-rc2
- [Docker Compose 1.11.0-rc1](https://github.com/docker/compose/releases/tag/1.11.0-rc1)
- Linux kernel 4.9.8

**Bug fixes and minor improvements**

- VPNKit: set the Recursion Available bit on DNS responses from the cache
- Don’t use port 4222 inside the Linux VM

### Beta 40 Release Notes (2017-01-31 1.13.1-rc1-beta40)

**Upgrades**

- [Docker 1.13.1-rc1](https://github.com/docker/docker/releases/tag/v1.13.1-rc1)
- Linux kernel 4.9.6

**New**

- Allow to reset faulty `daemon.json` through a link in advanced subpanel
- Add link to experimental features
- Hide restart button in settings window
- Increase the maximum number of vCPUs to 64

**Bug fixes and minor improvements**

- VPNKit: Avoid diagnostics to capture too much data
- VPNKit: Fix a source of occasional packet loss (truncation) on the virtual ethernet link
- HyperKit: Dump guest physical and linear address from VMCS when dumping state
- HyperKit: Kernel boots with `panic=1` arg

### Beta 39 Release Notes (2017-01-26 1.13.0-beta39)

**Upgrades**

- Linux kernel 4.9.5

**New**

- More options when moving disk image
- Filesharing and daemon table empty fields are editable
- DNS forwarder ignores responses from malfunctioning servers ([docker/for-mac#1025](https://github.com/docker/for-mac/issues/1025))
- DNS forwarder send all queries in parallel, process results in order
- DNS forwarder includes servers with zones in general searches ([docker/for-mac#997](https://github.com/docker/for-mac/issues/997))
- Parses aliases from /etc/hosts ([docker/for-mac#983](https://github.com/docker/for-mac/issues/983))
- Can resolve DNS requests through servers listed in the /etc/resolver directory on the host

**Bug fixes and minor improvements**

- Fix bug where update window hides when app not focused
- Limit vCPUs to 16 ([docker/for-mac#1144](https://github.com/docker/for-mac/issues/1144))
- Fix for swap not being mounted
- Fix AUFS xattr delete issue ([docker/docker#30245](https://github.com/docker/docker/issues/30245))

### Beta 38 Release Notes (2017-01-20 1.13.0-beta38)

**Upgrades**

- [Docker 1.13.0](https://github.com/docker/docker/releases/tag/v1.13.0)
- [Docker Compose 1.10](https://github.com/docker/compose/releases/tag/1.10.0)
- [Docker Machine 0.9.0](https://github.com/docker/machine/releases/tag/v0.9.0)
- [Notary 0.4.3](https://github.com/docker/notary/releases/tag/v0.4.3)
- Linux kernel 4.9.4
- QCOW-tool 0.7.2

**New**

- The storage location of the Linux volume can now be moved
- Reclaim disk size on reboot
- You can now edit filesharing paths
- Memory can be allocated with 256 MiB steps
- Proxy can now be completely disabled
- Support for arm, aarch64, ppc64le architectures using qemu
- Dedicated preference pane for advanced configuration of the docker daemon (edit daemon.json)
- Docker Experimental mode can be toggled
- Better support for Split DNS VPN configurations
- Use more DNS servers, respect order

**Bug fixes and minor improvements**

- You can't edit settings while docker is restarting
- Support Copy/Paste in About box
- Auto update polling every 24h
- Kernel boots with vsyscall=emulate arg and CONFIG_LEGACY_VSYSCALL is set to NONE in Moby
- Fixed vsock deadlock under heavy write load
- If you opt-out of analytics, you're prompted for approval before a bug report is sent
- Fixed bug where search domain could be read as `DomainName`
- Dedicated preference pane for HTTP proxy settings.
- Dedicated preference pane for CPU & Memory computing resources.
- Privacy settings moved to the general preference pane
- Fixed an issue where the preference pane disappeared when the welcome whale menu was closed.
- HyperKit: code cleanup and minor fixes
- Improvements to Logging and Diagnostics
- osxfs: switch to libev/kqueue to improve latency
- VPNKit: improvements to DNS handling
- VPNKit: Improved diagnostics
- VPNKit: Forwarded UDP datagrams should have correct source port numbers
- VPNKit: add a local cache of DNS responses
- VPNKit: If one request fails, allow other concurrent requests to succeed.
  For example this allows IPv4 servers to work even if IPv6 is broken.
- VPNKit: Fix bug which could cause the connection tracking to
  underestimate the number of active connections

### Beta 37 Release Notes (2017-01-16 1.13.0-rc7-beta37)

**Upgrades**

- Docker 1.13.0-rc7
- Notary 0.4.3
- Linux kernel 4.9.3

### Beta 36 Release Notes (2017-01-12 1.13.0-rc6-beta36)

> [!IMPORTANT]
>
> Plugins installed using the experimental "managed plugins" feature in Docker 1.12 must be removed/uninstalled before upgrading.

**Upgrades**

- Docker 1.13.0-rc6
- Docker Compose 1.10-rc2
- Linux Kernel 4.9.2

**Bug fixes and minor improvements**

- Uninstall should be more reliable

### Beta 35 Release Notes (2017-01-06 1.13.0-rc5-beta35)

> [!IMPORTANT]
>
> Plugins installed using the experimental "managed plugins" feature in Docker 1.12 must be removed/uninstalled before upgrading.

**Upgrades**

- Docker 1.13.0-rc5
- Docker Compose 1.10-rc1

