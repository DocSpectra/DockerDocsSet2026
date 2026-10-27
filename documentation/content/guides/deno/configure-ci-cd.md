---
title: Configure CI/CD for your Deno application
linkTitle: Configure CI/CD
weight: 40
keywords: ci/cd, github actions, deno, shiny
description: Learn how to configure CI/CD using GitHub Actions for your Deno application.
aliases:
- /language/deno/configure-ci-cd/
---

## Prerequisites

Complete all the previous sections of this guide, starting with [Containerize a Deno application](containerize.md). You must have a [GitHub](https://github.com/signup) account and a verified [Docker](https://hub.docker.com/signup) account to complete this section.

## Overview

In this section, you'll learn how to set up and use GitHub Actions to build and test your Docker image as well as push it to Docker Hub. You will complete the following steps:

1. Create a new repository on GitHub.
2. Define the GitHub Actions workflow.
3. Run the workflow.

## Prepare the repository

Follow [Username variable and token secret](/guides/github-actions-repository.md#username-variable-and-token-secret). At the commit step, run:

```console
$ git commit -m "my commit"
```

## Set up the workflow

Set up your GitHub Actions workflow for building and pushing the image
to Docker Hub.

Follow [Create the workflow file](/guides/github-actions-run.md#create-the-workflow-file), using the configuration below.

```yaml
name: ci

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Docker Hub
        uses: docker/login-action@{{% param "login_action_version" %}}
        with:
          username: ${{ vars.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
      -
        name: Build and push
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          platforms: linux/amd64,linux/arm64
          push: true
          tags: ${{ vars.DOCKER_USERNAME }}/${{ github.event.repository.name }}:latest
```

For more information about the YAML syntax for `docker/build-push-action`,
refer to the [GitHub Action README](https://github.com/docker/build-push-action/blob/master/README.md).

## Run the workflow

Follow [Verify repository publication](/guides/github-actions-run.md#verify-repository-publication).

## Summary

In this section, you learned how to set up a GitHub Actions workflow for your Deno application.

Related information:
 - [Introduction to GitHub Actions](/manuals/build/ci/github-actions/_index.md)
 - [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## Next steps

Next, learn how you can locally test and debug your workloads on Kubernetes before deploying.

[Test the Kubernetes deployment](deploy.md).
