---
title: Configure a custom registry for Kubernetes control plane images
linkTitle: Kubernetes image registry
description: Image lists, registry configuration steps, and ECI requirements for Kubernetes control plane images.
weight: 55
---

Docker Desktop uses containers to run the Kubernetes control plane. By default, Docker Desktop pulls
the associated container images from Docker Hub. The images pulled depend on the [cluster provisioning mode](kubernetes.md#cluster-provisioning-method).

## Find a registry setup task

- [Identify required images](#required-control-plane-images) and [their tags](#image-tags-and-version-scope)
- [Review setting scope and ECI requirements](#scope-and-eci-requirements)
- [Configure the repository name](#configure-the-registry-repository)
- [Mirror images and switch registries](#mirror-images-and-switch-registries)

## Required control plane images

### kind

For example, in `kind` mode it requires the following images:

```console
docker.io/kindest/node:<tag>
docker.io/envoyproxy/envoy:<tag>
docker.io/docker/desktop-cloud-provider-kind:<tag>
docker.io/docker/desktop-containerd-registry-mirror:<tag>
```

### kubeadm

In `kubeadm` mode it requires the following images:

```console
docker.io/docker/desktop-kubernetes:<tag>
docker.io/docker/desktop-storage-provisioner:<tag>
docker.io/docker/desktop-vpnkit-controller:<tag>
docker.io/docker/desktop-kubernetes-etcd:<tag>
docker.io/docker/desktop-kubernetes-coredns:<tag>
docker.io/docker/desktop-kubernetes-pause:<tag>
docker.io/docker/desktop-kubernetes-apiserver:<tag>
docker.io/docker/desktop-kubernetes-controller-manager:<tag>
docker.io/docker/desktop-kubernetes-scheduler:<tag>
docker.io/docker/desktop-kubernetes-proxy:<tag>
```

## Image tags and version scope

The image tags are automatically selected by Docker Desktop based on several
factors, including the version of Kubernetes being used. The tags vary for each image and may change between Docker Desktop releases. To stay informed, monitor the Docker Desktop release notes.

> [!NOTE]
>
> In Docker Desktop versions 4.44 or later you can run `docker desktop kubernetes images list` to list Kubernetes images used by the currently installed version of Docker Desktop.
> For more information, see the [Docker Desktop CLI](/reference/cli/docker/desktop/kubernetes/images).

## Scope and ECI requirements

> [!NOTE]
>
> The `KubernetesImagesRepository` setting only applies to control plane images used by Docker Desktop
> to set up the Kubernetes cluster. It has no effect on other Kubernetes pods.

> [!NOTE]
>
> In Docker Desktop versions 4.43 or earlier, when using `KubernetesImagesRepository` and [Enhanced Container Isolation (ECI)](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/_index.md)
> is enabled, add the following images to the [ECI Docker socket mount image list](/manuals/enterprise/security/hardened-desktop/settings-management/configure-json-file.md#enhanced-container-isolation):
>
> `[imagesRepository]/desktop-cloud-provider-kind:`
> `[imagesRepository]/desktop-containerd-registry-mirror:`
>
> These containers mount the Docker socket, so you must add the images to the ECI images list. If not,
> ECI will block the mount and Kubernetes won't start.

## Configure the registry repository

To accommodate scenarios where access to Docker Hub is not allowed, admins can
configure Docker Desktop to pull the above listed images from a different registry (e.g., a mirror)
using the [KubernetesImagesRepository](/manuals/enterprise/security/hardened-desktop/settings-management/configure-json-file.md#kubernetes) setting as follows.

An image name can be broken into `[registry[:port]/][namespace/]repository[:tag]` components.
The `KubernetesImagesRepository` setting allows users to override the `[registry[:port]/][namespace]`
portion of the image's name.

For example, if Docker Desktop Kubernetes is configured in `kind` mode and
`KubernetesImagesRepository` is set to `my-registry:5000/kind-images`, then
Docker Desktop will pull the images from:

```console
my-registry:5000/kind-images/node:<tag>
my-registry:5000/kind-images/envoy:<tag>
my-registry:5000/kind-images/desktop-cloud-provider-kind:<tag>
my-registry:5000/kind-images/desktop-containerd-registry-mirror:<tag>
```

These images should be cloned/mirrored from their respective images in Docker Hub. The tags must
also match what Docker Desktop expects.

## Mirror images and switch registries

The recommended approach to set this up is the following:

1. Start Kubernetes using the desired cluster provisioning method: `kubeadm` or `kind`.
2. After Kubernetes has started, use either:
   - (Docker Desktop version 4.44 or later) `docker desktop kubernetes images list` to list the image tags that will be pulled by the current Docker Desktop installation
   - `docker ps` to view the container images used by Docker Desktop for the Kubernetes control plane
3. Clone or mirror those images (with matching tags) to your custom registry.
4. Stop the Kubernetes cluster.
5. Configure the `KubernetesImagesRepository` setting to point to your custom registry.
6. Restart Docker Desktop.
7. Verify that the Kubernetes cluster is using the custom registry images using the `docker ps` command.

## Related tasks

- [Choose a provisioning method and create a cluster](kubernetes.md#cluster-provisioning-method)
- [Edit or stop your cluster](kubernetes.md#edit-or-stop-your-cluster)
- [Troubleshoot Kubernetes](kubernetes.md#troubleshooting)
