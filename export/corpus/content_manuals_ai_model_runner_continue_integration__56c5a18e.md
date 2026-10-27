---
title: Configure Continue with Docker Model Runner
description: Configure Continue to use local models with Docker Model Runner.
---

## Prerequisites

Complete the [local client setup](client-setup.md).

## Continue (VS Code / JetBrains)

[Continue](https://continue.dev) is an open-source AI code assistant that works with VS Code and JetBrains IDEs.

### Configuration

Edit your Continue configuration file (`~/.continue/config.json`):

```json
{
  "models": [
    {
      "title": "Docker Model Runner",
      "provider": "openai",
      "model": "ai/qwen2.5-coder",
      "apiBase": "http://localhost:12434/engines/v1",
      "apiKey": "not-needed"
    }
  ]
}
```

### Using Ollama provider

Continue also supports the Ollama provider, which works with DMR:

```json
{
  "models": [
    {
      "title": "Docker Model Runner (Ollama)",
      "provider": "ollama",
      "model": "ai/qwen2.5-coder",
      "apiBase": "http://localhost:12434"
    }
  ]
}
```


## Connection and model troubleshooting

See [common client issues](client-setup.md#common-issues) and the [API reference](api-reference.md).
