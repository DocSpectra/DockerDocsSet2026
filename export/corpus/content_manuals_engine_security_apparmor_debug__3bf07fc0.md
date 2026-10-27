---
title: Debug AppArmor profiles
---

See [AppArmor policies and profile management](apparmor-profiles.md) for default policies and loading profiles.

## Debug AppArmor

You can use `dmesg` to debug problems and `aa-status` check the loaded profiles.

### Use dmesg

Here are some helpful tips for debugging any problems you might be facing with
regard to AppArmor.

AppArmor sends quite verbose messaging to `dmesg`. Usually an AppArmor line
looks like the following:

```text
[ 5442.864673] audit: type=1400 audit(1453830992.845:37): apparmor="ALLOWED" operation="open" profile="/usr/bin/docker" name="/home/jessie/docker/man/man1/docker-attach.1" pid=10923 comm="docker" requested_mask="r" denied_mask="r" fsuid=1000 ouid=0
```

In the above example, you can see `profile=/usr/bin/docker`. This means the
user has the `docker-engine` (Docker Engine daemon) profile loaded.

Look at another log line:

```text
[ 3256.689120] type=1400 audit(1405454041.341:73): apparmor="DENIED" operation="ptrace" profile="docker-default" pid=17651 comm="docker" requested_mask="receive" denied_mask="receive"
```

This time the profile is `docker-default`, which is run on containers by
default unless in `privileged` mode. This line shows that apparmor has denied
`ptrace` in the container. This is exactly as expected.

### Use aa-status

If you need to check which profiles are loaded,  you can use `aa-status`. The
output looks like:

```console
$ sudo aa-status
apparmor module is loaded.
14 profiles are loaded.
1 profiles are in enforce mode.
   docker-default
13 profiles are in complain mode.
   /usr/bin/docker
   /usr/bin/docker///bin/cat
   /usr/bin/docker///bin/ps
   /usr/bin/docker///sbin/apparmor_parser
   /usr/bin/docker///sbin/auplink
   /usr/bin/docker///sbin/blkid
   /usr/bin/docker///sbin/iptables
   /usr/bin/docker///sbin/mke2fs
   /usr/bin/docker///sbin/modprobe
   /usr/bin/docker///sbin/tune2fs
   /usr/bin/docker///sbin/xtables-multi
   /usr/bin/docker///sbin/zfs
   /usr/bin/docker///usr/bin/xz
38 processes have profiles defined.
37 processes are in enforce mode.
   docker-default (6044)
   ...
   docker-default (31899)
1 processes are in complain mode.
   /usr/bin/docker (29756)
0 processes are unconfined but have a profile defined.
```

The above output shows that the `docker-default` profile running on various
container PIDs is in `enforce` mode. This means AppArmor is actively blocking
and auditing in `dmesg` anything outside the bounds of the `docker-default`
profile.

The output above also shows the `/usr/bin/docker` (Docker Engine daemon) profile
is running in `complain` mode. This means AppArmor only logs to `dmesg`
activity outside the bounds of the profile. (Except in the case of Ubuntu
Trusty, where some interesting behaviors are enforced.)
