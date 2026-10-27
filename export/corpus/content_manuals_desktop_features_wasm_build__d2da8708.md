---
title: Build and push a Wasm module
---

> [!IMPORTANT]
>
> Wasm workloads are deprecated and will be removed in a future Docker Desktop release. This feature is no longer actively maintained. 

See [Image store capabilities](/manuals/engine/storage/image-store-capabilities.md) and [Wasm runtime and platform options](wasm-runtime-options.md).

## Building and pushing a Wasm module

1. Create a Dockerfile that builds your Wasm application.

   Exactly how to do this varies depending on the programming language you use.

2. In a separate stage in your `Dockerfile`, extract the module and set it as
   the `ENTRYPOINT`.

   ```dockerfile
   # syntax=docker/dockerfile:1
   FROM scratch
   COPY --from=build /build/hello_world.wasm /hello_world.wasm
   ENTRYPOINT [ "/hello_world.wasm" ]
   ```

3. Build and push the image specifying the `wasi/wasm` architecture. Buildx
   makes this easy to do in a single command.

   ```console
   $ docker buildx build --platform wasi/wasm -t username/hello-world .
   ...
   => exporting to image                                                                             0.0s
   => => exporting layers                                                                            0.0s
   => => exporting manifest sha256:2ca02b5be86607511da8dc688234a5a00ab4d58294ab9f6beaba48ab3ba8de56  0.0s
   => => exporting config sha256:a45b465c3b6760a1a9fd2eda9112bc7e3169c9722bf9e77cf8c20b37295f954b    0.0s
   => => naming to docker.io/username/hello-world:latest                                            0.0s
   => => unpacking to docker.io/username/hello-world:latest                                         0.0s
   $ docker push username/hello-world
   ```
