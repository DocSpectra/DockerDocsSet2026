---
title: Configure Cursor with Docker Model Runner
description: Configure Cursor to use local models with Docker Model Runner.
---

## Prerequisites

Complete the [local client setup](client-setup.md).

## Cursor

[Cursor](https://cursor.sh) is an AI-powered code editor.

### Configuration

1. Open Cursor Settings (Cmd/Ctrl + ,).
2. Navigate to **Models** > **OpenAI API Key**.
3. Configure:

   | Setting | Value |
   |---------|-------|
   | OpenAI API Key | `not-needed` |
   | Override OpenAI Base URL | `http://localhost:12434/engines/v1` |

4. In the model drop-down, enter your model name: `ai/qwen2.5-coder`

> [!NOTE]
> Some Cursor features may require models with specific capabilities (e.g., function calling).
> Use capable models like `ai/qwen2.5-coder` or `ai/llama3.2` for best results.


## Connection and model troubleshooting

See [common client issues](client-setup.md#common-issues) and the [API reference](api-reference.md).
