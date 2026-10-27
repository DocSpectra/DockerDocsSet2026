---
title: Use and debug DHI dev variants on OpenShift
description: Choose build-only variants, temporary anyuid debugging, or cluster debug containers.
---

Before you begin, review [OpenShift security constraints](../core-concepts/openshift.md) and [DHI registry authentication](authenticate.md).

## Use DHI dev variants in OpenShift

DHI `-dev` variants include a shell, package manager, and development tools.
They run as root (UID 0) by default, which conflicts with OpenShift’s
`restricted-v2` SCC. There are three approaches:

### Option 1: Use dev variants only in build stages (recommended)

Use `-dev` variants only in Dockerfile build stages and never deploy them
directly to OpenShift:

```dockerfile
FROM YOUR_ORG/dhi-node:24-alpine3.23-dev AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Set root group ownership for OpenShift compatibility
RUN chgrp -R 0 /app/dist /app/node_modules && \
    chmod -R g=u /app/dist /app/node_modules

FROM YOUR_ORG/dhi-node:24-alpine3.23
WORKDIR /app
COPY --from=build --chown=65532:0 /app/dist ./dist
COPY --from=build --chown=65532:0 /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

The final runtime image is non-root and distroless, fully compatible with
`restricted-v2`.

### Option 2: Grant the `anyuid` SCC for debugging

If you need to run a `-dev` variant directly in OpenShift for debugging, grant
the `anyuid` SCC to a dedicated service account:

```console
oc create serviceaccount dhi-debug
oc adm policy add-scc-to-user anyuid -z dhi-debug
```

Then reference it in your pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dhi-debug
spec:
  serviceAccountName: dhi-debug
  containers:
    - name: debug
      image: YOUR_ORG/dhi-node:24-alpine3.23-dev
      command: ["sleep", "infinity"]
  imagePullSecrets:
    - name: dhi-pull-secret
```

> [!IMPORTANT]
> 
> The `anyuid` SCC allows running as any UID including root. Only use this for
> temporary debugging — never in production workloads.

### Option 3: Use `oc debug` or ephemeral containers

For distroless runtime images with no shell, use OpenShift-native debugging
tools instead of `docker debug` (which only works with Docker Engine, not with
CRI-O on OpenShift).

Use `oc debug` to create a copy of a pod with a debug shell:

```console
# Create a debug pod based on a deployment
oc debug deployment/nginx-dhi

# Override the image to use a -dev variant with a shell
oc debug deployment/nginx-dhi --image=YOUR_ORG/dhi-node:24-alpine3.23-dev
```

Use ephemeral containers (OpenShift 4.12+ / Kubernetes 1.25+):

```console
kubectl debug -it <pod-name> --image=YOUR_ORG/dhi-node:24-alpine3.23-dev \
    --target=app -- sh
```

This attaches a temporary debug container to a running pod without restarting
it, sharing the pod’s process namespace.

> [!NOTE]
> 
> `docker debug` is a Docker Desktop/CLI feature for local development. It is
> not available on OpenShift clusters, which use CRI-O as their container
> runtime.
