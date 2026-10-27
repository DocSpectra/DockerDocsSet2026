---
title: Docker Engine 1.10 release notes
linkTitle: Engine 1.10
toc_max: 2
---

## Related guidance

- [Engine installation instructions](/manuals/engine/install/_index.md)
- [Deprecated and removed Engine features](/manuals/engine/deprecated.md)
- [Engine API version history](/reference/api/engine/version-history/)

## Find a release

- [1.10.3 (2016-03-10)](#1103-2016-03-10)
- [1.10.2 (2016-02-22)](#1102-2016-02-22)
- [1.10.1 (2016-02-11)](#1101-2016-02-11)
- [1.10.0 (2016-02-04)](#1100-2016-02-04)

## Find changes

- Security notes: [1.10.3 (2016-03-10)](#1103-2016-03-10), [1.10.2 (2016-02-22)](#1102-2016-02-22), [1.10.1 (2016-02-11)](#1101-2016-02-11), [1.10.0 (2016-02-04)](#1100-2016-02-04)

## 1.10.3 (2016-03-10)

### Runtime

- Fix Docker client exiting with an "Unrecognized input header" error [#20706](https://github.com/docker/docker/pull/20706)
- Fix Docker exiting if Exec is started with both `AttachStdin` and `Detach` [#20647](https://github.com/docker/docker/pull/20647)

### Distribution

- Fix a crash when pushing multiple images sharing the same layers to the same repository in parallel [#20831](https://github.com/docker/docker/pull/20831)
- Fix a panic when pushing images to a registry which uses a misconfigured token service [#21030](https://github.com/docker/docker/pull/21030)

### Plugin system

- Fix issue preventing volume plugins to start when SELinux is enabled [#20834](https://github.com/docker/docker/pull/20834)
- Prevent Docker from exiting if a volume plugin returns a null response for Get requests [#20682](https://github.com/docker/docker/pull/20682)
- Fix plugin system leaking file descriptors if a plugin has an error [#20680](https://github.com/docker/docker/pull/20680)

### Security

- Fix linux32 emulation to fail during docker build [#20672](https://github.com/docker/docker/pull/20672)
  It was due to the `personality` syscall being blocked by the default seccomp profile.
- Fix Oracle XE 10g failing to start in a container [#20981](https://github.com/docker/docker/pull/20981)
  It was due to the `ipc` syscall being blocked by the default seccomp profile.
- Fix user namespaces not working on Linux From Scratch [#20685](https://github.com/docker/docker/pull/20685)
- Fix issue preventing daemon to start if userns is enabled and the `subuid` or `subgid` files contain comments [#20725](https://github.com/docker/docker/pull/20725)

## 1.10.2 (2016-02-22)

### Runtime

- Prevent systemd from deleting containers' cgroups when its configuration is reloaded [#20518](https://github.com/docker/docker/pull/20518)
- Fix SELinux issues by disregarding `--read-only` when mounting `/dev/mqueue` [#20333](https://github.com/docker/docker/pull/20333)
- Fix chown permissions used during `docker cp` when userns is used [#20446](https://github.com/docker/docker/pull/20446)
- Fix configuration loading issue with all booleans defaulting to `true` [#20471](https://github.com/docker/docker/pull/20471)
- Fix occasional panic with `docker logs -f` [#20522](https://github.com/docker/docker/pull/20522)

### Distribution

- Keep layer reference if deletion failed to avoid a badly inconsistent state [#20513](https://github.com/docker/docker/pull/20513)
- Handle gracefully a corner case when canceling migration [#20372](https://github.com/docker/docker/pull/20372)
- Fix docker import on compressed data [#20367](https://github.com/docker/docker/pull/20367)
- Fix tar-split files corruption during migration that later cause docker push and docker save to fail [#20458](https://github.com/docker/docker/pull/20458)

### Networking

- Fix daemon crash if embedded DNS is sent garbage [#20510](https://github.com/docker/docker/pull/20510)

### Volumes

- Fix issue with multiple volume references with same name [#20381](https://github.com/docker/docker/pull/20381)

### Security

- Fix potential cache corruption and delegation conflict issues [#20523](https://github.com/docker/docker/pull/20523)

## 1.10.1 (2016-02-11)

### Runtime

* Do not stop daemon on migration hard failure [#20156](https://github.com/docker/docker/pull/20156)
- Fix various issues with migration to content-addressable images [#20058](https://github.com/docker/docker/pull/20058)
- Fix ZFS permission bug with user namespaces [#20045](https://github.com/docker/docker/pull/20045)
- Do not leak /dev/mqueue from the host to all containers, keep it container-specific [#19876](https://github.com/docker/docker/pull/19876) [#20133](https://github.com/docker/docker/pull/20133)
- Fix `docker ps --filter before=...` to not show stopped containers without providing `-a` flag [#20135](https://github.com/docker/docker/pull/20135)

### Security

- Fix issue preventing docker events to work properly with authorization plugin [#20002](https://github.com/docker/docker/pull/20002)

### Distribution

* Add additional verifications and prevent from uploading invalid data to registries [#20164](https://github.com/docker/docker/pull/20164)
- Fix regression preventing uppercase characters in image reference hostname [#20175](https://github.com/docker/docker/pull/20175)

### Networking

- Fix embedded DNS for user-defined networks in the presence of firewalld [#20060](https://github.com/docker/docker/pull/20060)
- Fix issue where removing a network during shutdown left Docker inoperable [#20181](https://github.com/docker/docker/issues/20181) [#20235](https://github.com/docker/docker/issues/20235)
- Embedded DNS is now able to return compressed results [#20181](https://github.com/docker/docker/issues/20181)
- Fix port-mapping issue with `userland-proxy=false` [#20181](https://github.com/docker/docker/issues/20181)

### Logging

- Fix bug where tcp+tls protocol would be rejected [#20109](https://github.com/docker/docker/pull/20109)

### Volumes

- Fix issue whereby older volume drivers would not receive volume options [#19983](https://github.com/docker/docker/pull/19983)

### Misc

- Remove TasksMax from Docker systemd service [#20167](https://github.com/docker/docker/pull/20167)

## 1.10.0 (2016-02-04)

> [!IMPORTANT]
>
> Docker 1.10 uses a new content-addressable storage for images and layers.

A migration is performed the first time `docker` is run, and can take a significant amount of time depending on the number of images present. Refer to this page on the wiki for more information: https://github.com/docker/docker/wiki/Engine-v1.10.0-content-addressability-migration
We also released a cool migration utility that enables you to perform the migration before updating to reduce downtime.
Engine 1.10 migrator can be found on Docker Hub: https://hub.docker.com/r/docker/v1.10-migrator/

### Runtime

+ New `docker update` command that allows updating resource constraints on running containers [#15078](https://github.com/docker/docker/pull/15078)
+ Add `--tmpfs` flag to `docker run` to create a tmpfs mount in a container [#13587](https://github.com/docker/docker/pull/13587)
+ Add `--format` flag to `docker images` command [#17692](https://github.com/docker/docker/pull/17692)
+ Allow to set daemon configuration in a file and hot-reload it with the `SIGHUP` signal [#18587](https://github.com/docker/docker/pull/18587)
+ Updated docker events to include more meta-data and event types [#18888](https://github.com/docker/docker/pull/18888)
  This change is backward compatible in the API, but not on the CLI.
+ Add `--blkio-weight-device` flag to `docker run` [#13959](https://github.com/docker/docker/pull/13959)
+ Add `--device-read-bps` and `--device-write-bps` flags to `docker run` [#14466](https://github.com/docker/docker/pull/14466)
+ Add `--device-read-iops` and `--device-write-iops` flags to `docker run` [#15879](https://github.com/docker/docker/pull/15879)
+ Add `--oom-score-adj` flag to `docker run` [#16277](https://github.com/docker/docker/pull/16277)
+ Add `--detach-keys` flag to `attach`, `run`, `start` and `exec` commands to override the default key sequence that detaches from a container  [#15666](https://github.com/docker/docker/pull/15666)
+ Add `--shm-size` flag to `run`, `create` and `build` to set the size of `/dev/shm` [#16168](https://github.com/docker/docker/pull/16168)
+ Show the number of running, stopped, and paused containers in `docker info` [#19249](https://github.com/docker/docker/pull/19249)
+ Show the `OSType` and `Architecture` in `docker info` [#17478](https://github.com/docker/docker/pull/17478)
+ Add `--cgroup-parent` flag on `daemon` to set cgroup parent for all containers [#19062](https://github.com/docker/docker/pull/19062)
+ Add `-L` flag to docker cp to follow symlinks [#16613](https://github.com/docker/docker/pull/16613)
+ New `status=dead` filter for `docker ps` [#17908](https://github.com/docker/docker/pull/17908)
* Change `docker run` exit codes to distinguish between runtime and application errors [#14012](https://github.com/docker/docker/pull/14012)
* Enhance `docker events --since` and `--until` to support nanoseconds and timezones [#17495](https://github.com/docker/docker/pull/17495)
* Add `--all`/`-a` flag to `stats` to include both running and stopped containers [#16742](https://github.com/docker/docker/pull/16742)
* Change the default cgroup-driver to `cgroupfs` [#17704](https://github.com/docker/docker/pull/17704)
* Emit a "tag" event when tagging an image with `build -t` [#17115](https://github.com/docker/docker/pull/17115)
* Best effort for linked containers' start order when starting the daemon [#18208](https://github.com/docker/docker/pull/18208)
* Add ability to add multiple tags on `build` [#15780](https://github.com/docker/docker/pull/15780)
* Permit `OPTIONS` request against any url, thus fixing issue with CORS [#19569](https://github.com/docker/docker/pull/19569)
- Fix the `--quiet` flag on `docker build` to actually be quiet [#17428](https://github.com/docker/docker/pull/17428)
- Fix `docker images --filter dangling=false` to now show all non-dangling images [#19326](https://github.com/docker/docker/pull/19326)
- Fix race condition causing autorestart turning off on restart [#17629](https://github.com/docker/docker/pull/17629)
- Recognize GPFS filesystems [#19216](https://github.com/docker/docker/pull/19216)
- Fix obscure bug preventing to start containers [#19751](https://github.com/docker/docker/pull/19751)
- Forbid `exec` during container restart [#19722](https://github.com/docker/docker/pull/19722)
- devicemapper: Increasing `--storage-opt dm.basesize` will now increase the base device size on daemon restart [#19123](https://github.com/docker/docker/pull/19123)

### Security

+ Add `--userns-remap` flag to `daemon` to support user namespaces (previously in experimental) [#19187](https://github.com/docker/docker/pull/19187)
+ Add support for custom seccomp profiles in `--security-opt` [#17989](https://github.com/docker/docker/pull/17989)
+ Add default seccomp profile [#18780](https://github.com/docker/docker/pull/18780)
+ Add `--authorization-plugin` flag to `daemon` to customize ACLs [#15365](https://github.com/docker/docker/pull/15365)
+ Docker Content Trust now supports the ability to read and write user delegations [#18887](https://github.com/docker/docker/pull/18887)
  This is an optional, opt-in feature that requires the explicit use of the Notary command-line utility in order to be enabled.
  Enabling delegation support in a specific repository will break the ability of Docker 1.9 and 1.8 to pull from that repository, if content trust is enabled.
* Allow SELinux to run in a container when using the BTRFS storage driver [#16452](https://github.com/docker/docker/pull/16452)

### Distribution

* Use content-addressable storage for images and layers [#17924](https://github.com/docker/docker/pull/17924)
  A migration is performed the first time docker is run; it can take a significant amount of time depending on the number of images and containers present.
  Images no longer depend on the parent chain but contain a list of layer references.
  `docker load`/`docker save` tarballs now also contain content-addressable image configurations.
  For more information: https://github.com/docker/docker/wiki/Engine-v1.10.0-content-addressability-migration
* Add support for the new [manifest format ("schema2")](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md) [#18785](https://github.com/docker/docker/pull/18785)
* Lots of improvements for push and pull: performance++, retries on failed downloads, cancelling on client disconnect [#18353](https://github.com/docker/docker/pull/18353), [#18418](https://github.com/docker/docker/pull/18418), [#19109](https://github.com/docker/docker/pull/19109), [#18353](https://github.com/docker/docker/pull/18353)
* Limit v1 protocol fallbacks [#18590](https://github.com/docker/docker/pull/18590)
- Fix issue where docker could hang indefinitely waiting for a nonexistent process to pull an image [#19743](https://github.com/docker/docker/pull/19743)

### Networking

+ Use DNS-based discovery instead of `/etc/hosts` [#19198](https://github.com/docker/docker/pull/19198)
+ Support for network-scoped alias using `--net-alias` on `run` and `--alias` on `network connect` [#19242](https://github.com/docker/docker/pull/19242)
+ Add `--ip` and `--ip6` on `run` and `network connect` to support custom IP addresses for a container in a network [#19001](https://github.com/docker/docker/pull/19001)
+ Add `--ipam-opt` to `network create` for passing custom IPAM options [#17316](https://github.com/docker/docker/pull/17316)
+ Add `--internal` flag to `network create` to restrict external access to and from the network [#19276](https://github.com/docker/docker/pull/19276)
+ Add `kv.path` option to `--cluster-store-opt` [#19167](https://github.com/docker/docker/pull/19167)
+ Add `discovery.heartbeat` and `discovery.ttl` options to `--cluster-store-opt` to configure discovery TTL and heartbeat timer [#18204](https://github.com/docker/docker/pull/18204)
+ Add `--format` flag to `network inspect` [#17481](https://github.com/docker/docker/pull/17481)
+ Add `--link` to `network connect` to provide a container-local alias [#19229](https://github.com/docker/docker/pull/19229)
+ Support for Capability exchange with remote IPAM plugins [#18775](https://github.com/docker/docker/pull/18775)
+ Add `--force` to `network disconnect` to force container to be disconnected from network [#19317](https://github.com/docker/docker/pull/19317)
* Support for multi-host networking using built-in overlay driver for all engine supported kernels: 3.10+ [#18775](https://github.com/docker/docker/pull/18775)
* `--link` is now supported on `docker run` for containers in user-defined network [#19229](https://github.com/docker/docker/pull/19229)
* Enhance `docker network rm` to allow removing multiple networks [#17489](https://github.com/docker/docker/pull/17489)
* Include container names in `network inspect` [#17615](https://github.com/docker/docker/pull/17615)
* Include auto-generated subnets for user-defined networks in `network inspect` [#17316](https://github.com/docker/docker/pull/17316)
* Add `--filter` flag to `network ls` to hide predefined networks [#17782](https://github.com/docker/docker/pull/17782)
* Add support for network connect/disconnect to stopped containers [#18906](https://github.com/docker/docker/pull/18906)
* Add network ID to container inspect [#19323](https://github.com/docker/docker/pull/19323)
- Fix MTU issue where Docker would not start with two or more default routes [#18108](https://github.com/docker/docker/pull/18108)
- Fix duplicate IP address for containers [#18106](https://github.com/docker/docker/pull/18106)
- Fix issue preventing sometimes docker from creating the bridge network [#19338](https://github.com/docker/docker/pull/19338)
- Do not substitute 127.0.0.1 name server when using `--net=host` [#19573](https://github.com/docker/docker/pull/19573)

### Logging

+ New logging driver for Splunk [#16488](https://github.com/docker/docker/pull/16488)
+ Add support for syslog over TCP+TLS [#18998](https://github.com/docker/docker/pull/18998)
* Enhance `docker logs --since` and `--until` to support nanoseconds and time [#17495](https://github.com/docker/docker/pull/17495)
* Enhance AWS logs to auto-detect region [#16640](https://github.com/docker/docker/pull/16640)

### Volumes

+ Add support to set the mount propagation mode for a volume [#17034](https://github.com/docker/docker/pull/17034)
* Add `ls` and `inspect` endpoints to volume plugin API [#16534](https://github.com/docker/docker/pull/16534)
  Existing plugins need to make use of these new APIs to satisfy users' expectation
  For that, use the new MIME type `application/vnd.docker.plugins.v1.2+json` [#19549](https://github.com/docker/docker/pull/19549)
- Fix data not being copied to named volumes [#19175](https://github.com/docker/docker/pull/19175)
- Fix issues preventing volume drivers from being containerized [#19500](https://github.com/docker/docker/pull/19500)
- Fix `docker volumes ls --dangling=false` to now show all non-dangling volumes [#19671](https://github.com/docker/docker/pull/19671)
- Do not remove named volumes on container removal [#19568](https://github.com/docker/docker/pull/19568)
- Allow external volume drivers to host anonymous volumes [#19190](https://github.com/docker/docker/pull/19190)

### Builder

+ Add support for `**` in `.dockerignore` to wildcard multiple levels of directories [#17090](https://github.com/docker/docker/pull/17090)
- Fix handling of UTF-8 characters in Dockerfiles [#17055](https://github.com/docker/docker/pull/17055)
- Fix permissions problem when reading from STDIN [#19283](https://github.com/docker/docker/pull/19283)

### Client

+ Add support for overriding the API version to use via an `DOCKER_API_VERSION` environment-variable [#15964](https://github.com/docker/docker/pull/15964)
- Fix a bug preventing Windows clients to log in to Docker Hub [#19891](https://github.com/docker/docker/pull/19891)

### Misc

* systemd: Set TasksMax in addition to LimitNPROC in systemd service file [#19391](https://github.com/docker/docker/pull/19391)

### Deprecations

* Remove LXC support. The LXC driver was deprecated in Docker 1.8, and has now been removed [#17700](https://github.com/docker/docker/pull/17700)
* Remove `--exec-driver` daemon flag, because it is no longer in use [#17700](https://github.com/docker/docker/pull/17700)
* Remove old deprecated single-dashed long CLI flags (such as `-rm`; use `--rm` instead) [#17724](https://github.com/docker/docker/pull/17724)
* Deprecate HostConfig at API container start [#17799](https://github.com/docker/docker/pull/17799)
* Deprecate docker packages for newly EOL'd Linux distributions: Fedora 21 and Ubuntu 15.04 (Vivid) [#18794](https://github.com/docker/docker/pull/18794), [#18809](https://github.com/docker/docker/pull/18809)
* Deprecate `-f` flag for docker tag [#18350](https://github.com/docker/docker/pull/18350)

