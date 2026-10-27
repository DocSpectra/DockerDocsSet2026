---
title: Wasm runtime and platform options
---

> [!IMPORTANT]
>
> Wasm workloads are deprecated and will be removed in a future Docker Desktop release. This feature is no longer actively maintained.

The `--runtime` and `--platform` flags:

- `--runtime=io.containerd.wasmedge.v1`: Informs the Docker engine that you want
  to use the Wasm containerd shim instead of the standard Linux container
  runtime
- `--platform=wasi/wasm`: Specifies the architecture of the image you want to
  use. By leveraging a Wasm architecture, you don’t need to build separate
  images for the different machine architectures. The Wasm runtime takes care of
  the final step of converting the Wasm binary to machine instructions.
