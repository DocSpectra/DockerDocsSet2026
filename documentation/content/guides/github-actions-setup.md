---
title: GitHub Actions workflow context and shared steps
description: Workflow concepts, build and push actions, and shared repository and publication procedures.
---

## Workflow context

GitHub Actions is a CI/CD (Continuous Integration and Continuous Deployment) automation tool built into GitHub. It allows you to define custom workflows for building, testing, and deploying your code when specific events occur (e.g., pushing code, creating a pull request, etc.). A workflow is a YAML-based automation script that defines a sequence of steps to be executed when triggered. Workflows are stored in the `.github/workflows/` directory of a repository.

## Create the repository and configure credentials

Follow steps 1–6 of [Username variable and token secret](/guides/github-actions-repository.md#username-variable-and-token-secret).

## Push source code

Follow [Push source code](/guides/github-actions-repository.md#push-source-code).

## Build and push actions

Each GitHub Actions workflow includes one or several jobs. Each job consists of steps. Each step can either run a set of commands or use already [existing actions](https://github.com/marketplace?type=actions).

1. [**Login to Docker Hub**](https://github.com/docker/login-action): Action logs in to Docker Hub using the Docker ID and Personal Access Token (PAT) you created earlier.

2. [**Set up Docker Buildx**](https://github.com/docker/setup-buildx-action): Action sets up Docker [Buildx](https://github.com/docker/buildx), a CLI plugin that extends the capabilities of the Docker CLI.

3. [**Build and push**](https://github.com/docker/build-push-action): Action builds and pushes the Docker image to Docker Hub. The `tags` parameter specifies the image name and tag.

## Run the workflow and check publication

Follow [Verify repository publication](/guides/github-actions-run.md#verify-repository-publication).
