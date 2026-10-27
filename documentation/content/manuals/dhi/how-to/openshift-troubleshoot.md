---
title: Troubleshoot DHI on OpenShift
description: Resolve permissions, SCC, passwd, ports, authentication, and Dockerfile errors.
---

Before you begin, review [OpenShift security constraints](../core-concepts/openshift.md) and [DHI registry authentication](authenticate.md).

See [file permission preparation](openshift-permissions.md), [UID handling](openshift-users.md), and [image pull setup](openshift-pull.md) for shared procedures.

## Common issues and solutions

**Pod fails to start with “container has runAsNonRoot and image has group or
user ID set to root.”** This happens when deploying a DHI `-dev` variant with
the default `restricted-v2` SCC. Either use the runtime variant instead, or
grant the `anyuid` SCC to the service account.

**Application cannot write to a directory.** The arbitrary UID assigned by
OpenShift doesn’t have write permissions. This is the most common issue with DHI
on OpenShift. All writable paths must be owned by GID 0 with group write
permissions. Fix this in the build stage:
`chgrp -R 0 /path && chmod -R g=u /path`, then `COPY --chown=<UID>:0` into the
runtime stage.

**Application fails with “user not found” or “no matching entries in passwd
file.”** Some applications require a valid `/etc/passwd` entry. OpenShift 4.x
automatically injects the arbitrary UID into `/etc/passwd` in most cases. If
your application still fails, use the passwd-injection pattern (requires a `-dev`
variant) or use the `nonroot` SCC to run with the image’s built-in UID.

**Pod fails to bind to port 80 or 443.** Ports lower than 1024 require root
privileges. DHI images use unprivileged ports by default (for example, Nginx
uses 8080). Configure your OpenShift Service to map the external port to the
container’s unprivileged port:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-dhi
spec:
  ports:
    - port: 80
      targetPort: 8080
  selector:
    app: nginx-dhi
```

**ImagePullBackOff with “unauthorized: authentication required.”** Verify the
pull secret is correctly configured and linked to the service account. Check
with `oc get secret dhi-pull-secret` and `oc describe sa default`.

**Dockerfile build fails with “exec: not found” in runtime stage.** You are
using `RUN` in a distroless runtime stage. DHI runtime images have no shell, so
`RUN` commands cannot execute. Move all `RUN` commands to the `-dev` build stage
and use `COPY --chown` to transfer results.
