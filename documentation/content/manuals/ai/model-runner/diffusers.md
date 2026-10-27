---
title: Generate images with Diffusers
description: Generate images with Diffusers with Docker Model Runner.
---

## Prerequisites

Review the [platform requirements](requirements.md). See [engine management](engine-management.md) for installation commands, packaging, and troubleshooting.

## Diffusers

[Diffusers](https://github.com/huggingface/diffusers) is an inference engine
for image generation models, including Stable Diffusion. Unlike llama.cpp and
vLLM which focus on text generation with LLMs, Diffusers enables you to generate
images from text prompts.

### Platform support

| Platform | GPU | Support status |
|----------|-----|----------------|
| Linux x86_64 | NVIDIA CUDA | Supported |
| Linux ARM64 | NVIDIA CUDA | Supported |
| Windows | - | Not supported |
| macOS | - | Not supported |

> [!IMPORTANT]
> Diffusers requires an NVIDIA GPU with CUDA support. It does not support
> CPU-only inference.

### Setting up Diffusers

Install the Model Runner with Diffusers backend:

```console
$ docker model reinstall-runner --backend diffusers --gpu cuda
```

Verify the installation:

```console
$ docker model status
Docker Model Runner is running

Status:
llama.cpp: running llama.cpp version: 34ce48d
mlx: not installed
sglang: sglang package not installed
vllm: vLLM binary not found
diffusers: running diffusers version: 0.36.0
```

### Pulling Diffusers models

Pull a Stable Diffusion model:

```console
$ docker model pull stable-diffusion:Q4
```

### Generating images with Diffusers

Diffusers uses an image generation API endpoint. To generate an image:

```console
$ curl -s -X POST http://localhost:12434/engines/diffusers/v1/images/generations \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stable-diffusion:Q4",
    "prompt": "A picture of a nice cat",
    "size": "512x512"
  }' | jq -r '.data[0].b64_json' | base64 -d > image.png
```

This command:
1. Sends a POST request to the Diffusers image generation endpoint
2. Specifies the model, prompt, and output image size
3. Extracts the base64-encoded image from the response
4. Decodes it and saves it as `image.png`

### Diffusers API endpoint

When using Diffusers, specify the engine in the API path:

```text
POST /engines/diffusers/v1/images/generations
```

### Supported parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Required. The model identifier (e.g., `stable-diffusion:Q4`). |
| `prompt` | string | Required. The text description of the image to generate. |
| `size` | string | Image dimensions in `WIDTHxHEIGHT` format (e.g., `512x512`). |

## Configuration and API reference

See [configuration options](configuration.md) and the [API reference](api-reference.md).
