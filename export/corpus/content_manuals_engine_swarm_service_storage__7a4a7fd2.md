---
title: Mount volumes and host paths in Swarm services
---

## Prerequisites and shared procedures

See [Create, update, and remove Swarm services](service-lifecycle.md) and [How services work](how-swarm-mode-works/services.md).

## Give a service access to volumes or bind mounts

For best performance and portability, you should avoid writing important data
directly into a container's writable layer. You should instead use data volumes
or bind mounts. This principle also applies to services.

You can create two types of mounts for services in a swarm, `volume` mounts or
`bind` mounts. Regardless of which type of mount you use, configure it using the
`--mount` flag when you create a service, or the `--mount-add` or `--mount-rm`
flag when updating an existing service. The default is a data volume if you
don't specify a type.

### Data volumes

Data volumes are storage that exist independently of a container. The
lifecycle of data volumes under swarm services is similar to that under
containers. Volumes outlive tasks and services, so their removal must be
managed separately. Volumes can be created before deploying a service, or if
they don't exist on a particular host when a task is scheduled there, they are
created automatically according to the volume specification on the service.

To use existing data volumes with a service use the `--mount` flag:

```console
$ docker service create \
  --mount src=<VOLUME-NAME>,dst=<CONTAINER-PATH> \
  --name myservice \
  <IMAGE>
```

If a volume with the name `<VOLUME-NAME>` doesn't exist when a task is
scheduled to a particular host, then one is created. The default volume
driver is `local`.  To use a different volume driver with this create-on-demand
pattern, specify the driver and its options with the `--mount` flag:

```console
$ docker service create \
  --mount type=volume,src=<VOLUME-NAME>,dst=<CONTAINER-PATH>,volume-driver=<DRIVER>,volume-opt=<KEY0>=<VALUE0>,volume-opt=<KEY1>=<VALUE1>
  --name myservice \
  <IMAGE>
```

For more information on how to create data volumes and the use of volume
drivers, see [Use volumes](/manuals/engine/storage/volumes.md).


### Bind mounts

Bind mounts are file system paths from the host where the scheduler deploys
the container for the task. Docker mounts the path into the container. The
file system path must exist before the swarm initializes the container for the
task.

The following examples show bind mount syntax:

- To mount a read-write bind:

  ```console
  $ docker service create \
    --mount type=bind,src=<HOST-PATH>,dst=<CONTAINER-PATH> \
    --name myservice \
    <IMAGE>
  ```

- To mount a read-only bind:

  ```console
  $ docker service create \
    --mount type=bind,src=<HOST-PATH>,dst=<CONTAINER-PATH>,readonly \
    --name myservice \
    <IMAGE>
  ```

> [!IMPORTANT]
>
> Bind mounts can be useful but they can also cause problems. In
> most cases, it is recommended that you architect your application such that
> mounting paths from the host is unnecessary. The main risks include the
> following:
>
> - If you bind mount a host path into your service’s containers, the path
>   must exist on every swarm node. The Docker swarm mode scheduler can schedule
>   containers on any machine that meets resource availability requirements
>   and satisfies all constraints and placement preferences you specify.
>
> - The Docker swarm mode scheduler may reschedule your running service
>   containers at any time if they become unhealthy or unreachable.
>
> - Host bind mounts are non-portable. When you use bind mounts, there is no
>   guarantee that your application runs the same way in development as it does
>   in production.
