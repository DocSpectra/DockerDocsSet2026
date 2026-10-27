---
title: Apply and check a local Kubernetes deployment
description: Apply a manifest, check deployments and NodePort services, verify the application, and clean up.
---

## Prerequisites and context

See [Local Kubernetes deployment context](/guides/local-kubernetes.md) for turning on Kubernetes in Docker Desktop and testing and debugging locally.

> **New to Kubernetes?**
> Visit the [Kubernetes basics tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/) to get familiar with how clusters, pods, deployments, and services work.

## Apply the configuration

In a terminal, navigate to the directory containing your Kubernetes YAML file. Use the apply command from your application guide. Output indicating that the Kubernetes objects were created confirms creation.

## Check deployments

List your deployments:

```console
$ kubectl get deployments
```

A ready, available replica indicates that the requested pod is up and running. Compare the output with your application guide.

## Check services

List your services:

```console
$ kubectl get services
```

In addition to the default `kubernetes` service, look for the application service and its NodePort.

## Open the application

Open the browser address from your application guide and check its expected response.

## Clean up

Use the delete command from your application guide to tear down the application after testing.

For Kubernetes YAML and resource context, see [Kubernetes YAML](/guides/orchestration-manifests.md#kubernetes-yaml).
