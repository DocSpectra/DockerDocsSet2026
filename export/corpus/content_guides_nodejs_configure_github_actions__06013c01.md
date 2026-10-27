---
title: Automate Node.js builds with GitHub Actions
linkTitle: Automate your builds with GitHub Actions
weight: 50
keywords: CI/CD, GitHub Actions, Node.js, Docker
description: Learn how to configure CI/CD using GitHub Actions for your Node.js application.
aliases:
  - /language/nodejs/configure-ci-cd/
  - /guides/language/nodejs/configure-ci-cd/
---

## Prerequisites

Complete all the previous sections of this guide, starting with [Containerize a Node.js application](containerize.md).

You must also have:

- A [GitHub](https://github.com/signup) account.
- A verified [Docker Hub](https://hub.docker.com/signup) account.

---

## Overview

In this section, you'll set up a **CI/CD pipeline** using [GitHub Actions](https://docs.github.com/en/actions) to automatically:

- Build your Node.js application inside a Docker container.
- Run unit and integration tests, and make sure your application meets solid code quality standards.
- Perform security scanning and vulnerability assessment.
- Push production-ready images to [Docker Hub](https://hub.docker.com).

---

## Prepare repositories and credentials

Follow [Credentials stored as repository secrets](/guides/github-actions-repository.md#credentials-stored-as-repository-secrets) with these project values:

| Setting | Value |
| --- | --- |
| Suggested access-token name | `docker-nodejs-sample` |
| Example Docker Hub repository name | `nodejs-sample` |
| Local project | `docker-nodejs-sample` |

At the commit step, run:

```console
$ git commit -m "Initial commit with CI/CD pipeline"
```

## Set up the workflow

Follow [Create the workflow file](/guides/github-actions-run.md#create-the-workflow-file), using the configuration below.

```yaml
name: CI/CD – Node.js Application with Docker

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
    types: [opened, synchronize, reopened]

jobs:
  test:
    name: Run Node.js Tests
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:18-alpine
        env:
          POSTGRES_DB: todoapp_test
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
      - name: Checkout code
        uses: actions/checkout@{{% param "checkout_action_version" %}}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}

      - name: Cache npm dependencies
        uses: actions/cache@{{% param "cache_action_version" %}}
        with:
          path: ~/.npm
          key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
          restore-keys: ${{ runner.os }}-npm-

      - name: Build test image
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          context: .
          target: test
          tags: nodejs-app-test:latest
          platforms: linux/amd64
          load: true
          cache-from: type=local,src=/tmp/.buildx-cache
          cache-to: type=local,dest=/tmp/.buildx-cache,mode=max

      - name: Run tests inside container
        run: |
          docker run --rm \
            --network host \
            -e NODE_ENV=test \
            -e POSTGRES_HOST=localhost \
            -e POSTGRES_PORT=5432 \
            -e POSTGRES_DB=todoapp_test \
            -e POSTGRES_USER=postgres \
            -e POSTGRES_PASSWORD=postgres \
            nodejs-app-test:latest
        env:
          CI: true
        timeout-minutes: 10

  build-and-push:
    name: Build and Push Docker Image
    runs-on: ubuntu-latest
    needs: test

    steps:
      - name: Checkout code
        uses: actions/checkout@{{% param "checkout_action_version" %}}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}

      - name: Cache Docker layers
        uses: actions/cache@{{% param "cache_action_version" %}}
        with:
          path: /tmp/.buildx-cache
          key: ${{ runner.os }}-buildx-${{ github.sha }}
          restore-keys: ${{ runner.os }}-buildx-

      - name: Extract metadata
        id: meta
        run: |
          echo "REPO_NAME=${GITHUB_REPOSITORY##*/}" >> "$GITHUB_OUTPUT"
          echo "SHORT_SHA=${GITHUB_SHA::7}" >> "$GITHUB_OUTPUT"

      - name: Log in to Docker Hub
        uses: docker/login-action@{{% param "login_action_version" %}}
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push multi-arch production image
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          context: .
          target: production
          push: true
          platforms: linux/amd64,linux/arm64
          tags: |
            ${{ secrets.DOCKER_USERNAME }}/${{ secrets.DOCKERHUB_PROJECT_NAME }}:latest
            ${{ secrets.DOCKER_USERNAME }}/${{ secrets.DOCKERHUB_PROJECT_NAME }}:${{ steps.meta.outputs.SHORT_SHA }}
          cache-from: type=local,src=/tmp/.buildx-cache
          cache-to: type=local,dest=/tmp/.buildx-cache,mode=max
```

This workflow performs the following tasks for your Node.js application:

- Triggers on every `push` or `pull request` to the `main` branch.
- Builds a test Docker image using the `test` stage.
- Runs tests in a containerized environment.
- Stops the workflow if any test fails.
- Caches Docker build layers and npm dependencies for faster runs.
- Authenticates with Docker Hub using GitHub secrets.
- Builds an image using the `production` stage.
- Tags and pushes the image to Docker Hub with `latest` and short SHA tags.

> [!NOTE]
> For more information about `docker/build-push-action`, refer to the [GitHub Action README](https://github.com/docker/build-push-action/blob/master/README.md).

---

## Run the workflow

Follow [Run and verify tagged images](/guides/github-actions-run.md#run-and-verify-tagged-images), including the Docker Hub tag checks and branch-protection tip.

From your GitHub repository, go to the **Actions** tab. Select the workflow run to follow each step: **test**, **build**, **security**, and (if successful) **push** and **deploy**.

## Related resources

Deepen your understanding of automation and best practices for containerized apps:

- [Introduction to GitHub Actions](/guides/gha.md) – Learn how GitHub Actions automate your workflows
- [Docker Build GitHub Actions](/manuals/build/ci/github-actions/_index.md) – Set up container builds with GitHub Actions
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) – Full reference for writing GitHub workflows
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) – Learn about GHCR features and usage
- [Best practices for writing Dockerfiles](/develop/develop-images/dockerfile_best-practices/) – Optimize your image for performance and security

---

## Next steps

Next, learn how you can deploy your containerized Node.js application to Kubernetes with production-ready configuration. This helps you ensure your application behaves as expected in a production-like environment, reducing surprises during deployment.

[Test the Kubernetes deployment](deploy.md).
