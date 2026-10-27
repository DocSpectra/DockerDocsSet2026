---
title: Deploy DHI Nginx on OpenShift
description: Build an Nginx image with writable paths and deploy it with a restricted security context.
---

Before you begin, review [OpenShift security constraints](../core-concepts/openshift.md) and [DHI registry authentication](authenticate.md).

Follow [image pull setup](openshift-pull.md) and [file permission preparation](openshift-permissions.md) before using this example.

## Example: Nginx for OpenShift

```dockerfile
# Build stage — has a shell, can run commands
FROM YOUR_ORG/dhi-nginx:1.29-alpine3.23-dev AS build

# Copy custom config and set root group ownership
COPY nginx.conf /tmp/nginx.conf
COPY default.conf /tmp/default.conf

# Prepare writable directories with GID 0
# (Nginx needs to write to cache, logs, and PID file locations)
RUN mkdir -p /tmp/nginx-cache /tmp/nginx-run && \
    chgrp -R 0 /tmp/nginx-cache /tmp/nginx-run && \
    chmod -R g=u /tmp/nginx-cache /tmp/nginx-run

# Runtime stage — distroless, NO shell, NO RUN commands
FROM YOUR_ORG/dhi-nginx:1.29-alpine3.23

COPY --from=build --chown=65532:0 /tmp/nginx.conf /etc/nginx/nginx.conf
COPY --from=build --chown=65532:0 /tmp/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build --chown=65532:0 /tmp/nginx-cache /var/cache/nginx
COPY --from=build --chown=65532:0 /tmp/nginx-run /var/run
```

Deploy to OpenShift:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-dhi
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-dhi
  template:
    metadata:
      labels:
        app: nginx-dhi
    spec:
      containers:
        - name: nginx
          image: YOUR_ORG/dhi-nginx:1.29-alpine3.23
          ports:
            - containerPort: 8080
          securityContext:
            allowPrivilegeEscalation: false
            runAsNonRoot: true
            seccompProfile:
              type: RuntimeDefault
            capabilities:
              drop:
                - ALL
      imagePullSecrets:
        - name: dhi-pull-secret
```

DHI Nginx listens on port 8080 by default (not 80), which is compatible with
the non-root requirement. No SCC changes are needed.
