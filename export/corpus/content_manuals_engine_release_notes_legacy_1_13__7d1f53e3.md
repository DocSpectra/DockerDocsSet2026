---
title: Docker Engine 1.13 release notes
linkTitle: Engine 1.13
toc_max: 2
---

## Related guidance

- [Engine installation instructions](/manuals/engine/install/_index.md)
- [Deprecated and removed Engine features](/manuals/engine/deprecated.md)
- [Engine API version history](/reference/api/engine/version-history/)

## Find a release

- [1.13.1 (2017-02-08)](#1131-2017-02-08)
- [1.13.0 (2017-01-18)](#1130-2017-01-18)

## Find changes

- Security notes: [1.13.0 (2017-01-18)](#1130-2017-01-18)

## 1.13.1 (2017-02-08)

> [!IMPORTANT]
>
> Before upgrading to Docker 1.13, read the [storage-driver and plugin upgrade requirements](upgrade.md#docker-113-storage-drivers-and-plugins), including recovery steps if the daemon no longer starts.

### Contrib

* Do not require a custom build of tini [#28454](https://github.com/docker/docker/pull/28454)
* Upgrade to Go 1.7.5 [#30489](https://github.com/docker/docker/pull/30489)

### Remote API (v1.26) & Client

+ Support secrets in docker stack deploy with compose file [#30144](https://github.com/docker/docker/pull/30144)

### Runtime

* Fix size issue in `docker system df` [#30378](https://github.com/docker/docker/pull/30378)
* Fix error on `docker inspect` when Swarm certificates were expired. [#29246](https://github.com/docker/docker/pull/29246)
* Fix deadlock on v1 plugin with activate error [#30408](https://github.com/docker/docker/pull/30408)
* Fix SELinux regression [#30649](https://github.com/docker/docker/pull/30649)

### Plugins

* Support global scoped network plugins (v2) in swarm mode [#30332](https://github.com/docker/docker/pull/30332)
+ Add `docker plugin upgrade` [#29414](https://github.com/docker/docker/pull/29414)

### Windows

* Fix small regression with old plugins in Windows [#30150](https://github.com/docker/docker/pull/30150)
* Fix warning on Windows [#30730](https://github.com/docker/docker/pull/30730)

## 1.13.0 (2017-01-18)

> [!IMPORTANT]
>
> Before upgrading to Docker 1.13, read the [storage-driver and plugin upgrade requirements](upgrade.md#docker-113-storage-drivers-and-plugins), including recovery steps if the daemon no longer starts.

### Builder

+ Add capability to specify images used as a cache source on build. These images do not need to have local parent chain and can be pulled from other registries [#26839](https://github.com/docker/docker/pull/26839)
+ (experimental) Add option to squash image layers to the FROM image after successful builds [#22641](https://github.com/docker/docker/pull/22641)
* Fix dockerfile parser with empty line after escape [#24725](https://github.com/docker/docker/pull/24725)
- Add step number on `docker build` [#24978](https://github.com/docker/docker/pull/24978)
+ Add support for compressing build context during image build [#25837](https://github.com/docker/docker/pull/25837)
+ add `--network` to `docker build` [#27702](https://github.com/docker/docker/pull/27702)
- Fix inconsistent behavior between `--label` flag on `docker build` and `docker run` [#26027](https://github.com/docker/docker/issues/26027)
- Fix image layer inconsistencies when using the overlay storage driver [#27209](https://github.com/docker/docker/pull/27209)
* Unused build-args are now allowed. A warning is presented instead of an error and failed build [#27412](https://github.com/docker/docker/pull/27412)
- Fix builder cache issue on Windows [#27805](https://github.com/docker/docker/pull/27805)
+ Allow `USER` in builder on Windows [#28415](https://github.com/docker/docker/pull/28415)
+ Handle env case-insensitive on Windows [#28725](https://github.com/docker/docker/pull/28725)

### Contrib

+ Add support for building docker debs for Ubuntu 16.04 Xenial on PPC64LE [#23438](https://github.com/docker/docker/pull/23438)
+ Add support for building docker debs for Ubuntu 16.04 Xenial on s390x [#26104](https://github.com/docker/docker/pull/26104)
+ Add support for building docker debs for Ubuntu 16.10 Yakkety Yak on PPC64LE [#28046](https://github.com/docker/docker/pull/28046)
- Add RPM builder for VMWare Photon OS [#24116](https://github.com/docker/docker/pull/24116)
+ Add shell completions to tgz [#27735](https://github.com/docker/docker/pull/27735)
* Update the install script to allow using the mirror in China [#27005](https://github.com/docker/docker/pull/27005)
+ Add DEB builder for Ubuntu 16.10 Yakkety Yak [#27993](https://github.com/docker/docker/pull/27993)
+ Add RPM builder for Fedora 25 [#28222](https://github.com/docker/docker/pull/28222)
+ Add `make deb` support for aarch64 [#27625](https://github.com/docker/docker/pull/27625)

### Distribution

* Update notary dependency to 0.4.2 (full changelogs [here](https://github.com/docker/notary/releases/tag/v0.4.2)) [#27074](https://github.com/docker/docker/pull/27074)
  - Support for compilation on windows [docker/notary#970](https://github.com/docker/notary/pull/970)
  - Improved error messages for client authentication errors [docker/notary#972](https://github.com/docker/notary/pull/972)
  - Support for finding keys that are anywhere in the `~/.docker/trust/private` directory, not just under `~/.docker/trust/private/root_keys` or `~/.docker/trust/private/tuf_keys` [docker/notary#981](https://github.com/docker/notary/pull/981)
  - Previously, on any error updating, the client would fall back on the cache.  Now we only do so if there is a network error or if the server is unavailable or missing the TUF data. Invalid TUF data will cause the update to fail - for example if there was an invalid root rotation. [docker/notary#982](https://github.com/docker/notary/pull/982)
  - Improve root validation and yubikey debug logging [docker/notary#858](https://github.com/docker/notary/pull/858) [docker/notary#891](https://github.com/docker/notary/pull/891)
  - Warn if certificates for root or delegations are near expiry [docker/notary#802](https://github.com/docker/notary/pull/802)
  - Warn if role metadata is near expiry [docker/notary#786](https://github.com/docker/notary/pull/786)
  - Fix passphrase retrieval attempt counting and terminal detection [docker/notary#906](https://github.com/docker/notary/pull/906)
- Avoid unnecessary blob uploads when different users push same layers to authenticated registry [#26564](https://github.com/docker/docker/pull/26564)
* Allow external storage for registry credentials [#26354](https://github.com/docker/docker/pull/26354)

### Logging

* Standardize the default logging tag value in all logging drivers [#22911](https://github.com/docker/docker/pull/22911)
- Improve performance and memory use when logging of long log lines [#22982](https://github.com/docker/docker/pull/22982)
+ Enable syslog driver for windows [#25736](https://github.com/docker/docker/pull/25736)
+ Add Logentries Driver [#27471](https://github.com/docker/docker/pull/27471)
+ Update of AWS log driver to support tags [#27707](https://github.com/docker/docker/pull/27707)
+ Unix socket support for fluentd [#26088](https://github.com/docker/docker/pull/26088)
* Enable fluentd logging driver on Windows [#28189](https://github.com/docker/docker/pull/28189)
- Sanitize docker labels when used as journald field names [#23725](https://github.com/docker/docker/pull/23725)
- Fix an issue where `docker logs --tail` returned less lines than expected [#28203](https://github.com/docker/docker/pull/28203)
- Splunk Logging Driver: performance and reliability improvements [#26207](https://github.com/docker/docker/pull/26207)
- Splunk Logging Driver: configurable formats and skip for verifying connection [#25786](https://github.com/docker/docker/pull/25786)

### Networking

+ Add `--attachable` network support to enable `docker run` to work in swarm-mode overlay network [#25962](https://github.com/docker/docker/pull/25962)
+ Add support for host port PublishMode in services using the `--publish` option in `docker service create` [#27917](https://github.com/docker/docker/pull/27917) and [#28943](https://github.com/docker/docker/pull/28943)
+ Add support for Windows server 2016 overlay network driver (requires upcoming ws2016 update) [#28182](https://github.com/docker/docker/pull/28182)
* Change the default `FORWARD` policy to `DROP` [#28257](https://github.com/docker/docker/pull/28257)
+ Add support for specifying static IP addresses for predefined network on windows [#22208](https://github.com/docker/docker/pull/22208)
- Fix `--publish` flag on `docker run` not working with IPv6 addresses [#27860](https://github.com/docker/docker/pull/27860)
- Fix inspect network show gateway with mask [#25564](https://github.com/docker/docker/pull/25564)
- Fix an issue where multiple addresses in a bridge may cause `--fixed-cidr` to not have the correct addresses [#26659](https://github.com/docker/docker/pull/26659)
+ Add creation timestamp to `docker network inspect` [#26130](https://github.com/docker/docker/pull/26130)
- Show peer nodes in `docker network inspect` for swarm overlay networks [#28078](https://github.com/docker/docker/pull/28078)
- Enable ping for service VIP address [#28019](https://github.com/docker/docker/pull/28019)

### Plugins

- Move plugins out of experimental [#28226](https://github.com/docker/docker/pull/28226)
- Add `--force` on `docker plugin remove` [#25096](https://github.com/docker/docker/pull/25096)
* Add support for dynamically reloading authorization plugins [#22770](https://github.com/docker/docker/pull/22770)
+ Add description in `docker plugin ls` [#25556](https://github.com/docker/docker/pull/25556)
+ Add `-f`/`--format` to `docker plugin inspect` [#25990](https://github.com/docker/docker/pull/25990)
+ Add `docker plugin create` command [#28164](https://github.com/docker/docker/pull/28164)
* Send request's TLS peer certificates to authorization plugins [#27383](https://github.com/docker/docker/pull/27383)
* Support for global-scoped network and ipam plugins in swarm-mode [#27287](https://github.com/docker/docker/pull/27287)
* Split `docker plugin install` into two API call `/privileges` and `/pull` [#28963](https://github.com/docker/docker/pull/28963)

### Remote API (v1.25) & Client

+ Support `docker stack deploy` from a Compose file [#27998](https://github.com/docker/docker/pull/27998)
+ (experimental) Implement checkpoint and restore [#22049](https://github.com/docker/docker/pull/22049)
+ Add `--format` flag to `docker info` [#23808](https://github.com/docker/docker/pull/23808)
* Remove `--name` from `docker volume create` [#23830](https://github.com/docker/docker/pull/23830)
+ Add `docker stack ls` [#23886](https://github.com/docker/docker/pull/23886)
+ Add a new `is-task` ps filter [#24411](https://github.com/docker/docker/pull/24411)
+ Add `--env-file` flag to `docker service create` [#24844](https://github.com/docker/docker/pull/24844)
+ Add `--format` on `docker stats` [#24987](https://github.com/docker/docker/pull/24987)
+ Make `docker node ps` default to `self` in swarm node [#25214](https://github.com/docker/docker/pull/25214)
+ Add `--group` in `docker service create` [#25317](https://github.com/docker/docker/pull/25317)
+ Add `--no-trunc` to service/node/stack ps output [#25337](https://github.com/docker/docker/pull/25337)
+ Add Logs to `ContainerAttachOptions` so go clients can request to retrieve container logs as part of the attach process [#26718](https://github.com/docker/docker/pull/26718)
+ Allow client to talk to an older server [#27745](https://github.com/docker/docker/pull/27745)
* Inform user client-side that a container removal is in progress [#26074](https://github.com/docker/docker/pull/26074)
+ Add `Isolation` to the /info endpoint [#26255](https://github.com/docker/docker/pull/26255)
+ Add `userns` to the /info endpoint [#27840](https://github.com/docker/docker/pull/27840)
- Do not allow more than one mode be requested at once in the services endpoint [#26643](https://github.com/docker/docker/pull/26643)
+ Add capability to /containers/create API to specify mounts in a more granular and safer way [#22373](https://github.com/docker/docker/pull/22373)
+ Add `--format` flag to `network ls` and `volume ls` [#23475](https://github.com/docker/docker/pull/23475)
* Allow the top-level `docker inspect` command to inspect any kind of resource [#23614](https://github.com/docker/docker/pull/23614)
+ Add --cpus flag to control cpu resources for `docker run` and `docker create`, and add `NanoCPUs` to `HostConfig` [#27958](https://github.com/docker/docker/pull/27958)
- Allow unsetting the `--entrypoint` in `docker run` or `docker create` [#23718](https://github.com/docker/docker/pull/23718)
* Restructure CLI commands by adding `docker image` and `docker container` commands for more consistency [#26025](https://github.com/docker/docker/pull/26025)
- Remove `COMMAND` column from `service ls` output [#28029](https://github.com/docker/docker/pull/28029)
+ Add `--format` to `docker events` [#26268](https://github.com/docker/docker/pull/26268)
* Allow specifying multiple nodes on `docker node ps` [#26299](https://github.com/docker/docker/pull/26299)
* Restrict fractional digits to 2 decimals in `docker images` output [#26303](https://github.com/docker/docker/pull/26303)
+ Add `--dns-option` to `docker run` [#28186](https://github.com/docker/docker/pull/28186)
+ Add Image ID to container commit event [#28128](https://github.com/docker/docker/pull/28128)
+ Add external binaries version to docker info [#27955](https://github.com/docker/docker/pull/27955)
+ Add information for `Manager Addresses` in the output of `docker info` [#28042](https://github.com/docker/docker/pull/28042)
+ Add a new reference filter for `docker images` [#27872](https://github.com/docker/docker/pull/27872)

### Runtime

+ Add `--experimental` daemon flag to enable experimental features, instead of shipping them in a separate build [#27223](https://github.com/docker/docker/pull/27223)
+ Add a `--shutdown-timeout` daemon flag to specify the default timeout (in seconds) to stop containers gracefully before daemon exit [#23036](https://github.com/docker/docker/pull/23036)
+ Add `--stop-timeout` to specify the timeout value (in seconds) for individual containers to stop [#22566](https://github.com/docker/docker/pull/22566)
+ Add a new daemon flag `--userland-proxy-path` to allow configuring the userland proxy instead of using the hardcoded `docker-proxy` from `$PATH` [#26882](https://github.com/docker/docker/pull/26882)
+ Add boolean flag `--init` on `dockerd` and on `docker run` to use [tini](https://github.com/krallin/tini) a zombie-reaping init process as PID 1 [#26061](https://github.com/docker/docker/pull/26061) [#28037](https://github.com/docker/docker/pull/28037)
+ Add a new daemon flag `--init-path` to allow configuring the path to the `docker-init` binary [#26941](https://github.com/docker/docker/pull/26941)
+ Add support for live reloading insecure registry in configuration [#22337](https://github.com/docker/docker/pull/22337)
+ Add support for storage-opt size on Windows daemons [#23391](https://github.com/docker/docker/pull/23391)
* Improve reliability of `docker run --rm` by moving it from the client to the daemon  [#20848](https://github.com/docker/docker/pull/20848)
+ Add support for `--cpu-rt-period` and `--cpu-rt-runtime` flags, allowing containers to run real-time threads when `CONFIG_RT_GROUP_SCHED` is enabled in the kernel [#23430](https://github.com/docker/docker/pull/23430)
* Allow parallel stop, pause, unpause [#24761](https://github.com/docker/docker/pull/24761) / [#26778](https://github.com/docker/docker/pull/26778)
* Implement XFS quota for overlay2 [#24771](https://github.com/docker/docker/pull/24771)
- Fix partial/full filter issue in `service tasks --filter` [#24850](https://github.com/docker/docker/pull/24850)
- Allow engine to run inside a user namespace [#25672](https://github.com/docker/docker/pull/25672)
- Fix a race condition between device deferred removal and resume device, when using the devicemapper graphdriver [#23497](https://github.com/docker/docker/pull/23497)
- Add `docker stats` support in Windows [#25737](https://github.com/docker/docker/pull/25737)
- Allow using `--pid=host` and `--net=host` when `--userns=host` [#25771](https://github.com/docker/docker/pull/25771)
+ (experimental) Add metrics (Prometheus) output for basic `container`, `image`, and `daemon` operations [#25820](https://github.com/docker/docker/pull/25820)
- Fix issue in `docker stats` with `NetworkDisabled=true` [#25905](https://github.com/docker/docker/pull/25905)
+ Add `docker top` support in Windows [#25891](https://github.com/docker/docker/pull/25891)
+ Record pid of exec'd process [#27470](https://github.com/docker/docker/pull/27470)
+ Add support for looking up user/groups via `getent` [#27599](https://github.com/docker/docker/pull/27599)
+ Add new `docker system` command with `df` and `prune` subcommands for system resource management, as well as `docker {container,image,volume,network} prune` subcommands [#26108](https://github.com/docker/docker/pull/26108) [#27525](https://github.com/docker/docker/pull/27525) / [#27525](https://github.com/docker/docker/pull/27525)
- Fix an issue where containers could not be stopped or killed by setting xfs max_retries to 0 upon ENOSPC with devicemapper [#26212](https://github.com/docker/docker/pull/26212)
- Fix `docker cp` failing to copy to a container's volume dir on CentOS with devicemapper [#28047](https://github.com/docker/docker/pull/28047)
* Promote overlay(2) graphdriver [#27932](https://github.com/docker/docker/pull/27932)
+ Add `--seccomp-profile` daemon flag to specify a path to a seccomp profile that overrides the default [#26276](https://github.com/docker/docker/pull/26276)
- Fix ulimits in `docker inspect` when `--default-ulimit` is set on daemon [#26405](https://github.com/docker/docker/pull/26405)
- Add workaround for overlay issues during build in older kernels [#28138](https://github.com/docker/docker/pull/28138)
+ Add `TERM` environment variable on `docker exec -t` [#26461](https://github.com/docker/docker/pull/26461)
* Honor a container’s `--stop-signal` setting upon `docker kill` [#26464](https://github.com/docker/docker/pull/26464)

### Swarm Mode

+ Add secret management [#27794](https://github.com/docker/docker/pull/27794)
+ Add support for templating service options (hostname, mounts, and environment variables) [#28025](https://github.com/docker/docker/pull/28025)
* Display the endpoint mode in the output of `docker service inspect --pretty` [#26906](https://github.com/docker/docker/pull/26906)
* Make `docker service ps` output more bearable by shortening service IDs in task names [#28088](https://github.com/docker/docker/pull/28088)
* Make `docker node ps` default to the current node [#25214](https://github.com/docker/docker/pull/25214)
+ Add `--dns`, -`-dns-opt`, and `--dns-search` to service create. [#27567](https://github.com/docker/docker/pull/27567)
+ Add `--force` to `docker service update` [#27596](https://github.com/docker/docker/pull/27596)
+ Add `--health-*` and `--no-healthcheck` flags to `docker service create` and `docker service update` [#27369](https://github.com/docker/docker/pull/27369)
+ Add `-q` to `docker service ps` [#27654](https://github.com/docker/docker/pull/27654)
* Display number of global services in `docker service ls` [#27710](https://github.com/docker/docker/pull/27710)
- Remove `--name` flag from `docker service update`. This flag is only functional on `docker service create`, so was removed from the `update` command [#26988](https://github.com/docker/docker/pull/26988)
- Fix worker nodes failing to recover because of transient networking issues [#26646](https://github.com/docker/docker/issues/26646)
* Add support for health aware load balancing and DNS records [#27279](https://github.com/docker/docker/pull/27279)
+ Add `--hostname` to `docker service create` [#27857](https://github.com/docker/docker/pull/27857)
+ Add `--host` to `docker service create`, and `--host-add`, `--host-rm` to `docker service update` [#28031](https://github.com/docker/docker/pull/28031)
+ Add `--tty` flag to `docker service create`/`update` [#28076](https://github.com/docker/docker/pull/28076)
* Autodetect, store, and expose node IP address as seen by the manager [#27910](https://github.com/docker/docker/pull/27910)
* Encryption at rest of manager keys and raft data [#27967](https://github.com/docker/docker/pull/27967)
+ Add `--update-max-failure-ratio`, `--update-monitor` and `--rollback` flags to `docker service update` [#26421](https://github.com/docker/docker/pull/26421)
- Fix an issue with address autodiscovery on `docker swarm init` running inside a container [#26457](https://github.com/docker/docker/pull/26457)
+ (experimental) Add `docker service logs` command to view logs for a service [#28089](https://github.com/docker/docker/pull/28089)
+ Pin images by digest for `docker service create` and `update` [#28173](https://github.com/docker/docker/pull/28173)
* Add short (`-f`) flag for `docker node rm --force` and `docker swarm leave --force` [#28196](https://github.com/docker/docker/pull/28196)
+ Add options to customize Raft snapshots (`--max-snapshots`, `--snapshot-interval`) [#27997](https://github.com/docker/docker/pull/27997)
- Don't repull image if pinned by digest [#28265](https://github.com/docker/docker/pull/28265)
+ Swarm-mode support for Windows [#27838](https://github.com/docker/docker/pull/27838)
+ Allow hostname to be updated on service [#28771](https://github.com/docker/docker/pull/28771)
+ Support v2 plugins [#29433](https://github.com/docker/docker/pull/29433)
+ Add content trust for services [#29469](https://github.com/docker/docker/pull/29469)

### Volume

+ Add support for labels on volumes [#21270](https://github.com/docker/docker/pull/21270)
+ Add support for filtering volumes by label [#25628](https://github.com/docker/docker/pull/25628)
* Add a `--force` flag in `docker volume rm` to forcefully purge the data of the volume that has already been deleted [#23436](https://github.com/docker/docker/pull/23436)
* Enhance `docker volume inspect` to show all options used when creating the volume [#26671](https://github.com/docker/docker/pull/26671)
* Add support for local NFS volumes to resolve hostnames [#27329](https://github.com/docker/docker/pull/27329)

### Security

- Fix selinux labeling of volumes shared in a container [#23024](https://github.com/docker/docker/pull/23024)
- Prohibit `/sys/firmware/**` from being accessed with apparmor [#26618](https://github.com/docker/docker/pull/26618)

### Deprecation

- Marked the `docker daemon` command as deprecated. The daemon is moved to a separate binary (`dockerd`), and should be used instead [#26834](https://github.com/docker/docker/pull/26834)
- Deprecate unversioned API endpoints [#28208](https://github.com/docker/docker/pull/28208)
- Remove Ubuntu 15.10 (Wily Werewolf) as supported platform. Ubuntu 15.10 is EOL, and no longer receives updates [#27042](https://github.com/docker/docker/pull/27042)
- Remove Fedora 22 as supported platform. Fedora 22 is EOL, and no longer receives updates [#27432](https://github.com/docker/docker/pull/27432)
- Remove Fedora 23 as supported platform. Fedora 23 is EOL, and no longer receives updates [#29455](https://github.com/docker/docker/pull/29455)
- Deprecate the `repo:shortid` syntax on `docker pull` [#27207](https://github.com/docker/docker/pull/27207)
- Deprecate backing filesystem without `d_type` for overlay and overlay2 storage drivers [#27433](https://github.com/docker/docker/pull/27433)
- Deprecate `MAINTAINER` in Dockerfile [#25466](https://github.com/docker/docker/pull/25466)
- Deprecate `filter` param for endpoint `/images/json` [#27872](https://github.com/docker/docker/pull/27872)
- Deprecate setting duplicate engine labels [#24533](https://github.com/docker/docker/pull/24533)
- Deprecate "top-level" network information in `NetworkSettings` [#28437](https://github.com/docker/docker/pull/28437)

