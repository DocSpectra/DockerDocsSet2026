---
description: Run, develop, and share data science projects using JupyterLab and Docker
keywords: getting started, jupyter, notebook, python, jupyterlab, data science
title: Data science with JupyterLab
toc_max: 2
summary: |
  Use Docker to run Jupyter notebooks.
tags: [data-science]
languages: [python]
aliases:
  - /guides/use-case/jupyter/
params:
  time: 20 minutes
---

Docker and JupyterLab are two powerful tools that can enhance your data science
workflow. In this guide, you will learn how to use them together to create and
run reproducible data science environments. This guide is based on
[Supercharging AI/ML Development with JupyterLab and
Docker](https://www.docker.com/blog/supercharging-ai-ml-development-with-jupyterlab-and-docker/).

In this guide, you'll learn how to:

- Run a personal Jupyter Server with JupyterLab on your local machine
- Customize your JupyterLab environment
- Share your JupyterLab notebook and environment with other data scientists

## What is JupyterLab?

[JupyterLab and Docker concepts](jupyter-context.md#what-is-jupyterlab).

## Why use Docker and JupyterLab together?

[Benefits of Docker and JupyterLab](jupyter-context.md#why-use-docker-and-jupyterlab-together).

## Prerequisites

[Latest Docker Desktop](prerequisites.md#latest-docker-desktop).

## Run and access a JupyterLab container

[Run and access a JupyterLab container](jupyter-run.md).

[Open an existing notebook with a bind mount](jupyter-bind-mount.md).

## Save and access notebooks

[Save and access notebooks](jupyter-notebooks.md).

## Customize your JupyterLab environment

[Customize your JupyterLab environment](jupyter-customize.md).

## Run your image as a container

[Run your image as a container](jupyter-customize.md).

## Use Compose to run your container

[Use Compose to run your container](jupyter-compose.md).

## Share your work

[Share your work](jupyter-share.md).

## Summary

In this guide, you learned how to leverage Docker and JupyterLab to create
reproducible data science environments, facilitating the development and sharing
of data science projects. This included, running a personal JupyterLab server,
customizing the environment with necessary tools and packages, and sharing
notebooks and environments with other data scientists.

Related information:

- [Dockerfile reference](/reference/dockerfile/)
- [Compose file reference](/reference/compose-file/)
- [Docker CLI reference](/reference/cli/docker/)
- [Jupyter Docker Stacks docs](https://jupyter-docker-stacks.readthedocs.io/en/latest/)
