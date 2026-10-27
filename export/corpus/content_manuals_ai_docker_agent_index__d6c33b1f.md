---
title: Docker Agent
description: Docker Agent lets you build, orchestrate, and share AI agents that work together as a team.
weight: 60
aliases:
  - /ai/cagent/
  - /manuals/ai/cagent/
params:
  sidebar:
    group: Open source
    badge:
      color: violet
      text: Experimental
keywords: [ai, agent, docker agent, cagent]
---

{{< summary-bar feature_name="Docker Agent" >}}

[Docker Agent](https://github.com/docker/docker-agent) is an open-source framework
for building teams of specialized AI agents. Instead of prompting one
generalist model, you define agents with specific roles and instructions that
collaborate to solve problems. Run these agent teams from your terminal using
any LLM provider.

> [!NOTE]
> Docker Agent is a framework for building and running custom agent teams.
> For Docker's built-in AI assistant, see [Gordon](/ai/gordon/) (`docker ai`).

## Why agent teams

See [agent teams and configuration](agent-teams.md).

## Installation

See [Install Docker Agent](installation.md).

## Get started

[Run the bug investigator and fixer team](run-debugger.md).

## How it works

See [agent contexts and delegation](agent-teams.md#how-it-works).

## Configuration options

See [agent configuration](agent-teams.md#configuration-options) and the [configuration reference](reference/config.md).

## Share agent teams

See [Sharing agents](sharing-agents.md).

## What's next

- Follow the [tutorial](./tutorial.md) to build your first coding agent
- Learn [best practices](./best-practices.md) for building effective agents
- Integrate Docker Agent with your [editor](./integrations/acp.md) or use agents as
  [tools in MCP clients](./integrations/mcp.md)
- Browse example agent configurations in the [Docker Agent
  repository](https://github.com/docker/docker-agent/tree/main/examples)
- Use `docker agent new` to generate agent teams with AI <!-- TODO: link to some page
  where we explain this, probably a CLI reference? -->
- Connect agents to external tools via the [Docker MCP
  Gateway](/manuals/ai/mcp-catalog-and-toolkit/mcp-gateway.md)
- Read the full [configuration
  reference](https://github.com/docker/docker-agent?tab=readme-ov-file#-configuration-reference)
  <!-- TODO: move to this site/repo -->
