---
title: Configure Aider with Docker Model Runner
description: Configure Aider to use local models with Docker Model Runner.
---

## Prerequisites

Complete the [local client setup](client-setup.md).

## Aider

[Aider](https://aider.chat) is an AI pair programming tool for the terminal.

### Configuration

Set environment variables or use command-line flags:

```bash
export OPENAI_API_BASE=http://localhost:12434/engines/v1
export OPENAI_API_KEY=not-needed

aider --model openai/ai/qwen2.5-coder
```

Or in a single command:

```console
$ aider --openai-api-base http://localhost:12434/engines/v1 \
        --openai-api-key not-needed \
        --model openai/ai/qwen2.5-coder
```


## Connection and model troubleshooting

See [common client issues](client-setup.md#common-issues) and the [API reference](api-reference.md).
