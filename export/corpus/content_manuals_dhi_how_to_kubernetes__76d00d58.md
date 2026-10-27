---
title: Use Docker Hardened Images with Kubernetes
description: Create and test image pull secrets for DHI registries.
---

## Use with Kubernetes

When deploying Docker Hardened Images to Kubernetes, the process is similar to
using any other container image with one key difference: you must configure
image pull secrets to authenticate to the DHI registry. This applies whether
you're pulling directly from `dhi.io`, from a mirror on Docker Hub, or from
your own third-party registry.

### Create an image pull secret

You can create an image pull secret using either an access token or Docker Desktop credentials.

For the `--docker-server` value:

- Use `dhi.io` for community images pulled directly from Docker Hardened Images
- Use `docker.io` for mirrored repositories on Docker Hub
- Use your registry's hostname for third-party registries

#### Using an access token

Create a secret using a [Personal Access Token
(PAT)](../../security/access-tokens.md) or [Organization Access Token
(OAT)](../../enterprise/security/access-tokens.md). Ensure the token has at
least read-only access to the repositories.

```console
$ kubectl create -n <kubernetes namespace> secret docker-registry <secret name> --docker-server=<registry server> \
        --docker-username=<registry user> --docker-password=<access token> \
        --docker-email=<registry email>
```

#### Using Docker Desktop credentials

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

### Test the image pull secret

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

## Create a Kubernetes secret for Helm chart image pulls

You need to create a Kubernetes secret for pulling images from `dhi.io`, Docker
Hub, or your own registry. This is necessary because Docker Hardened Image
repositories require authentication. If you mirror the images to your own
registry, you still need to create this secret if the registry requires
authentication.

1. For `dhi.io` or Docker Hub, create a [personal access token
   (PAT)](/security/access-tokens/) using your Docker account or an
   [organization access token (OAT)](/enterprise/security/access-tokens/).
   Ensure the token has at least read-only access to the Docker Hardened Image
   repositories.
2. Create a secret in Kubernetes using the following command. Replace `<your-secret-name>`, `<your-username>`,
   `<your-personal-access-token>`, and `<your-email>` with your own values.

   > [!NOTE]
   >
   > You need to create this secret in each Kubernetes namespace that uses a
   > DHI. If you've mirror your DHIs to another registry, replace
   > `dhi.io` with your registry's hostname. Replace
   > `<your-username>`, `<your-access-token>`, and `<your-email>` with your own
   > values. `<your-username>` is Docker ID if using a PAT or your organization
   > name if using an OAT. `<your-secret-name>` is a name you choose for the
   > secret.

   ```console
   $ kubectl create secret docker-registry <your-secret-name> \
       --docker-server=dhi.io \
       --docker-username=<your-username> \
       --docker-password=<your-access-token> \
       --docker-email=<your-email>
   ```

   For example:

    ```console
    $ kubectl create secret docker-registry dhi-pull-secret \
        --docker-server=dhi.io \
        --docker-username=docs \
        --docker-password=dckr_pat_12345 \
        --docker-email=moby@example.com
   ```
