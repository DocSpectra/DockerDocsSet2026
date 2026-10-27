---
title: Run Node.js sample tasks with Task Runner
description: Task Runner commands for the sample application.
---

## Prerequisites

Use the [Node.js sample application](containerize.md). For Compose command context, see the [Compose CLI reference](/reference/cli/docker/compose/).

## Use Task Runner (alternative)

The project includes a Taskfile.yml for advanced workflows:

```console
# Development
$ task dev              # Start development environment
$ task dev:build        # Build development image
$ task dev:run          # Run development container

# Production
$ task build            # Build production image
$ task run              # Run production container
$ task build-run        # Build and run in one step

# Testing
$ task test             # Run all tests
$ task test:unit        # Run unit tests with coverage
$ task test:lint        # Run linting

# Kubernetes
$ task k8s:deploy       # Deploy to Kubernetes
$ task k8s:status       # Check deployment status
$ task k8s:logs         # View pod logs

# Utilities
$ task clean            # Clean up containers and images
$ task health           # Check application health
$ task logs             # View container logs
```
