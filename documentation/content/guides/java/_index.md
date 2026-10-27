---
title: Java language-specific guide
linkTitle: Java
keywords: java, getting started
description: Containerize Java apps using Docker
summary: |
  This guide demonstrates how to containerize Java applications using Docker.
toc_min: 1
toc_max: 2
aliases:
  - /language/java/
  - /guides/language/java/
languages: [java]
params:
  time: 20 minutes
---

## Tasks

The Java getting started guide teaches you how to create a containerized Spring Boot application using Docker. In this module, you’ll learn how to:

- [Containerize and run a Spring Boot application with Maven](containerize.md)
- [Set up a local development environment](develop.md) to [connect a database](develop.md#add-a-local-database-and-persist-data), [configure a debugger](develop.md#connect-a-debugger), and [use Compose Watch for live reload](develop.md#automatically-update-services)
- [Run your unit tests inside a container](run-tests.md)
- [Configure a CI/CD pipeline for your application using GitHub Actions](configure-ci-cd.md)
- [Deploy your containerized application locally to Kubernetes to test and debug your deployment](deploy.md)

After completing the Java getting started modules, you should be able to containerize your own Java application based on the examples and instructions provided in this guide.

## Get started

[Review the prerequisites](containerize.md#prerequisites).

[Get started containerizing your first Java app](containerize.md).
