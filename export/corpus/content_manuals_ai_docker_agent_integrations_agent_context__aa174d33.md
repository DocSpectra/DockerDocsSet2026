---
title: Agent behavior in editors and MCP clients
description: File context, tool exposure, and agent design for ACP and MCP integrations.
---

## Editor context with ACP

When you run Docker Agent with ACP, it becomes part of your editor's environment. You
select code, highlight a function, or reference a file - the agent sees what you
see. No copying file paths or switching to a terminal.

Ask "explain this function" and the agent reads the file you're viewing. Ask it
to "add error handling" and it edits the code right in your editor. The agent
works with your editor's view of the project, not some external file system it
has to navigate.

The difference from running Docker Agent in a terminal: file operations go through
your editor instead of the agent directly accessing your filesystem. When the
agent needs to read or write a file, it requests it from your editor. This keeps
the agent's view of your code synchronized with yours - same working directory,
same files, same state.

## Agents as MCP tools

You configure Claude Desktop (or another MCP client) to connect to Docker Agent. Your
agents appear in Claude's tool list. When you ask Claude to use one, it calls
that agent through the MCP protocol.

Say you have a security agent configured. Ask Claude Desktop "Use the security
agent to audit this authentication code" and Claude calls it. The agent runs
with its configured tools (filesystem, shell, whatever you gave it), then
returns results to Claude.

If your configuration has multiple agents, each one becomes a separate tool. A
config with `root`, `designer`, and `engineer` agents gives Claude three tools
to choose from. Claude might call the engineer directly or use the root
coordinator—depends on your agent descriptions and what you ask for.

## Designing agents for MCP

MCP clients see each of your agents as a separate tool and can call any of them
directly. This changes how you should think about agent design compared to
running agents with `docker agent run`.

### Write good descriptions

The `description` field tells the MCP client what the agent does. This is how
the client decides when to call it. "Analyzes code for security vulnerabilities
and compliance issues" is specific. "A helpful security agent" doesn't say what
it actually does.

```yaml
agents:
  security_auditor:
    description: Analyzes code for security vulnerabilities and compliance issues
    # Not: "A helpful security agent"
```

### MCP clients call agents directly

The MCP client can call any of your agents, not just root. If you have `root`,
`designer`, and `engineer` agents, the client might call the engineer directly
instead of going through root. Design each agent to work on its own:

```yaml
agents:
  engineer:
    description: Implements features and writes production code
    instruction: |
      You implement code based on requirements provided.
      You can work independently without a coordinator.
    toolsets:
      - type: filesystem
      - type: shell
```

If an agent needs others to work properly, say so in the description:
"Coordinates design and engineering agents to implement complete features."

### Test each agent on its own

MCP clients call agents individually, so test them that way:

```console
$ docker agent run agent.yml --agent engineer
```

Make sure the agent works without going through root first. Check that it has
the right tools and that its instructions make sense when it's called directly.

