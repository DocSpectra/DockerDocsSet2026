---
title: User namespace mappings and limitations
---

## About remapping and subordinate user and group IDs

The remapping itself is handled by two files: `/etc/subuid` and `/etc/subgid`.
Each file works the same, but one is concerned with the user ID range, and the
other with the group ID range. Consider the following entry in `/etc/subuid`:

```text
testuser:231072:65536
```

This means that `testuser` is assigned a subordinate user ID range of `231072`
and the next 65536 integers in sequence. UID `231072` is mapped within the
namespace (within the container, in this case) as UID `0` (`root`). UID `231073`
is mapped as UID `1`, and so forth. If a process attempts to escalate privilege
outside of the namespace, the process is running as an unprivileged high-number
UID on the host, which does not even map to a real user. This means the process
has no privileges on the host system at all.

> [!NOTE]
>
> It is possible to assign multiple subordinate ranges for a given user or group
> by adding multiple non-overlapping mappings for the same user or group in the
> `/etc/subuid` or `/etc/subgid` file. In this case, Docker uses only the first
> five mappings, in accordance with the kernel's limitation of only five entries
> in `/proc/self/uid_map` and `/proc/self/gid_map`.

When you configure Docker to use the `userns-remap` feature, you can optionally
specify an existing user and/or group, or you can specify `default`. If you
specify `default`, a user and group `dockremap` is created and used for this
purpose.

> [!WARNING]
>
> Some distributions do not automatically add the new group to the
> `/etc/subuid` and `/etc/subgid` files. If that's the case, you may have
> to manually edit these files and assign non-overlapping ranges. This step is
> covered in [Prerequisites](#prerequisites).

It is very important that the ranges do not overlap, so that a process cannot gain
access in a different namespace. On most Linux distributions, system utilities
manage the ranges for you when you add or remove users.

This re-mapping is transparent to the container, but introduces some
configuration complexity in situations where the container needs access to
resources on the Docker host, such as bind mounts into areas of the filesystem
that the system user cannot write to. From a security standpoint, it is best to
avoid these situations.

## Prerequisites

1.  The subordinate UID and GID ranges must be associated with an existing user,
    even though the association is an implementation detail. The user owns
    the namespaced storage directories under `/var/lib/docker/`. If you don't
    want to use an existing user, Docker can create one for you and use that. If
    you want to use an existing username or user ID, it must already exist.
    Typically, this means that the relevant entries need to be in
    `/etc/passwd` and `/etc/group`, but if you are using a different
    authentication back-end, this requirement may translate differently.

    To verify this, use the `id` command:

    ```console
    $ id testuser

    uid=1001(testuser) gid=1001(testuser) groups=1001(testuser)
    ```

2.  The way the namespace remapping is handled on the host is using two files,
    `/etc/subuid` and `/etc/subgid`. These files are typically managed
    automatically when you add or remove users or groups, but on some
    distributions, you may need to manage these files manually.

    Each file contains three fields: the username or ID of the user, followed by
    a beginning UID or GID (which is treated as UID or GID 0 within the namespace)
    and a maximum number of UIDs or GIDs available to the user. For instance,
    given the following entry:

    ```text
    testuser:231072:65536
    ```

    This means that user-namespaced processes started by `testuser` are
    owned by host UID `231072` (which looks like UID `0` inside the
    namespace) through 296607 (231072 + 65536 - 1). These ranges should not overlap,
    to ensure that namespaced processes cannot access each other's namespaces.

    After adding your user, check `/etc/subuid` and `/etc/subgid` to see if your
    user has an entry in each. If not, you need to add it, being careful to
    avoid overlap.

    If you want to use the `dockremap` user automatically created by Docker,
    check for the `dockremap` entry in these files after
    configuring and restarting Docker.

3.  If there are any locations on the Docker host where the unprivileged
    user needs to write, adjust the permissions of those locations
    accordingly. This is also true if you want to use the `dockremap` user
    automatically created by Docker, but you can't modify the
    permissions until after configuring and restarting Docker.

4.  Enabling `userns-remap` effectively masks existing image and container
    layers, as well as other Docker objects within `/var/lib/docker/`. This is
    because Docker needs to adjust the ownership of these resources and actually
    stores them in a subdirectory within `/var/lib/docker/`. It is best to enable
    this feature on a new Docker installation rather than an existing one.

    Along the same lines, if you disable `userns-remap` you can't access any
    of the resources created while it was enabled.

5.  Check the [limitations](#user-namespace-known-limitations) on user
    namespaces to be sure your use case is possible.

## User namespace known limitations

The following standard Docker features are incompatible with running a Docker
daemon with user namespaces enabled:

- Sharing PID or NET namespaces with the host (`--pid=host` or `--network=host`).
- External (volume or storage) drivers which are unaware or incapable of using
  daemon user mappings.
- Using the `--privileged` mode flag on `docker run` without also specifying
  `--userns=host`.

User namespaces are an advanced feature and require coordination with other
capabilities. For example, if volumes are mounted from the host, file ownership
must be pre-arranged if you need read or write access to the volume contents.

While the root user inside a user-namespaced container process has many of the
expected privileges of the superuser within the container, the Linux kernel
imposes restrictions based on internal knowledge that this is a user-namespaced
process. One notable restriction is the inability to use the `mknod` command.
Permission is denied for device creation within the container when run by
the `root` user.
