---
title: "Kafka versions and image choices"
description: "Kafka versions and image choices"
---

Beginning with [Kafka 3.3](https://www.confluent.io/blog/apache-kafka-3-3-0-new-features-and-updates/), the deployment of Kafka was greatly simplified by no longer requiring Zookeeper thanks to KRaft (Kafka Raft). With KRaft, setting up a Kafka instance for local development is much easier. Starting with the launch of [Kafka 3.8](https://www.confluent.io/blog/introducing-apache-kafka-3-8/), a new [kafka-native](https://hub.docker.com/r/apache/kafka-native) Docker image is now available, providing a significantly faster startup and lower memory footprint.

> [!TIP]
>
> This guide will be using the apache/kafka image, as it includes many helpful scripts to manage and work with Kafka. However, you may want to use the apache/kafka-native image, as it starts more quickly and requires fewer resources.
