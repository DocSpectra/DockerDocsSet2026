---
title: Use Docker Hardened Images with Kubernetes
linktitle: Use with Kubernetes
description: Configure image pull secrets and test Docker Hardened Image pulls in Kubernetes.
weight: 33
---

For OpenShift-specific steps, see [Use Docker Hardened Images with Red Hat
OpenShift](/guides/dhi-openshift/). For Helm deployments, see [Use a Helm
chart](./helm.md).

## Before you begin

When deploying Docker Hardened Images to Kubernetes, the process is similar to
using any other container image with one key difference: you must configure
image pull secrets to authenticate to the DHI registry. This applies whether
you're pulling directly from `dhi.io`, from a mirror on Docker Hub, or from
your own third-party registry.

## Create an image pull secret

You can create an image pull secret using either an access token or Docker Desktop credentials.

For the `--docker-server` value:

- Use `dhi.io` for community images pulled directly from Docker Hardened Images
- Use `docker.io` for mirrored repositories on Docker Hub
- Use your registry's hostname for third-party registries

### Using an access token

Create a secret using a [Personal Access Token
(PAT)](../../security/access-tokens.md) or [Organization Access Token
(OAT)](../../enterprise/security/access-tokens.md). Ensure the token has at
least read-only access to the repositories.

```console
$ kubectl create -n <kubernetes namespace> secret docker-registry <secret name> --docker-server=<registry server> \
        --docker-username=<registry user> --docker-password=<access token> \
        --docker-email=<registry email>
```

### Using Docker Desktop credentials

If you're already authenticated with Docker Desktop, you can create a secret
using your stored credentials. This method works for registries you've
authenticated to via Docker Desktop (using `docker login <registry>`).

```console
$ NS=<namespace>
$ kubectl create -n ${NS} secret docker-registry dhi-pull-secret \
    --docker-server=<registry server> \
    --docker-username=<registry user> \
    --docker-password="$(echo https://<registry server> | docker-credential-desktop get | jq -r .Secret)" \
    --docker-email=<registry email>
```

This method extracts credentials from Docker Desktop's credential store, avoiding the need to create a separate access token for local development.

## Test the image pull secret

After creating the secret, verify it works by deploying a test pod that
references the secret in its `imagePullSecrets` configuration.

Create a test pod:

```console
kubectl apply --wait -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: dhi-test
  namespace: <kubernetes namespace>
spec:
  containers:
  - name: test
    image: bash:5
    command: [ "sh", "-c", "echo 'Hello from DHI in Kubernetes!'" ]
  imagePullSecrets:
  - name: <secret name>
EOF
```

Check the pod status to ensure it completed successfully:

```console
$ kubectl get -n <kubernetes namespace> pods/dhi-test
```

A successful test shows `Completed` status:

```console
NAME       READY   STATUS      RESTARTS     AGE
dhi-test   0/1     Completed   ...          ...
```

If you see `ErrImagePull` status instead, there's an issue with your secret
configuration:

```console
NAME       READY   STATUS         RESTARTS   AGE
dhi-test   0/1     ErrImagePull   0          ...
```

Verify the pod output matches the expected message:

```console
$ kubectl logs -n <kubernetes namespace> pods/dhi-test
Hello from DHI in Kubernetes!
```

Clean up the test pod:

```console
$ kubectl delete -n <kubernetes namespace> pods/dhi-test
```
