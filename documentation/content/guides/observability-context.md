---
title: "Observability with OpenTelemetry, Prometheus, and Grafana"
description: "Observability with OpenTelemetry, Prometheus, and Grafana"
---

## OpenTelemetry and OTLP

OpenTelemetry (OTel) is an open-source observability framework that provides a set of APIs, SDKs, and tools for collecting telemetry data, such as metrics, logs, and traces, from applications. With OpenTelemetry, developers can obtain valuable insights into how their services perform in production or during local development.

A key component of OpenTelemetry is the OpenTelemetry Protocol (OTLP) a general-purpose, vendor-agnostic protocol designed to transmit telemetry data efficiently and reliably. OTLP supports multiple data types (traces, metrics, logs) over HTTP or gRPC, making it the default and recommended protocol for communication between instrumented applications, the OpenTelemetry Collector, and backends such as Jaeger or Prometheus.

## Using OpenTelemetry with Docker

The [Docker Official Image for OpenTelemetry](https://hub.docker.com/r/otel/opentelemetry-collector-contrib) provides a convenient way to deploy and manage Dex instances. OpenTelemetry is available for various CPU architectures, including amd64, armv7, and arm64, ensuring compatibility with different devices and platforms. Same for the [Jaeger Docker image](https://hub.docker.com/r/jaegertracing/jaeger).

## Prometheus and Grafana

To make sure your application is working as intended, monitoring is important. One of the most popular monitoring tools is Prometheus. Prometheus is an open-source monitoring and alerting toolkit that is designed for reliability and scalability. It collects metrics from monitored targets by scraping metrics HTTP endpoints on these targets. To visualize the metrics, you can use Grafana. Grafana is an open-source platform for monitoring and observability that allows you to query, visualize, alert on, and understand your metrics no matter where they are stored.
