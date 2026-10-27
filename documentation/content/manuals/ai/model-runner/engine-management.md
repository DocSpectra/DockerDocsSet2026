---
title: Manage Model Runner inference engines
description: Run multiple engines, install and reinstall backends, package models, and troubleshoot engines.
---

## Running multiple engines

You can run llama.cpp, vLLM, and Diffusers simultaneously. Docker Model Runner routes
requests to the appropriate engine based on the model or explicit engine selection.

Check which engines are running:

```console
$ docker model status
Docker Model Runner is running

Status:
llama.cpp: running llama.cpp version: 34ce48d
mlx: not installed
sglang: sglang package not installed
vllm: running vllm version: 0.11.0
diffusers: running diffusers version: 0.36.0
```

### Engine-specific API paths

| Engine | API path | Use case |
|--------|----------|----------|
| llama.cpp | `/engines/llama.cpp/v1/chat/completions` | Text generation |
| vLLM | `/engines/vllm/v1/chat/completions` | Text generation |
| Diffusers | `/engines/diffusers/v1/images/generations` | Image generation |
| Auto-select | `/engines/v1/chat/completions` | Text generation (auto-selects engine) |

## Managing inference engines

### Install an engine

```console
$ docker model install-runner --backend <engine> [--gpu <type>]
```

Options:
- `--backend`: `llama.cpp`, `vllm`, or `diffusers`
- `--gpu`: `cuda`, `rocm`, `vulkan`, or `metal` (depends on platform)

### Reinstall an engine

```console
$ docker model reinstall-runner --backend <engine>
```

### Check engine status

```console
$ docker model status
```

### View engine logs

```console
$ docker model logs
```

## Packaging models for each engine

### Package a GGUF model (llama.cpp)

```console
$ docker model package --gguf ./model.gguf --push myorg/mymodel:Q4_K_M
```

### Package a Safetensors model (vLLM)

```console
$ docker model package --safetensors ./model/ --push myorg/mymodel-vllm
```

## Troubleshooting

### vLLM won't start

1. Verify NVIDIA GPU is available:
   ```console
   $ nvidia-smi
   ```

2. Check Docker has GPU access:
   ```console
   $ docker run --rm --gpus all nvidia/cuda:12.0-base nvidia-smi
   ```

3. Verify you're on a supported platform (Linux x86_64 or Windows WSL2).

### llama.cpp is slow

1. Ensure GPU acceleration is working (check logs for Metal/CUDA messages).

2. Try a more aggressive quantization:
   ```console
   $ docker model pull ai/model:Q4_K_M
   ```

3. Reduce context size:
   ```console
   $ docker model configure --context-size 2048 ai/model
   ```

### Out of memory errors

1. Use a smaller quantization (Q4 instead of Q8).
2. Reduce context size.
3. For vLLM, adjust `gpu_memory_utilization`:
   ```console
   $ docker model configure --hf_overrides '{"gpu_memory_utilization": 0.8}' ai/model
   ```

