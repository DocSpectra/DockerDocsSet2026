---
description: Enabling seccomp in Docker
keywords: seccomp, security, docker, documentation
title: Seccomp security profiles for Docker
---

Secure computing mode (`seccomp`) is a Linux kernel feature. You can use it to
restrict the actions available within the container. The `seccomp()` system
call operates on the seccomp state of the calling process. You can use this
feature to restrict your application's access.

This feature is available only if Docker has been built with `seccomp` and the
kernel is configured with `CONFIG_SECCOMP` enabled. To check if your kernel
supports `seccomp`:

```console
$ grep CONFIG_SECCOMP= /boot/config-$(uname -r)
CONFIG_SECCOMP=y
```

For isolation context, see [Container isolation and kernel security](kernel-security.md).

## Pass a profile for a container

The [default `seccomp` profile](https://github.com/moby/profiles/blob/main/seccomp/default.json)
provides a sane default for running containers with seccomp and disables around
44 system calls out of 300+. It is moderately protective while providing wide
application compatibility.

In effect, the profile is an allowlist that denies access to system calls by
default and then allows specific system calls. The profile works by defining a
`defaultAction` of `SCMP_ACT_ERRNO` and overriding that action only for specific
system calls. The effect of `SCMP_ACT_ERRNO` is to cause a `Permission Denied`
error. Next, the profile defines a specific list of system calls which are fully
allowed, because their `action` is overridden to be `SCMP_ACT_ALLOW`. Finally,
some specific rules are for individual system calls such as `personality`, and others,
to allow variants of those system calls with specific arguments.

`seccomp` is instrumental for running Docker containers with least privilege. It
is not recommended to change the default `seccomp` profile.

When you run a container, it uses the default profile unless you override it
with the `--security-opt` option. For example, the following explicitly
specifies a policy:

```console
$ docker run --rm \
             -it \
             --security-opt seccomp=/path/to/seccomp/profile.json \
             hello-world
```

### Significant syscalls blocked by the default profile

See [System calls blocked by the default seccomp profile](seccomp-syscalls.md).

## Run without the default seccomp profile

You can pass `unconfined` to run a container without the default seccomp
profile.

```console
$ docker run --rm -it --security-opt seccomp=unconfined debian:latest \
    unshare --map-root-user --user sh -c whoami
```
