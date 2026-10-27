---
title: Configure OpenShift image pulls for DHI
description: Create an image pull secret and link it to a service account.
---

Before you begin, review [OpenShift security constraints](../core-concepts/openshift.md) and [DHI registry authentication](authenticate.md).

## Pull DHI images into OpenShift

Before deploying, create an image pull secret so your OpenShift cluster can
authenticate to the DHI registry or your mirrored repository on Docker Hub.

### Create an image pull secret

```console
oc create secret docker-registry dhi-pull-secret \
    --docker-server=docker.io \
    --docker-username=<your-docker-username> \
    --docker-password=<your-docker-access-token> \
    --docker-email=<your-email>
```

If you’re pulling directly from `dhi.io` instead of a mirrored repository, set
`--docker-server=dhi.io`.

### Link the secret to a service account

Link the pull secret to the `default` service account in your project so that
all deployments can pull DHI images automatically:

```console
oc secrets link default dhi-pull-secret --for=pull
```

To use the secret with a specific service account instead:

```console
oc secrets link <service-account-name> dhi-pull-secret --for=pull
```
