---
title: Install daemon and client binaries on Linux
---

Before installing, read the shared [binary installation caveats](binary-installation.md).
For upgrades, follow [Upgrade static binaries](binary-installation.md#upgrade-static-binaries).

## Prerequisites {#prerequisites}

Before attempting to install Docker from binaries, be sure your host machine
meets the prerequisites:

- A 64-bit installation
- Version 3.10 or higher of the Linux kernel. The latest version of the kernel
  available for your platform is recommended.
- `iptables` version 1.4 or higher
- `git` version 1.7 or higher
- A `ps` executable, usually provided by `procps` or a similar package.
- [XZ Utils](https://tukaani.org/xz/) 4.9 or higher
- A [properly mounted](
  https://github.com/tianon/cgroupfs-mount/blob/master/cgroupfs-mount)
  `cgroupfs` hierarchy; a single, all-encompassing `cgroup` mount
  point is not sufficient. See Github issues
  [#2683](https://github.com/moby/moby/issues/2683),
  [#3485](https://github.com/moby/moby/issues/3485),
  [#4568](https://github.com/moby/moby/issues/4568)).

### Secure your environment as much as possible {#secure-your-environment-as-much-as-possible}

#### OS considerations {#os-considerations}

Enable SELinux or AppArmor if possible.

It is recommended to use AppArmor or SELinux if your Linux distribution supports
either of the two. This helps improve security and blocks certain
types of exploits. Review the documentation for your Linux distribution for
instructions for enabling and configuring AppArmor or SELinux.

> **Security warning**
>
> If either of the security mechanisms is enabled, do not disable it as a
> work-around to make Docker or its containers run. Instead, configure it
> correctly to fix any problems.

#### Docker daemon considerations {#docker-daemon-considerations}

- Enable `seccomp` security profiles if possible. See
  [Enabling `seccomp` for Docker](../security/seccomp.md).

- Enable user namespaces if possible. See the
  [Daemon user namespace options](/reference/cli/dockerd/#daemon-user-namespace-options).

## Install static binaries {#install-static-binaries}

1.  Download the static binary archive. Go to
    [https://download.docker.com/linux/static/stable/](https://download.docker.com/linux/static/stable/),
    choose your hardware platform, and download the `.tgz` file relating to the
    version of Docker Engine you want to install.

2.  Extract the archive using the `tar` utility. The `dockerd` and `docker`
    binaries are extracted.

    ```console
    $ tar xzvf /path/to/<FILE>.tar.gz
    ```

3.  **Optional**: Move the binaries to a directory on your executable path, such
    as `/usr/bin/`. If you skip this step, you must provide the path to the
    executable when you invoke `docker` or `dockerd` commands.

    ```console
    $ sudo cp docker/* /usr/bin/
    ```

4.  Start the Docker daemon:

    ```console
    $ sudo dockerd &
    ```

    If you need to start the daemon with additional options, modify the above
    command accordingly or create and edit the file `/etc/docker/daemon.json`
    to add the custom configuration options.

5.  Verify that Docker is installed correctly by running the `hello-world`
    image.

    ```console
    $ sudo docker run hello-world
    ```

    This command downloads a test image and runs it in a container. When the
    container runs, it prints a message and exits.

You have now successfully installed and started Docker Engine.

{{% include "root-errors.md" %}}
