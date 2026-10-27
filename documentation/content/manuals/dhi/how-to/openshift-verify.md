---
title: Verify a DHI deployment on OpenShift
description: Check SCC, runtime UID, distroless behavior, and scan the deployed image.
---

Before you begin, review [OpenShift security constraints](../core-concepts/openshift.md) and [DHI registry authentication](authenticate.md).

## Verify your deployment

After deploying a DHI image to OpenShift, verify the security configuration.

### Check the assigned SCC

```console
oc get pods -o 'custom-columns=NAME:.metadata.name,SCC:.metadata.annotations.openshift\.io/scc'
```

Runtime DHI images should show `restricted-v2` (or `nonroot` if you configured
it).

### Check the running UID

```console
oc exec <pod-name> -- id
```

With the `restricted-v2` SCC, you should see output like:

```text
uid=1000650000 gid=0(root) groups=0(root),1000650000
```

The UID is from the project’s allocated range, and the primary GID is always 0
(root group). With the `nonroot` SCC and `runAsUser: 65532`, you would see
`uid=65532`.

### Confirm the image is distroless

```console
oc exec <pod-name> -- sh -c "echo hello"
```

For runtime (non-dev) DHI images, this command should fail with an error
indicating that `sh` was not found in `$PATH`. The exact error format varies
between CRI-O versions.

### Scan the deployed image

Use Docker Scout to verify the security posture of the deployed image (run this
from your local machine, not on the cluster):

```console
docker scout cves YOUR_ORG/dhi-nginx:1.29-alpine3.23
docker scout quickview YOUR_ORG/dhi-nginx:1.29-alpine3.23
```
