---
title: Install client binaries on macOS
---

Before installing, read the shared [binary installation caveats](binary-installation.md).
For upgrades, follow [Upgrade static binaries](binary-installation.md#upgrade-static-binaries).

> [!NOTE]
>
> The following instructions are mostly suitable for testing purposes. The macOS
> binary includes the Docker client only. It does not include the `dockerd` daemon
> which is required to run containers. Therefore, we recommend that you install
> [Docker Desktop](/manuals/desktop/_index.md) instead.

The binaries for Mac also do not contain:

- A runtime environment. You must set up a functional engine either in a Virtual Machine, or on a remote Linux machine.
- Docker components such as `buildx` and `docker compose`.

To install client binaries, perform the following steps:

1.  Download the static binary archive. Go to
    [https://download.docker.com/mac/static/stable/](https://download.docker.com/mac/static/stable/) and select `x86_64` (for Mac on Intel chip) or `aarch64` (for Mac on Apple silicon),
    and then download the `.tgz` file relating to the version of Docker Engine you want
    to install.

2.  Extract the archive using the `tar` utility. The `docker` binary is
    extracted.

    ```console
    $ tar xzvf /path/to/<FILE>.tar.gz
    ```

3.  Clear the extended attributes to allow it run.

    ```console
    $ sudo xattr -rc docker
    ```

    Now, when you run the following command, you can see the Docker CLI usage instructions:

    ```console
    $ docker/docker
    ```

4.  **Optional**: Move the binary to a directory on your executable path, such
    as `/usr/local/bin/`. If you skip this step, you must provide the path to the
    executable when you invoke `docker` or `dockerd` commands.

    ```console
    $ sudo cp docker/docker /usr/local/bin/
    ```

5.  Verify that Docker is installed correctly by running the `hello-world`
    image. The value of `<hostname>` is a hostname or IP address running the
    Docker daemon and accessible to the client.

    ```console
    $ sudo docker -H <hostname> run hello-world
    ```

    This command downloads a test image and runs it in a container. When the
    container runs, it prints a message and exits.
