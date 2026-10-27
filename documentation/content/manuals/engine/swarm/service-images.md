---
title: Select and update Swarm service images
---

## Prerequisites and shared procedures

See [Create, update, and remove Swarm services](service-lifecycle.md) and [How services work](how-swarm-mode-works/services.md).

## Create a service using an image on a private registry

If your image is available on a private registry which requires login, use the
`--with-registry-auth` flag with `docker service create`, after logging in. If
your image is stored on `registry.example.com`, which is a private registry, use
a command like the following:

```console
$ docker login registry.example.com

$ docker service  create \
  --with-registry-auth \
  --name my_service \
  registry.example.com/acme/my_image:latest
```

This passes the login token from your local client to the swarm nodes where the
service is deployed, using the encrypted WAL logs. With this information, the
nodes are able to log into the registry and pull the image.

## Specify the image version a service should use

When you create a service without specifying any details about the version of
the image to use, the service uses the version tagged with the `latest` tag.
You can force the service to use a specific version of the image in a few
different ways, depending on your desired outcome.

An image version can be expressed in several different ways:

- If you specify a tag, the manager (or the Docker client, if you use
  [content trust](../security/trust/_index.md)) resolves that tag to a digest.
  When the request to create a container task is received on a worker node, the
  worker node only sees the digest, not the tag.

  ```console
  $ docker service create --name="myservice" ubuntu:16.04
  ```

  Some tags represent discrete releases, such as `ubuntu:16.04`. Tags like this
  almost always resolve to a stable digest over time. It is recommended
  that you use this kind of tag when possible.

  Other types of tags, such as `latest` or `nightly`, may resolve to a new
  digest often, depending on how often an image's author updates the tag. It is
  not recommended to run services using a tag which is updated frequently, to
  prevent different service replica tasks from using different image versions.

- If you don't specify a version at all, by convention the image's `latest` tag
  is resolved to a digest. Workers use the image at this digest when creating
  the service task.

  Thus, the following two commands are equivalent:

  ```console
  $ docker service create --name="myservice" ubuntu

  $ docker service create --name="myservice" ubuntu:latest
  ```

- If you specify a digest directly, that exact version of the image is always
  used when creating service tasks.

  ```console
  $ docker service create \
      --name="myservice" \
      ubuntu:16.04@sha256:35bc48a1ca97c3971611dc4662d08d131869daa692acb281c7e9e052924e38b1
  ```

When you create a service, the image's tag is resolved to the specific digest
the tag points to **at the time of service creation**. Worker nodes for that
service use that specific digest forever unless the service is explicitly
updated. This feature is particularly important if you do use often-changing tags
such as `latest`, because it ensures that all service tasks use the same version
of the image.

> [!NOTE]>
>
> If [content trust](../security/trust/_index.md) is
> enabled, the client actually resolves the image's tag to a digest before
> contacting the swarm manager, to verify that the image is signed.
> Thus, if you use content trust, the swarm manager receives the request
> pre-resolved. In this case, if the client cannot resolve the image to a
> digest, the request fails.

If the manager can't resolve the tag to a digest, each worker
node is responsible for resolving the tag to a digest, and different nodes may
use different versions of the image. If this happens, a warning like the
following is logged, substituting the placeholders for real information.

```text
unable to pin image <IMAGE-NAME> to digest: <REASON>
```

To see an image's current digest, issue the command
`docker inspect <IMAGE>:<TAG>` and look for the `RepoDigests` line. The
following is the current digest for `ubuntu:latest` at the time this content
was written. The output is truncated for clarity.

```console
$ docker inspect ubuntu:latest
```

```json
"RepoDigests": [
    "ubuntu@sha256:35bc48a1ca97c3971611dc4662d08d131869daa692acb281c7e9e052924e38b1"
],
```

After you create a service, its image is never updated unless you explicitly run
`docker service update` with the `--image` flag as described below. Other update
operations such as scaling the service, adding or removing networks or volumes,
renaming the service, or any other type of update operation do not update the
service's image.

## Update a service's image after creation

Each tag represents a digest, similar to a Git hash. Some tags, such as
`latest`, are updated often to point to a new digest. Others, such as
`ubuntu:16.04`, represent a released software version and are not expected to
update to point to a new digest often if at all. When you create a service, it
is constrained to create tasks using a specific digest of an image until you
update the service using `service update` with the `--image` flag.

When you run `service update` with the `--image` flag, the swarm manager queries
Docker Hub or your private Docker registry for the digest the tag currently
points to and updates the service tasks to use that digest.

> [!NOTE]
>
> If you use [content trust](../security/trust/_index.md), the Docker
> client resolves image and the swarm manager receives the image and digest,
>  rather than a tag.

Usually, the manager can resolve the tag to a new digest and the service
updates, redeploying each task to use the new image. If the manager can't
resolve the tag or some other problem occurs, the next two sections outline what
to expect.

### If the manager resolves the tag

If the swarm manager can resolve the image tag to a digest, it instructs the
worker nodes to redeploy the tasks and use the image at that digest.

- If a worker has cached the image at that digest, it uses it.

- If not, it attempts to pull the image from Docker Hub or the private registry.

  - If it succeeds, the task is deployed using the new image.

  - If the worker fails to pull the image, the service fails to deploy on that
    worker node. Docker tries again to deploy the task, possibly on a different
    worker node.

### If the manager cannot resolve the tag

If the swarm manager cannot resolve the image to a digest, all is not lost:

- The manager instructs the worker nodes to redeploy the tasks using the image
  at that tag.

- If the worker has a locally cached image that resolves to that tag, it uses
  that image.

- If the worker does not have a locally cached image that resolves to the tag,
  the worker tries to connect to Docker Hub or the private registry to pull the
  image at that tag.

  - If this succeeds, the worker uses that image.

  - If this fails, the task fails to deploy and the manager tries again to deploy
    the task, possibly on a different worker node.
