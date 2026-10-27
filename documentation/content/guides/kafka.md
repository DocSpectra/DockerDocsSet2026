---
description: Developing event-driven applications with Kafka and Docker
keywords: kafka, container-supported development
title: Developing event-driven applications with Kafka and Docker
linktitle: Event-driven apps with Kafka
summary: |
  This guide explains how to run Apache Kafka in Docker containers.
tags: [distributed-systems]
languages: [js]
aliases:
  - /guides/use-case/kafka/
params:
  time: 20 minutes
---

With the rise of microservices, event-driven architectures have become increasingly popular.
[Apache Kafka](https://kafka.apache.org/), a distributed event streaming platform, is often at the
heart of these architectures. Unfortunately, setting up and deploying your own Kafka instance for development
is often tricky. Fortunately, Docker and containers make this much easier.

In this guide, you will learn how to:

1. Use Docker to launch up a Kafka cluster
2. Connect a non-containerized app to the cluster
3. Connect a containerized app to the cluster
4. Deploy Kafka-UI to help with troubleshooting and debugging

## Prerequisites

The following prerequisites are required to follow along with this how-to guide:

- [Docker Desktop](prerequisites.md#docker-desktop)
- [Node.js and yarn](prerequisites.md#nodejs-and-yarn)
- Basic knowledge of Kafka and Docker

## Launching Kafka

[Launching Kafka](kafka-start.md).

## Connecting to Kafka from a non-containerized app

[Connecting to Kafka from a non-containerized app](kafka-native-app.md).

## Connecting to Kafka from both containers and native apps

[Connecting to Kafka from both containers and native apps](kafka-container-app.md).

## Adding cluster visualization

[Adding cluster visualization](kafka-ui.md).

## Testing with Kafka

If you’re interested in learning how you can integrate Kafka easily into your integration tests, check out the [Testing Spring Boot Kafka Listener using Testcontainers guide](https://testcontainers.com/guides/testing-spring-boot-kafka-listener-using-testcontainers/). This guide will teach you how to use Testcontainers to manage the lifecycle of Kafka containers in your tests.

## Conclusion

By using Docker, you can simplify the process of developing and testing event-driven applications with Kafka. Containers simplify the process of setting up and deploying the various services you need to develop. And once they’re defined in Compose, everyone on the team can benefit from the ease of use.

In case you missed it earlier, all of the sample app code can be found at dockersamples/kafka-development-node.
