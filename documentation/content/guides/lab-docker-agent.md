---
title: "Lab: Getting Started with Docker Agent"
linkTitle: "Lab: Getting Started with Docker Agent"
description: |
  Build intelligent multi-agent teams with Docker Agent and Docker in this hands-on
  interactive lab.
summary: |
  Hands-on lab: Create, share, and orchestrate intelligent AI agents using
  Docker Agent, MCP Toolkit, and Docker.
keywords: AI, Docker, docker agent, agents, multi-agent, MCP Toolkit, lab, labspace
aliases:
  - /labs/docker-for-ai/cagent/
  - /guides/lab-cagent/
params:
  tags: [ai, labs]
  time: 20 minutes
  resource_links:
    - title: Docker Agent documentation
      url: https://github.com/docker/docker-agent
    - title: Docker MCP Toolkit
      url: https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/
    - title: Labspace repository
      url: https://github.com/ajeetraina/labspace-cagent
---

This lab walks you through building intelligent agents with Docker Agent. You'll learn beginner
agent concepts, then build sophisticated multi-agent teams that handle complex
real-world tasks. Learn how to create, share, and orchestrate AI agents with
Docker.

Review [what you'll learn](#what-youll-learn) and the [modules](#modules), or [launch the lab](#launch-the-lab).

## Launch the lab

{{< labspace-launch image="dockersamples/labspace-cagent" >}}

## What you'll learn

- Create simple agents with Docker Agent
- Use built-in generic agentic tools for common tasks
- Integrate MCP servers from the MCP Toolkit
- Share agents using the Docker Registry
- Build multi-agent systems for complex workflows
- Use Docker Model Runner with Docker Agent (preview)

## Modules

| # | Module | Description |
|---|--------|-------------|
| 1 | Introduction | Overview of Docker Agent and intelligent agent concepts |
| 2 | Getting Started | Create your first agent with Docker Agent |
| 3 | Using Built-in Tools | Leverage the generic agentic tools in Docker Agent |
| 4 | Using MCP | Integrate MCP servers from the MCP Toolkit |
| 5 | Sharing Agents | Package and share agents via Docker Registry |
| 6 | Introduction to Sub-agents | Build multi-agent systems with sub-agent orchestration |
| 7 | Conclusion | Summary and next steps |

## Related documentation

- [Docker Agent installation](../manuals/ai/docker-agent/_index.md#installation)
- [Coding-agent tutorial](../manuals/ai/docker-agent/tutorial.md)
- [Local models with Docker Model Runner](../manuals/ai/docker-agent/local-models.md)
- [Sharing agents](../manuals/ai/docker-agent/sharing-agents.md)
