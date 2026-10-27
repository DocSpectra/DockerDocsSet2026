---
title: Run a bug investigator and fixer team
description: Run and share the two-agent debugger example with Docker Agent.
---

## Prerequisites

[Install Docker Agent](installation.md). See [model providers](model-providers.md) for API keys and [agent teams](agent-teams.md) for delegation and configuration.

## Debugger configuration

Here's a two-agent team that debugs problems:

```yaml
agents:
  root:
    model: openai/gpt-5-mini # Change to the model that you want to use
    description: Bug investigator
    instruction: |
      Analyze error messages, stack traces, and code to find bug root causes.
      Explain what's wrong and why it's happening.
      Delegate fix implementation to the fixer agent.
    sub_agents: [fixer]
    toolsets:
      - type: filesystem
      - type: mcp
        ref: docker:duckduckgo

  fixer:
    model: anthropic/claude-sonnet-4-5 # Change to the model that you want to use
    description: Fix implementer
    instruction: |
      Write fixes for bugs diagnosed by the investigator.
      Make minimal, targeted changes and add tests to prevent regression.
    toolsets:
      - type: filesystem
      - type: shell
```

The root agent investigates and explains the problem. When it understands the
issue, it hands off to `fixer` for implementation. Each agent stays focused on
its specialty.

## Get started

Try the bug analyzer team:

1. Set your API key for the model provider you want to use:

   ```console
   $ export ANTHROPIC_API_KEY=<your_key>  # For Claude models
   $ export OPENAI_API_KEY=<your_key>     # For OpenAI models
   $ export GOOGLE_API_KEY=<your_key>     # For Gemini models
   ```

2. Save the [example configuration](#debugger-configuration) as `debugger.yaml`.

3. Run your agent team:

   ```console
   $ docker agent run debugger.yaml
   ```

You'll see a prompt where you can describe bugs or paste error messages. The
investigator analyzes the problem, then hands off to the fixer for
implementation.

## Share agent teams

See [registry authentication and publishing](sharing-agents.md) before sharing the team:

```console
$ docker agent share push ./debugger.yaml myusername/debugger
$ docker agent share pull myusername/debugger
```


