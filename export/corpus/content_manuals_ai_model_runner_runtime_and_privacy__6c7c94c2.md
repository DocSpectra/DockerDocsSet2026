---
title: Model Runner runtime and privacy
description: Model caching, inference engines, context size, and data collection.
---

## How Docker Model Runner works

Models are pulled from Docker Hub, an OCI-compliant registry, or
[Hugging Face](https://huggingface.co/) the first time you use them and are
stored locally. They load into memory only at runtime when a request is made,
and unload when not in use to optimize resources. Because models can be large,
the initial pull may take some time. After that, they're cached locally for
faster access. You can interact with the model using
[OpenAI and Ollama-compatible APIs](api-reference.md).

### Inference engines

Docker Model Runner supports three inference engines:

| Engine | Best for | Model format |
|--------|----------|--------------|
| [llama.cpp](inference-engines.md#llamacpp) | Local development, resource efficiency | GGUF (quantized) |
| [vLLM](inference-engines.md#vllm) | Production, high throughput | Safetensors |
| [Diffusers](inference-engines.md#diffusers) | Image generation (Stable Diffusion) | Safetensors |

llama.cpp is the default engine and works on all platforms. vLLM requires NVIDIA GPUs and is supported on Linux x86_64 and Windows with WSL2. Diffusers enables image generation and requires NVIDIA GPUs on Linux (x86_64 or ARM64). See [Inference engines](inference-engines.md) for detailed comparison and setup.

### Context size

Models have a configurable context size (context length) that determines how many tokens they can process. The default varies by model but is typically 2,048-8,192 tokens. You can adjust this per-model:

```console
$ docker model configure --context-size 8192 ai/qwen2.5-coder
```

See [Configuration options](configuration.md) for details on context size and other parameters.

> [!TIP]
>
> Using Testcontainers or Docker Compose?
> [Testcontainers for Java](https://java.testcontainers.org/modules/docker_model_runner/)
> and [Go](https://golang.testcontainers.org/modules/dockermodelrunner/), and
> [Docker Compose](/manuals/ai/compose/models-and-compose.md) support Docker
> Model Runner.

## Privacy and data collection

Docker Model Runner respects your privacy settings in Docker Desktop. Data collection is controlled by the **Send usage statistics** setting:

- **Disabled**: No usage data is collected
- **Enabled**: Only minimal, non-personal data is collected:
  - [Model names](https://github.com/docker/model-runner/blob/eb76b5defb1a598396f99001a500a30bbbb48f01/pkg/metrics/metrics.go#L96) (via HEAD requests to Docker Hub)
  - User agent information
  - Whether requests originate from the host or containers

When using Docker Model Runner with Docker Engine, HEAD requests to Docker Hub are made to track model names, regardless of any settings.

No prompt content, responses, or personally identifiable information is ever collected.

