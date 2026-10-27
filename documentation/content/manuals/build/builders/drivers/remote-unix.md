---
title: Connect Buildx to BuildKit over a Unix socket
---

For shared options and behavior, see [remote driver reference](remote-reference.md).
For shared procedures, see [Select a builder](../selection.md) and
[Load build results](../image-loading.md).

## Example: Remote BuildKit over Unix sockets

This guide shows you how to create a setup with a BuildKit daemon listening on a
Unix socket, and have Buildx connect through it.

1. Ensure that [BuildKit](https://github.com/moby/buildkit) is installed.

   For example, you can launch an instance of buildkitd with:

   ```console
   $ sudo ./buildkitd --group $(id -gn) --addr unix://$HOME/buildkitd.sock
   ```

   Alternatively, refer to the [Rootless Buildkit documentation](https://github.com/moby/buildkit/blob/master/docs/rootless.md)
   for running buildkitd in rootless mode, or [the BuildKit systemd examples](https://github.com/moby/buildkit/tree/master/examples/systemd)
   for running it as a systemd service.

2. Check that you have a Unix socket that you can connect to.

   ```console
   $ ls -lh /home/user/buildkitd.sock
   srw-rw---- 1 root user 0 May  5 11:04 /home/user/buildkitd.sock
   ```

3. Connect Buildx to it using the remote driver:

   ```console
   $ docker buildx create \
     --name remote-unix \
     --driver remote \
     unix://$HOME/buildkitd.sock
   ```

4. List available builders with `docker buildx ls`. You should then see
   `remote-unix` among them:

   ```console
   $ docker buildx ls
   NAME/NODE           DRIVER/ENDPOINT                        STATUS  PLATFORMS
   remote-unix         remote
     remote-unix0      unix:///home/.../buildkitd.sock        running linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/386
   default *           docker
     default           default                                running linux/amd64, linux/386
   ```

You can switch to this new builder as the default using
`docker buildx use remote-unix`, or specify it per build using `--builder`:

```console
$ docker buildx build --builder=remote-unix -t test --load .
```

Remember that you need to use the `--load` flag if you want to load the build
result into the Docker daemon.


