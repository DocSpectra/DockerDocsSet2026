---
title: Use llama.cpp
description: Use llama.cpp with Docker Model Runner.
---

## Prerequisites

Review the [platform requirements](requirements.md). See [engine management](engine-management.md) for installation commands, packaging, and troubleshooting.

## llama.cpp

[llama.cpp](https://github.com/ggerganov/llama.cpp) is the default inference
engine in Docker Model Runner. It's designed for efficient local inference and
supports a wide range of hardware configurations.

### Platform support

| Platform | GPU support | Notes |
|----------|-------------|-------|
| macOS (Apple Silicon) | Metal | Automatic GPU acceleration |
| Windows (x64) | NVIDIA CUDA | Requires NVIDIA drivers 576.57+ |
| Windows (ARM64) | Adreno OpenCL | Qualcomm 6xx series and later |
| Linux (x64) | NVIDIA, AMD, Vulkan | Multiple backend options |
| Linux | CPU only | Works on any x64/ARM64 system |

### Model format: GGUF

llama.cpp uses the GGUF format, which supports efficient quantization for reduced
memory usage without significant quality loss.

#### Quantization levels

| Quantization | Bits per weight | Memory usage | Quality |
|--------------|-----------------|--------------|---------|
| Q2_K | ~2.5 | Lowest | Reduced |
| Q3_K_M | ~3.5 | Minimal | Acceptable |
| Q4_K_M | ~4.5 | Low | Good |
| Q5_K_M | ~5.5 | Moderate | Excellent |
| Q6_K | ~6.5 | Higher | Excellent |
| Q8_0 | 8 | High | Near-original |
| F16 | 16 | Highest | Original |

**Recommended**: Q4_K_M offers the best balance of quality and memory usage for
most use cases.

#### Pulling quantized models

Models on Docker Hub often include quantization in the tag:

```console
$ docker model pull ai/llama3.2:3B-Q4_K_M
```

### Using llama.cpp

llama.cpp is the default engine. No special configuration is required:

```console
$ docker model run ai/smollm2
```

To explicitly specify llama.cpp when running models:

```console
$ docker model run ai/smollm2 --backend llama.cpp
```

### llama.cpp API endpoints

When using llama.cpp, API calls use the llama.cpp engine path:

```text
POST /engines/llama.cpp/v1/chat/completions
```

Or without the engine prefix:

```text
POST /engines/v1/chat/completions
```

## Configuration and API reference

See [configuration options](configuration.md) and the [API reference](api-reference.md).
