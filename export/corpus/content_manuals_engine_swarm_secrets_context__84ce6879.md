---
title: Docker secret lifecycle and platform support
---

## About secrets

In terms of Docker Swarm services, a _secret_ is a blob of data, such as a
password, SSH private key, SSL certificate, or another piece of data that should
not be transmitted over a network or stored unencrypted in a Dockerfile or in
your application's source code. You can use Docker _secrets_ to centrally manage
this data and securely transmit it to only those containers that need access to
it. Secrets are encrypted during transit and at rest in a Docker swarm. A given
secret is only accessible to those services which have been granted explicit
access to it, and only while those service tasks are running.

You can use secrets to manage any sensitive data which a container needs at
runtime but you don't want to store in the image or in source control, such as:

- Usernames and passwords
- TLS certificates and keys
- SSH keys
- Other important data such as the name of a database or internal server
- Generic strings or binary content (up to 500 kb in size)

> [!NOTE]
>
> Docker secrets are only available to swarm services, not to
> standalone containers. To use this feature, consider adapting your container
> to run as a service. Stateful containers can typically run with a scale of 1
> without changing the container code.

Another use case for using secrets is to provide a layer of abstraction between
the container and a set of credentials. Consider a scenario where you have
separate development, test, and production environments for your application.
Each of these environments can have different credentials, stored in the
development, test, and production swarms with the same secret name. Your
containers only need to know the name of the secret to function in all
three environments.

You can also use secrets to manage non-sensitive data, such as configuration
files. However, Docker supports the use of [configs](configs-context.md)
for storing non-sensitive data. Configs are mounted into the container's
filesystem directly, without the use of a RAM disk.

### Windows support

Docker includes support for secrets on Windows containers. Where there are
differences in the implementations, they are called out in the
examples below. Keep the following notable differences in mind:

- Microsoft Windows has no built-in driver for managing RAM disks, so within
  running Windows containers, secrets are persisted in clear text to the
  container's root disk. However, the secrets are explicitly removed when a
  container stops. In addition, Windows does not support persisting a running
  container as an image using `docker commit` or similar commands.

- On Windows, we recommend enabling
  [BitLocker](https://technet.microsoft.com/en-us/library/cc732774(v=ws.11).aspx)
  on the volume containing the Docker root directory on the host machine to
  ensure that secrets for running containers are encrypted at rest.

- Secret files with custom targets are not directly bind-mounted into Windows
  containers, since Windows does not support non-directory file bind-mounts.
  Instead, secrets for a container are all mounted in
  `C:\ProgramData\Docker\internal\secrets` (an implementation detail which
  should not be relied upon by applications) within the container. Symbolic
  links are used to point from there to the desired target of the secret within
  the container. The default target is `C:\ProgramData\Docker\secrets`.

- When creating a service which uses Windows containers, the options to specify
  UID, GID, and mode are not supported for secrets. Secrets are currently only
  accessible by administrators and users with `system` access within the
  container.

## How Docker manages secrets

When you add a secret to the swarm, Docker sends the secret to the swarm manager
over a mutual TLS connection. The secret is stored in the Raft log, which is
encrypted. The entire Raft log is replicated across the other managers, ensuring
the same high availability guarantees for secrets as for the rest of the swarm
management data.

When you grant a newly-created or running service access to a secret, the
decrypted secret is mounted into the container in an in-memory filesystem. The
location of the mount point within the container defaults to
`/run/secrets/<secret_name>` in Linux containers, or
`C:\ProgramData\Docker\secrets` in Windows containers. You can also specify a
custom location.

You can update a service to grant it access to additional secrets or revoke its
access to a given secret at any time.

A node only has access to (encrypted) secrets if the node is a swarm manager or
if it is running service tasks which have been granted access to the secret.
When a container task stops running, the decrypted secrets shared to it are
unmounted from the in-memory filesystem for that container and flushed from the
node's memory.

If a node loses connectivity to the swarm while it is running a task container
with access to a secret, the task container still has access to its secrets, but
cannot receive updates until the node reconnects to the swarm.

You can add or inspect an individual secret at any time, or list all
secrets. You cannot remove a secret that a running service is
using. 

To update or roll back secrets more easily, consider adding a version
number or date to the secret name. This is made easier by the ability to control
the mount point of the secret within a given container.

## Example scope

> [!NOTE]
>
> These examples use a single-Engine swarm and unscaled services for
> simplicity. The examples use Linux containers, but Windows containers also
> support secrets. See [Windows support](#windows-support).
