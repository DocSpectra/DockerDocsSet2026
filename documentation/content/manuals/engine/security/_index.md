---
description: Review of the Docker Daemon attack surface
keywords: Docker, Docker documentation, security
title: Docker Engine security
linkTitle: Security
weight: 80
aliases:
- /articles/security/
- /engine/articles/security/
- /engine/security/security/
- /security/security/
---

There are four major areas to consider when reviewing Docker security:

 - The intrinsic security of the kernel and its support for
   namespaces and cgroups
 - The attack surface of the Docker daemon itself
 - Loopholes in the container configuration profile, either by default,
   or when customized by users.
 - The "hardening" security features of the kernel and how they
   interact with containers.

## Kernel namespaces

See [Kernel namespaces](kernel-security.md#kernel-namespaces).

## Control groups

See [Control groups](kernel-security.md#control-groups).

## Docker daemon attack surface

See [Docker daemon attack surface](daemon-security.md#docker-daemon-attack-surface).

## Linux kernel capabilities

See [Linux kernel capabilities](kernel-security.md#linux-kernel-capabilities).

## Docker Content Trust signature verification

Docker Engine can be configured to only run signed images. The Docker Content 
Trust signature verification feature is built directly into the `dockerd` binary.  
This is configured in the Dockerd configuration file. 

To enable this feature, trustpinning can be configured in `daemon.json`, whereby 
only repositories signed with a user-specified root key can be pulled and run.
  
This feature provides more insight to administrators than previously available with
the CLI for enforcing and performing image signature verification. 

For more information on configuring Docker Content Trust Signature Verification, go to 
[Content trust in Docker](trust/_index.md).

## Other kernel security features

See [Other kernel security features](kernel-security.md#other-kernel-security-features).

## Conclusions

Docker containers are, by default, quite secure; especially if you
run your processes as non-privileged users inside the container.

You can add an extra layer of safety by enabling AppArmor, SELinux,
GRSEC, or another appropriate hardening system.

If you think of ways to make docker more secure, we welcome feature requests,
pull requests, or comments on the Docker community forums.

## Related information

* [Use trusted images](trust/_index.md)
* [Seccomp security profiles for Docker](seccomp.md)
* [AppArmor security profiles for Docker](apparmor.md)
* [On the Security of Containers (2014)](https://medium.com/@ewindisch/on-the-security-of-containers-2c60ffe25a9e)
* [Docker swarm mode overlay network security model](/manuals/engine/network/drivers/overlay.md)
