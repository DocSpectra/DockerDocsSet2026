---
title: Set up Model Runner for local clients
description: Shared prerequisites, model selection, and troubleshooting for local Model Runner clients.
---

## Prerequisites

Before configuring any tool:

1. [Enable Docker Model Runner](setup.md#enable-docker-model-runner) in Docker Desktop or Docker Engine.
2. [Enable TCP host access](api-reference.md#enable-host-tcp-access).
3. Pull a model:
   ```console
   $ docker model pull ai/qwen2.5-coder
   ```

> [!TIP]
> 
> The default context size for many models (such as `gpt-oss`) is 4,096 tokens, which is limiting for coding tasks.
> You can repackage it with a larger context window:
>
> ```console
> $ docker model pull gpt-oss
> $ docker model package --from ai/gpt-oss --context-size 32000 gpt-oss:32k
> ```
> Alternatively, models like ai/glm-4.7-flash, ai/qwen2.5-coder, and ai/devstral-small-2
> come with 128K context by default and work without repackaging.

## Common issues

### "Connection refused" errors

1. Ensure Docker Model Runner is enabled and running:
   ```console
   $ docker model status
   ```

2. [Verify TCP access](api-reference.md#verify-host-connectivity).

3. Check if another service is using port 12434.

4. If you run your tool in WSL and want to connect to DMR on the host via `localhost`, this might not directly work. Configuring WSL to use [mirrored networking](https://learn.microsoft.com/en-us/windows/wsl/networking#mirrored-mode-networking) can solve this.

### "Model not found" errors

1. Verify the model is pulled:
   ```console
   $ docker model list
   ```

2. Use the full model name including namespace (e.g., `ai/qwen2.5-coder`, not just `qwen2.5-coder`).

### Slow responses or timeouts

1. For first requests, models need to load into memory. Subsequent requests are faster.

2. Consider using a smaller model or adjusting the context size:
   ```console
   $ docker model configure --context-size 4096 ai/qwen2.5-coder
   ```

3. Check available system resources (RAM, GPU memory).

### CORS errors (web-based tools)

If using browser-based tools, add the origin to CORS allowed origins:

1. Docker Desktop: Settings > AI > CORS Allowed Origins
2. Add your tool's URL (e.g., `http://localhost:3000`)

## Recommended models by use case

| Use case | Recommended model | Notes |
|----------|-------------------|-------|
| Code completion | `ai/qwen3-coder` | Optimized for coding tasks with a large context window |
| Agentic coding | `ai/devstral-small-2` | Good fit for tools such as Claude Code and OpenCode |
| General assistant | `ai/llama3.2` | Good balance of capabilities |
| Small/fast | `ai/smollm2` | Low resource usage |
| Embeddings | `ai/all-minilm` | For RAG and semantic search |

