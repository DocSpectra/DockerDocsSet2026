---
title: Get started with DMR
description: How to install, enable, and use Docker Model Runner to manage and run AI models.
weight: 10
keywords: Docker, ai, model runner, setup, installation, getting started
---

Docker Model Runner (DMR) lets you run and manage AI models locally using Docker. This page shows you how to enable DMR, pull and run a model, configure model settings, and publish custom models.

## Enable Docker Model Runner

See [Enable and update Docker Model Runner](setup.md).

### Docker Desktop

See [Docker Desktop setup](setup.md#docker-desktop).

### Docker Engine

See [Docker Engine installation](setup.md#docker-engine).

### Update DMR in Docker Engine

See [update instructions and model-preservation options](setup.md#update-dmr-in-docker-engine).

## Pull a model

See [Pull a model](run-models.md#pull-a-model).

## Run a model

See [Run a model](run-models.md#run-a-model).

## Configure a model

You can configure a model, such as its maximum token limit and more,
use Docker Compose.
See [Models and Compose - Model configuration options](../compose/models-and-compose.md#model-configuration-options).

## Publish a model

See [Tag, package, and publish models](publish-models.md).

## Troubleshooting

See [logs and request inspection](diagnose.md).

### Display the logs

See [display the logs](diagnose.md#display-the-logs).

### Inspect requests and responses

See [inspect requests and responses](diagnose.md#inspect-requests-and-responses).

## Related pages

- [API reference](./api-reference.md) - OpenAI and Ollama-compatible API documentation
- [Configuration options](./configuration.md) - Context size and runtime parameters
- [Inference engines](./inference-engines.md) - llama.cpp and vLLM details
- [IDE integrations](./ide-integrations.md) - Connect Cline, Continue, Cursor, and more
- [Open WebUI integration](./openwebui-integration.md) - Set up a web chat interface
- [Models and Compose](../compose/models-and-compose.md) - Use models in Compose applications
- [Docker Model Runner CLI reference](/reference/cli/docker/model) - Complete CLI documentation