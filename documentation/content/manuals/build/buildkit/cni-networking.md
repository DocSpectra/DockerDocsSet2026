---
title: Use CNI networking with BuildKit
---

Before following these steps, see [Apply a BuildKit configuration](configuration.md).

## CNI networking

CNI networking for builders can be useful for dealing with network port
contention during concurrent builds. CNI is [not yet](https://github.com/moby/buildkit/issues/28)
available in the default BuildKit image. But you can create your own image that
includes CNI support.

The following Dockerfile example shows a custom BuildKit image with CNI support.
It uses the [CNI config for integration tests](https://github.com/moby/buildkit/blob/master//hack/fixtures/cni.json)
in BuildKit as an example. Feel free to include your own CNI configuration.

```dockerfile
# syntax=docker/dockerfile:1

ARG BUILDKIT_VERSION=v{{% param "buildkit_version" %}}
ARG CNI_VERSION=v1.0.1

FROM --platform=$BUILDPLATFORM alpine AS cni-plugins
RUN apk add --no-cache curl
ARG CNI_VERSION
ARG TARGETOS
ARG TARGETARCH
WORKDIR /opt/cni/bin
RUN curl -Ls https://github.com/containernetworking/plugins/releases/download/$CNI_VERSION/cni-plugins-$TARGETOS-$TARGETARCH-$CNI_VERSION.tgz | tar xzv

FROM moby/buildkit:${BUILDKIT_VERSION}
ARG BUILDKIT_VERSION
RUN apk add --no-cache iptables
COPY --from=cni-plugins /opt/cni/bin /opt/cni/bin
ADD https://raw.githubusercontent.com/moby/buildkit/${BUILDKIT_VERSION}/hack/fixtures/cni.json /etc/buildkit/cni.json
```

Now you can build this image, and create a builder instance from it using
[the `--driver-opt image` option](/reference/cli/docker/buildx/create/#driver-opt):

```console
$ docker buildx build --tag buildkit-cni:local --load .
$ docker buildx create --use --bootstrap \
  --name mybuilder \
  --driver docker-container \
  --driver-opt "image=buildkit-cni:local" \
  --buildkitd-flags "--oci-worker-net=cni"
```


