---
title: Connect LlamaIndex to Docker Model Runner
description: Connect LlamaIndex to use local models with Docker Model Runner.
---

## Prerequisites

Complete the [local client setup](client-setup.md).

## LlamaIndex

```python
from llama_index.llms.openai_like import OpenAILike

llm = OpenAILike(
    api_base="http://localhost:12434/engines/v1",
    api_key="not-needed",
    model="ai/qwen2.5-coder"
)

response = llm.complete("Write a hello world function")
print(response.text)
```


## Connection and model troubleshooting

See [common client issues](client-setup.md#common-issues) and the [API reference](api-reference.md).
