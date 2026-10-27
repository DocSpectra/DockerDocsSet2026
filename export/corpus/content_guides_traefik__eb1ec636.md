---
title: HTTP routing with Traefik
description: &desc Use Traefik to easily route traffic between multiple containers or non-containerized workloads
keywords: traefik, container-supported development
linktitle: HTTP routing with Traefik
summary: *desc
tags: [networking, dhi]
params:
  time: 20 minutes
---

## Introduction

During local development, it’s quite common to need to run multiple HTTP services. You might have both an API and a frontend app, a WireMock service to mock data endpoints, or a database visualizer (such as phpMyAdmin or pgAdmin). In many development setups, these services are exposed on different ports, which then requires you to remember what’s on what port but can also introduce other problems (such as CORS).

A reverse proxy can dramatically simplify this setup by being the single exposed service and then routing requests to the appropriate service based on the request URL (either by path or hostname). [Traefik](https://traefik.io/traefik/) is a modern, cloud-native reverse proxy and load balancer that makes developing and deploying multi-service applications easier. This guide will show you how to use Traefik with Docker to enhance your development environment.

In this guide, you will learn how to:

1. Start Traefik with Docker
2. Configure routing rules to split traffic between two containers
3. Use Traefik in a containerized development environment
4. Use Traefik to send requests to non-containerized workloads

## Prerequisites

[Docker Desktop](prerequisites.md#docker-desktop).

[Node.js and yarn](prerequisites.md#nodejs-and-yarn).

Basic of Docker.

## Using Traefik with Docker

[Using Traefik with Docker](traefik-docker.md).

## Using Traefik in development

[Using Traefik in development](traefik-development.md).

## Sending traffic to non-containerized workloads

[Sending traffic to non-containerized workloads](traefik-native.md).

## Recap

Running multiple services doesn’t have to require tricky port configuration and a good memory. With tools like Traefik, it’s easy to launch the services you need and easily access them - whether they’re for the app itself (such as the frontend and backend) or for additional development tooling (such as phpMyAdmin).
