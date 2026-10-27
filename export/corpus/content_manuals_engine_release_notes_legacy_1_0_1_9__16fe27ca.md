---
title: Docker Engine 1.0-1.9 release notes
linkTitle: Engine 1.0-1.9
toc_max: 2
---

## Related guidance

- [Engine installation instructions](/manuals/engine/install/_index.md)
- [Deprecated and removed Engine features](/manuals/engine/deprecated.md)
- [Engine API version history](/reference/api/engine/version-history/)

## Find a release

- [1.9.1 (2015-11-21)](#191-2015-11-21)
- [1.9.0 (2015-11-03)](#190-2015-11-03)
- [1.8.3 (2015-10-12)](#183-2015-10-12)
- [1.8.2 (2015-09-10)](#182-2015-09-10)
- [1.8.1 (2015-08-12)](#181-2015-08-12)
- [1.8.0 (2015-08-11)](#180-2015-08-11)
- [1.7.1 (2015-07-14)](#171-2015-07-14)
- [1.7.0 (2015-06-16)](#170-2015-06-16)
- [1.6.2 (2015-05-13)](#162-2015-05-13)
- [1.6.1 (2015-05-07)](#161-2015-05-07)
- [1.6.0 (2015-04-07)](#160-2015-04-07)
- [1.5.0 (2015-02-10)](#150-2015-02-10)
- [1.4.1 (2014-12-15)](#141-2014-12-15)
- [1.4.0 (2014-12-11)](#140-2014-12-11)
- [1.3.3 (2014-12-11)](#133-2014-12-11)
- [1.3.2 (2014-11-20)](#132-2014-11-20)
- [1.3.1 (2014-10-28)](#131-2014-10-28)
- [1.3.0 (2014-10-14)](#130-2014-10-14)
- [1.2.0 (2014-08-20)](#120-2014-08-20)
- [1.1.2 (2014-07-23)](#112-2014-07-23)
- [1.1.1 (2014-07-09)](#111-2014-07-09)
- [1.1.0 (2014-07-03)](#110-2014-07-03)
- [1.0.1 (2014-06-19)](#101-2014-06-19)
- [1.0.0 (2014-06-09)](#100-2014-06-09)

## Find changes

- Security notes: [1.9.0 (2015-11-03)](#190-2015-11-03), [1.8.3 (2015-10-12)](#183-2015-10-12), [1.6.1 (2015-05-07)](#161-2015-05-07), [1.3.3 (2014-12-11)](#133-2014-12-11), [1.3.2 (2014-11-20)](#132-2014-11-20), [1.3.1 (2014-10-28)](#131-2014-10-28)

## 1.9.1 (2015-11-21)

### Runtime

- Do not prevent daemon from booting if images could not be restored (#17695)
- Force IPC mount to unmount on daemon shutdown/init (#17539)
- Turn IPC unmount errors into warnings (#17554)
- Fix `docker stats` performance regression (#17638)
- Clarify cryptic error message upon `docker logs` if `--log-driver=none` (#17767)
- Fix seldom panics (#17639, #17634, #17703)
- Fix opq whiteouts problems for files with dot prefix (#17819)
- devicemapper: try defaulting to xfs instead of ext4 for performance reasons (#17903, #17918)
- devicemapper: fix displayed fs in docker info (#17974)
- selinux: only relabel if user requested so with the `z` option (#17450, #17834)
- Do not make network calls when normalizing names (#18014)

### Client

- Fix `docker login` on windows (#17738)
- Fix bug with `docker inspect` output when not connected to daemon (#17715)
- Fix `docker inspect -f {{.HostConfig.Dns}} somecontainer` (#17680)

### Builder

- Fix regression with symlink behavior in ADD/COPY (#17710)

### Networking

- Allow passing a network ID as an argument for `--net` (#17558)
- Fix connect to host and prevent disconnect from host for `host` network (#17476)
- Fix `--fixed-cidr` issue when gateway ip falls in ip-range and ip-range is
  not the first block in the network (#17853)
- Restore deterministic `IPv6` generation from `MAC` address on default `bridge` network (#17890)
- Allow port-mapping only for endpoints created on docker run (#17858)
- Fixed an endpoint delete issue with a possible stale sbox (#18102)

### Distribution

- Correct parent chain in v2 push when v1Compatibility files on the disk are inconsistent (#18047)

## 1.9.0 (2015-11-03)

### Runtime

+ `docker stats` now returns block IO metrics (#15005)
+ `docker stats` now details network stats per interface (#15786)
+ Add `ancestor=<image>` filter to `docker ps --filter` flag to filter
containers based on their ancestor images (#14570)
+ Add `label=<somelabel>` filter to `docker ps --filter` to filter containers
based on label (#16530)
+ Add `--kernel-memory` flag to `docker run` (#14006)
+ Add `--message` flag to `docker import` allowing to specify an optional
message (#15711)
+ Add `--privileged` flag to `docker exec` (#14113)
+ Add `--stop-signal` flag to `docker run` allowing to replace the container
process stopping signal (#15307)
+ Add a new `unless-stopped` restart policy (#15348)
+ Inspecting an image now returns tags (#13185)
+ Add container size information to `docker inspect` (#15796)
+ Add `RepoTags` and `RepoDigests` field to `/images/{name:.*}/json` (#17275)
- Remove the deprecated `/container/ps` endpoint from the API (#15972)
- Send and document correct HTTP codes for `/exec/<name>/start` (#16250)
- Share shm and mqueue between containers sharing IPC namespace (#15862)
- Event stream now shows OOM status when `--oom-kill-disable` is set (#16235)
- Ensure special network files (/etc/hosts etc.) are read-only if bind-mounted
with `ro` option (#14965)
- Improve `rmi` performance (#16890)
- Do not update /etc/hosts for the default bridge network, except for links (#17325)
- Fix conflict with duplicate container names (#17389)
- Fix an issue with incorrect template execution in `docker inspect` (#17284)
- DEPRECATE `-c` short flag variant for `--cpu-shares` in docker run (#16271)

### Client

+ Allow `docker import` to import from local files (#11907)

### Builder

+ Add a `STOPSIGNAL` Dockerfile instruction allowing to set a different
stop-signal for the container process (#15307)
+ Add an `ARG` Dockerfile instruction and a `--build-arg` flag to `docker build`
that allows to add build-time environment variables (#15182)
- Improve cache miss performance (#16890)

### Storage

- devicemapper: Implement deferred deletion capability (#16381)

### Networking

+ `docker network` exits experimental and is part of standard release (#16645)
+ New network top-level concept, with associated subcommands and API (#16645)
  WARNING: the API is different from the experimental API
+ Support for multiple isolated/micro-segmented networks (#16645)
+ Built-in multihost networking using VXLAN based overlay driver (#14071)
+ Support for third-party network plugins (#13424)
+ Ability to dynamically connect containers to multiple networks (#16645)
+ Support for user-defined IP address management via pluggable IPAM drivers (#16910)
+ Add daemon flags `--cluster-store` and `--cluster-advertise` for built-in nodes discovery (#16229)
+ Add `--cluster-store-opt` for setting up TLS settings (#16644)
+ Add `--dns-opt` to the daemon (#16031)
- DEPRECATE following container `NetworkSettings` fields in API v1.21: `EndpointID`, `Gateway`,
  `GlobalIPv6Address`, `GlobalIPv6PrefixLen`, `IPAddress`, `IPPrefixLen`, `IPv6Gateway` and `MacAddress`.
  Those are now specific to the `bridge` network. Use `NetworkSettings.Networks` to inspect
  the networking settings of a container per network.

### Volumes

+ New top-level `volume` subcommand and API (#14242)
- Move API volume driver settings to host-specific config (#15798)
- Print an error message if volume name is not unique (#16009)
- Ensure volumes created from Dockerfiles always use the local volume driver
(#15507)
- DEPRECATE auto-creating missing host paths for bind mounts (#16349)

### Logging

+ Add `awslogs` logging driver for Amazon CloudWatch (#15495)
+ Add generic `tag` log option to allow customizing container/image
information passed to driver (#15384)
- Implement the `docker logs` endpoint for the journald driver (#13707)
- DEPRECATE driver-specific log tags (#15384)

### Distribution

+ `docker search` now works with partial names (#16509)
- Push optimization: avoid buffering to file (#15493)
- The daemon will display progress for images that were already being pulled
by another client (#15489)
- Only permissions required for the current action being performed are requested (#)
+ Renaming trust keys (and respective environment variables) from `offline` to
`root` and `tagging` to `repository` (#16894)
- DEPRECATE trust key environment variables
`DOCKER_CONTENT_TRUST_OFFLINE_PASSPHRASE` and
`DOCKER_CONTENT_TRUST_TAGGING_PASSPHRASE` (#16894)

### Security

+ Add SELinux profiles to the rpm package (#15832)
- Fix various issues with AppArmor profiles provided in the deb package
(#14609)
- Add AppArmor policy that prevents writing to /proc (#15571)

## 1.8.3 (2015-10-12)

### Distribution

- Fix layer IDs lead to local graph poisoning (CVE-2014-8178)
- Fix manifest validation and parsing logic errors allow pull-by-digest validation bypass (CVE-2014-8179)
+ Add `--disable-legacy-registry` to prevent a daemon from using a v1 registry

## 1.8.2 (2015-09-10)

### Distribution

- Fixes rare edge case of handling GNU LongLink and LongName entries.
- Fix ^C on docker pull.
- Fix docker pull issues on client disconnection.
- Fix issue that caused the daemon to panic when loggers weren't configured properly.
- Fix goroutine leak pulling images from registry V2.

### Runtime

- Fix a bug mounting cgroups for docker daemons running inside docker containers.
- Initialize log configuration properly.

### Client:

- Handle `-q` flag in `docker ps` properly when there is a default format.

### Networking

- Fix several corner cases with netlink.

### Contrib

- Fix several issues with bash completion.

## 1.8.1 (2015-08-12)

### Distribution

* Fix a bug where pushing multiple tags would result in invalid images

## 1.8.0 (2015-08-11)

### Distribution

+ Trusted pull, push and build, disabled by default
* Make tar layers deterministic between registries
* Don't allow deleting the image of running containers
* Check if a tag name to load is a valid digest
* Allow one character repository names
* Add a more accurate error description for invalid tag name
* Make build cache ignore mtime

### Cli

+ Add support for DOCKER_CONFIG/--config to specify config file dir
+ Add --type flag  for docker inspect command
+ Add formatting options to `docker ps` with `--format`
+ Replace `docker -d` with new subcommand `docker daemon`
* Zsh completion updates and improvements
* Add some missing events to bash completion
* Support daemon urls with base paths in `docker -H`
* Validate status= filter to docker ps
* Display when a container is in --net=host in docker ps
* Extend docker inspect to export image metadata related to graph driver
* Restore --default-gateway{,-v6} daemon options
* Add missing unpublished ports in docker ps
* Allow duration strings in `docker events` as --since/--until
* Expose more mounts information in `docker inspect`

### Runtime

+ Add new Fluentd logging driver
+ Allow `docker import` to load from local files
+ Add logging driver for GELF via UDP
+ Allow to copy files from host to containers with `docker cp`
+ Promote volume drivers from experimental to master
+ Add rollover options to json-file log driver, and --log-driver-opts flag
+ Add memory swappiness tuning options
* Remove cgroup read-only flag when privileged
* Make /proc, /sys, & /dev readonly for readonly containers
* Add cgroup bind mount by default
* Overlay: Export metadata for container and image in `docker inspect`
* Devicemapper: external device activation
* Devicemapper: Compare uuid of base device on startup
* Remove RC4 from the list of registry cipher suites
* Add syslog-facility option
* LXC execdriver compatibility with recent LXC versions
* Mark LXC execriver as deprecated (to be removed with the migration to runc)

### Plugins

* Separate plugin sockets and specs locations
* Allow TLS connections to plugins

### Bug fixes

- Add missing 'Names' field to /containers/json API output
- Make `docker rmi` of dangling images safe while pulling
- Devicemapper: Change default basesize to 100G
- Go Scheduler issue with sync.Mutex and gcc
- Fix issue where Search API endpoint would panic due to empty AuthConfig
- Set image canonical names correctly
- Check dockerinit only if lxc driver is used
- Fix ulimit usage of nproc
- Always attach STDIN if -i,--interactive is specified
- Show error messages when saving container state fails
- Fixed incorrect assumption on --bridge=none treated as disable network
- Check for invalid port specifications in host configuration
- Fix endpoint leave failure for --net=host mode
- Fix goroutine leak in the stats API if the container is not running
- Check for apparmor file before reading it
- Fix DOCKER_TLS_VERIFY being ignored
- Set umask to the default on startup
- Correct the message of pause and unpause a non-running container
- Adjust disallowed CpuShares in container creation
- ZFS: correctly apply selinux context
- Display empty string instead of <nil> when IP opt is nil
- `docker kill` returns error when container is not running
- Fix COPY/ADD quoted/json form
- Fix goroutine leak on logs -f with no output
- Remove panic in nat package on invalid hostport
- Fix container linking in Fedora 22
- Fix error caused using default gateways outside of the allocated range
- Format times in inspect command with a template as RFC3339Nano
- Make registry client to accept 2xx and 3xx http status responses as successful
- Fix race issue that caused the daemon to crash with certain layer downloads failed in a specific order.
- Fix error when the docker ps format was not valid.
- Remove redundant ip forward check.
- Fix issue trying to push images to repository mirrors.
- Fix error cleaning up network entrypoints when there is an initialization issue.

## 1.7.1 (2015-07-14)

### Runtime

- Fix default user spawning exec process with `docker exec`
- Make `--bridge=none` not to configure the network bridge
- Publish networking stats properly
- Fix implicit devicemapper selection with static binaries
- Fix socket connections that hung intermittently
- Fix bridge interface creation on CentOS/RHEL 6.6
- Fix local dns lookups added to resolv.conf
- Fix copy command mounting volumes
- Fix read/write privileges in volumes mounted with --volumes-from

### Remote API

- Fix unmarshalling of Command and Entrypoint
- Set limit for minimum client version supported
- Validate port specification
- Return proper errors when attach/reattach fail

### Distribution

- Fix pulling private images
- Fix fallback between registry V2 and V1

## 1.7.0 (2015-06-16)

### Runtime
+ Experimental feature: support for out-of-process volume plugins
* The userland proxy can be disabled in favor of hairpin NAT using the daemon’s `--userland-proxy=false` flag
* The `exec` command supports the `-u|--user` flag to specify the new process owner
+ Default gateway for containers can be specified daemon-wide using the `--default-gateway` and `--default-gateway-v6` flags
+ The CPU CFS (Completely Fair Scheduler) quota can be set in `docker run` using `--cpu-quota`
+ Container block IO can be controlled in `docker run` using`--blkio-weight`
+ ZFS support
+ The `docker logs` command supports a `--since` argument
+ UTS namespace can be shared with the host with `docker run --uts=host`

### Quality
* Networking stack was entirely rewritten as part of the libnetwork effort
* Engine internals refactoring
* Volumes code was entirely rewritten to support the plugins effort
+ Sending SIGUSR1 to a daemon will dump all goroutines stacks without exiting

### Build
+ Support ${variable:-value} and ${variable:+value} syntax for environment variables
+ Support resource management flags `--cgroup-parent`, `--cpu-period`, `--cpu-quota`, `--cpuset-cpus`, `--cpuset-mems`
+ git context changes with branches and directories
* The .dockerignore file support exclusion rules

### Distribution
+ Client support for v2 mirroring support for the official registry

### Bugfixes
* Firewalld is now supported and will automatically be used when available
* mounting --device recursively

## 1.6.2 (2015-05-13)

### Runtime
- Revert change prohibiting mounting into /sys

## 1.6.1 (2015-05-07)

### Security
- Fix read/write /proc paths (CVE-2015-3630)
- Prohibit VOLUME /proc and VOLUME / (CVE-2015-3631)
- Fix opening of file-descriptor 1 (CVE-2015-3627)
- Fix symlink traversal on container respawn allowing local privilege escalation (CVE-2015-3629)
- Prohibit mount of /sys

### Runtime
- Update AppArmor policy to not allow mounts

## 1.6.0 (2015-04-07)

### Builder
+ Building images from an image ID
+ Build containers with resource constraints, ie `docker build --cpu-shares=100 --memory=1024m...`
+ `commit --change` to apply specified Dockerfile instructions while committing the image
+ `import --change` to apply specified Dockerfile instructions while importing the image
+ Builds no longer continue in the background when canceled with CTRL-C

### Client
+ Windows Support

### Runtime
+ Container and image Labels
+ `--cgroup-parent` for specifying a parent cgroup to place container cgroup within
+ Logging drivers, `json-file`, `syslog`, or `none`
+ Pulling images by ID
+ `--ulimit` to set the ulimit on a container
+ `--default-ulimit` option on the daemon which applies to all created containers (and overwritten by `--ulimit` on run)

## 1.5.0 (2015-02-10)

### Builder
+ Dockerfile to use for a given `docker build` can be specified with the `-f` flag
* Dockerfile and .dockerignore files can be themselves excluded as part of the .dockerignore file, thus preventing modifications to these files invalidating ADD or COPY instructions cache
* ADD and COPY instructions accept relative paths
* Dockerfile `FROM scratch` instruction is now interpreted as a no-base specifier
* Improve performance when exposing a large number of ports

### Hack
+ Allow client-side only integration tests for Windows
* Include docker-py integration tests against Docker daemon as part of our test suites

### Packaging
+ Support for the new version of the registry HTTP API
* Speed up `docker push` for images with a majority of already existing layers
- Fixed contacting a private registry through a proxy

### Remote API
+ A new endpoint will stream live container resource metrics and can be accessed with the `docker stats` command
+ Containers can be renamed using the new `rename` endpoint and the associated `docker rename` command
* Container `inspect` endpoint show the ID of `exec` commands running in this container
* Container `inspect` endpoint show the number of times Docker auto-restarted the container
* New types of event can be streamed by the `events` endpoint: ‘OOM’ (container died with out of memory), ‘exec_create’, and ‘exec_start'
- Fixed returned string fields which hold numeric characters incorrectly omitting surrounding double quotes

### Runtime
+ Docker daemon has full IPv6 support
+ The `docker run` command can take the `--pid=host` flag to use the host PID namespace, which makes it possible for example to debug host processes using containerized debugging tools
+ The `docker run` command can take the `--read-only` flag to make the container’s root filesystem mounted as readonly, which can be used in combination with volumes to force a container’s processes to only write to locations that will be persisted
+ Container total memory usage can be limited for `docker run` using the `--memory-swap` flag
* Major stability improvements for devicemapper storage driver
* Better integration with host system: containers will reflect changes to the host's `/etc/resolv.conf` file when restarted
* Better integration with host system: per-container iptable rules are moved to the DOCKER chain
- Fixed container exiting on out of memory to return an invalid exit code

### Other
* The HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environment variables are properly taken into account by the client when connecting to the Docker daemon

## 1.4.1 (2014-12-15)

### Runtime
- Fix issue with volumes-from and bind mounts not being honored after create

## 1.4.0 (2014-12-11)

### Notable Features since 1.3.0
+ Set key=value labels to the daemon (displayed in `docker info`), applied with
  new `-label` daemon flag
+ Add support for `ENV` in Dockerfile of the form:
  `ENV name=value name2=value2...`
+ New Overlayfs Storage Driver
+ `docker info` now returns an `ID` and `Name` field
+ Filter events by event name, container, or image
+ `docker cp` now supports copying from container volumes
- Fixed `docker tag`, so it honors `--force` when overriding a tag for existing
  image.

## 1.3.3 (2014-12-11)

### Security
- Fix path traversal vulnerability in processing of absolute symbolic links (CVE-2014-9356)
- Fix decompression of xz image archives, preventing privilege escalation (CVE-2014-9357)
- Validate image IDs (CVE-2014-9358)

### Runtime
- Fix an issue when image archives are being read slowly

### Client
- Fix a regression related to stdin redirection
- Fix a regression with `docker cp` when destination is the current directory

## 1.3.2 (2014-11-20)

### Security
- Fix tar breakout vulnerability
* Extractions are now sandboxed chroot
- Security options are no longer committed to images

### Runtime
- Fix deadlock in `docker ps -f exited=1`
- Fix a bug when `--volumes-from` references a container that failed to start

### Registry
+ `--insecure-registry` now accepts CIDR notation such as 10.1.0.0/16
* Private registries whose IPs fall in the 127.0.0.0/8 range do no need the `--insecure-registry` flag
- Skip the experimental registry v2 API when mirroring is enabled

## 1.3.1 (2014-10-28)

### Security
* Prevent fallback to SSL protocols < TLS 1.0 for client, daemon and registry
+ Secure HTTPS connection to registries with certificate verification and without HTTP fallback unless `--insecure-registry` is specified

### Runtime
- Fix issue where volumes would not be shared

### Client
- Fix issue with `--iptables=false` not automatically setting `--ip-masq=false`
- Fix docker run output to non-TTY stdout

### Builder
- Fix escaping `$` for environment variables
- Fix issue with lowercase `onbuild` Dockerfile instruction
- Restrict environment variable expansion to `ENV`, `ADD`, `COPY`, `WORKDIR`, `EXPOSE`, `VOLUME` and `USER`

## 1.3.0 (2014-10-14)

### Notable features since 1.2.0
+ Docker `exec` allows you to run additional processes inside existing containers
+ Docker `create` gives you the ability to create a container via the CLI without executing a process
+ `--security-opts` options to allow user to customize container labels and apparmor profiles
+ Docker `ps` filters
- Wildcard support to COPY/ADD
+ Move production URLs to get.docker.com from get.docker.io
+ Allocate IP address on the bridge inside a valid CIDR
+ Use drone.io for PR and CI testing
+ Ability to setup an official registry mirror
+ Ability to save multiple images with docker `save`

## 1.2.0 (2014-08-20)

### Runtime
+ Make /etc/hosts /etc/resolv.conf and /etc/hostname editable at runtime
+ Auto-restart containers using policies
+ Use /var/lib/docker/tmp for large temporary files
+ `--cap-add` and `--cap-drop` to tweak what linux capability you want
+ `--device` to use devices in containers

### Client
+ `docker search` on private registries
+ Add `exited` filter to `docker ps --filter`
* `docker rm -f` now kills instead of stop
+ Support for IPv6 addresses in `--dns` flag

### Proxy
+ Proxy instances in separate processes
* Small bug fix on UDP proxy

## 1.1.2 (2014-07-23)

### Runtime
+ Fix port allocation for existing containers
+ Fix containers restart on daemon restart

### Packaging
+ Fix /etc/init.d/docker issue on Debian

## 1.1.1 (2014-07-09)

### Builder
* Fix issue with ADD

## 1.1.0 (2014-07-03)

### Notable features since 1.0.1
+ Add `.dockerignore` support
+ Pause containers during `docker commit`
+ Add `--tail` to `docker logs`

### Builder
+ Allow a tar file as context for `docker build`
* Fix issue with white-spaces and multi-lines in `Dockerfiles`

### Runtime
* Overall performance improvements
* Allow `/` as source of `docker run -v`
* Fix port allocation
* Fix bug in `docker save`
* Add links information to `docker inspect`

### Client
* Improve command line parsing for `docker commit`

### Remote API
* Improve status code for the `start` and `stop` endpoints

## 1.0.1 (2014-06-19)

### Notable features since 1.0.0
* Enhance security for the LXC driver

### Builder
* Fix `ONBUILD` instruction passed to grandchildren

### Runtime
* Fix events subscription
* Fix /etc/hostname file with host networking
* Allow `-h` and `--net=none`
* Fix issue with hotplug devices in `--privileged`

### Client
* Fix artifacts with events
* Fix a panic with empty flags
* Fix `docker cp` on Mac OS X

### Miscellaneous
* Fix compilation on Mac OS X
* Fix several races

## 1.0.0 (2014-06-09)

### Notable features since 0.12.0
* Production support

