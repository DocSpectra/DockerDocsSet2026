---
title: Docker Engine 1.11 release notes
linkTitle: Engine 1.11
toc_max: 2
---

## Related guidance

- [Engine installation instructions](/manuals/engine/install/_index.md)
- [Deprecated and removed Engine features](/manuals/engine/deprecated.md)
- [Engine API version history](/reference/api/engine/version-history/)

## Find a release

- [1.11.2 (2016-05-31)](#1112-2016-05-31)
- [1.11.1 (2016-04-26)](#1111-2016-04-26)
- [1.11.0 (2016-04-13)](#1110-2016-04-13)

## Find changes

- Security notes: [1.11.0 (2016-04-13)](#1110-2016-04-13)

## 1.11.2 (2016-05-31)

### Networking

- Fix a stale endpoint issue on overlay networks during ungraceful restart ([#23015](https://github.com/docker/docker/pull/23015))
- Fix an issue where the wrong port could be reported by `docker inspect/ps/port` ([#22997](https://github.com/docker/docker/pull/22997))

### Runtime

- Fix a potential panic when running `docker build` ([#23032](https://github.com/docker/docker/pull/23032))
- Fix interpretation of `--user` parameter ([#22998](https://github.com/docker/docker/pull/22998))
- Fix a bug preventing container statistics to be correctly reported ([#22955](https://github.com/docker/docker/pull/22955))
- Fix an issue preventing container to be restarted after daemon restart ([#22947](https://github.com/docker/docker/pull/22947))
- Fix issues when running 32 bit binaries on Ubuntu 16.04 ([#22922](https://github.com/docker/docker/pull/22922))
- Fix a possible deadlock on image deletion and container attach ([#22918](https://github.com/docker/docker/pull/22918))
- Fix an issue where containers fail to start after a daemon restart if they depend on a containerized cluster store ([#22561](https://github.com/docker/docker/pull/22561))
- Fix an issue causing `docker ps` to hang on CentOS when using devicemapper ([#22168](https://github.com/docker/docker/pull/22168), [#23067](https://github.com/docker/docker/pull/23067))
- Fix a bug preventing to `docker exec` into a container when using devicemapper ([#22168](https://github.com/docker/docker/pull/22168), [#23067](https://github.com/docker/docker/pull/23067))


## 1.11.1 (2016-04-26)

### Distribution

- Fix schema2 manifest media type to be of type `application/vnd.docker.container.image.v1+json` ([#21949](https://github.com/docker/docker/pull/21949))

### Documentation

+ Add missing API documentation for changes introduced with 1.11.0 ([#22048](https://github.com/docker/docker/pull/22048))

### Builder

* Append label passed to `docker build` as arguments as an implicit `LABEL` command at the end of the processed `Dockerfile` ([#22184](https://github.com/docker/docker/pull/22184))

### Networking

- Fix a panic that would occur when forwarding DNS query ([#22261](https://github.com/docker/docker/pull/22261))
- Fix an issue where OS threads could end up within an incorrect network namespace when using user defined networks ([#22261](https://github.com/docker/docker/pull/22261))

### Runtime

- Fix a bug preventing labels configuration to be reloaded via the config file ([#22299](https://github.com/docker/docker/pull/22299))
- Fix a regression where container mounting `/var/run` would prevent other containers from being removed ([#22256](https://github.com/docker/docker/pull/22256))
- Fix an issue where it would be impossible to update both `memory-swap` and `memory` value together ([#22255](https://github.com/docker/docker/pull/22255))
- Fix a regression from 1.11.0 where the `/auth` endpoint would not initialize `serveraddress` if it is not provided ([#22254](https://github.com/docker/docker/pull/22254))
- Add missing cleanup of container temporary files when cancelling a schedule restart ([#22237](https://github.com/docker/docker/pull/22237))
- Remove scary error message when no restart policy is specified ([#21993](https://github.com/docker/docker/pull/21993))
- Fix a panic that would occur when the plugins were activated via the json spec ([#22191](https://github.com/docker/docker/pull/22191))
- Fix restart backoff logic to correctly reset delay if container ran for at least 10secs ([#22125](https://github.com/docker/docker/pull/22125))
- Remove error message when a container restart get cancelled ([#22123](https://github.com/docker/docker/pull/22123))
- Fix an issue where `docker` would not correctly clean up after `docker exec` ([#22121](https://github.com/docker/docker/pull/22121))
- Fix a panic that could occur when serving concurrent `docker stats` commands ([#22120](https://github.com/docker/docker/pull/22120))`
- Revert deprecation of non-existent host directories auto-creation ([#22065](https://github.com/docker/docker/pull/22065))
- Hide misleading rpc error on daemon shutdown ([#22058](https://github.com/docker/docker/pull/22058))

## 1.11.0 (2016-04-13)

> [!IMPORTANT]
>
> With Docker 1.11, a Linux Docker installation is now made of 4 binaries (`docker`, [`docker-containerd`](https://github.com/docker/containerd), [`docker-containerd-shim`](https://github.com/docker/containerd) and [`docker-runc`](https://github.com/opencontainers/runc)). If you have scripts relying on `docker` being a single static binaries, make sure to update them. Interaction with the daemon stay the same otherwise, the usage of the other binaries should be transparent. A Windows Docker installation remains a single binary, `docker.exe`.

### Builder

- Fix a bug where Docker would not use the correct uid/gid when processing the `WORKDIR` command ([#21033](https://github.com/docker/docker/pull/21033))
- Fix a bug where copy operations with userns would not use the proper uid/gid ([#20782](https://github.com/docker/docker/pull/20782), [#21162](https://github.com/docker/docker/pull/21162))

### Client

* Usage of the `:` separator for security option has been deprecated. `=` should be used instead ([#21232](https://github.com/docker/docker/pull/21232))
+ The client user agent is now passed to the registry on `pull`, `build`, `push`, `login` and `search` operations ([#21306](https://github.com/docker/docker/pull/21306), [#21373](https://github.com/docker/docker/pull/21373))
* Allow setting the Domainname and Hostname separately through the API ([#20200](https://github.com/docker/docker/pull/20200))
* Docker info will now warn users if it can not detect the kernel version or the operating system ([#21128](https://github.com/docker/docker/pull/21128))
- Fix an issue where `docker stats --no-stream` output could be all 0s ([#20803](https://github.com/docker/docker/pull/20803))
- Fix a bug where some newly started container would not appear in a running `docker stats` command ([#20792](https://github.com/docker/docker/pull/20792))
* Post processing is no longer enabled for linux-cgo terminals ([#20587](https://github.com/docker/docker/pull/20587))
- Values to `--hostname` are now refused if they do not comply with [RFC1123](https://tools.ietf.org/html/rfc1123) ([#20566](https://github.com/docker/docker/pull/20566))
+ Docker learned how to use a SOCKS proxy ([#20366](https://github.com/docker/docker/pull/20366), [#18373](https://github.com/docker/docker/pull/18373))
+ Docker now supports external credential stores ([#20107](https://github.com/docker/docker/pull/20107))
* `docker ps` now supports displaying the list of volumes mounted inside a container ([#20017](https://github.com/docker/docker/pull/20017))
* `docker info` now also reports Docker's root directory location ([#19986](https://github.com/docker/docker/pull/19986))
- Docker now prohibits login in with an empty username (spaces are trimmed) ([#19806](https://github.com/docker/docker/pull/19806))
* Docker events attributes are now sorted by key ([#19761](https://github.com/docker/docker/pull/19761))
* `docker ps` no longer shows exported port for stopped containers ([#19483](https://github.com/docker/docker/pull/19483))
- Docker now cleans after itself if a save/export command fails ([#17849](https://github.com/docker/docker/pull/17849))
* Docker load learned how to display a progress bar ([#17329](https://github.com/docker/docker/pull/17329), [#120078](https://github.com/docker/docker/pull/20078))

### Distribution

- Fix a panic that occurred when pulling an image with 0 layers ([#21222](https://github.com/docker/docker/pull/21222))
- Fix a panic that could occur on error while pushing to a registry with a misconfigured token service ([#21212](https://github.com/docker/docker/pull/21212))
+ All first-level delegation roles are now signed when doing a trusted push ([#21046](https://github.com/docker/docker/pull/21046))
+ OAuth support for registries was added ([#20970](https://github.com/docker/docker/pull/20970))
* `docker login` now handles token using the implementation found in [docker/distribution](https://github.com/docker/distribution) ([#20832](https://github.com/docker/docker/pull/20832))
* `docker login` will no longer prompt for an email ([#20565](https://github.com/docker/docker/pull/20565))
* Docker will now fallback to registry V1 if no basic auth credentials are available ([#20241](https://github.com/docker/docker/pull/20241))
* Docker will now try to resume layer download where it left off after a network error/timeout ([#19840](https://github.com/docker/docker/pull/19840))
- Fix generated manifest mediaType when pushing cross-repository ([#19509](https://github.com/docker/docker/pull/19509))
- Fix docker requesting additional push credentials when pulling an image if Content Trust is enabled ([#20382](https://github.com/docker/docker/pull/20382))

### Logging

- Fix a race in the journald log driver ([#21311](https://github.com/docker/docker/pull/21311))
* Docker syslog driver now uses the RFC-5424 format when emitting logs ([#20121](https://github.com/docker/docker/pull/20121))
* Docker GELF log driver now allows to specify the compression algorithm and level via the `gelf-compression-type` and `gelf-compression-level` options ([#19831](https://github.com/docker/docker/pull/19831))
* Docker daemon learned to output uncolorized logs via the `--raw-logs` options ([#19794](https://github.com/docker/docker/pull/19794))
+ Docker, on Windows platform, now includes an ETW (Event Tracing in Windows) logging driver named `etwlogs` ([#19689](https://github.com/docker/docker/pull/19689))
* Journald log driver learned how to handle tags ([#19564](https://github.com/docker/docker/pull/19564))
+ The fluentd log driver learned the following options: `fluentd-address`, `fluentd-buffer-limit`, `fluentd-retry-wait`, `fluentd-max-retries` and `fluentd-async-connect` ([#19439](https://github.com/docker/docker/pull/19439))
+ Docker learned to send log to Google Cloud via the new `gcplogs` logging driver. ([#18766](https://github.com/docker/docker/pull/18766))


### Misc

+ When saving linked images together with `docker save` a subsequent `docker load` will correctly restore their parent/child relationship ([#21385](https://github.com/docker/docker/pull/21385))
+ Support for building the Docker cli for OpenBSD was added ([#21325](https://github.com/docker/docker/pull/21325))
+ Labels can now be applied at network, volume and image creation ([#21270](https://github.com/docker/docker/pull/21270))
* The `dockremap` is now created as a system user ([#21266](https://github.com/docker/docker/pull/21266))
- Fix a few response body leaks ([#21258](https://github.com/docker/docker/pull/21258))
- Docker, when run as a service with systemd, will now properly manage its processes cgroups ([#20633](https://github.com/docker/docker/pull/20633))
* `docker info` now reports the value of cgroup KernelMemory or emits a warning if it is not supported ([#20863](https://github.com/docker/docker/pull/20863))
* `docker info` now also reports the cgroup driver in use ([#20388](https://github.com/docker/docker/pull/20388))
* Docker completion is now available on PowerShell ([#19894](https://github.com/docker/docker/pull/19894))
* `dockerinit` is no more ([#19490](https://github.com/docker/docker/pull/19490),[#19851](https://github.com/docker/docker/pull/19851))
+ Support for building Docker on arm64 was added ([#19013](https://github.com/docker/docker/pull/19013))
+ Experimental support for building docker.exe in a native Windows Docker installation ([#18348](https://github.com/docker/docker/pull/18348))

### Networking

- Fix panic if a node is forcibly removed from the cluster ([#21671](https://github.com/docker/docker/pull/21671))
- Fix "error creating vxlan interface" when starting a container in a Swarm cluster ([#21671](https://github.com/docker/docker/pull/21671))
* `docker network inspect` will now report all endpoints whether they have an active container or not ([#21160](https://github.com/docker/docker/pull/21160))
+ Experimental support for the MacVlan and IPVlan network drivers has been added ([#21122](https://github.com/docker/docker/pull/21122))
* Output of `docker network ls` is now sorted by network name ([#20383](https://github.com/docker/docker/pull/20383))
- Fix a bug where Docker would allow a network to be created with the reserved `default` name ([#19431](https://github.com/docker/docker/pull/19431))
* `docker network inspect` returns whether a network is internal or not ([#19357](https://github.com/docker/docker/pull/19357))
+ Control IPv6 via explicit option when creating a network (`docker network create --ipv6`). This shows up as a new `EnableIPv6` field in `docker network inspect` ([#17513](https://github.com/docker/docker/pull/17513))
* Support for AAAA Records (aka IPv6 Service Discovery) in embedded DNS Server ([#21396](https://github.com/docker/docker/pull/21396))
- Fix to not forward docker domain IPv6 queries to external servers ([#21396](https://github.com/docker/docker/pull/21396))
* Multiple A/AAAA records from embedded DNS Server for DNS Round robin ([#21019](https://github.com/docker/docker/pull/21019))
- Fix endpoint count inconsistency after an ungraceful daemon restart ([#21261](https://github.com/docker/docker/pull/21261))
- Move the ownership of exposed ports and port-mapping options from Endpoint to Sandbox ([#21019](https://github.com/docker/docker/pull/21019))
- Fixed a bug which prevents docker reload when host is configured with ipv6.disable=1 ([#21019](https://github.com/docker/docker/pull/21019))
- Added inbuilt nil IPAM driver ([#21019](https://github.com/docker/docker/pull/21019))
- Fixed bug in iptables.Exists() logic [#21019](https://github.com/docker/docker/pull/21019)
- Fixed a Veth interface leak when using overlay network ([#21019](https://github.com/docker/docker/pull/21019))
- Fixed a bug which prevents docker reload after a network delete during shutdown ([#20214](https://github.com/docker/docker/pull/20214))
- Make sure iptables chains are recreated on firewalld reload ([#20419](https://github.com/docker/docker/pull/20419))
- Allow to pass global datastore during config reload ([#20419](https://github.com/docker/docker/pull/20419))
- For anonymous containers use the alias name for IP to name mapping, ie:DNS PTR record ([#21019](https://github.com/docker/docker/pull/21019))
- Fix a panic when deleting an entry from /etc/hosts file  ([#21019](https://github.com/docker/docker/pull/21019))
- Source the forwarded DNS queries from the container net namespace  ([#21019](https://github.com/docker/docker/pull/21019))
- Fix to retain the network internal mode config for bridge networks on daemon reload ([#21780] (https://github.com/docker/docker/pull/21780))
- Fix to retain IPAM driver option configs on daemon reload ([#21914] (https://github.com/docker/docker/pull/21914))

### Plugins

- Fix a file descriptor leak that would occur every time plugins were enumerated ([#20686](https://github.com/docker/docker/pull/20686))
- Fix an issue where Authz plugin would corrupt the payload body when faced with a large amount of data ([#20602](https://github.com/docker/docker/pull/20602))

### Runtime

- Fix a panic that could occur when cleanup after a container started with invalid parameters ([#21716](https://github.com/docker/docker/pull/21716))
- Fix a race with event timers stopping early ([#21692](https://github.com/docker/docker/pull/21692))
- Fix race conditions in the layer store, potentially corrupting the map and crashing the process ([#21677](https://github.com/docker/docker/pull/21677))
- Un-deprecate auto-creation of host directories for mounts. This feature was marked deprecated in ([#21666](https://github.com/docker/docker/pull/21666))
  Docker 1.9, but was decided to be too much of a backward-incompatible change, so it was decided to keep the feature.
+ It is now possible for containers to share the NET and IPC namespaces when `userns` is enabled ([#21383](https://github.com/docker/docker/pull/21383))
+ `docker inspect <image-id>` will now expose the rootfs layers ([#21370](https://github.com/docker/docker/pull/21370))
+ Docker Windows gained a minimal `top` implementation ([#21354](https://github.com/docker/docker/pull/21354))
* Docker learned to report the faulty exe when a container cannot be started due to its condition ([#21345](https://github.com/docker/docker/pull/21345))
* Docker with device mapper will now refuse to run if `udev sync` is not available ([#21097](https://github.com/docker/docker/pull/21097))
- Fix a bug where Docker would not validate the config file upon configuration reload ([#21089](https://github.com/docker/docker/pull/21089))
- Fix a hang that would happen on attach if initial start was to fail ([#21048](https://github.com/docker/docker/pull/21048))
- Fix an issue where registry service options in the daemon configuration file were not properly taken into account ([#21045](https://github.com/docker/docker/pull/21045))
- Fix a race between the exec and resize operations ([#21022](https://github.com/docker/docker/pull/21022))
- Fix an issue where nanoseconds were not correctly taken in account when filtering Docker events ([#21013](https://github.com/docker/docker/pull/21013))
- Fix the handling of Docker command when passed a 64 bytes id ([#21002](https://github.com/docker/docker/pull/21002))
* Docker will now return a `204` (i.e http.StatusNoContent) code when it successfully deleted a network ([#20977](https://github.com/docker/docker/pull/20977))
- Fix a bug where the daemon would wait indefinitely in case the process it was about to killed had already exited on its own ([#20967](https://github.com/docker/docker/pull/20967)
* The devmapper driver learned the `dm.min_free_space` option. If the mapped device free space reaches the passed value, new device creation will be prohibited. ([#20786](https://github.com/docker/docker/pull/20786))
+ Docker can now prevent processes in container to gain new privileges via the `--security-opt=no-new-privileges` flag ([#20727](https://github.com/docker/docker/pull/20727))
- Starting a container with the `--device` option will now correctly resolves symlinks ([#20684](https://github.com/docker/docker/pull/20684))
+ Docker now relies on [`containerd`](https://github.com/docker/containerd) and [`runc`](https://github.com/opencontainers/runc) to spawn containers. ([#20662](https://github.com/docker/docker/pull/20662))
- Fix docker configuration reloading to only alter value present in the given config file ([#20604](https://github.com/docker/docker/pull/20604))
+ Docker now allows setting a container hostname via the `--hostname` flag when `--net=host` ([#20177](https://github.com/docker/docker/pull/20177))
+ Docker now allows executing privileged container while running with `--userns-remap` if both `--privileged` and the new `--userns=host` flag are specified ([#20111](https://github.com/docker/docker/pull/20111))
- Fix Docker not cleaning up correctly old containers upon restarting after a crash ([#19679](https://github.com/docker/docker/pull/19679))
* Docker will now error out if it doesn't recognize a configuration key within the config file ([#19517](https://github.com/docker/docker/pull/19517))
- Fix container loading, on daemon startup, when they depends on a plugin running within a container ([#19500](https://github.com/docker/docker/pull/19500))
* `docker update` learned how to change a container restart policy ([#19116](https://github.com/docker/docker/pull/19116))
* `docker inspect` now also returns a new `State` field containing the container state in a human readable way (i.e. one of `created`, `restarting`, `running`, `paused`, `exited` or `dead`)([#18966](https://github.com/docker/docker/pull/18966))
+ Docker learned to limit the number of active pids (i.e. processes) within the container via the `pids-limit` flags. NOTE: This requires `CGROUP_PIDS=y` to be in the kernel configuration. ([#18697](https://github.com/docker/docker/pull/18697))
- `docker load` now has a `--quiet` option to suppress the load output ([#20078](https://github.com/docker/docker/pull/20078))
- Fix a bug in neighbor discovery for IPv6 peers ([#20842](https://github.com/docker/docker/pull/20842))
- Fix a panic during cleanup if a container was started with invalid options ([#21802](https://github.com/docker/docker/pull/21802))
- Fix a situation where a container cannot be stopped if the terminal is closed ([#21840](https://github.com/docker/docker/pull/21840))

### Security

* Object with the `pcp_pmcd_t` selinux type were given management access to `/var/lib/docker(/.*)?` ([#21370](https://github.com/docker/docker/pull/21370))
* `restart_syscall`, `copy_file_range`, `mlock2` joined the list of allowed calls in the default seccomp profile ([#21117](https://github.com/docker/docker/pull/21117), [#21262](https://github.com/docker/docker/pull/21262))
* `send`, `recv` and `x32` were added to the list of allowed syscalls and arch in the default seccomp profile ([#19432](https://github.com/docker/docker/pull/19432))
* Docker Content Trust now requests the server to perform snapshot signing ([#21046](https://github.com/docker/docker/pull/21046))
* Support for using YubiKeys for Content Trust signing has been moved out of experimental ([#21591](https://github.com/docker/docker/pull/21591))

### Volumes

* Output of `docker volume ls` is now sorted by volume name ([#20389](https://github.com/docker/docker/pull/20389))
* Local volumes can now accept options similar to the unix `mount` tool ([#20262](https://github.com/docker/docker/pull/20262))
- Fix an issue where one letter directory name could not be used as source for volumes ([#21106](https://github.com/docker/docker/pull/21106))
+ `docker run -v` now accepts a new flag `nocopy`. This tells the runtime not to copy the container path content into the volume (which is the default behavior) ([#21223](https://github.com/docker/docker/pull/21223))

