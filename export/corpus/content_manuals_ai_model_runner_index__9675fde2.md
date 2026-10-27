---
title: Docker Model Runner
linkTitle: Model Runner
params:
  sidebar:
    group: AI
weight: 30
description: Learn how to use Docker Model Runner to manage and run AI models.
keywords: Docker, ai, model runner, docker desktop, docker engine, llm, openai, ollama, llama.cpp, vllm, diffusers, cpu, nvidia, cuda, amd, rocm, vulkan, cline, continue, cursor, image generation, stable diffusion
aliases:
  - /desktop/features/model-runner/
  - /model-runner/
---

{{< summary-bar feature_name="Docker Model Runner" >}}

Docker Model Runner (DMR) makes it easy to manage, run, and
deploy AI models using Docker. Designed for developers,
Docker Model Runner streamlines the process of pulling, running, and serving
large language models (LLMs) and other AI models directly from Docker Hub,
any OCI-compliant registry, or [Hugging Face](https://huggingface.co/).

With seamless integration into Docker Desktop and Docker
Engine, you can serve models via OpenAI and Ollama-compatible APIs, package GGUF files as
OCI Artifacts, and interact with models from both the command line and graphical
interface.

Whether you're building generative AI applications, experimenting with machine
learning workflows, or integrating AI into your software development lifecycle,
Docker Model Runner provides a consistent, secure, and efficient way to work
with AI models locally.

## Key features

- [Pull and push models to and from Docker Hub or any OCI-compliant registry](https://hub.docker.com/u/ai)
- [Pull models from Hugging Face](https://huggingface.co/)
- Serve models on [OpenAI and Ollama-compatible APIs](api-reference.md) for easy integration with existing apps
- Support for [llama.cpp, vLLM, and Diffusers inference engines](inference-engines.md) (vLLM and Diffusers on Linux with NVIDIA GPUs)
- [Generate images from text prompts](inference-engines.md#diffusers) using Stable Diffusion models with the Diffusers backend
- Package GGUF and Safetensors files as OCI Artifacts and publish them to any Container Registry
- Run and interact with AI models directly from the command line or from the Docker Desktop GUI
- [Connect to AI coding tools](ide-integrations.md) like Cline, Continue, Cursor, and Aider
- [Configure context size and model parameters](configuration.md) to tune performance
- [Set up Open WebUI](openwebui-integration.md) for a ChatGPT-like web interface
- Manage local models and display logs
- Display prompt and response details
- Conversational context support for multi-turn interactions

## Requirements

See [platform requirements](requirements.md).

## How Docker Model Runner works

See [runtime behavior, engines, and context size](runtime-and-privacy.md).

### Inference engines

See [inference engines](runtime-and-privacy.md#inference-engines).

### Context size

See [context size](runtime-and-privacy.md#context-size).

## Known issues

See [Model Runner diagnostics](diagnose.md#known-issues).

### `docker model` is not recognised

See [plugin discovery](diagnose.md#docker-model-is-not-recognised).

## Privacy and data collection

See [privacy and data collection](runtime-and-privacy.md#privacy-and-data-collection).

## Share feedback

Thanks for trying out Docker Model Runner. To report bugs or request features, [open an issue on GitHub](https://github.com/docker/model-runner/issues). You can also give feedback through the **Give feedback** link next to the **Enable Docker Model Runner** setting.

## Next steps

- [Get started with DMR](get-started.md) - Enable DMR and run your first model
- [API reference](api-reference.md) - OpenAI and Ollama-compatible API documentation
- [Configuration options](configuration.md) - Context size and runtime parameters
- [Inference engines](inference-engines.md) - llama.cpp, vLLM, and Diffusers details
- [IDE integrations](ide-integrations.md) - Connect Cline, Continue, Cursor, and more
- [Open WebUI integration](openwebui-integration.md) - Set up a web chat interface
