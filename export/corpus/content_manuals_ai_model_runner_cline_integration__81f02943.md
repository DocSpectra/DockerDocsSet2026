---
title: Configure Cline with Docker Model Runner
description: Configure Cline to use local models with Docker Model Runner.
---

## Prerequisites

Complete the [local client setup](client-setup.md).

## Cline (VS Code)

[Cline](https://github.com/cline/cline) is an AI coding assistant for VS Code.

### Configuration

1. Open VS Code and go to the Cline extension settings.
2. Select **OpenAI Compatible** as the API provider.
3. Configure the following settings:

| Setting | Value |
|---------|-------|
| Base URL | `http://localhost:12434/engines/v1` |
| API Key | `not-needed` (or any placeholder value) |
| Model ID | `ai/qwen2.5-coder` (or your preferred model) |

> [!IMPORTANT]
> The base URL must include `/engines/v1` at the end. Do not include a trailing slash.

### Troubleshooting Cline

If Cline fails to connect:

1. Verify DMR is running:
   ```console
   $ docker model status
   ```

2. Test the endpoint directly:
   ```console
   $ curl http://localhost:12434/engines/v1/models
   ```

3. Check that CORS is configured if running a web-based version:
   - In Docker Desktop Settings > AI, add your origin to **CORS Allowed Origins**


## Connection and model troubleshooting

See [common client issues](client-setup.md#common-issues) and the [API reference](api-reference.md).
