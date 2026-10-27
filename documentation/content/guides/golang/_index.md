---
title: Go language-specific guide
linkTitle: Go
description: Containerize Go apps using Docker
keywords: docker, getting started, go, golang, language, dockerfile
summary: |
  This guide teaches you how to containerize Go applications using Docker.
toc_min: 1
toc_max: 2
aliases:
  - /language/golang/
  - /guides/language/golang/
languages: [go]
params:
  time: 30 minutes
---

This guide will show you how to create, test, and deploy containerized Go applications using Docker.

> **Acknowledgment**
>
> Docker would like to thank [Oliver Frolovs](https://www.linkedin.com/in/ofr/) for his contribution to this guide.

## What will you learn?

In this guide, you’ll learn how to:

- [Create a `Dockerfile` which contains the instructions for building a container image for a program written in Go.](build-images.md)
- [Run the image as a container in your local Docker instance and manage the container's lifecycle.](run-containers.md)
- [Use multi-stage builds for building small images efficiently while keeping your Dockerfiles easy to read and maintain.](build-images.md#multi-stage-builds)
- [Use Docker Compose to orchestrate running of multiple related containers together in a development environment.](develop-compose.md)
- [Run unit tests](run-tests.md)
- [Configure a CI/CD pipeline for your application using](configure-ci-cd.md) [GitHub Actions](https://docs.github.com/en/actions)
- [Deploy your containerized Go application.](deploy.md)

## Prerequisites

See [Go guide prerequisites](prerequisites.md).

## What's next?

The aim of this guide is to provide enough examples and instructions for you to containerize your own Go application and deploy it into the Cloud.

Start by building your first Go image.
