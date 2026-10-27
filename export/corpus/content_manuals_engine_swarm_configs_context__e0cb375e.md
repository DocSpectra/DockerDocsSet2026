---
title: Docker config lifecycle and platform support
---

## About configs

Docker swarm service configs  allow you to store non-sensitive information,
such as configuration files, outside a service's image or running containers.
This allows you to keep your images as generic as possible, without the need to
bind-mount configuration files into the containers or use environment variables.

Configs operate in a similar way to secrets, except that they are
not encrypted at rest and are mounted directly into the container's filesystem
without the use of RAM disks. Configs can be added or removed from a service at
any time, and services can share a config. You can even use configs in
conjunction with environment variables or labels, for maximum flexibility.
Config values can be generic strings or binary content (up to 500 kb in size).

> [!NOTE]
>
> Docker configs are only available to swarm services, not to
> standalone containers. To use this feature, consider adapting your container
> to run as a service with a scale of 1.

Configs are supported on both Linux and Windows services.

### Windows support

Docker includes support for configs on Windows containers, but there are differences
in the implementations, which are called out in the examples below. Keep the
following notable differences in mind:

- Config files with custom targets are not directly bind-mounted into Windows
  containers, since Windows does not support non-directory file bind-mounts.
  Instead, configs for a container are all mounted in
  `C:\ProgramData\Docker\internal\configs` (an implementation detail which
  should not be relied upon by applications) within the container. Symbolic
  links are used to point from there to the desired target of the config within
  the container. The default target is `C:\ProgramData\Docker\configs`.

- When creating a service which uses Windows containers, the options to specify
  UID, GID, and mode are not supported for configs. Configs are currently only
  accessible by administrators and users with `system` access within the
  container.

- On Windows, create or update a service using `--credential-spec` with the
  `config://<config-name>` format.  This passes the gMSA credentials file
  directly to nodes before a container starts. No gMSA credentials are written
  to disk on worker nodes.

## How Docker manages configs

When you add a config to the swarm, Docker sends the config to the swarm manager
over a mutual TLS connection. The config is stored in the Raft log, which is
encrypted. The entire Raft log is replicated across the other managers, ensuring
the same high availability guarantees for configs as for the rest of the swarm
management data.

When you grant a newly-created or running service access to a config, the config
is mounted as a file in the container. The location of the mount point within
the container defaults to `/<config-name>` in Linux containers. In Windows
containers, configs are all mounted into `C:\ProgramData\Docker\configs` and
symbolic links are created to the desired location, which defaults to
`C:\<config-name>`.

You can set the ownership (`uid` and `gid`) for the config, using either the
numerical ID or the name of the user or group. You can also specify the file
permissions (`mode`). These settings are ignored for Windows containers.

- If not set, the config is owned by the user running the container
  command (often `root`) and that user's default group (also often `root`).
- If not set, the config has world-readable permissions (mode `0444`), unless a
  `umask` is set within the container, in which case the mode is impacted by
  that `umask` value.

You can update a service to grant it access to additional configs or revoke its
access to a given config at any time.

A node only has access to configs if the node is a swarm manager or if it is
running service tasks which have been granted access to the config. When a
container task stops running, the configs shared to it are unmounted from the
in-memory filesystem for that container and flushed from the node's memory.

If a node loses connectivity to the swarm while it is running a task container
with access to a config, the task container still has access to its configs, but
cannot receive updates until the node reconnects to the swarm.

You can add or inspect an individual config at any time, or list all
configs. You cannot remove a config that a running service is
using. 

To update or roll back configs more easily, consider adding a version
number or date to the config name. This is made easier by the ability to control
the mount point of the config within a given container.

To update a stack, make changes to your Compose file, then re-run `docker
stack deploy -c <new-compose-file> <stack-name>`. If you use a new config in
that file, your services start using them. Keep in mind that configurations
are immutable, so you can't change the file for an existing service.
Instead, you create a new config to use a different file

You can run `docker stack rm` to stop the app and take down the stack. This
removes any config that was created by `docker stack deploy` with the same stack
name. This removes _all_ configs, including those not referenced by services and
those remaining after a `docker service update --config-rm`.

## Example scope

> [!NOTE]
>
> These examples use a single-engine swarm and unscaled services for
> simplicity. The examples use Linux containers, but Windows containers also
> support configs.
