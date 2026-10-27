---
title: Rust language-specific guide
linkTitle: Rust
description: Containerize Rust apps using Docker
keywords: Docker, getting started, Rust, language
summary: |
  This guide covers how to containerize Rust applications using Docker.
toc_min: 1
toc_max: 2
aliases:
  - /language/rust/
  - /guides/language/rust/
languages: [rust]
tags: [dhi]
params:
  time: 20 minutes
---

## Tasks

The Rust language-specific guide teaches you how to create a containerized Rust application using Docker. In this guide, you'll learn how to:

- [Containerize a Rust application](build-images.md)
- [Build an image](build-images.md#build-an-image) and [run the newly built image as a container](run-containers.md)
- [Set up volumes and networking](develop.md#run-a-database-in-a-container)
- [Orchestrate containers using Compose](develop.md#use-compose-to-develop-locally)
- [Use containers for development](develop.md)
- [Configure a CI/CD pipeline for your application using GitHub Actions](configure-ci-cd.md)
- [Deploy your containerized Rust application locally to Kubernetes to test and debug your deployment](deploy.md)

After completing the Rust modules, you should be able to containerize your own Rust application based on the examples and instructions provided in this guide.

## Get started

[Review the prerequisites](build-images.md#prerequisites).

[Start with building your first Rust image](build-images.md).
