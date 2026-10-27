---
title: Docker Desktop for Windows Edge 2017 release notes
linkTitle: Windows Edge 2017
toc_max: 3
sitemap: false
---

## Related guidance

- [Historical Edge release caveats and update prerequisites](/manuals/desktop/release-availability.md#historical-edge-releases)
- [Historical upgrade and update procedures](upgrade-guidance.md)

## Edge Releases of 2017
### Docker Community Edition 17.12.0-ce-rc4-win44 2017-12-21

* Upgrades
  - [Docker 17.12.0-ce-rc4](https://github.com/docker/docker-ce/releases/tag/v17.12.0-ce-rc4)
  - [Docker compose 1.18.0](https://github.com/docker/compose/releases/tag/1.18.0)

* Bug fixes and minor changes
  - Fix DNS "search domain" and "domain name" settings. See [docker/for-win#1437](https://github.com/docker/for-win/issues/1437).
  - Fix VPNkit issue when username has spaces. See [docker/for-win#1429](https://github.com/docker/for-win/issues/1429).
  - Diagnostic improvements to get virtual machine logs before virtual machine shutdown.

### Docker Community Edition 17.12.0-ce-rc3-win43 2017-12-15

* Upgrades
  - [Docker 17.12.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v17.12.0-ce-rc3)

* Bug fixes and minor changes
  - Fix installer check for not supported Windows `CoreCountrySpecific` Edition.

### Docker Community Edition 17.12.0-ce-rc2-win41 2017-12-13

* Upgrades
  - [Docker 17.12.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v17.12.0-ce-rc2)
  - [Docker compose 1.18.0-rc2](https://github.com/docker/compose/releases/tag/1.18.0-rc2)


* Bug fixes and minor changes
  - Fix a class of startup failures where the database fails to start, see [docker/for-win#498](https://github.com/docker/for-win/issues/498)
  - Display various component versions in About box
  - Better removal of LCOW images and containers when uninstalling Docker
  - Links in update changelog open the default browser instead of IE (fixes [docker/for-win#1311](https://github.com/docker/for-win/issues/1311))

### Docker Community Edition 17.11.0-ce-win40 2017-11-22

* Upgrades
  - [Docker 17.11.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.11.0-ce)

### Docker Community Edition 17.11.0-ce-rc4-win39 2017-11-17

* Upgrades
  - [Docker 17.11.0-ce-rc4](https://github.com/docker/docker-ce/releases/tag/v17.11.0-ce-rc4)
  - [Docker compose 1.17.1](https://github.com/docker/compose/releases/tag/1.17.1)
  - Linux Kernel 4.9.60

* Bug fixes and minor changes
  - Increased timeout for virtual machine boot startup to 2 minutes.

### Docker Community Edition 17.11.0-ce-rc3-win38 2017-11-09

* Upgrades
  - [Docker 17.11.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v17.11.0-ce-rc3)

* New
  - Use Microsoft localhost port forwarder for Windows and LCOW Containers when it is available (insider build RS4)

* Bug fixes and minor changes
  - Fix docker build exits successfully but fails to build image [moby/#35413](https://github.com/moby/moby/issues/35413)
  - Fix bug during Windows fast-startup process. Fixes [for-win/#953](https://github.com/docker/for-win/issues/953)
  - Fix uninstaller issue (in some specific cases dockerd process was not killed properly)
  - Do not propose toolbox migration popup after clicking "Try LCOW" on first startup
  - Fix `docker.for.win.localhost` not working in proxy settings. Fixes [for-win/#1130](https://github.com/docker/for-win/issues/1130)

### Docker Community Edition 17.11.0-ce-rc2-win37 2017-11-02

* Upgrades
  - [Docker 17.11.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v17.11.0-ce-rc2)
  - [Docker compose 1.17.0](https://github.com/docker/compose/releases/tag/1.17.0)
  - Linuxkit blueprint updated to [linuxkit/linuxkit#2633](https://github.com/linuxkit/linuxkit/pull/2633), fixes CVE-2017-15650

* New
  - Add localhost port forwarder for Windows and LCOW Containers (thanks @simonferquel)

* Bug fixes and minor changes
  - Fix centos:5 and centos:6 images not starting properly with LinuxKit virtual machine (fixes [docker/for-win#1245](https://github.com/docker/for-win/issues/1245)).

### Docker Community Edition 17.10.0-ce-win36 2017-10-24

* Upgrades
  - [Docker 17.10.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.10.0-ce)
  - [Docker Machine 0.13.0](https://github.com/docker/machine/releases/tag/v0.13.0)
  - [Docker compose 1.17.0-rc1](https://github.com/docker/compose/releases/tag/1.17.0-rc1)

* New
  - Virtual machine entirely built with Linuxkit
  - Experimental support for Microsoft Linux Containers On Windows, on Windows 10 RS3.


### Docker Community Edition 17.09.0-ce-win34 2017-10-06

* Bug fixes
  - Fix Docker For Windows unable to start in some cases: removed use of libgmp sometimes causing the VPNkit process to die.


### Docker Community Edition 17.09.0-ce-win31 2017-09-29

* Upgrades
  - [Docker 17.09.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.09.0-ce)

* Bug fixes and minor changes
  - VPNKit: security fix to reduce the risk of DNS cache poisoning attack (reported by Hannes Mehnert https://hannes.nqsb.io/)


### Docker Community Edition 17.09.0-ce-rc3-win30 2017-09-22

* Upgrades
  - [Docker 17.09.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v17.09.0-ce-rc3)

### Docker Community Edition 17.09.0-ce-rc2-win29 2017-09-19

* Upgrades
  - [Docker 17.09.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v17.09.0-ce-rc2)
  - Linux Kernel 4.9.49
  - AUFS 20170911

* Bug fixes and minor changes
  - Kernel: Enable TASK_XACCT and TASK_IO_ACCOUNTING
  - Rotate logs in the VM more often (docker/for-win#244)
  - VPNkit: do not block startup when ICMP permission is denied. (Fixes docker/for-win#1036, docker/for-win#1035, docker/for-win#1040)
  - Fix minor bug on update checks

### Docker Community Edition 17.09.0-ce-rc1-win28 2017-09-07

* Upgrades
  - [Docker 17.09.0-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v17.09.0-ce-rc1)
  - [Docker compose 1.16.1](https://github.com/docker/compose/releases/tag/1.16.1)
  - Linux Kernel 4.9.46

* New
  - Add `Skip this version` button in update window

* Bug fixes and minor changes
  - VPNKit: change protocol to support error messages reported back from the server
  - Reset to default stops all engines and removes settings including all daemon.json files
  - Better backend service checks (related to https://github.com/docker/for-win/issues/953)
  - Fix auto updates checkbox, no need to restart the application
  - Fix check for updates menu when auto updates was disable

### Docker Community Edition 17.07.0-win26 Release Notes (2017-09-01 17.07.0-win26)

* Upgrades
  - [Docker 17.07.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce)
  - [Docker compose 1.16.0](https://github.com/docker/compose/releases/tag/1.16.0)
  - [Docker Credential Helpers 0.6.0](https://github.com/docker/docker-credential-helpers/releases/tag/v0.6.0)

### Docker Community Edition 17.07.0-rc4-win25 Release Notes (2017-08-24 17.07.0-win25)

**Upgrades**

- [Docker 17.07.0-ce-rc4](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce-rc4)
- [Docker compose 1.16.0-rc1](https://github.com/docker/compose/releases/tag/1.16.0-rc1)

**Bug fixes and minor changes**

- VPNKit: Fixed a bug which causes a socket to leak if the corresponding
TCP connection is idle for more than 5 minutes (related to
[docker/for-mac#1374](https://github.com/docker/for-mac/issues/1374))

> [!NOTE]
>
> The link above goes to Docker for Mac issues because a
Mac user reported this problem, which applied to both Mac and Windows and was fixed on both.

### Docker Community Edition 17.07.0-rc3-win23 Release Notes (2017-08-21 17.07.0-win23)

**Upgrades**

- [Docker 17.07.0-ce-rc3](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce-rc3)

**New**

- Store Linux daemon configuration in `~\.docker\daemon.json` instead of settings file
- Store Windows daemon configuration in `C:\ProgramData\Docker\config\daemon.json` instead of settings file
- VPNKit: Added support for ping!
- VPNKit: Added `slirp/port-max-idle-timeout` to allow the timeout to be adjusted or even disabled
- VPNKit: Bridge mode is default everywhere now

**Bug fixes and minor changes**

- VPNKit: Improved the logging around the UNIX domain socket connections
- VPNKit: Automatically trim whitespace from `int` or `bool` database keys

### Docker Community Edition 17.07.0-ce-rc2-win22 Release Notes (2017-08-11 17.06.0-win22)

**Upgrades**

- [Docker 17.07.0-ce-rc2](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce-rc2)
- Linux Kernel 4.9.41

### Docker Community Edition 17.07.0-ce-rc1-win21 Release Notes (2017-07-31 17.07.0-win21)

**Upgrades**

- [Docker 17.07.0-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v17.07.0-ce-rc1)
- [Docker compose 1.15.0](https://github.com/docker/compose/releases/tag/1.15.0)
- [Docker Machine 0.12.2](https://github.com/docker/machine/releases/tag/v0.12.2)
- Linux Kernel 4.9.38

**New**

- Windows Docker daemon is now started as service for better lifecycle management

**Bug fixes and minor changes**

- Keep Docker info in the same place as before in the registry, used by Visual Studio 2017 (Fixes [docker/for-win#939](https://github.com/docker/for-win/issues/939))
- Fix `config.json` not being released properly (Fixes [docker/for-win#867](https://github.com/docker/for-win/issues/867))
- Do not anymore move credentials in credential store at startup

### Docker Community Edition 17.06.1-ce-rc1-win20 Release Notes (2017-07-18 17.06.1-win20)

**Upgrades**

- [Docker 17.06.1-ce-rc1](https://github.com/docker/docker-ce/releases/tag/v17.06.1-ce-rc1)
- Linux Kernel 4.9.36
- AUFS 20170703

**Bug fixes and minor changes**

- Fix locked container id file (Fixes [docker/for-win#818](https://github.com/docker/for-win/issues/818))
- Avoid expanding variables in PATH env variable (Fixes [docker/for-win#859](https://github.com/docker/for-win/issues/859))

### Docker Community Edition 17.06.0-win17 Release Notes (2017-06-28 17.06.0-win17)

**Upgrades**

- [Docker 17.06.0-ce](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce)

### Docker Community Edition 17.06.0-win16 Release Notes (2017-06-21 17.06.0-rc5-ce-win16)

**Upgrades**

- [Docker 17.06.0-ce-rc5](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce-rc5)
 - [Docker compose 1.14.0](https://github.com/docker/compose/releases/tag/1.14.0)

### Docker Community Edition 17.06.0-win15 Release Notes (2017-06-16 17.06.0-rc4-ce-win15)

**Upgrades**

- [Docker 17.06.0-rc4-ce](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce-rc4)
- [Docker Credential Helpers 0.5.2](https://github.com/docker/docker-credential-helpers/releases/tag/v0.5.2)
- Linux Kernel 4.9.31


### Docker Community Edition 17.06.0-win14 Release Notes (2017-06-08 17.06.0-rc2-ce-win14)

**Upgrades**

  - [Docker 17.06.0-rc2-ce](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce-rc2)
  - [Docker Machine 0.12.0](https://github.com/docker/machine/releases/tag/v0.12.0)
  - [Docker compose 1.14.0-rc2](https://github.com/docker/compose/releases/tag/1.14.0-rc2)

**New**

- Added reset to defaults button in error report window
- Unified login between Docker CLI and Docker Hub, Docker Cloud.

**Bug fixes and minor changes**

- Fixed group access check for users logged in with Active Directory (fixes [docker/for-win#785](https://github.com/docker/for-win/issues/785))
- Check environment variables and add some warnings in logs if they can cause docker to fail

### Docker Community Edition 17.06.0-win13 Release Notes (2017-06-01 17.06.0-rc1-ce-win13)

**Upgrades**

- [Docker 17.06.0-rc1-ce](https://github.com/docker/docker-ce/releases/tag/v17.06.0-ce-rc1)
- [Docker Credential Helpers 0.5.1](https://github.com/docker/docker-credential-helpers/releases/tag/v0.5.1)
- Linux Kernel 4.9.30

**New**

- Sharing a drive can be done on demand, the first time a mount is requested
- Add an experimental DNS name for the host: `docker.for.win.localhost`
- Support for client (i.e. "login") certificates for authenticating
registry access (fixes [docker/for-win#569](https://github.com/docker/for-win/issues/569))

**Bug fixes and minor changes**

- Many processes that were running in admin mode are now running within the user identity
- Cloud federation command lines now opens in the user home directory
- Named pipes are now created with more constrained security descriptors to improve security
- Security fix: Users must be part of a specific group "docker-users" to run Docker for Windows

### Docker Community Edition 17.0.5-win11 Release Notes (2017-05-12 17.05.0-ce-win11)

**Upgrades**

- Security fix for CVE-2017-7308

### Docker Community Edition 17.0.5-win9 Release Notes (2017-05-09 17.05.0-ce-win9)

**Upgrades**

- [Docker 17.05.0-ce](https://github.com/docker/docker/releases/tag/v17.05.0-ce)
- [Docker Compose 1.13.0](https://github.com/docker/compose/releases/tag/1.13.0)
- [Docker Machine 1.11.0](https://github.com/docker/machine/releases/tag/v0.11.0)

**Security**

- Disable TCP exposition of the Daemon (tcp://localhost:2375), now an opt-in feature.

**Bug fixes and minor changes**

- Reset to default / uninstall and also reset docker cli settings and logout user from Docker Cloud and registries
- Detected a bitlocker policy preventing windows containers from working
- Fixed an issue on filesharing when explicitly disabled on VMswitch interface
- Fixed virtual machine not starting when machine had very long name
- Fixed a bug where Windows daemon.json file was not written (fixes [docker/for-win#670](https://github.com/docker/for-win/issues/670))

### Docker Community Edition 17.0.5-win8 Release Notes (2017-04-13 17.05.0-ce-rc1-win8)

**Upgrades**

- [Docker 17.05.0-ce-rc1](https://github.com/docker/docker/releases/tag/v17.05.0-ce-rc1)

### Docker Community Edition 17.0.4-win7 Release Notes (2017-04-06 17.04.0-ce-win7)

**New**

- New installer experience
- Experimental Windows Server 2016 support

**Upgrades**

- [Docker 17.04.0-ce](https://github.com/docker/docker/releases/tag/v17.04.0-ce)
- [Docker Compose 1.12.0](https://github.com/docker/compose/releases/tag/1.12.0)
- Linux Kernel 4.9.19

**Bug fixes and minor changes**

- Added patches to the kernel to fix VMBus crash

### Docker Community Edition 17.04.0-ce-win6 Release Notes (2017-04-03 17.04.0-ce-rc2-win6)

**Upgrades**

- [Docker 17.04.0-ce-rc2](https://github.com/docker/docker/releases/tag/v17.04.0-ce-rc2)
- [Docker Compose 1.12.0-rc2](https://github.com/docker/compose/releases/tag/1.12.0-rc2)
- Linux Kernel 4.9.18

**Bug fixes and minor changes**

- Named pipe client connection should not trigger dead locks on `docker run` with data in stdin anymore
- Buffered data should be treated correctly when docker client requests are upgraded to raw streams

### Docker Community Edition 17.03.1 Release Notes (2017-03-28 17.03.1-ce-rc1-win3)

**Upgrades**

- [Docker 17.03.1-ce-rc1](https://github.com/docker/docker/releases/tag/v17.03.1-ce-rc1)
- [Docker Credential Helpers 0.5.0](https://github.com/docker/docker-credential-helpers/releases/tag/v0.5.0)
- Linux Kernel 4.9.14

**Bug fixes and minor changes**

- VPNKit: capture up to 64KiB of NTP traffic for diagnostics, better handling of DNS

### Docker Community Edition 17.03.0 Release Notes (2017-03-06 17.03.0-ce-win1)

**New**

- Renamed to Docker Community Edition
- Integration with Docker Cloud: control remote Swarms from the local CLI and view your repositories. This feature is going to be rolled out to all users progressively

**Upgrades**

- [Docker 17.03.0-ce](https://github.com/docker/docker/releases/tag/v17.03.0-ce)
- [Docker Compose 1.11.2](https://github.com/docker/compose/releases/tag/1.11.2)
- [Docker Machine 0.10.0](https://github.com/docker/machine/releases/tag/v0.10.0)
- Linux Kernel 4.9.12

**Bug fixes and minor changes**

- VPNKit: fix unmarshalling of DNS packets containing pointers to pointers to labels
- Match Hyper-V Integration Services by ID, not name
- Don't consume 100% CPU when the service is stopped
- Log the diagnostic id when uploading
- Improved Firewall handling: stop listing the rules since it can take a lot of time
- Don't rollback to the previous engine when the desired engine fails to start

### Docker Community Edition 17.03.0 Release Notes (2017-02-22 17.03.0-ce-rc1-win1)

**New**

- Introduce Docker Community Edition
- Integration with Docker Cloud: control remote Swarms from the local CLI and view your repositories. This feature is being rolled out to all users progressively.

**Upgrades**

- Docker 17.03.0-ce-rc1
- Linux Kernel 4.9.11

**Bug fixes and minor changes**

- VPNKit: Fixed unmarshalling of DNS packets containing pointers to pointers to labels
- Match Hyper-V Integration Services by ID, not name
- Don't consume 100% CPU when the service is stopped
- Log the diagnostic ID when uploading
- Improved Firewall handling: stop listing the rules since it can take a lot of time
- Don't rollback to the previous engine when the desired engine fails to start

### Beta 41 Release Notes (2017-02-07 1.13.1-rc2-beta41)

**Upgrades**

- Docker 1.13.1-rc2
- [Docker Compose 1.11.0-rc1](https://github.com/docker/compose/releases/tag/1.11.0-rc1)
- Linux kernel 4.9.8

**Bug fixes and minor improvements**

- VPNKit: set the Recursion Available bit on DNS responses from the cache
- Don't use port 4222 inside the Linux VM

### Beta 40 Release Notes (2017-01-31 1.13.1-rc1-beta40)

**Upgrades**

- [Docker 1.13.1-rc1](https://github.com/docker/docker/releases/tag/v1.13.1-rc1)
- Linux kernel 4.9.6

**Bug fixes and minor improvements**

- Fix startup error of `ObjectNotFound` in Set-VMFirmware
- Add detailed logs when firewall is configured
- Add a link to the Experimental Features documentation
- Fixed the Copyright in About Dialog
- VPNKit: Avoid diagnostics to capture too much data
- VPNKit: fix a source of occasional packet loss (truncation) on the virtual ethernet link
- Fix negotiation of TimeSync protocol version (through kernel update)

### Beta 39 Release Notes (2017-01-26 1.13.0-beta39)

**Upgrades**

- Linux kernel 4.9.5

**New**

- DNS forwarder ignores responses from malfunctioning servers
- DNS forwarder send all queries in parallel, process results in order
- DNS forwarder includes servers with zones in general searches
- Significantly increased single-stream TCP throughput

**Bug fixes and minor improvements**

- Fix some timeout issues in port forwarding
- Fix for swap not being mounted ([docker/for-win#403](https://github.com/docker/for-win/issues/403))
- Fix aufs xattr delete issue ([docker/docker#30245](https://github.com/docker/docker/issues/30245))

### Beta 38 Release Notes (2017-01-20 1.13.0-beta38)

**Upgrades**

- [Docker 1.13.0](https://github.com/docker/docker/releases/tag/v1.13.0)
- [Docker Compose 1.10](https://github.com/docker/compose/releases/tag/1.10.0)
- [Docker Machine 0.9.0](https://github.com/docker/machine/releases/tag/v0.9.0)
- [Notary 0.4.3](https://github.com/docker/notary/releases/tag/v0.4.3)
- Linux kernel 4.9.4
- qcow-tool 0.7.2

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

**Bug fixes and minor changes**

- You cannot edit settings while Docker is restarting
- Support Copy/Paste in About box
- Auto update polling every 24h
- Kernel boots with vsyscall=emulate arg and CONFIG_LEGACY_VSYSCALL is set to NONE in Moby
- Fixed vsock deadlock under heavy write load
- If you opt-out of analytics, you're prompted for approval before a bug report is sent
- Fixed bug where search domain could be read as `DomainName`
- Dedicated preference pane for HTTP proxy settings.
- Dedicated preference pane for CPU and Memory computing resources.
- Privacy settings moved to the general preference pane.
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
- VPNKit: Fixed bug which could cause the connection tracking to
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

