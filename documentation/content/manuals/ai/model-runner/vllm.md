---
title: Use vLLM
description: Use vLLM with Docker Model Runner.
---

## Prerequisites

Review the [platform requirements](requirements.md). See [engine management](engine-management.md) for installation commands, packaging, and troubleshooting.

## vLLM

[vLLM](https://github.com/vllm-project/vllm) is a high-performance inference
engine optimized for production workloads with high throughput requirements.

### Platform support

| Platform | GPU | Support status |
|----------|-----|----------------|
| Linux x86_64 | NVIDIA CUDA | Supported |
| Windows with WSL2 | NVIDIA CUDA | Supported (Docker Desktop 4.54+) |
| macOS | - | Not supported |
| Linux ARM64 | - | Not supported |
| AMD GPUs | - | Not supported |

> [!IMPORTANT]
> vLLM requires an NVIDIA GPU with CUDA support. It does not support CPU-only
> inference.

### Model format: Safetensors

vLLM works with models in Safetensors format, which is the standard format for
HuggingFace models. These models typically use more memory than quantized GGUF
models but may offer better quality and faster inference on powerful hardware.

### Setting up vLLM

#### Docker Engine (Linux)

Install the Model Runner with vLLM backend:

```console
$ docker model install-runner --backend vllm --gpu cuda
```

Verify the installation:

```console
$ docker model status
Docker Model Runner is running

Status:
llama.cpp: running llama.cpp version: c22473b
vllm: running vllm version: 0.11.0
```

#### Docker Desktop (Windows with WSL2)

1. Ensure you have:
   - Docker Desktop 4.54 or later (minimum version for vLLM support)
   - NVIDIA GPU with updated drivers
   - WSL2 enabled

2. Install vLLM backend:
   ```console
   $ docker model install-runner --backend vllm --gpu cuda
   ```

### Running models with vLLM

vLLM models are typically tagged with `-vllm` suffix:

```console
$ docker model run ai/smollm2-vllm
```

To specify the vLLM backend explicitly:

```console
$ docker model run ai/model --backend vllm
```

### vLLM API endpoints

When using vLLM, specify the engine in the API path:

```text
POST /engines/vllm/v1/chat/completions
```

### vLLM configuration

#### HuggingFace overrides

Use `--hf_overrides` to pass model configuration overrides:

```console
$ docker model configure --hf_overrides '{"max_model_len": 8192}' ai/model-vllm
```

#### Common vLLM settings

| Setting | Description | Example |
|---------|-------------|---------|
| `max_model_len` | Maximum context length | 8192 |
| `gpu_memory_utilization` | Fraction of GPU memory to use | 0.9 |
| `tensor_parallel_size` | GPUs for tensor parallelism | 2 |

### vLLM and llama.cpp performance comparison

| Scenario | Recommended engine |
|----------|-------------------|
| Single user, local development | llama.cpp |
| Multiple concurrent requests | vLLM |
| Limited GPU memory | llama.cpp (with quantization) |
| Maximum throughput | vLLM |
| CPU-only system | llama.cpp |
| Apple Silicon Mac | llama.cpp |
| Production deployment | vLLM (if hardware supports it) |

## Configuration and API reference

See [configuration options](configuration.md) and the [API reference](api-reference.md).
