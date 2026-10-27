---
title: Connect Buildx to manually managed BuildKit in Kubernetes
---

For shared options and behavior, see [remote driver reference](remote-reference.md).
For shared procedures, see [Select a builder](../selection.md) and
[Load build results](../image-loading.md).

## Example: Remote BuildKit in Kubernetes

This guide will show you how to create a setup similar to the `kubernetes`
driver by manually creating a BuildKit `Deployment`. While the `kubernetes`
driver will do this under-the-hood, it might sometimes be desirable to scale
BuildKit manually. Additionally, when executing builds from inside Kubernetes
pods, the Buildx builder will need to be recreated from within each pod or
copied between them.

1. Create a Kubernetes deployment of `buildkitd` by following the instructions
   [in the BuildKit documentation](https://github.com/moby/buildkit/tree/master/examples/kubernetes).

   Create certificates for the BuildKit daemon and client using the
   [create-certs.sh](https://github.com/moby/buildkit/blob/master/examples/kubernetes/create-certs.sh),
   script and create a deployment of BuildKit pods with a service that connects
   to them.

2. Assuming that the service is called `buildkitd`, create a remote builder in
   Buildx, ensuring that the listed certificate files are present:

   ```console
   $ docker buildx create \
     --name remote-kubernetes \
     --driver remote \
     --driver-opt cacert=${PWD}/.certs/client/ca.pem,cert=${PWD}/.certs/client/cert.pem,key=${PWD}/.certs/client/key.pem \
     tcp://buildkitd.default.svc:1234
   ```

Note that this only works internally, within the cluster, since the BuildKit
setup guide only creates a `ClusterIP` service. To access a builder remotely,
you can set up and use an ingress, which is outside the scope of this guide.

### Debug a remote builder in Kubernetes

If you're having trouble accessing a remote builder deployed in Kubernetes, you
can use the `kube-pod://` URL scheme to connect directly to a BuildKit pod
through the Kubernetes API. Note that this method only connects to a single pod
in the deployment.

```console
$ kubectl get pods --selector=app=buildkitd -o json | jq -r '.items[].metadata.name'
buildkitd-XXXXXXXXXX-xxxxx
$ docker buildx create \
  --name remote-container \
  --driver remote \
  kube-pod://buildkitd-XXXXXXXXXX-xxxxx
```

Alternatively, use the port forwarding mechanism of `kubectl`:

```console
$ kubectl port-forward svc/buildkitd 1234:1234
```

Then you can point the remote driver at `tcp://localhost:1234`.

