---
title: Configure model endpoints for services
description: Use the short and long model examples in a Compose application.
---

{{< summary-bar feature_name="Compose models" >}}

## Model configuration and caveats

See [model declarations and attributes](models.md), [service model access and environment variable names](services.md#models), and [Use AI models in Compose](/manuals/ai/compose/models-and-compose.md).

## Examples

### Example 1

```yaml
services:
  app:
    image: app
    models:
      - ai_model


models:
  ai_model:
    model: ai/model
```

In this basic example:

 - The app service uses the `ai_model`.
 - The `ai_model` is defined as an OCI artifact (`ai/model`) that is pulled and served by the model runner.
 - Docker Compose injects connection info, for example `AI_MODEL_URL`, into the container. 

### Example 2

```yaml
services:
  app:
    image: app
    models:
      my_model:
        endpoint_var: MODEL_URL

models:
  my_model:
    model: ai/model
    context_size: 1024
    runtime_flags: 
      - "--a-flag"
      - "--another-flag=42"
```

In this advanced setup:

 - The service app references `my_model` using the long syntax.
 - Compose injects the model runner's URL as the environment variable `MODEL_URL`.

