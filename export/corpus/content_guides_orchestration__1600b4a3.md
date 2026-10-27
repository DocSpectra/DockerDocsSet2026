---
title: Deployment and orchestration
keywords: orchestration, deploy, kubernetes, swarm,
description: Get oriented on some basics of Docker and install Docker Desktop.
aliases:
  - /get-started/orchestration/
  - /guides/deployment-orchestration/orchestration/
summary: |
  Explore the essentials of container orchestration with Docker.
tags: [deploy]
params:
  time: 10 minutes
---

Containerization provides an opportunity to move and scale applications to
clouds and data centers. Containers effectively guarantee that those applications run the
same way anywhere, allowing you to quickly and easily take advantage of all
these environments. Additionally, as you scale your applications up, you need some
tooling to help automate the maintenance of those applications, enable the
replacement of failed containers automatically, and manage the roll-out of
updates and reconfigurations of those containers during their lifecycle.

Tools to manage, scale, and maintain containerized applications are called
orchestrators. Two of the most popular orchestration tools are Kubernetes and
Docker Swarm. Docker Desktop provides development environments for both of these
orchestrators.

The advanced modules teach you how to:

1. [Set up and use a Kubernetes environment on your development machine](kube-deploy.md)
2. [Set up and use a Swarm environment on your development machine](swarm-deploy.md)

## Turn on Kubernetes

See [Enable and verify Kubernetes in Docker Desktop](orchestration-kubernetes-setup.md).

## Enable Docker Swarm

See [Enable and verify Swarm in Docker Desktop](orchestration-swarm-setup.md).

## Conclusion

At this point, you've confirmed that you can run simple containerized workloads in Kubernetes and Swarm. The next step is to write a YAML file that describes how to run and manage these containers.

- [Deploy to Kubernetes](kube-deploy.md)
- [Deploy to Swarm](swarm-deploy.md)

## CLI references

Further documentation for all CLI commands used in this article are available here:

- [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply)
- [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get)
- [`kubectl logs`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs)
- [`kubectl delete`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete)
- [`docker swarm init`](/reference/cli/docker/swarm/init/)
- [`docker service *`](/reference/cli/docker/service/)
