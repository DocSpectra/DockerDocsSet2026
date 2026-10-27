---
title: Inference engines
description: Learn about the llama.cpp, vLLM, and Diffusers inference engines in Docker Model Runner.
weight: 50
keywords: Docker, ai, model runner, llama.cpp, vllm, diffusers, inference, gguf, safetensors, cuda, gpu, image generation, stable diffusion
---

Docker Model Runner supports three inference engines: **llama.cpp**, **vLLM**, and **Diffusers**.
Each engine has different strengths, supported platforms, and model format
requirements. This guide helps you choose the right engine and configure it for
your use case.

## Engine comparison

| Feature | llama.cpp | vLLM | Diffusers                           |
|---------|-----------|------|-------------------------------------|
| **Model formats** | GGUF | Safetensors, HuggingFace | DDUF                                |
| **Platforms** | All (macOS, Windows, Linux) | Linux x86_64 only | Linux (x86_64, ARM64)               |
| **GPU support** | NVIDIA, AMD, Apple Silicon, Vulkan | NVIDIA CUDA only | NVIDIA CUDA only                    |
| **CPU inference** | Yes | No | No                                  |
| **Quantization** | Built-in (Q4, Q5, Q8, etc.) | Limited | Limited                             |
| **Memory efficiency** | High (with quantization) | Moderate | Moderate                            |
| **Throughput** | Good | High (with batching) | Good                                |
| **Best for** | Local development, resource-constrained environments | Production, high throughput | Image generation                    |
| **Use case** | Text generation (LLMs) | Text generation (LLMs) | Image generation (Stable Diffusion) |

## llama.cpp

See [Use llama.cpp](llama-cpp.md).

## vLLM

See [Use vLLM](vllm.md).

## Diffusers

See [Generate images with Diffusers](diffusers.md).

## Running multiple engines

See [running multiple engines](engine-management.md#running-multiple-engines).

## Managing inference engines

See [engine management](engine-management.md#managing-inference-engines).

## Packaging models for each engine

See [packaging models](engine-management.md#packaging-models-for-each-engine).

## Troubleshooting

See [engine troubleshooting](engine-management.md#troubleshooting).

## What's next

- [Configuration options](configuration.md) - Detailed parameter reference
- [API reference](api-reference.md) - API documentation
- [GPU support](/manuals/desktop/features/gpu.md) - GPU configuration for Docker Desktop
