---
title: Docker Engine 1.12 release notes
linkTitle: Engine 1.12
toc_max: 2
---

## Related guidance

- [Engine installation instructions](/manuals/engine/install/_index.md)
- [Deprecated and removed Engine features](/manuals/engine/deprecated.md)
- [Engine API version history](/reference/api/engine/version-history/)

## Find a release

- [1.12.6 (2017-01-10)](#1126-2017-01-10)
- [1.12.5 (2016-12-15)](#1125-2016-12-15)
- [1.12.4 (2016-12-12)](#1124-2016-12-12)
- [1.12.3 (2016-10-26)](#1123-2016-10-26)
- [1.12.2 (2016-10-11)](#1122-2016-10-11)
- [1.12.1 (2016-08-18)](#1121-2016-08-18)
- [1.12.0 (2016-07-28)](#1120-2016-07-28)

## Find changes

- Security notes: [1.12.6 (2017-01-10)](#1126-2017-01-10), [1.12.3 (2016-10-26)](#1123-2016-10-26), [1.12.1 (2016-08-18)](#1121-2016-08-18)

## 1.12.6 (2017-01-10)

> [!IMPORTANT]
>
> Docker 1.12 ships with an updated systemd unit file for rpm
based installs (which includes RHEL, Fedora, CentOS, and Oracle Linux 7). When upgrading from an older version of Docker, the upgrade process may not automatically install the updated version of the unit file, or fail to start the `docker service` if;
> - the systemd unit file (`/usr/lib/systemd/system/docker.service`) contains local changes, or
> - a systemd drop-in file is present, and contains `-H fd://` in the `ExecStart` directive

Starting the `docker service` will produce an error:

    Failed to start docker.service: Unit docker.socket failed to load: No such file or directory.

or

    no sockets found via socket activation: make sure the service was started by systemd.

To resolve this:

- Backup the current version of the unit file, and replace the file with the
  [version that ships with docker 1.12](https://raw.githubusercontent.com/docker/docker/v1.12.0/contrib/init/systemd/docker.service.rpm)
- Remove the `Requires=docker.socket` directive from the `/usr/lib/systemd/system/docker.service` file if present
- Remove `-H fd://` from the `ExecStart` directive (both in the main unit file, and in any drop-in files present).

After making those changes, run `sudo systemctl daemon-reload`, and `sudo
systemctl restart docker` to reload changes and (re)start the docker daemon.

> [!NOTE]
>
> Docker 1.12.5 will correctly validate that either an IPv6 subnet is provided or that the IPAM driver can provide one when you specify the `--ipv6` option.

If you are currently using the `--ipv6` option _without_ specifying the
`--fixed-cidr-v6` option, the Docker daemon will refuse to start with the
following message:

```text
Error starting daemon: Error initializing network controller: Error creating
                       default "bridge" network: failed to parse pool request
                       for address space "LocalDefault" pool " subpool ":
                       could not find an available, non-overlapping IPv6 address
                       pool among the defaults to assign to the network
```

To resolve this error, either remove the `--ipv6` flag (to preserve the same
behavior as in Docker 1.12.3 and earlier), or provide an IPv6 subnet as the
value of the `--fixed-cidr-v6` flag.

In a similar way, if you specify the `--ipv6` flag when creating a network
with the default IPAM driver, without providing an IPv6 `--subnet`, network
creation will fail with the following message:

```text
Error response from daemon: failed to parse pool request for address space
                            "LocalDefault" pool "" subpool "": could not find an
                            available, non-overlapping IPv6 address pool among
                            the defaults to assign to the network
```

To resolve this, either remove the `--ipv6` flag (to preserve the same behavior
as in Docker 1.12.3 and earlier), or provide an IPv6 subnet as the value of the
`--subnet` flag.

The network creation will instead succeed if you use an external IPAM driver
which supports automatic allocation of IPv6 subnets.

### Runtime

- Fix runC privilege escalation (CVE-2016-9962)

## 1.12.5 (2016-12-15)

> [!IMPORTANT]
>
> Docker 1.12 ships with an updated systemd unit file for rpm
based installs (which includes RHEL, Fedora, CentOS, and Oracle Linux 7). When upgrading from an older version of Docker, the upgrade process may not automatically install the updated version of the unit file, or fail to start the `docker service` if;
> - the systemd unit file (`/usr/lib/systemd/system/docker.service`) contains local changes, or
> - a systemd drop-in file is present, and contains `-H fd://` in the `ExecStart` directive

Starting the `docker service` will produce an error:

    Failed to start docker.service: Unit docker.socket failed to load: No such file or directory.

or

    no sockets found via socket activation: make sure the service was started by systemd.

To resolve this:

- Backup the current version of the unit file, and replace the file with the
  [version that ships with docker 1.12](https://raw.githubusercontent.com/docker/docker/v1.12.0/contrib/init/systemd/docker.service.rpm)
- Remove the `Requires=docker.socket` directive from the `/usr/lib/systemd/system/docker.service` file if present
- Remove `-H fd://` from the `ExecStart` directive (both in the main unit file, and in any drop-in files present).

After making those changes, run `sudo systemctl daemon-reload`, and `sudo
systemctl restart docker` to reload changes and (re)start the docker daemon.

> [!NOTE]
>
> Docker 1.12.5 will correctly validate that either an IPv6 subnet is provided or that the IPAM driver can provide one when you specify the `--ipv6` option.

If you are currently using the `--ipv6` option _without_ specifying the
`--fixed-cidr-v6` option, the Docker daemon will refuse to start with the
following message:

```text
Error starting daemon: Error initializing network controller: Error creating
                       default "bridge" network: failed to parse pool request
                       for address space "LocalDefault" pool " subpool ":
                       could not find an available, non-overlapping IPv6 address
                       pool among the defaults to assign to the network
```

To resolve this error, either remove the `--ipv6` flag (to preserve the same
behavior as in Docker 1.12.3 and earlier), or provide an IPv6 subnet as the
value of the `--fixed-cidr-v6` flag.

In a similar way, if you specify the `--ipv6` flag when creating a network
with the default IPAM driver, without providing an IPv6 `--subnet`, network
creation will fail with the following message:

```text
Error response from daemon: failed to parse pool request for address space
                            "LocalDefault" pool "" subpool "": could not find an
                            available, non-overlapping IPv6 address pool among
                            the defaults to assign to the network
```

To resolve this, either remove the `--ipv6` flag (to preserve the same behavior
as in Docker 1.12.3 and earlier), or provide an IPv6 subnet as the value of the
`--subnet` flag.

The network network creation will instead succeed if you use an external IPAM driver
which supports automatic allocation of IPv6 subnets.

### Runtime

- Fix race on sending stdin close event [#29424](https://github.com/docker/docker/pull/29424)

### Networking

- Fix panic in docker network ls when a network was created with `--ipv6` and no ipv6 `--subnet` in older docker versions [#29416](https://github.com/docker/docker/pull/29416)

### Contrib

- Fix compilation on Darwin [#29370](https://github.com/docker/docker/pull/29370)

## 1.12.4 (2016-12-12)

> [!IMPORTANT]
>
> Docker 1.12 ships with an updated systemd unit file for rpm
based installs (which includes RHEL, Fedora, CentOS, and Oracle Linux 7). When upgrading from an older version of Docker, the upgrade process may not automatically install the updated version of the unit file, or fail to start the `docker service` if;
> - the systemd unit file (`/usr/lib/systemd/system/docker.service`) contains local changes, or
> - a systemd drop-in file is present, and contains `-H fd://` in the `ExecStart` directive

Starting the `docker service` will produce an error:

    Failed to start docker.service: Unit docker.socket failed to load: No such file or directory.

or

    no sockets found via socket activation: make sure the service was started by systemd.

To resolve this:

- Backup the current version of the unit file, and replace the file with the
  [version that ships with docker 1.12](https://raw.githubusercontent.com/docker/docker/v1.12.0/contrib/init/systemd/docker.service.rpm)
- Remove the `Requires=docker.socket` directive from the `/usr/lib/systemd/system/docker.service` file if present
- Remove `-H fd://` from the `ExecStart` directive (both in the main unit file, and in any drop-in files present).

After making those changes, run `sudo systemctl daemon-reload`, and `sudo
systemctl restart docker` to reload changes and (re)start the docker daemon.


### Runtime

- Fix issue where volume metadata was not removed [#29083](https://github.com/docker/docker/pull/29083)
- Asynchronously close streams to prevent holding container lock [#29050](https://github.com/docker/docker/pull/29050)
- Fix selinux labels for newly created container volumes [#29050](https://github.com/docker/docker/pull/29050)
- Remove hostname validation [#28990](https://github.com/docker/docker/pull/28990)
- Fix deadlocks caused by IO races [#29095](https://github.com/docker/docker/pull/29095) [#29141](https://github.com/docker/docker/pull/29141)
- Return an empty stats if the container is restarting [#29150](https://github.com/docker/docker/pull/29150)
- Fix volume store locking [#29151](https://github.com/docker/docker/pull/29151)
- Ensure consistent status code in API [#29150](https://github.com/docker/docker/pull/29150)
- Fix incorrect opaque directory permission in overlay2 [#29093](https://github.com/docker/docker/pull/29093)
- Detect plugin content and error out on `docker pull` [#29297](https://github.com/docker/docker/pull/29297)

### Swarm Mode

* Update Swarmkit [#29047](https://github.com/docker/docker/pull/29047)
  - orchestrator/global: Fix deadlock on updates [docker/swarmkit#1760](https://github.com/docker/swarmkit/pull/1760)
  - on leader switchover preserve the vxlan id for existing networks [docker/swarmkit#1773](https://github.com/docker/swarmkit/pull/1773)
- Refuse swarm spec not named "default" [#29152](https://github.com/docker/docker/pull/29152)

### Networking

* Update libnetwork [#29004](https://github.com/docker/docker/pull/29004) [#29146](https://github.com/docker/docker/pull/29146)
  - Fix panic in embedded DNS [docker/libnetwork#1561](https://github.com/docker/libnetwork/pull/1561)
  - Fix unmarhalling panic when passing --link-local-ip on global scope network [docker/libnetwork#1564](https://github.com/docker/libnetwork/pull/1564)
  - Fix panic when network plugin returns nil StaticRoutes [docker/libnetwork#1563](https://github.com/docker/libnetwork/pull/1563)
  - Fix panic in `osl.(*networkNamespace).DeleteNeighbor` [docker/libnetwork#1555](https://github.com/docker/libnetwork/pull/1555)
  - Fix panic in swarm networking concurrent map read/write [docker/libnetwork#1570](https://github.com/docker/libnetwork/pull/1570)
  * Allow encrypted networks when running docker inside a container [docker/libnetwork#1502](https://github.com/docker/libnetwork/pull/1502)
  - Do not block autoallocation of IPv6 pool [docker/libnetwork#1538](https://github.com/docker/libnetwork/pull/1538)
  - Set timeout for netlink calls [docker/libnetwork#1557](https://github.com/docker/libnetwork/pull/1557)
  - Increase networking local store timeout to one minute [docker/libkv#140](https://github.com/docker/libkv/pull/140)
  - Fix a panic in `libnetwork.(*sandbox).execFunc` [docker/libnetwork#1556](https://github.com/docker/libnetwork/pull/1556)
  - Honor icc=false for internal networks [docker/libnetwork#1525](https://github.com/docker/libnetwork/pull/1525)

### Logging

* Update syslog log driver [#29150](https://github.com/docker/docker/pull/29150)

### Contrib

- Run "dnf upgrade" before installing in fedora [#29150](https://github.com/docker/docker/pull/29150)
- Add build-date back to RPM packages [#29150](https://github.com/docker/docker/pull/29150)
- deb package filename changed to include distribution to distinguish between distribution code names [#27829](https://github.com/docker/docker/pull/27829)

## 1.12.3 (2016-10-26)

> [!IMPORTANT]
>
> Docker 1.12 ships with an updated systemd unit file for rpm
based installs (which includes RHEL, Fedora, CentOS, and Oracle Linux 7). When upgrading from an older version of Docker, the upgrade process may not automatically install the updated version of the unit file, or fail to start the Docker service if;
> - the systemd unit file (`/usr/lib/systemd/system/docker.service`) contains local changes, or
> - a systemd drop-in file is present, and contains `-H fd://` in the `ExecStart` directive

Starting the `docker service` will produce an error:

    Failed to start docker.service: Unit docker.socket failed to load: No such file or directory.

or

    no sockets found via socket activation: make sure the service was started by systemd.

To resolve this:

- Backup the current version of the unit file, and replace the file with the
  [version that ships with docker 1.12](https://raw.githubusercontent.com/docker/docker/v1.12.0/contrib/init/systemd/docker.service.rpm)
- Remove the `Requires=docker.socket` directive from the `/usr/lib/systemd/system/docker.service` file if present
- Remove `-H fd://` from the `ExecStart` directive (both in the main unit file, and in any drop-in files present).

After making those changes, run `sudo systemctl daemon-reload`, and `sudo
systemctl restart docker` to reload changes and (re)start the docker daemon.


### Runtime

- Fix ambient capability usage in containers (CVE-2016-8867) [#27610](https://github.com/docker/docker/pull/27610)
- Prevent a deadlock in libcontainerd for Windows [#27136](https://github.com/docker/docker/pull/27136)
- Fix error reporting in CopyFileWithTar [#27075](https://github.com/docker/docker/pull/27075)
* Reset health status to starting when a container is restarted [#27387](https://github.com/docker/docker/pull/27387)
* Properly handle shared mount propagation in storage directory [#27609](https://github.com/docker/docker/pull/27609)
- Fix docker exec [#27610](https://github.com/docker/docker/pull/27610)
- Fix backward compatibility with containerd’s events log [#27693](https://github.com/docker/docker/pull/27693)

### Swarm Mode

- Fix conversion of restart-policy [#27062](https://github.com/docker/docker/pull/27062)
* Update Swarmkit [#27554](https://github.com/docker/docker/pull/27554)
 * Avoid restarting a task that has already been restarted [docker/swarmkit#1305](https://github.com/docker/swarmkit/pull/1305)
 * Allow duplicate published ports when they use different protocols [docker/swarmkit#1632](https://github.com/docker/swarmkit/pull/1632)
 * Allow multiple randomly assigned published ports on service [docker/swarmkit#1657](https://github.com/docker/swarmkit/pull/1657)
 - Fix panic when allocations happen at init time [docker/swarmkit#1651](https://github.com/docker/swarmkit/pull/1651)

### Networking

* Update libnetwork [#27559](https://github.com/docker/docker/pull/27559)
 - Fix race in serializing sandbox to string [docker/libnetwork#1495](https://github.com/docker/libnetwork/pull/1495)
 - Fix race during deletion [docker/libnetwork#1503](https://github.com/docker/libnetwork/pull/1503)
 * Reset endpoint port info on connectivity revoke in bridge driver [docker/libnetwork#1504](https://github.com/docker/libnetwork/pull/1504)
 - Fix a deadlock in networking code [docker/libnetwork#1507](https://github.com/docker/libnetwork/pull/1507)
 - Fix a race in load balancer state [docker/libnetwork#1512](https://github.com/docker/libnetwork/pull/1512)

### Logging

* Update fluent-logger-golang to v1.2.1 [#27474](https://github.com/docker/docker/pull/27474)

### Contrib

* Update buildtags for armhf ubuntu-trusty [#27327](https://github.com/docker/docker/pull/27327)
* Add AppArmor to runc buildtags for armhf [#27421](https://github.com/docker/docker/pull/27421)

## 1.12.2 (2016-10-11)

> [!IMPORTANT]
>
> Docker 1.12 ships with an updated systemd unit file for rpm
based installs (which includes RHEL, Fedora, CentOS, and Oracle Linux 7). When upgrading from an older version of Docker, the upgrade process may not automatically install the updated version of the unit file, or fail to start the `docker service` if;
> - the systemd unit file (`/usr/lib/systemd/system/docker.service`) contains local changes, or
> - a systemd drop-in file is present, and contains `-H fd://` in the `ExecStart` directive

Starting the `docker service` will produce an error:

    Failed to start docker.service: Unit docker.socket failed to load: No such file or directory.

or

    no sockets found via socket activation: make sure the service was started by systemd.

To resolve this:

- Backup the current version of the unit file, and replace the file with the
  [version that ships with docker 1.12](https://raw.githubusercontent.com/docker/docker/v1.12.0/contrib/init/systemd/docker.service.rpm)
- Remove the `Requires=docker.socket` directive from the `/usr/lib/systemd/system/docker.service` file if present
- Remove `-H fd://` from the `ExecStart` directive (both in the main unit file, and in any drop-in files present).

After making those changes, run `sudo systemctl daemon-reload`, and `sudo
systemctl restart docker` to reload changes and (re)start the docker daemon.


### Runtime

- Fix a panic due to a race condition filtering `docker ps` [#26049](https://github.com/docker/docker/pull/26049)
* Implement retry logic to prevent "Unable to remove filesystem" errors when using the aufs storage driver [#26536](https://github.com/docker/docker/pull/26536)
* Prevent devicemapper from removing device symlinks if `dm.use_deferred_removal` is enabled [#24740](https://github.com/docker/docker/pull/24740)
- Fix an issue where the CLI did not return correct exit codes if a command was run with invalid options [#26777](https://github.com/docker/docker/pull/26777)
- Fix a panic due to a bug in stdout / stderr processing in health checks [#26507](https://github.com/docker/docker/pull/26507)
- Fix exec's children handling [#26874](https://github.com/docker/docker/pull/26874)
- Fix exec form of HEALTHCHECK CMD [#26208](https://github.com/docker/docker/pull/26208)

### Networking

- Fix a daemon start panic on armv5 [#24315](https://github.com/docker/docker/issues/24315)
* Vendor libnetwork [#26879](https://github.com/docker/docker/pull/26879) [#26953](https://github.com/docker/docker/pull/26953)
 * Avoid returning early on agent join failures [docker/libnetwork#1473](https://github.com/docker/libnetwork/pull/1473)
 - Fix service published port cleanup issues [docker/libetwork#1432](https://github.com/docker/libnetwork/pull/1432) [docker/libnetwork#1433](https://github.com/docker/libnetwork/pull/1433)
 * Recover properly from transient gossip failures [docker/libnetwork#1446](https://github.com/docker/libnetwork/pull/1446)
 * Disambiguate node names known to gossip cluster to avoid node name collision [docker/libnetwork#1451](https://github.com/docker/libnetwork/pull/1451)
 * Honor user provided listen address for gossip  [docker/libnetwork#1460](https://github.com/docker/libnetwork/pull/1460)
 * Allow reachability via published port across services on the same host [docker/libnetwork#1398](https://github.com/docker/libnetwork/pull/1398)
 * Change the ingress sandbox name from random id to just `ingress_sbox` [docker/libnetwork#1449](https://github.com/docker/libnetwork/pull/1449)
 - Disable service discovery in ingress network [docker/libnetwork#1489](https://github.com/docker/libnetwork/pull/1489)

### Swarm Mode

* Fix remote detection of a node's address when it joins the cluster [#26211](https://github.com/docker/docker/pull/26211)
* Vendor SwarmKit [#26765](https://github.com/docker/docker/pull/26765)
 * Bounce session after failed status update [docker/swarmkit#1539](https://github.com/docker/swarmkit/pull/1539)
 - Fix possible raft deadlocks [docker/swarmkit#1537](https://github.com/docker/swarmkit/pull/1537)
 - Fix panic and endpoint leak when a service is updated with no endpoints [docker/swarmkit#1481](https://github.com/docker/swarmkit/pull/1481)
 * Produce an error if the same port is published twice on `service create` or `service update` [docker/swarmkit#1495](https://github.com/docker/swarmkit/pull/1495)
 - Fix an issue where changes to a service were not detected, resulting in the service not being updated [docker/swarmkit#1497](https://github.com/docker/swarmkit/pull/1497)
 - Do not allow service creation on ingress network [docker/swarmkit#1600](https://github.com/docker/swarmkit/pull/1600)

### Contrib

* Update the debian sysv-init script to use `dockerd` instead of `docker daemon` [#25869](https://github.com/docker/docker/pull/25869)
* Improve stability when running the docker client on MacOS Sierra [#26875](https://github.com/docker/docker/pull/26875)
- Fix installation on debian stretch [#27184](https://github.com/docker/docker/pull/27184)

### Windows

- Fix an issue where arrow-navigation did not work when running the docker client in ConEmu [#25578](https://github.com/docker/docker/pull/25578)

## 1.12.1 (2016-08-18)

> [!IMPORTANT]
>
> Docker 1.12 ships with an updated systemd unit file for rpm
based installs (which includes RHEL, Fedora, CentOS, and Oracle Linux 7). When upgrading from an older version of Docker, the upgrade process may not automatically install the updated version of the unit file, or fail to start the `docker service` if;
> - the systemd unit file (`/usr/lib/systemd/system/docker.service`) contains local changes, or
> - a systemd drop-in file is present, and contains `-H fd://` in the `ExecStart` directive

Starting the `docker service` will produce an error:

    Failed to start docker.service: Unit docker.socket failed to load: No such file or directory.

or

    no sockets found via socket activation: make sure the service was started by systemd.

To resolve this:

- Backup the current version of the unit file, and replace the file with the
  [version that ships with docker 1.12](https://raw.githubusercontent.com/docker/docker/v1.12.0/contrib/init/systemd/docker.service.rpm)
- Remove the `Requires=docker.socket` directive from the `/usr/lib/systemd/system/docker.service` file if present
- Remove `-H fd://` from the `ExecStart` directive (both in the main unit file, and in any drop-in files present).

After making those changes, run `sudo systemctl daemon-reload`, and `sudo
systemctl restart docker` to reload changes and (re)start the docker daemon.


### Client

* Add `Joined at` information in `node inspect --pretty` [#25512](https://github.com/docker/docker/pull/25512)
- Fix a crash on `service inspect` [#25454](https://github.com/docker/docker/pull/25454)
- Fix issue preventing `service update --env-add` to work as intended [#25427](https://github.com/docker/docker/pull/25427)
- Fix issue preventing `service update --publish-add` to work as intended [#25428](https://github.com/docker/docker/pull/25428)
- Remove `service update --network-add` and `service update --network-rm` flags
  because this feature is not yet implemented in 1.12, but was inadvertently added
  to the client in 1.12.0 [#25646](https://github.com/docker/docker/pull/25646)

### Contrib

+ Official ARM installation for Debian Jessie, Ubuntu Trusty, and Raspbian Jessie [#24815](https://github.com/docker/docker/pull/24815) [#25591](https://github.com/docker/docker/pull/25637)
- Add selinux policy per distribution/version, fixing issue preventing successful installation on Fedora 24, and Oracle Linux [#25334](https://github.com/docker/docker/pull/25334) [#25593](https://github.com/docker/docker/pull/25593)

### Networking

- Fix issue that prevented containers to be accessed by hostname with Docker overlay driver in Swarm Mode [#25603](https://github.com/docker/docker/pull/25603) [#25648](https://github.com/docker/docker/pull/25648)
- Fix random network issues on service with published port [#25603](https://github.com/docker/docker/pull/25603)
- Fix unreliable inter-service communication after scaling down and up [#25603](https://github.com/docker/docker/pull/25603)
- Fix issue where removing all tasks on a node and adding them back breaks connectivity with other services [#25603](https://github.com/docker/docker/pull/25603)
- Fix issue where a task that fails to start results in a race, causing a `network xxx not found` error that masks the actual error [#25550](https://github.com/docker/docker/pull/25550)
- Relax validation of SRV records for external services that use SRV records not formatted according to RFC 2782 [#25739](https://github.com/docker/docker/pull/25739)

### Plugins (experimental)

* Make daemon events listen for plugin lifecycle events [#24760](https://github.com/docker/docker/pull/24760)
* Check for plugin state before enabling plugin [#25033](https://github.com/docker/docker/pull/25033)
- Remove plugin root from filesystem on `plugin rm` [#25187](https://github.com/docker/docker/pull/25187)
- Prevent deadlock when more than one plugin is installed [#25384](https://github.com/docker/docker/pull/25384)

### Runtime

* Mask join tokens in daemon logs [#25346](https://github.com/docker/docker/pull/25346)
- Fix `docker ps --filter` causing the results to no longer be sorted by creation time [#25387](https://github.com/docker/docker/pull/25387)
- Fix various crashes [#25053](https://github.com/docker/docker/pull/25053)

### Security

* Add `/proc/timer_list` to the masked paths list to prevent information leak from the host [#25630](https://github.com/docker/docker/pull/25630)
* Allow systemd to run with only `--cap-add SYS_ADMIN` rather than having to also add `--cap-add DAC_READ_SEARCH` or disabling seccomp filtering [#25567](https://github.com/docker/docker/pull/25567)

### Swarm

- Fix an issue where the swarm can get stuck electing a new leader after quorum is lost [#25055](https://github.com/docker/docker/issues/25055)
- Fix unwanted rescheduling of containers after a leader failover [#25017](https://github.com/docker/docker/issues/25017)
- Change swarm root CA key to P256 curve [swarmkit#1376](https://github.com/docker/swarmkit/pull/1376)
- Allow forced removal of a node from a swarm [#25159](https://github.com/docker/docker/pull/25159)
- Fix connection leak when a node leaves a swarm [swarmkit/#1277](https://github.com/docker/swarmkit/pull/1277)
- Backdate swarm certificates by one hour to tolerate more clock skew [swarmkit/#1243](https://github.com/docker/swarmkit/pull/1243)
- Avoid high CPU use with many unschedulable tasks [swarmkit/#1287](https://github.com/docker/swarmkit/pull/1287)
- Fix issue with global tasks not starting up [swarmkit/#1295](https://github.com/docker/swarmkit/pull/1295)
- Garbage collect raft logs [swarmkit/#1327](https://github.com/docker/swarmkit/pull/1327)

### Volume

- Persist local volume options after a daemon restart [#25316](https://github.com/docker/docker/pull/25316)
- Fix an issue where the mount ID was not returned on volume unmount [#25333](https://github.com/docker/docker/pull/25333)
- Fix an issue where a volume mount could inadvertently create a bind mount [#25309](https://github.com/docker/docker/pull/25309)
- `docker service create --mount type=bind,...` now correctly validates if the source path exists, instead of creating it [#25494](https://github.com/docker/docker/pull/25494)

## 1.12.0 (2016-07-28)


> [!IMPORTANT]
>
> Docker 1.12.0 ships with an updated systemd unit file for rpm
based installs (which includes RHEL, Fedora, CentOS, and Oracle Linux 7). When upgrading from an older version of Docker, the upgrade process may not automatically install the updated version of the unit file, or fail to start the `docker service` if;
> - the systemd unit file (`/usr/lib/systemd/system/docker.service`) contains local changes, or
> - a systemd drop-in file is present, and contains `-H fd://` in the `ExecStart` directive

Starting the `docker service` will produce an error:

    Failed to start docker.service: Unit docker.socket failed to load: No such file or directory.

or

    no sockets found via socket activation: make sure the service was started by systemd.

To resolve this:

- Backup the current version of the unit file, and replace the file with the
  [version that ships with docker 1.12](https://raw.githubusercontent.com/docker/docker/v1.12.0/contrib/init/systemd/docker.service.rpm)
- Remove the `Requires=docker.socket` directive from the `/usr/lib/systemd/system/docker.service` file if present
- Remove `-H fd://` from the `ExecStart` directive (both in the main unit file, and in any drop-in files present).

After making those changes, run `sudo systemctl daemon-reload`, and `sudo
systemctl restart docker` to reload changes and (re)start the docker daemon.

> [!IMPORTANT]
>
> With Docker 1.12, a Linux `docker` installation now has two
additional binaries; `dockerd`, and `docker-proxy`. If you have scripts for installing `docker`, make sure to update them accordingly.

### Builder

+ New `HEALTHCHECK` Dockerfile instruction to support user-defined healthchecks [#23218](https://github.com/docker/docker/pull/23218)
+ New `SHELL` Dockerfile instruction to specify the default shell when using the shell form for commands in a Dockerfile [#22489](https://github.com/docker/docker/pull/22489)
+ Add `#escape=` Dockerfile directive to support platform-specific parsing of file paths in Dockerfile [#22268](https://github.com/docker/docker/pull/22268)
+ Add support for comments in `.dockerignore` [#23111](https://github.com/docker/docker/pull/23111)
* Support for UTF-8 in Dockerfiles [#23372](https://github.com/docker/docker/pull/23372)
* Skip UTF-8 BOM bytes from `Dockerfile` and `.dockerignore` if exist [#23234](https://github.com/docker/docker/pull/23234)
* Windows: support for `ARG` to match Linux [#22508](https://github.com/docker/docker/pull/22508)
- Fix error message when building using a daemon with the bridge network disabled [#22932](https://github.com/docker/docker/pull/22932)

### Contrib

* Enable seccomp for Centos 7 and Oracle Linux 7 [#22344](https://github.com/docker/docker/pull/22344)
- Remove MountFlags in systemd unit to allow shared mount propagation [#22806](https://github.com/docker/docker/pull/22806)

### Distribution

+ Add `--max-concurrent-downloads` and `--max-concurrent-uploads` daemon flags useful for situations where network connections don't support multiple downloads/uploads [#22445](https://github.com/docker/docker/pull/22445)
* Registry operations now honor the `ALL_PROXY` environment variable [#22316](https://github.com/docker/docker/pull/22316)
* Provide more information to the user on `docker load` [#23377](https://github.com/docker/docker/pull/23377)
* Always save registry digest metadata about images pushed and pulled [#23996](https://github.com/docker/docker/pull/23996)

### Logging

+ Syslog logging driver now supports DGRAM sockets [#21613](https://github.com/docker/docker/pull/21613)
+ Add `--details` option to `docker logs` to also display log tags [#21889](https://github.com/docker/docker/pull/21889)
+ Enable syslog logger to have access to env and labels [#21724](https://github.com/docker/docker/pull/21724)
+ An additional syslog-format option `rfc5424micro` to allow microsecond resolution in syslog timestamp [#21844](https://github.com/docker/docker/pull/21844)
* Inherit the daemon log options when creating containers [#21153](https://github.com/docker/docker/pull/21153)
* Remove `docker/` prefix from log messages tag and replace it with `{{.DaemonName}}` so that users have the option of changing the prefix [#22384](https://github.com/docker/docker/pull/22384)

### Networking

+ Built-in Virtual-IP based  internal and ingress load-balancing using IPVS [#23361](https://github.com/docker/docker/pull/23361)
+ Routing Mesh using ingress overlay network [#23361](https://github.com/docker/docker/pull/23361)
+ Secured multi-host overlay networking using encrypted control-plane and Data-plane [#23361](https://github.com/docker/docker/pull/23361)
+ MacVlan driver is out of experimental [#23524](https://github.com/docker/docker/pull/23524)
+ Add `driver` filter to `network ls` [#22319](https://github.com/docker/docker/pull/22319)
+ Adding `network` filter to `docker ps --filter` [#23300](https://github.com/docker/docker/pull/23300)
+ Add `--link-local-ip` flag to `create`, `run` and `network connect` to specify a container's link-local address [#23415](https://github.com/docker/docker/pull/23415)
+ Add network label filter support [#21495](https://github.com/docker/docker/pull/21495)
* Removed dependency on external KV-Store for Overlay networking in Swarm-Mode  [#23361](https://github.com/docker/docker/pull/23361)
* Add container's short-id as default network alias [#21901](https://github.com/docker/docker/pull/21901)
* `run` options `--dns` and `--net=host` are no longer mutually exclusive [#22408](https://github.com/docker/docker/pull/22408)
- Fix DNS issue when renaming containers with generated names [#22716](https://github.com/docker/docker/pull/22716)
- Allow both `network inspect -f {{.Id}}` and `network inspect -f {{.ID}}` to address inconsistency with inspect output [#23226](https://github.com/docker/docker/pull/23226)

### Plugins (experimental)

+ New `plugin` command to manager plugins with `install`, `enable`, `disable`, `rm`, `inspect`, `set` subcommands [#23446](https://github.com/docker/docker/pull/23446)

### Remote API (v1.24) & Client

+ Split the binary into two: `docker` (client) and `dockerd` (daemon) [#20639](https://github.com/docker/docker/pull/20639)
+ Add `before` and `since` filters to `docker images --filter` [#22908](https://github.com/docker/docker/pull/22908)
+ Add `--limit` option to `docker search` [#23107](https://github.com/docker/docker/pull/23107)
+ Add `--filter` option to `docker search` [#22369](https://github.com/docker/docker/pull/22369)
+ Add security options to `docker info` output [#21172](https://github.com/docker/docker/pull/21172) [#23520](https://github.com/docker/docker/pull/23520)
+ Add insecure registries to `docker info` output [#20410](https://github.com/docker/docker/pull/20410)
+ Extend Docker authorization with TLS user information [#21556](https://github.com/docker/docker/pull/21556)
+ devicemapper: expose Minimum Thin Pool Free Space through `docker info` [#21945](https://github.com/docker/docker/pull/21945)
* API now returns a JSON object when an error occurs making it more consistent [#22880](https://github.com/docker/docker/pull/22880)
- Prevent `docker run -i --restart` from hanging on exit [#22777](https://github.com/docker/docker/pull/22777)
- Fix API/CLI discrepancy on hostname validation [#21641](https://github.com/docker/docker/pull/21641)
- Fix discrepancy in the format of sizes in `stats` from HumanSize to BytesSize [#21773](https://github.com/docker/docker/pull/21773)
- authz: when request is denied return forbidden exit code (403) [#22448](https://github.com/docker/docker/pull/22448)
- Windows: fix tty-related displaying issues [#23878](https://github.com/docker/docker/pull/23878)

### Runtime

+ Split the userland proxy to a separate binary (`docker-proxy`) [#23312](https://github.com/docker/docker/pull/23312)
+ Add `--live-restore` daemon flag to keep containers running when daemon shuts down, and regain control on startup [#23213](https://github.com/docker/docker/pull/23213)
+ Ability to add OCI-compatible runtimes (via `--add-runtime` daemon flag) and select one with `--runtime` on `create` and `run` [#22983](https://github.com/docker/docker/pull/22983)
+ New `overlay2` graphdriver for Linux 4.0+ with multiple lower directory support [#22126](https://github.com/docker/docker/pull/22126)
+ New load/save image events [#22137](https://github.com/docker/docker/pull/22137)
+ Add support for reloading daemon configuration through systemd [#22446](https://github.com/docker/docker/pull/22446)
+ Add disk quota support for btrfs [#19651](https://github.com/docker/docker/pull/19651)
+ Add disk quota support for zfs [#21946](https://github.com/docker/docker/pull/21946)
+ Add support for `docker run --pid=container:<id>` [#22481](https://github.com/docker/docker/pull/22481)
+ Align default seccomp profile with selected capabilities [#22554](https://github.com/docker/docker/pull/22554)
+ Add a `daemon reload` event when the daemon reloads its configuration [#22590](https://github.com/docker/docker/pull/22590)
+ Add `trace` capability in the pprof profiler to show execution traces in binary form [#22715](https://github.com/docker/docker/pull/22715)
+ Add a `detach` event [#22898](https://github.com/docker/docker/pull/22898)
+ Add support for setting sysctls with `--sysctl` [#19265](https://github.com/docker/docker/pull/19265)
+ Add `--storage-opt` flag to `create` and `run` allowing to set `size` on devicemapper [#19367](https://github.com/docker/docker/pull/19367)
+ Add `--oom-score-adjust` daemon flag with a default value of `-500` making the daemon less likely to be killed before containers [#24516](https://github.com/docker/docker/pull/24516)
* Undeprecate the `-c` short alias of `--cpu-shares` on `run`, `build`, `create`, `update` [#22621](https://github.com/docker/docker/pull/22621)
* Prevent from using aufs and overlay graphdrivers on an eCryptfs mount [#23121](https://github.com/docker/docker/pull/23121)
- Fix issues with tmpfs mount ordering [#22329](https://github.com/docker/docker/pull/22329)
- Created containers are no longer listed on `docker ps -a -f exited=0` [#21947](https://github.com/docker/docker/pull/21947)
- Fix an issue where containers are stuck in a "Removal In Progress" state [#22423](https://github.com/docker/docker/pull/22423)
- Fix bug that was returning an HTTP 500 instead of a 400 when not specifying a command on run/create [#22762](https://github.com/docker/docker/pull/22762)
- Fix bug with `--detach-keys` whereby input matching a prefix of the detach key was not preserved [#22943](https://github.com/docker/docker/pull/22943)
- SELinux labeling is now disabled when using `--privileged` mode [#22993](https://github.com/docker/docker/pull/22993)
- If volume-mounted into a container, `/etc/hosts`, `/etc/resolv.conf`, `/etc/hostname` are no longer SELinux-relabeled [#22993](https://github.com/docker/docker/pull/22993)
- Fix inconsistency in `--tmpfs` behavior regarding mount options [#22438](https://github.com/docker/docker/pull/22438)
- Fix an issue where daemon hangs at startup [#23148](https://github.com/docker/docker/pull/23148)
- Ignore SIGPIPE events to prevent journald restarts to crash docker in some cases [#22460](https://github.com/docker/docker/pull/22460)
- Containers are not removed from stats list on error [#20835](https://github.com/docker/docker/pull/20835)
- Fix `on-failure` restart policy when daemon restarts [#20853](https://github.com/docker/docker/pull/20853)
- Fix an issue with `stats` when a container is using another container's network [#21904](https://github.com/docker/docker/pull/21904)

### Swarm Mode

+ New `swarm` command to manage swarms with `init`, `join`, `join-token`, `leave`, `update` subcommands [#23361](https://github.com/docker/docker/pull/23361) [#24823](https://github.com/docker/docker/pull/24823)
+ New `service` command to manage swarm-wide services with `create`, `inspect`, `update`, `rm`, `ps` subcommands [#23361](https://github.com/docker/docker/pull/23361) [#25140](https://github.com/docker/docker/pull/25140)
+ New `node` command to manage nodes with `accept`, `promote`, `demote`, `inspect`, `update`, `ps`, `ls` and `rm` subcommands [#23361](https://github.com/docker/docker/pull/23361) [#25140](https://github.com/docker/docker/pull/25140)
+ (experimental) New `stack` and `deploy` commands to manage and deploy multi-service applications [#23522](https://github.com/docker/docker/pull/23522) [#25140](https://github.com/docker/docker/pull/25140)

### Volume

+ Add support for local and global volume scopes (analogous to network scopes) [#22077](https://github.com/docker/docker/pull/22077)
+ Allow volume drivers to provide a `Status` field [#21006](https://github.com/docker/docker/pull/21006)
+ Add name/driver filter support for volume [#21361](https://github.com/docker/docker/pull/21361)
* Mount/Unmount operations now receives an opaque ID to allow volume drivers to differentiate between two callers [#21015](https://github.com/docker/docker/pull/21015)
- Fix issue preventing to remove a volume in a corner case [#22103](https://github.com/docker/docker/pull/22103)
- Windows: Enable auto-creation of host-path to match Linux [#22094](https://github.com/docker/docker/pull/22094)


### Deprecation

* Environment variables `DOCKER_CONTENT_TRUST_OFFLINE_PASSPHRASE` and `DOCKER_CONTENT_TRUST_TAGGING_PASSPHRASE` have been renamed
  to `DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE` and `DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE` respectively [#22574](https://github.com/docker/docker/pull/22574)
* Remove deprecated `syslog-tag`, `gelf-tag`, `fluentd-tag` log option in favor of the more generic `tag` one [#22620](https://github.com/docker/docker/pull/22620)
* Remove deprecated feature of passing HostConfig at API container start [#22570](https://github.com/docker/docker/pull/22570)
* Remove deprecated `-f`/`--force` flag on docker tag [#23090](https://github.com/docker/docker/pull/23090)
* Remove deprecated `/containers/<id|name>/copy` endpoint [#22149](https://github.com/docker/docker/pull/22149)
* Remove deprecated `docker ps` flags `--since` and `--before` [#22138](https://github.com/docker/docker/pull/22138)
* Deprecate the old 3-args form of `docker import` [#23273](https://github.com/docker/docker/pull/23273)

