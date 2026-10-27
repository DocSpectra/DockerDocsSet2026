---
title: Components of an agentic application
description: Models, agents, MCP gateways, and Compose in an agentic application.
---

Agentic applications are transforming how software gets built. These apps don't
just respond, they decide, plan, and act. They're powered by models,
orchestrated by agents, and integrated with APIs, tools, and services in real
time.

All these new agentic applications, no matter what they do, share a common
architecture. It's a new kind of stack, built from three core components:

- Models: These are your GPTs, CodeLlamas, Mistrals. They're doing the
  reasoning, writing, and planning. They're the engine behind the intelligence.

- Agent: This is where the logic lives. Agents take a goal, break it down, and
  figure out how to get it done. They orchestrate everything. They talk to the
  UI, the tools, the model, and the gateway.

- MCP gateway: This is what links your agents to the outside world, including
  APIs, tools, and services. It provides a standard way for agents to call
  capabilities via the Model Context Protocol (MCP).

Docker makes this AI-powered stack simpler, faster, and more secure by unifying
models, and tool gateways into a developer-friendly workflow that uses Docker
Compose.

This guide walks you through the core components of agentic development and
shows how Docker ties them all together with the following tools:

- [Docker Model Runner](/manuals/ai/model-runner/_index.md) lets you run LLMs
  locally with simple command and OpenAI-compatible APIs.
- [Docker MCP Catalog and
  Toolkit](/manuals/ai/mcp-catalog-and-toolkit/_index.md) helps you discover
  and securely run external tools, like APIs and databases, using the Model
  Context Protocol (MCP).
- [Docker MCP Gateway](/manuals/ai/mcp-catalog-and-toolkit/mcp-gateway.md) lets you orchestrate and manage MCP servers.
- [Docker Compose](/manuals/ai/compose/models-and-compose.md) is the tool that ties it all
  together, letting you define and run multi-container applications with a
  single file.

