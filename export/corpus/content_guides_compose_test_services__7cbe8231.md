---
title: Use a development image for Compose tests
description: Shared test-service command overrides and one-off container cleanup.
---

## Reuse the development environment

A test service can reuse the same `Dockerfile.dev` used for development and override the default command to run tests. This provides a consistent test environment that matches the local development configuration.

## Run and remove the test container

The [`docker compose run --rm`](/reference/cli/docker/compose/run/) command starts the test service, executes its test script, and automatically removes the container after tests complete.

For Compose commands and profiles, see the [Compose CLI reference](/reference/cli/docker/compose/).
