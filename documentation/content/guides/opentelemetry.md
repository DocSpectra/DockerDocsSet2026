---
title: Instrumenting a JavaScript App with OpenTelemetry
description: &desc Learn how to instrument a JavaScript application using OpenTelemetry in a Dockerized environment.
keywords: OpenTelemetry, observability, tracing
linktitle: Instrumenting JS Apps with OpenTelemetry
summary: *desc
tags: [app-dev, observability]
languages: [js]
params:
  time: 10 minutes
---

[OpenTelemetry and OTLP context](observability-context.md#opentelemetry-and-otlp).

This guide walks you through how to instrument a simple Node.js application with OpenTelemetry and run both the app and a collector using Docker. This setup is ideal for local development and testing observability before integrating with external observability platforms like Prometheus, Jaeger, or Grafana.

In this guide, you'll learn how to:

- How to set up OpenTelemetry in a Node.js app.
- How to run an OpenTelemetry Collector in Docker.
- How to visualize traces with Jaeger.
- How to use Docker Compose to manage the full observability stack.

## Using OpenTelemetry with Docker

[Image and architecture context](observability-context.md#using-opentelemetry-with-docker).

## Prerequisites

[Docker Compose](/compose/): Recommended for managing multi-container Docker applications.

Basic knowledge of Node.js and Docker.

## Project Structure

[Project Structure](opentelemetry-app.md#project-structure).

## Create a Simple Node.js App

[Create a Simple Node.js App](opentelemetry-app.md#create-a-simple-nodejs-app).

## Configure OpenTelemetry Tracing

[Configure OpenTelemetry Tracing](opentelemetry-app.md#configure-opentelemetry-tracing).

## Configure the OpenTelemetry Collector

[Configure the OpenTelemetry Collector](opentelemetry-stack.md#configure-the-opentelemetry-collector).

## Add Docker Compose Configuration

[Add Docker Compose Configuration](opentelemetry-stack.md#add-docker-compose-configuration).

## Start the Stack

[Start the Stack](opentelemetry-stack.md#start-the-stack).

## Verify Traces in Jaeger

[Verify Traces in Jaeger](opentelemetry-stack.md#verify-traces-in-jaeger).

## Conclusion

You now have a fully functional OpenTelemetry setup using Docker Compose. You've instrumented a basic JavaScript app to export traces and visualized them using Jaeger. This architecture is extendable for more complex applications and observability pipelines using Prometheus, Grafana, or cloud-native exporters.

For advanced topics such as custom span creation, metrics, and logs, consult the OpenTelemetry JavaScript docs.
