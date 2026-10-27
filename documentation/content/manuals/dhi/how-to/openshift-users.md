---
title: Handle arbitrary and fixed UIDs for DHI on OpenShift
description: Use a passwd wrapper or configure the nonroot SCC for a fixed UID.
---

Before you begin, review [OpenShift security constraints](../core-concepts/openshift.md) and [DHI registry authentication](authenticate.md).

## Handle arbitrary user IDs

OpenShift’s `restricted-v2` SCC assigns a random UID to the container process.
This UID won’t exist in `/etc/passwd` inside the image, but the container will
still run — the process just won’t have a username associated with it.

This can cause issues with applications that:

- Look up the current user’s home directory or username
- Write to directories owned by a specific UID
- Check `/etc/passwd` for the running user

### Add a `passwd` entry for the arbitrary UID

Some applications (notably those using certain Python or Java libraries) require
a valid `/etc/passwd` entry for the running user. You can handle this with a
wrapper entrypoint script.

Because this pattern requires a shell, it only works with DHI `-dev` variants or
with a DHI Enterprise customized image that includes a shell. Prepare the image
in the build stage:

```dockerfile
FROM YOUR_ORG/dhi-python:3.13-alpine3.23-dev AS build
# ... build your application ...

# Make /etc/passwd group-writable so the entrypoint can append to it
RUN chgrp 0 /etc/passwd && chmod g=u /etc/passwd

# Create the entrypoint wrapper
RUN printf '#!/bin/sh\n\
if ! whoami > /dev/null 2>&1; then\n\
  if [ -w /etc/passwd ]; then\n\
    echo "${USER_NAME:-appuser}:x:$(id -u):0:dynamic user:/tmp:/sbin/nologin" >> /etc/passwd\n\
  fi\n\
fi\n\
exec "$@"\n' > /entrypoint.sh && chmod +x /entrypoint.sh

# This pattern requires a -dev variant as runtime (has shell)
FROM YOUR_ORG/dhi-python:3.13-alpine3.23-dev
COPY --from=build --chown=65532:0 /app ./app
COPY --from=build --chown=65532:0 /entrypoint.sh /entrypoint.sh
COPY --from=build --chown=65532:0 /etc/passwd /etc/passwd
USER 65532
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "app/main.py"]
```

> [!NOTE]
> 
> For distroless runtime images (no shell), the passwd-injection pattern is not
> possible. Instead, use the [`nonroot` SCC](#use-the-non-root-scc-for-fixed-uids) to run with the
> image’s built-in UID so the existing `/etc/passwd` entry matches the running
> process. Alternatively, OpenShift 4.x automatically injects the arbitrary UID
> into `/etc/passwd` in most cases, which resolves this for many applications.

## Use the non-root SCC for fixed UIDs

If your application requires running as the specific UID defined in the image
(typically 65532 for DHI), you can use the `nonroot` SCC instead of the default
`restricted-v2`. The `nonroot` SCC uses the `MustRunAsNonRoot` strategy, which
allows any non-zero UID.

> [!IMPORTANT]
> 
> For the `nonroot` SCC to work, the image’s `USER` directive must specify a
> **numeric** UID (for example, `65532`), not a username string like `nonroot`.
> OpenShift cannot verify that a username maps to a non-zero UID. Verify your
> DHI image with:
> `docker inspect YOUR_ORG/dhi-node:24-alpine3.23 --format '{{.Config.User}}'`
> If the output is a string rather than a number, set `runAsUser` explicitly in
> the pod spec.

Create a service account and grant it the `nonroot` SCC:

```console
oc create serviceaccount dhi-nonroot
oc adm policy add-scc-to-user nonroot -z dhi-nonroot
```

Reference the service account in your deployment:

```yaml
spec:
  template:
    spec:
      serviceAccountName: dhi-nonroot
      containers:
        - name: app
          image: YOUR_ORG/dhi-node:24-alpine3.23
          securityContext:
            runAsUser: 65532
            runAsNonRoot: true
            allowPrivilegeEscalation: false
            seccompProfile:
              type: RuntimeDefault
            capabilities:
              drop:
                - ALL
```

Verify the SCC assignment after deployment:

```console
oc get pod <pod-name> -o jsonpath='{.metadata.annotations.openshift\.io/scc}'
```

This should return `nonroot`.

When using the `nonroot` SCC with a fixed UID, the process runs as 65532
(matching the image’s file ownership), so the GID 0 adjustments are not strictly
required for paths already owned by 65532. However, applying `chown <UID>:0` is
still recommended for portability across both `restricted-v2` and `nonroot` SCCs.
