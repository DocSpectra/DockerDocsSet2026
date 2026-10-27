---
title: Automate your builds with GitHub Actions
linkTitle: Automate your builds with GitHub Actions
weight: 20
keywords: ci/cd, github actions, ruby, flask
description: Learn how to configure CI/CD using GitHub Actions for your Ruby on Rails application.
aliases:
  - /language/ruby/configure-ci-cd/
  - /guides/language/ruby/configure-ci-cd/
  - /guides/ruby/configure-ci-cd/
---

## Prerequisites

Complete all the previous sections of this guide, starting with [Containerize a Ruby on Rails application](containerize.md). You must have a [GitHub](https://github.com/signup) account and a verified [Docker](https://hub.docker.com/signup) account to complete this section.

If you didn't create a [GitHub repository](https://github.com/new) for your project yet, it is time to do it. After creating the repository, don't forget to [add a remote](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories) and ensure you can commit and [push your code](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#about-git-push) to GitHub.

Follow [Username variable and token secret](/guides/github-actions-repository.md#username-variable-and-token-secret), steps 2–5.

## Overview

For workflow context, see [Workflow context](/guides/github-actions-setup.md#workflow-context).

In this section, you'll learn how to set up and use GitHub Actions to build your Docker image as well as push it to Docker Hub. You will complete the following steps:

1. Define the GitHub Actions workflow.
2. Run the workflow.

## 1. Define the GitHub Actions workflow

You can create a GitHub Actions workflow by creating a YAML file in the `.github/workflows/` directory of your repository. To do this use your favorite text editor or the GitHub web interface. The following steps show you how to create a workflow file using the GitHub web interface.

If you prefer to use the GitHub web interface, follow these steps:

1. Go to your repository on GitHub and then select the **Actions** tab.

2. Select **set up a workflow yourself**.

   This takes you to a page for creating a new GitHub Actions workflow file in
   your repository. By default, the file is created under `.github/workflows/main.yml`, let's change it name to `build.yml`.

If you prefer to use your text editor, create a new file named `build.yml` in the `.github/workflows/` directory of your repository.

Add the following content to the file:

```yaml
name: Build and push Docker image

on:
  push:
    branches:
      - main

jobs:
  build_and_push:
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
          push: true
          tags: ${{ vars.DOCKER_USERNAME }}/${{ github.event.repository.name }}:latest
```

For the workflow steps, see [Build and push actions](/guides/github-actions-setup.md#build-and-push-actions). The `latest` tag is used in this example.

## 2. Run the workflow

Commit the changes and push them to the `main` branch. This workflow is runs every time you push changes to the `main` branch. You can find more information about workflow triggers [in the GitHub documentation](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows).

Follow [Verify repository publication](/guides/github-actions-run.md#verify-repository-publication), steps 2–3.

## Summary

In this section, you learned how to set up a GitHub Actions workflow for your Ruby on Rails application.

Related information:

- [Introduction to GitHub Actions](/guides/gha.md)
- [Docker Build GitHub Actions](/manuals/build/ci/github-actions/_index.md)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## Next steps

In the next section, you'll learn how you can develop your application using containers.

