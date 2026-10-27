---
title: Deploy your Node.js application
linkTitle: Deploy your app
weight: 50
keywords: deploy, kubernetes, node, node.js, production
description: Learn how to deploy your containerized Node.js application to Kubernetes with production-ready configuration
aliases:
  - /language/nodejs/deploy/
  - /guides/language/nodejs/deploy/
---

## Prerequisites

- Complete all the previous sections of this guide, starting with [Containerize a Node.js application](containerize.md).
- Complete the [Kubernetes prerequisite](/guides/local-kubernetes.md#prerequisites).

## Overview

In this section, you'll learn how to deploy your containerized Node.js application to Kubernetes using Docker Desktop. This deployment uses production-ready configurations including security hardening, auto-scaling, persistent storage, and high availability features.

You'll deploy a complete stack including:

- Node.js Todo application with 3 replicas.
- PostgreSQL database with persistent storage.
- Auto-scaling based on CPU and memory usage.
- Ingress configuration for external access.
- Security settings.

## Prepare the manifest

[Create and customize the Node.js Kubernetes manifest](kubernetes-manifest.md). Review [architecture, security, availability, scaling, and persistence](kubernetes-context.md).

For the shared local deployment context, see [Local Kubernetes deployment context](/guides/local-kubernetes.md).

## Deploy your application

### Step 1: Deploy to Kubernetes

Deploy your application to the local Kubernetes cluster:

```console
$ kubectl apply -f nodejs-sample-kubernetes.yaml
```

You should see output confirming all resources were created:

```shell
namespace/todoapp created
secret/todoapp-secrets created
configmap/todoapp-config created
persistentvolumeclaim/postgres-pvc created
deployment.apps/todoapp-postgres created
service/todoapp-postgres created
deployment.apps/todoapp-deployment created
service/todoapp-service created
ingress.networking.k8s.io/todoapp-ingress created
poddisruptionbudget.policy/todoapp-pdb created
horizontalpodautoscaler.autoscaling/todoapp-hpa created
```

### Step 2: Verify the deployment

Check that your deployments are running:

```console
$ kubectl get deployments -n todoapp
```

Expected output:

```shell
NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
todoapp-deployment   3/3     3            3           30s
todoapp-postgres     1/1     1            1           30s
```

Verify your services are created:

```console
$ kubectl get services -n todoapp
```

Expected output:

```shell
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
todoapp-service    ClusterIP   10.111.101.229   <none>        80/TCP     45s
todoapp-postgres   ClusterIP   10.111.102.130   <none>        5432/TCP   45s
```

Check that persistent storage is working:

```console
$ kubectl get pvc -n todoapp
```

Expected output:

```shell
NAME           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
postgres-pvc   Bound    pvc-12345678-1234-1234-1234-123456789012   10Gi       RWO            standard       1m
```

### Step 3: Access your application

For local testing, use port forwarding to access your application:

```console
$ kubectl port-forward -n todoapp service/todoapp-service 8080:80
```

Open your browser and visit [http://localhost:8080](http://localhost:8080) to see your Todo application running in Kubernetes.

### Step 4: Test the deployment

Test that your application is working correctly:

1. **Add some todos** through the web interface
2. **Check application pods**:

   ```console
   $ kubectl get pods -n todoapp -l app=todoapp
   ```

3. **View application logs**:

   ```console
   $ kubectl logs -f deployment/todoapp-deployment -n todoapp
   ```

4. **Check database connectivity**:

   ```console
   $ kubectl get pods -n todoapp -l app=todoapp-postgres
   ```

5. **Monitor auto-scaling**:
   ```console
   $ kubectl describe hpa todoapp-hpa -n todoapp
   ```

### Step 5: Clean up

When you're done testing, remove the deployment:

```console
$ kubectl delete -f nodejs-sample-kubernetes.yaml
```

## Summary

You've deployed your containerized Node.js application to Kubernetes. You learned how to:

- Create a comprehensive Kubernetes deployment file with security hardening
- Deploy a multi-tier application (Node.js + PostgreSQL) with persistent storage
- Configure auto-scaling, health checks, and high availability features
- Test and monitor your deployment locally using Docker Desktop's Kubernetes

Your application is now running in a production-like environment with enterprise-grade features including security contexts, resource management, and automatic scaling.

---

## Related resources

Explore official references and best practices to sharpen your Kubernetes deployment workflow:

- [Kubernetes documentation](https://kubernetes.io/docs/home/) – Learn about core concepts, workloads, services, and more.
- [Deploy on Kubernetes with Docker Desktop](/manuals/desktop/use-desktop/kubernetes.md) – Use Docker Desktop's built-in Kubernetes support for local testing and development.
- [`kubectl` CLI reference](https://kubernetes.io/docs/reference/kubectl/) – Manage Kubernetes clusters from the command line.
- [Kubernetes Deployment resource](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) – Understand how to manage and scale applications using Deployments.
- [Kubernetes Service resource](https://kubernetes.io/docs/concepts/services-networking/service/) – Learn how to expose your application to internal and external traffic.
