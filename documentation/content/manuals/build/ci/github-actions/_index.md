---
title: Docker Build GitHub Actions
linkTitle: GitHub Actions
description: Docker maintains a set of official GitHub Actions for building Docker images.
keywords: ci, github actions, gha,  build, introduction, tutorial
aliases:
  - /ci-cd/github-actions/
  - /build/ci/github-actions/examples/
---

GitHub Actions is a popular CI/CD platform for automating your build, test, and
deployment pipeline. Docker provides a set of official GitHub Actions for you to
use in your workflows. These official actions are reusable, easy-to-use
components for building, annotating, and pushing images.

## Get started with GitHub Actions

The [Introduction to GitHub Actions with Docker](/guides/gha.md) guide walks
you through the process of setting up and using Docker GitHub Actions for
building Docker images, and pushing images to Docker Hub.

## Available actions

The following GitHub Actions are available:

- [Build and push Docker images](https://github.com/marketplace/actions/build-and-push-docker-images):
  build and push Docker images with BuildKit.
- [Docker Buildx Bake](https://github.com/marketplace/actions/docker-buildx-bake):
  enables using high-level builds with [Bake](../../bake/_index.md).
- [Docker Login](https://github.com/marketplace/actions/docker-login):
  sign in to a Docker registry.
- [Docker Setup Buildx](https://github.com/marketplace/actions/docker-setup-buildx):
  creates and boots a BuildKit builder.
- [Docker Metadata action](https://github.com/marketplace/actions/docker-metadata-action):
  extracts metadata from Git reference and GitHub events to generate tags,
  labels, and annotations.
- [Docker Setup Compose](https://github.com/marketplace/actions/docker-setup-compose):
  installs and sets up [Compose](../../../compose).
- [Docker Setup Docker](https://github.com/marketplace/actions/docker-setup-docker):
  installs Docker Engine.
- [Docker Setup QEMU](https://github.com/marketplace/actions/docker-setup-qemu):
  installs [QEMU](https://github.com/qemu/qemu) static binaries for
  multi-platform builds.
- [Docker Scout](https://github.com/docker/scout-action):
  analyze Docker images for security vulnerabilities.

Using Docker's actions provides an easy-to-use interface, while still allowing
flexibility for customizing build parameters.

## Examples

### Set up builds

- [Configure the builder](configure-builder.md)
- [Use Docker GitHub Builder reusable workflows](github-builder/_index.md)
- [Manage cache](cache.md)
- [Build multi-platform images](multi-platform.md)

### Configure and validate inputs

- [Use named contexts](named-contexts.md)
- [Pass build secrets and SSH mounts](secrets.md)
- [Set reproducible build timestamps](reproducible-builds.md)
- [Run build checks](checks.md)

### Add image metadata

- [Manage tags and labels](manage-tags-labels.md)
- [Add annotations](annotations.md)
- [Add SBOM and provenance attestations](attestations.md)

### Use and publish results

- [Load an image into Docker](export-docker.md)
- [Use a local registry](local-registry.md)
- [Share an image between jobs](share-image-jobs.md)
- [Test an image before pushing](test-before-push.md)
- [Push to multiple registries](push-multi-registries.md)
- [Copy an image between registries](copy-image-registries.md)
- [Update the Docker Hub description](update-dockerhub-desc.md)

### Inspect builds

- [View summaries and import build records](build-summary.md)
