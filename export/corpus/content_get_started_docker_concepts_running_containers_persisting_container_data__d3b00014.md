---
title: Persisting container data
weight: 3
keywords: concepts, build, images, container, docker desktop
aliases:
 - /guides/walkthroughs/persist-data/
 - /guides/docker-concepts/running-containers/persisting-container-data/
---

{{< youtube-embed 10_2BjqB_Ls >}}

## Explanation

When a container starts, it uses the files and configuration provided by the image. Each container is able to create, modify, and delete files and does so without affecting any other containers. When the container is deleted, these file changes are also deleted.

While this ephemeral nature of containers is great, it poses a challenge when you want to persist the data. For example, if you restart a database container, you might not want to start with an empty database. So, how do you persist files?

### Container volumes

Volumes are a storage mechanism that provide the ability to persist data beyond the lifecycle of an individual container. Think of it like providing a shortcut or symlink from inside the container to outside the container. 

As an example, imagine you create a volume named `log-data`. 

```console
$ docker volume create log-data
```

When starting a container with the following command, the volume will be mounted (or attached) into the container at `/logs`:

```console
$ docker run -d -p 80:80 -v log-data:/logs docker/welcome-to-docker
```

If the volume `log-data` doesn't exist, Docker will automatically create it for you. 

When the container runs, all files it writes into the `/logs` folder will be saved in this volume, outside of the container. If you delete the container and start a new container using the same volume, the files will still be there.

> **Sharing files using volumes**
>
> You can attach the same volume to multiple containers to share files between containers. This might be helpful in scenarios such as log aggregation, data pipelines, or other event-driven applications.


### Managing volumes

Volumes have their own lifecycle beyond that of containers and can grow quite large depending on the type of data and applications you’re using. The following commands will be helpful to manage volumes:

- `docker volume ls` - list all volumes
- `docker volume rm <volume-name-or-id>` - remove a volume (only works when the volume is not attached to any containers)
- `docker volume prune` - remove all unused (unattached) volumes

## Container filesystems and volume mounts

When a container runs, it uses the various layers from an image for its filesystem.
Each container also gets its own "scratch space" to create/update/remove files. Any
changes won't be seen in another container, even if they're using the same image.

### Volume mounts

Each container starts from the image definition each time it starts. 
While containers can create, update, and delete files, those changes are lost when you remove the container 
and Docker isolates all changes to that container. With volumes, you can change all of this.

[Volumes](/manuals/engine/storage/volumes.md) provide the ability to connect specific filesystem paths of 
the container back to the host machine. If you mount a directory in the container, changes in that
directory are also seen on the host machine. If you mount that same directory across container restarts, you'd see
the same files.


## Docker-managed storage

Think of a volume mount as an opaque bucket of data. 
Docker fully manages the volume, including the storage location on disk. You only need to remember the
name of the volume.

## Additional resources

The following resources will help you learn more about volumes:

- [Manage data in Docker](/engine/storage)
- [Volumes](/engine/storage/volumes)
- [Volume mounts](/engine/containers/run/#volume-mounts)
