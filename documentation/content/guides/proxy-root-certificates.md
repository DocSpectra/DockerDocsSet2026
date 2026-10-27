---
title: Install a proxy root certificate in Docker images
---

To enable containers to use and trust the Zscaler proxy, embed the certificate
in the image and configure the image's trust store. Installing certificates at
image build time is the preferred approach, as it removes the need for
configuration during startup and provides an auditable, consistent environment.

## Build with the certificate

To install these certificates when building images, copy the certificate into
the build container and update the trust store. An example Dockerfile looks
like this:

```dockerfile
FROM debian:bookworm
COPY zscaler-root-ca.crt /usr/local/share/ca-certificates/zscaler-root-ca.crt
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates
```

Here, `zscaler-root-ca.crt` is the root certificate, located at the root of the
build context (often within the application's Git repository).

If you use an artifact repository, you can fetch the certificate directly using
the `ADD` instruction. You can also use the `--checksum` flag to verify that
the content digest of the certificate is correct.

```dockerfile
FROM debian:bookworm
ADD --checksum=sha256:24454f830cdb571e2c4ad15481119c43b3cafd48dd869a9b2945d1036d1dc68d \
    https://artifacts.example/certs/zscaler-root-ca.crt /usr/local/share/ca-certificates/zscaler-root-ca.crt
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates
```

For general build-stage context, see [Multi-stage builds](/manuals/build/building/multi-stage.md).

## Multi-stage builds

For multi-stage builds where certificates are needed in the final runtime
image, ensure the certificate installation occurs in the final stage.

```dockerfile
FROM debian:bookworm AS build
WORKDIR /build
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    git
RUN --mount=target=. cmake -B output/

FROM debian:bookworm-slim AS final
ADD --checksum=sha256:24454f830cdb571e2c4ad15481119c43b3cafd48dd869a9b2945d1036d1dc68d \
    https://artifacts.example/certs/zscaler-root-ca.crt /usr/local/share/ca-certificates/zscaler-root-ca.crt
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates
WORKDIR /app
COPY --from=build /build/output/bin .
ENTRYPOINT ["/app/bin"]
```
