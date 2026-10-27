---
title: Connect to the Docker daemon with SSH
---

See [Docker daemon attack surface](daemon-security.md) for access context.

## Use SSH to protect the Docker daemon socket

> [!NOTE]
>
> The given `USERNAME` must have permissions to access the docker socket on the
> remote machine. Refer to [manage Docker as a non-root user](../install/linux-postinstall.md#manage-docker-as-a-non-root-user)
> to learn how to give a non-root user access to the docker socket.

The following example creates a [`docker context`](/manuals/engine/manage-resources/contexts.md)
to connect with a remote `dockerd` daemon on `host1.example.com` using SSH, and
as the `docker-user` user on the remote machine:

```console
$ docker context create \
    --docker host=ssh://docker-user@host1.example.com \
    --description="Remote engine" \
    my-remote-engine

my-remote-engine
Successfully created context "my-remote-engine"
```

After creating the context, use `docker context use` to switch the `docker` CLI
to use it, and to connect to the remote engine:

```console
$ docker context use my-remote-engine
my-remote-engine
Current context is now "my-remote-engine"

$ docker info
<prints output of the remote engine>
```

Use the `default` context to switch back to the default (local) daemon:

```console
$ docker context use default
default
Current context is now "default"
```

Alternatively, use the `DOCKER_HOST` environment variable to temporarily switch
the `docker` CLI to connect to the remote host using SSH. This does not require
creating a context, and can be useful to create an ad-hoc connection with a different
engine:

```console
$ export DOCKER_HOST=ssh://docker-user@host1.example.com
$ docker info
<prints output of the remote engine>
```

### SSH Tips

For the best user experience with SSH, configure `~/.ssh/config` as follows to allow
reusing a SSH connection for multiple invocations of the `docker` CLI:

```text
ControlMaster     auto
ControlPath       ~/.ssh/control-%C
ControlPersist    yes
```
