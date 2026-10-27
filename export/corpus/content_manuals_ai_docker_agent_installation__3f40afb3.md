---
title: Install Docker Agent
description: Install Docker Agent with Docker Desktop or as a custom installation.
---

## Installation

Docker Agent is included in Docker Desktop 4.63 and later. In Docker Desktop versions 4.49 through 4.62, this feature was called cagent.

For Docker Engine users or custom installations:

- **Homebrew**: `brew install docker-agent`
- **Winget**: `winget install Docker.Agent`
- **Pre-built binaries**: [GitHub
  releases](https://github.com/docker/docker-agent/releases)
- **From source**: See the [Docker Agent
  repository](https://github.com/docker/docker-agent?tab=readme-ov-file#build-from-source)

The `docker-agent` binary should be copied to `~/.docker/cli-plugins` and then can be used with the `docker agent` command. Alternatively, it can be used as a standalone binary.

