---
title: Configure CI/CD for your Go application
linkTitle: Configure CI/CD
weight: 40
keywords: go, CI/CD, local, development
description: Learn how to Configure CI/CD for your Go application
aliases:
  - /language/golang/configure-ci-cd/
  - /guides/language/golang/configure-ci-cd/
---

## Prerequisites

See [Go guide prerequisites](prerequisites.md).

Complete the previous sections of this guide, starting with [Build your Go image](build-images.md). You must have a [GitHub](https://github.com/signup) account and a verified [Docker](https://hub.docker.com/signup) account to complete this section.

## Overview

In this section, you'll learn how to set up and use GitHub Actions to build and push your Docker image to Docker Hub. You will complete the following steps:

1. Create a new repository on GitHub.
2. Define the GitHub Actions workflow.
3. Run the workflow.

## Step one: Create the repository

Follow [Create the repository and configure credentials](/guides/github-actions-setup.md#create-the-repository-and-configure-credentials).

Then follow [Push source code](/guides/github-actions-setup.md#push-source-code).

## Step two: Set up the workflow

Set up your GitHub Actions workflow for building, testing, and pushing the image
to Docker Hub.

1. Go to your repository on GitHub and then select the **Actions** tab.

2. Select **set up a workflow yourself**.

   This takes you to a page for creating a new GitHub actions workflow file in
   your repository, under `.github/workflows/main.yml` by default.

3. In the editor window, copy and paste the following YAML configuration and commit the changes.

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
         - name: Login to Docker Hub
           uses: docker/login-action@{{% param "login_action_version" %}}
           with:
             username: ${{ vars.DOCKER_USERNAME }}
             password: ${{ secrets.DOCKERHUB_TOKEN }}

         - name: Set up Docker Buildx
           uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}

         - name: Build and push
           uses: docker/build-push-action@{{% param "build_push_action_version" %}}
           with:
             platforms: linux/amd64,linux/arm64
             push: true
             tags: ${{ vars.DOCKER_USERNAME }}/${{ github.event.repository.name }}:latest
   ```

   For more information about the YAML syntax for `docker/build-push-action`,
   refer to the [GitHub Action README](https://github.com/docker/build-push-action/blob/master/README.md).

## Step three: Run the workflow

Follow [Run the workflow and check publication](/guides/github-actions-setup.md#run-the-workflow-and-check-publication).

## Summary

In this section, you learned how to set up a GitHub Actions workflow for your application.

Related information:

- [Introduction to GitHub Actions](/guides/gha.md)
- [Docker Build GitHub Actions](/manuals/build/ci/github-actions/_index.md)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## Next steps

Next, learn how you can locally test and debug your workloads on Kubernetes before deploying.
