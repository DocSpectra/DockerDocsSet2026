---
title: Access private resources from Docker Build Cloud
---

For shared build authentication steps, see [Build secrets](/manuals/build/building/secrets.md).

## Private resource access

Private resource access lets cloud builders pull images and packages from private resources. This feature is useful when builds rely on self-hosted artifact repositories or private OCI registries.

For example, if your organization hosts a private [PyPI](https://pypi.org/) repository on a private network, Docker Build Cloud would not be able to access it by default, since the cloud builder is not connected to your private network.

To enable your cloud builders to access your private resources, enter the host name and port of your private resource and then select **Add**.

### Authentication

If your internal artifacts require authentication, make sure that you
authenticate with the repository either before or during the build. For
internal package repositories for npm or PyPI, use [build secrets](/manuals/build/building/secrets.md)
to authenticate during the build. For internal OCI registries, use `docker
login` to authenticate before building.

If you use a private registry that requires authentication, you need to
authenticate twice before building: once to Docker Hub (to access Docker Build
Cloud), and once to your private registry (to push/pull images).

```console
$ echo $DOCKER_PAT | docker login docker.io -u <username> --password-stdin
$ echo $REGISTRY_PASSWORD | docker login registry.example.com -u <username> --password-stdin
$ docker build --builder <cloud-builder> --tag registry.example.com/<image> --push .
```


