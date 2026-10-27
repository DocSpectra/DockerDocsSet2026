---
title: Kubernetes cluster provisioning methods
---

## Cluster provisioning method

Docker Desktop Kubernetes can be provisioned with either the `kubeadm` or `kind`
provisioners.

`kubeadm` is the older provisioner. It supports a single-node cluster, you can't select the kubernetes
version, it's slower to provision than `kind`, and it's not supported by [Enhanced Container Isolation](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/_index.md) (ECI),
meaning that if ECI is enabled the cluster works but it's not protected by ECI.

`kind` is the newer provisioner. It supports multi-node clusters (for
a more realistic Kubernetes setup), you can choose the Kubernetes version, it's
faster to provision than `kubeadm`, and it's supported by ECI - when ECI is
enabled, the Kubernetes cluster runs in unprivileged Docker containers, thus
making it more secure. 

| Feature | `kubeadm` | `kind` |
| :------ | :-----: | :--: |
| Multi-node cluster support | No | Yes |
| Kubernetes version selector | No | Yes |
| Speed to provision | ~1 min | ~30 seconds |
| Supported by ECI | No | Yes |
| Works with containerd image store | Yes | Yes |
| Works with Docker image store | Yes | No |
