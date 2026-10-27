---
title: Docker container driver options and behavior
---



The Docker container driver allows creation of a managed and customizable
BuildKit environment in a dedicated Docker container.

Using the Docker container driver has a couple of advantages over the default
Docker driver. For example:

- Specify custom BuildKit versions to use.
- Build multi-arch images, see [QEMU](container-qemu.md#qemu)
- Advanced options for [cache import and export](/manuals/build/cache/backends/_index.md)

## Synopsis

Run the following command to create a new builder, named `container`, that uses
the Docker container driver:

```console
$ docker buildx create \
  --name container \
  --driver=docker-container \
  --driver-opt=[key=value,...]
container
```

The following table describes the available driver-specific options that you can
pass to `--driver-opt`:

| Parameter        | Type    | Default          | Description                                                                                                            |
| ---------------- | ------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `image`          | String  |                  | Sets the BuildKit image to use for the container.                                                                      |
| `memory`         | String  |                  | Sets the amount of memory the container can use.                                                                       |
| `memory-swap`    | String  |                  | Sets the memory swap limit for the container.                                                                          |
| `cpu-quota`      | String  |                  | Imposes a CPU CFS quota on the container.                                                                              |
| `cpu-period`     | String  |                  | Sets the CPU CFS scheduler period for the container.                                                                   |
| `cpu-shares`     | String  |                  | Configures CPU shares (relative weight) of the container.                                                              |
| `cpuset-cpus`    | String  |                  | Limits the set of CPU cores the container can use.                                                                     |
| `cpuset-mems`    | String  |                  | Limits the set of CPU memory nodes the container can use.                                                              |
| `default-load`   | Boolean | `false`          | Automatically load images to the Docker Engine image store.                                                            |
| `network`        | String  |                  | Sets the network mode for the container.                                                                               |
| `cgroup-parent`  | String  | `/docker/buildx` | Sets the cgroup parent of the container if Docker is using the "cgroupfs" driver.                                      |
| `restart-policy` | String  | `unless-stopped` | Sets the container's [restart policy](/manuals/engine/containers/start-containers-automatically.md#use-a-restart-policy).      |
| `env.<key>`      | String  |                  | Sets the environment variable `key` to the specified `value` in the container.                                         |
| `provenance-add-gha`   | Boolean |    `true`       | Automatically writes GitHub Actions context into the builder for provenance.                                                   |

Before you configure the resource limits for the container,
read about [configuring runtime resource constraints for containers](/engine/containers/resource_constraints/).

## Usage

When you run a build, Buildx pulls the specified `image` (by default,
[`moby/buildkit`](https://hub.docker.com/r/moby/buildkit)).
When the container has started, Buildx submits the build submitted to the
containerized build server.

```console
$ docker buildx build -t <image> --builder=container .
WARNING: No output specified with docker-container driver. Build result will only remain in the build cache. To push result image into registry use --push or to load image into docker use --load
#1 [internal] booting buildkit
#1 pulling image moby/buildkit:buildx-stable-1
#1 pulling image moby/buildkit:buildx-stable-1 1.9s done
#1 creating container buildx_buildkit_container0
#1 creating container buildx_buildkit_container0 0.5s done
#1 DONE 2.4s
...
```

## Further reading

For more information on the Docker container driver, see the
[buildx reference](/reference/cli/docker/buildx/create/#driver).
