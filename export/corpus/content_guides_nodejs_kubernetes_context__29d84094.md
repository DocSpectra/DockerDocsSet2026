---
title: Node.js Kubernetes architecture and settings
description: Architecture, security, availability, scaling, and persistence in the Node.js deployment example.
---

For shared Kubernetes resource context, see [Kubernetes YAML](/guides/orchestration-manifests.md#kubernetes-yaml).

## Understanding the deployment

The deployment file creates a complete application stack with multiple components working together.

### Architecture

The deployment includes:

- **Node.js application**: Runs 3 replicas of your containerized Todo app
- **PostgreSQL database**: Single instance with 10Gi of persistent storage
- **Services**: Kubernetes services handle load balancing across application replicas
- **Ingress**: External access through an ingress controller with SSL/TLS support

### Security

The deployment uses several security features:

- Containers run as a non-root user (UID 1001)
- Read-only root filesystem prevents unauthorized writes
- Linux capabilities are dropped to minimize attack surface
- Sensitive data like database passwords are stored in Kubernetes secrets

### High availability

To keep your application running reliably:

- Three application replicas ensure service continues if one pod fails
- Pod disruption budget maintains at least one available pod during updates
- Rolling updates allow zero-downtime deployments
- Health checks on the `/health` endpoint ensure only healthy pods receive traffic

### Auto-scaling

The Horizontal Pod Autoscaler scales your application based on resource usage:

- Scales between 1 and 5 replicas automatically
- Triggers scaling when CPU usage exceeds 70%
- Triggers scaling when memory usage exceeds 80%
- Resource limits: 256Mi-512Mi memory, 250m-500m CPU per pod

### Data persistence

PostgreSQL data is stored persistently:

- 10Gi persistent volume stores database files
- Database initializes automatically on first startup
- Data persists across pod restarts and updates
