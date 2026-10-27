---
title: Create a Kubernetes builder and build an image
---

For shared options and behavior, see [kubernetes driver reference](kubernetes-reference.md).
For shared procedures, see [Select a builder](../selection.md) and
[Load build results](../image-loading.md).

## Example: Creating a Buildx builder in Kubernetes

This guide shows you how to:

- Create a namespace for your Buildx resources
- Create a Kubernetes builder.
- List the available builders
- Build an image using your Kubernetes builders

Prerequisites:

- You have an existing Kubernetes cluster. If you don't already have one, you
  can follow along by installing
  [minikube](https://minikube.sigs.k8s.io/docs/).
- The cluster you want to connect to is accessible via the `kubectl` command,
  with the `KUBECONFIG` environment variable
  [set appropriately](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/#set-the-kubeconfig-environment-variable) if necessary.

1. Create a `buildkit` namespace.

   Creating a separate namespace helps keep your Buildx resources separate from
   other resources in the cluster.

   ```console
   $ kubectl create namespace buildkit
   namespace/buildkit created
   ```

2. Create a new builder with the Kubernetes driver:

   ```console
   $ docker buildx create \
     --bootstrap \
     --name=kube \
     --driver=kubernetes \
     --driver-opt=namespace=buildkit
   ```

   > [!NOTE]
   >
   > Remember to specify the namespace in driver options.

3. List available builders using `docker buildx ls`

   ```console
   $ docker buildx ls
   NAME/NODE                DRIVER/ENDPOINT STATUS  PLATFORMS
   kube                     kubernetes
     kube0-6977cdcb75-k9h9m                 running linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/386
   default *                docker
     default                default         running linux/amd64, linux/386
   ```

4. Inspect the running pods created by the build driver with `kubectl`.

   ```console
   $ kubectl -n buildkit get deployments
   NAME    READY   UP-TO-DATE   AVAILABLE   AGE
   kube0   1/1     1            1           32s

   $ kubectl -n buildkit get pods
   NAME                     READY   STATUS    RESTARTS   AGE
   kube0-6977cdcb75-k9h9m   1/1     Running   0          32s
   ```

   The build driver creates the necessary resources on your cluster in the
   specified namespace (in this case, `buildkit`), while keeping your driver
   configuration locally.

5. Use your new builder by including the `--builder` flag when running buildx
   commands. For example: :

   ```console
   # Replace <registry> with your Docker username
   # and <image> with the name of the image you want to build
   docker buildx build \
     --builder=kube \
     -t <registry>/<image> \
     --push .
   ```

That's it: you've now built an image from a Kubernetes pod, using Buildx.


