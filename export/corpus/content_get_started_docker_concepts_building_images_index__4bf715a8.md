---
title: Building images
weight: 20
keywords: build images, Dockerfile, layers, tag, push, cache, multi-stage
description: |
  Learn how to build Docker images from a Dockerfile. You'll understand the
  structure of a Dockerfile, how to build an image, and how to customize the
  build process.
summary: |
  Building container images is both technical and an art. You want to keep the
  image small and focused to increase your security posture, but also need to
  balance potential tradeoffs, such as caching impacts. In this series, you’ll
  deep dive into the secrets of images, how they are built and best practices.
layout: series
params:
  proficiencyLevel: Beginner
  time: 25 minutes
  prerequisites: None
---

## About this series

Learn how to build production-ready images that are lean and efficient Docker
images, essential for minimizing overhead and enhancing deployment in
production environments.

## What you'll learn

- Understanding image layers
- Writing a Dockerfile
- Build, tag and publish an image
- Using the build cache
- Multi-stage builds

## Choose a task or shared explanation

| Task | Shared explanation |
| --- | --- |
| [Create layers with container commit](/get-started/tasks/create-image-layers.md) | [Image layers](understanding-image-layers.md) |
| [Write the Node.js Dockerfile](/get-started/tasks/write-node-dockerfile.md) | [Dockerfile instructions](writing-a-dockerfile.md) |
| [Build and push the to-do image](/get-started/tasks/build-and-push-todo-image.md) | [Build, tag, and publish](build-tag-and-publish-an-image.md) |
| [Cache Node.js dependencies](/get-started/tasks/cache-node-builds.md) | [Build cache](using-the-build-cache.md) |
| [Build Spring Boot in stages](/get-started/tasks/build-java-in-stages.md) | [Multi-stage builds](multi-stage-builds.md) |
