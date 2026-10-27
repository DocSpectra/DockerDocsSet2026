---
title: Use the default Compose Bridge transformation
linkTitle: Usage
weight: 10
description: Learn how to use the default Compose Bridge transformation to convert Compose files into Kubernetes manifests
keywords: docker compose bridge, compose kubernetes transform, kubernetes from compose, compose bridge convert, compose.yaml to kubernetes
---

{{< summary-bar feature_name="Compose bridge" >}}

See [Default Compose Bridge output](default-output.md) for the generated resources, overlays, and model endpoints.

## Use the default Compose Bridge transformation

To convert your Compose file using the default transformation:

```console
$ docker compose bridge convert
```

Compose looks for a `compose.yaml` file inside the current directory and generates Kubernetes manifests.

Example output:

```console
$ docker compose -f compose.yaml bridge convert
Kubernetes resource backend-deployment.yaml created
Kubernetes resource frontend-deployment.yaml created
Kubernetes resource backend-expose.yaml created
Kubernetes resource frontend-expose.yaml created
Kubernetes resource 0-my-project-namespace.yaml created
Kubernetes resource default-network-policy.yaml created
Kubernetes resource backend-service.yaml created
Kubernetes resource frontend-service.yaml created
Kubernetes resource kustomization.yaml created
Kubernetes resource backend-deployment.yaml created
Kubernetes resource frontend-deployment.yaml created
Kubernetes resource backend-service.yaml created
Kubernetes resource frontend-service.yaml created
Kubernetes resource kustomization.yaml created
Kubernetes resource model-runner-configmap.yaml created
Kubernetes resource model-runner-deployment.yaml created
Kubernetes resource model-runner-service.yaml created
Kubernetes resource model-runner-volume-claim.yaml created
Kubernetes resource kustomization.yaml created
```

All generated files are stored in the `/out` directory in your project.

## Deploy the generated manifests

> [!IMPORTANT]
>
> Before you deploy your Compose Bridge transformations, make sure you have [enabled Kubernetes](/manuals/desktop/settings-and-maintenance/settings.md#kubernetes) in Docker Desktop.

Once the manifests are generated, deploy them to your local Kubernetes cluster:

```console
$ kubectl apply -k out/overlays/desktop/
```

> [!TIP]
>
> You can convert and deploy your Compose project to a Kubernetes cluster from the Compose file viewer.
> 
> Make sure you are signed in to your Docker account, navigate to your container in the **Containers** view, and in the top-right corner select **View configurations** and then **Convert and Deploy to Kubernetes**. 

## Additional commands

Convert a `compose.yaml` file located in another directory:

```console
$ docker compose -f <path-to-file>/compose.yaml bridge convert
```

To see all available flags, run:

```console
$ docker compose bridge convert --help
```

## Shared context

- [Transformation contract and template reference](transformations.md)
- [Generated resources, overlays, and model endpoints](default-output.md)
