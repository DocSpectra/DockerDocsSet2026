---
title: AppArmor policies and profile management
---

See [Container isolation and kernel security](kernel-security.md) for isolation context.


AppArmor (Application Armor) is a Linux security module that protects an
operating system and its applications from security threats. To use it, a system
administrator associates an AppArmor security profile with each program. Docker
expects to find an AppArmor policy loaded and enforced.

Docker automatically generates and loads a default profile for containers named
`docker-default`. The Docker binary generates this profile in `tmpfs` and then
loads it into the kernel.

> [!NOTE]
>
> This profile is used on containers, not on the Docker daemon.

A profile for the Docker Engine daemon exists but it is not currently installed
with the `deb` packages. If you are interested in the source for the daemon
profile, it is located in
[contrib/apparmor](https://github.com/moby/moby/tree/master/contrib/apparmor)
in the Docker Engine source repository.

## Understand the policies

The `docker-default` profile is the default for running containers. It is
moderately protective while providing wide application compatibility. The
profile is generated from the following
[template](https://github.com/moby/profiles/blob/main/apparmor/template.go).

When you run a container, it uses the `docker-default` policy unless you
override it with the `security-opt` option. For example, the following
explicitly specifies the default policy:

```console
$ docker run --rm -it --security-opt apparmor=docker-default hello-world
```

## Load and unload profiles

To load a new profile into AppArmor for use with containers:

```console
$ apparmor_parser -r -W /path/to/your_profile
```

Then, run the custom profile with `--security-opt`:

```console
$ docker run --rm -it --security-opt apparmor=your_profile hello-world
```

To unload a profile from AppArmor:

```console
# unload the profile
$ apparmor_parser -R /path/to/profile
```

### Resources for writing profiles

The syntax for file globbing in AppArmor is a bit different than some other
globbing implementations. It is highly suggested you take a look at some of the
below resources with regard to AppArmor profile syntax.

- [Quick Profile Language](https://gitlab.com/apparmor/apparmor/wikis/QuickProfileLanguage)
- [Globbing Syntax](https://gitlab.com/apparmor/apparmor/wikis/AppArmor_Core_Policy_Reference#AppArmor_globbing_syntax)

## Contribute to Docker's AppArmor code

Advanced users and package managers can find a profile for `/usr/bin/docker`
(Docker Engine daemon) underneath
[contrib/apparmor](https://github.com/moby/moby/tree/master/contrib/apparmor)
in the Docker Engine source repository.

The `docker-default` profile for containers lives in
[profiles/apparmor](https://github.com/moby/profiles/blob/main/apparmor).
