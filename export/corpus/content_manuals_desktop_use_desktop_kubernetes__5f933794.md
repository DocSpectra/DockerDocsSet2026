---
description: See how you can deploy to Kubernetes on Docker Desktop
keywords: deploy, kubernetes, kubectl, orchestration, Docker Desktop
title: Explore the Kubernetes view
linkTitle: Kubernetes
aliases:
- /docker-for-windows/kubernetes/
- /docker-for-mac/kubernetes/
- /desktop/kubernetes/
- /desktop/features/kubernetes/
weight: 50
---

Docker Desktop includes a standalone Kubernetes server and client, as well as Docker CLI integration, enabling local Kubernetes development and testing directly on your machine.

The Kubernetes server runs as a single or multi-node cluster, within Docker containers. This lightweight setup helps you explore Kubernetes features, test workloads, and work with container orchestration in parallel with other Docker features.

## Enable Kubernetes

With Docker Desktop version 4.51 and later, you can manage Kubernetes directly from the **Kubernetes** view in the Docker Desktop Dashboard.

1. Open the Docker Desktop Dashboard and select the **Kubernetes** view. 
2. Select **Create cluster**.
3. Choose your cluster type:
   - **Kubeadm** creates a single-node cluster and the version is set by Docker Desktop.
   - **kind** creates a multi-node cluster and you can set the version and number of nodes.
   For more detailed information on each cluster type, see [Cluster provisioning method](kubernetes-provisioning.md#cluster-provisioning-method).
4. Optional: Select **Show system containers (advanced)** to view internal containers when using Docker commands.
5. Select **Create**. 

This sets up the images required to run the Kubernetes server as containers, and installs the `kubectl` command-line tool on your system at `/usr/local/bin/kubectl` (Mac) or `C:\Program Files\Docker\Docker\resources\bin\kubectl.exe` (Windows). If you installed `kubectl` using Homebrew, or by some other method, and experience conflicts, remove `/usr/local/bin/kubectl`.

   > [!NOTE]
   >
   > Docker Desktop for Linux does not include `kubectl` by default. You can install it separately by following the [Kubernetes installation guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/). Ensure the `kubectl` binary is installed at `/usr/local/bin/kubectl`.

The following actions are also triggered in the Docker Desktop backend and VM:

- Generation of certificates and cluster configuration
- Download and installation of Kubernetes internal components
- Cluster boot-up
- Installation of additional controllers for networking and storage

When Kubernetes is enabled, its status is displayed in the Docker Desktop Dashboard footer and the Docker menu.

You can check which version of Kubernetes you're on with:

```console
$ kubectl version
```

### Cluster provisioning method

See [Kubernetes cluster provisioning methods](kubernetes-provisioning.md).

## Dashboard view

When a Kubernetes cluster is enabled, the **Kubernetes** view displays a live dashboard view showing:

- A namespace selector at the top
- A real-time list of resources - pods, services, deployments - in the selected namespace
- Automatic updates when resources are created, deleted, or modified

## Verify installation

Confirm that your cluster is running:

```console
$ kubectl get nodes
NAME                 STATUS    ROLES            AGE       VERSION
docker-desktop       Ready     control-plane    3h        v1.29.1
```

If kubectl is pointing to another environment, switch to the Docker Desktop context:

```console
$ kubectl config use-context docker-desktop
```

>[!TIP]
>
> If no contexts appear, try:
>
> - Running the command in the Command Prompt or PowerShell.
> - Setting the `KUBECONFIG` environment variable to point to your `.kube/config` file.


For more information about `kubectl`, see the
[`kubectl` documentation](https://kubernetes.io/docs/reference/kubectl/overview/).

## Edit or stop your cluster

When Kubernetes is enabled:

- Select **Edit cluster** to modify configuration. For example, switch between **kubeadm** and **kind**, or change the number of nodes.
- Select **Stop** to disable the cluster. Progress is displayed, and the **Kubernetes** view returns to the **Create cluster** screen. This stops and removes Kubernetes containers, and also removes the `/usr/local/bin/kubectl` command.

## Upgrade your cluster

Kubernetes clusters are not automatically upgraded with Docker Desktop updates. To upgrade the cluster, you must manually select **Reset cluster** in the **Kubernetes** settings.

## Configuring a custom image registry for Kubernetes control plane images

See [Use a custom registry for Kubernetes control plane images](kubernetes-custom-registry.md).

## Troubleshooting

- If Kubernetes fails to start, make sure Docker Desktop is running with enough allocated resources. Check **Settings** > **Resources**.
- If the `kubectl` commands return errors, confirm the context is set to `docker-desktop`
   ```console
   $ kubectl config use-context docker-desktop
   ```
   You can then try checking the logs of the Kubernetes system containers if you have enabled that setting.
- If you're experiencing cluster issues after updating, reset your Kubernetes cluster. Resetting a Kubernetes cluster can help resolve issues by essentially reverting the cluster to a clean state, and clearing out misconfigurations, corrupted data, or stuck resources that may be causing problems. If the issue still persists, you may need to clean and purge data, and then restart Docker Desktop.
