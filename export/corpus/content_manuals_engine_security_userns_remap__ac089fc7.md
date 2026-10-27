---
description: Isolate containers within a user namespace
keywords: security, namespaces
title: Isolate containers with a user namespace
---

Linux namespaces provide isolation for running processes, limiting their access
to system resources without the running process being aware of the limitations.
For more information on Linux namespaces, see
[Linux namespaces](https://www.linux.com/news/understanding-and-securing-linux-namespaces).

The best way to prevent privilege-escalation attacks from within a container is
to configure your container's applications to run as unprivileged users. For
containers whose processes must run as the `root` user within the container, you
can re-map this user to a less-privileged user on the Docker host. The mapped
user is assigned a range of UIDs which function within the namespace as normal
UIDs from 0 to 65536, but have no privileges on the host machine itself.

> [!NOTE]
>
> With `userns-remap`, the Docker daemon still runs as root. To run both the
> daemon and containers without root privileges, see [Rootless mode](rootless/_index.md)
> instead.

## About remapping and subordinate user and group IDs

See [User namespace mappings](userns-context.md#about-remapping-and-subordinate-user-and-group-ids).

For isolation context, see [Container isolation and kernel security](kernel-security.md).

## Prerequisites

Read [User namespace prerequisites](userns-context.md#prerequisites) before enabling remapping.

## Enable userns-remap on the daemon

You can start `dockerd` with the `--userns-remap` flag or follow this
procedure to configure the daemon using the `daemon.json` configuration file.
The `daemon.json` method is recommended. If you use the flag, use the following
command as a model:

```console
$ dockerd --userns-remap="testuser:testuser"
```

1.  Edit `/etc/docker/daemon.json`. Assuming the file was previously empty, the
    following entry enables `userns-remap` using user and group called
    `testuser`. You can address the user and group by ID or name. You only need to
    specify the group name or ID if it is different from the user name or ID. If
    you provide both the user and group name or ID, separate them by a colon
    (`:`) character. The following formats all work for the value, assuming
    the UID and GID of `testuser` are `1001`:

    - `testuser`
    - `testuser:testuser`
    - `1001`
    - `1001:1001`
    - `testuser:1001`
    - `1001:testuser`

    ```json
    {
      "userns-remap": "testuser"
    }
    ```

    > [!NOTE]
    >
    > To use the `dockremap` user and have Docker create it for you,
    > set the value to `default` rather than `testuser`.

    Save the file and restart Docker.

2.  If you are using the `dockremap` user, verify that Docker created it using
    the `id` command.

    ```console
    $ id dockremap

    uid=112(dockremap) gid=116(dockremap) groups=116(dockremap)
    ```

    Verify that the entry has been added to `/etc/subuid` and `/etc/subgid`:

    ```console
    $ grep dockremap /etc/subuid

    dockremap:231072:65536

    $ grep dockremap /etc/subgid

    dockremap:231072:65536
    ```

    If these entries are not present, edit the files as the `root` user and
    assign a starting UID and GID that is the highest-assigned one plus the
    offset (in this case, `65536`). Be careful not to allow any overlap in the
    ranges.

3.  Verify that previous images are not available using the `docker image ls`
    command. The output should be empty.

4.  Start a container from the `hello-world` image.

    ```console
    $ docker run hello-world
    ```

5.  Verify that a namespaced directory exists within `/var/lib/docker/` named
    with the UID and GID of the namespaced user, owned by that UID and GID,
    and not group-or-world-readable. Some of the subdirectories are still
    owned by `root` and have different permissions.

    ```console
    $ sudo ls -ld /var/lib/docker/231072.231072/

    drwx------ 11 231072 231072 11 Jun 21 21:19 /var/lib/docker/231072.231072/

    $ sudo ls -l /var/lib/docker/231072.231072/

    total 14
    drwx------ 5 231072 231072 5 Jun 21 21:19 aufs
    drwx------ 3 231072 231072 3 Jun 21 21:21 containers
    drwx------ 3 root   root   3 Jun 21 21:19 image
    drwxr-x--- 3 root   root   3 Jun 21 21:19 network
    drwx------ 4 root   root   4 Jun 21 21:19 plugins
    drwx------ 2 root   root   2 Jun 21 21:19 swarm
    drwx------ 2 231072 231072 2 Jun 21 21:21 tmp
    drwx------ 2 root   root   2 Jun 21 21:19 trust
    drwx------ 2 231072 231072 3 Jun 21 21:19 volumes
    ```

    Your directory listing may have some differences, especially if you
    use a different container storage driver than `aufs`.

    The directories which are owned by the remapped user are used instead
    of the same directories directly beneath `/var/lib/docker/` and the
    unused versions (such as `/var/lib/docker/tmp/` in the example here)
    can be removed. Docker does not use them while `userns-remap` is
    enabled.

## Disable namespace remapping for a container

If you enable user namespaces on the daemon, all containers are started with
user namespaces enabled by default. In some situations, such as privileged
containers, you may need to disable user namespaces for a specific container.
See
[user namespace known limitations](#user-namespace-known-limitations)
for some of these limitations.

To disable user namespaces for a specific container, add the `--userns=host`
flag to the `docker container create`, `docker container run`, or `docker container exec` command.

There is a side effect when using this flag: user remapping will not be enabled for that container but, because the read-only (image) layers are shared between containers, ownership of the containers filesystem will still be remapped.

What this means is that the whole container filesystem will belong to the user specified in the `--userns-remap` daemon config (`231072` in the example above). This can lead to unexpected behavior of programs inside the container. For instance `sudo` (which checks that its binaries belong to user `0`) or binaries with a `setuid` flag.

## User namespace known limitations

See [User namespace limitations](userns-context.md#user-namespace-known-limitations).
