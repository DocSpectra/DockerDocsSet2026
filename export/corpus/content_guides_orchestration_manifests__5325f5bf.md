---
title: Kubernetes and Swarm application manifests
description: Pods, deployments, services, and stack files.
---

## Kubernetes YAML

All containers in Kubernetes are scheduled as pods, which are groups of co-located containers that share some resources. Furthermore, in a realistic application you almost never create individual pods. Instead, most of your workloads are scheduled as deployments, which are scalable groups of pods maintained automatically by Kubernetes. Lastly, all Kubernetes objects can and should be described in manifests called Kubernetes YAML files. These YAML files describe all the components and configurations of your Kubernetes app, and can be used to create and destroy your app in any Kubernetes environment.

## Swarm stack files

Swarm never creates individual containers. Instead, all Swarm workloads are scheduled as services, which are scalable groups of containers with added networking features maintained automatically by Swarm. Furthermore, all Swarm objects can and should be described in manifests called stack files. These YAML files describe all the components and configurations of your Swarm app, and can be used to create and destroy your app in any Swarm environment.

## Kubernetes and Swarm services

> **Kubernetes Services and Swarm Services are very different**
>
> Despite the similar name, the two orchestrators mean very different things by
> the term 'service'. In Swarm, a service provides both scheduling and
> networking facilities, creating containers and providing tools for routing
> traffic to them. In Kubernetes, scheduling and networking are handled
> separately, deployments (or other controllers) handle the scheduling of
> containers as pods, while services are responsible only for adding
> networking features to those pods.

## Kubernetes YAML fields

While Kubernetes YAML can appear long and complicated at first, it almost always follows the same pattern:

- The `apiVersion`, which indicates the Kubernetes API that parses this object
- The `kind` indicating what sort of object this is
- Some `metadata` applying things like names to your objects
- The `spec` specifying all the parameters and configurations of your object.
