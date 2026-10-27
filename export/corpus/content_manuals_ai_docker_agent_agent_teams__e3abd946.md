---
title: Agent teams and configuration
description: How agent contexts, delegation, and YAML configuration work in Docker Agent.
---

## Why agent teams

One agent handling complex work means constant context-switching. Split the work
across focused agents instead - each handles what it's best at. Docker Agent manages
the coordination.

## How it works

You interact with the _root agent_, which can delegate work to sub-agents you
define. Each agent:

- Uses its own model and parameters
- Has its own context (agents don't share knowledge)
- Can access built-in tools like todo lists, memory, and task delegation
- Can use external tools via [MCP
  servers](/manuals/ai/mcp-catalog-and-toolkit/mcp-gateway.md)

The root agent delegates tasks to agents listed under `sub_agents`. Sub-agents
can have their own sub-agents for deeper hierarchies.

## Configuration options

Agent configurations are YAML files. A basic structure looks like this:

```yaml
agents:
  root:
    model: claude-sonnet-4-0
    description: Brief role summary
    instruction: |
      Detailed instructions for this agent...
    sub_agents: [helper]

  helper:
    model: gpt-5-mini
    description: Specialist agent role
    instruction: |
      Instructions for the helper agent...
```

You can also configure model settings (like context limits), tools (including
MCP servers), and more. See the [configuration
reference](./reference/config.md)
for complete details.

