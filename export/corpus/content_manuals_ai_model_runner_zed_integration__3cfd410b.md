---
title: Configure Zed with Docker Model Runner
description: Configure Zed to use local models with Docker Model Runner.
---

## Prerequisites

Complete the [local client setup](client-setup.md).

## Zed

[Zed](https://zed.dev) is a high-performance code editor with AI features.

### Configuration

Edit your Zed settings (`~/.config/zed/settings.json`):

```json
{
  "language_models": {
    "openai": {
      "api_url": "http://localhost:12434/engines/v1",
      "available_models": [
        {
          "name": "ai/qwen2.5-coder",
          "display_name": "Qwen 2.5 Coder (DMR)",
          "max_tokens": 8192
        }
      ]
    }
  }
}
```


## Connection and model troubleshooting

See [common client issues](client-setup.md#common-issues) and the [API reference](api-reference.md).
