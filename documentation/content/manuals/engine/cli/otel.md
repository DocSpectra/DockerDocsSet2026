---
title: OpenTelemetry for the Docker CLI
description: Learn about how to capture OpenTelemetry metrics for the Docker command line
keywords: otel, opentelemetry, telemetry, traces, tracing, metrics, logs
aliases:
  - /config/otel/
---

{{< summary-bar feature_name="Docker CLI OpenTelemetry" >}}

The Docker CLI supports [OpenTelemetry](https://opentelemetry.io/docs/) instrumentation
for emitting metrics about command invocations. This is disabled by default.
You can configure the CLI to start emitting metrics to the endpoint that you
specify. This allows you to capture information about your `docker` command
invocations for more insight into your Docker usage.

Exporting metrics is opt-in, and you control where data is being sent by
specifying the destination address of the metrics collector.

## What is OpenTelemetry?

See [OpenTelemetry concepts](otel-context.md#what-is-opentelemetry).

## How it works

See [How Docker CLI OpenTelemetry works](otel-context.md#how-it-works).

## Setup

To get started capturing telemetry data for the Docker CLI, you'll need to:

- Set the `DOCKER_CLI_OTEL_EXPORTER_OTLP_ENDPOINT` environment variable to point to an OpenTelemetry collector endpoint
- Run an OpenTelemetry collector that receives the signals from CLI command invocations
- Run a backend for storing the data received from the collector

The following Docker Compose file bootstraps a set of services to get started with OpenTelemetry.
It includes an OpenTelemetry collector that the CLI can send metrics to,
and a Prometheus backend that scrapes the metrics off the collector.

```yaml {collapse=true,title=compose.yaml}
name: cli-otel
services:
  prometheus:
    image: prom/prometheus
    command:
      - "--config.file=/etc/prometheus/prom.yml"
    ports:
      # Publish the Prometheus frontend on localhost:9091
      - 9091:9090
    restart: always
    volumes:
      # Store Prometheus data in a volume:
      - prom_data:/prometheus
      # Mount the prom.yml config file
      - ./prom.yml:/etc/prometheus/prom.yml
  otelcol:
    image: otel/opentelemetry-collector
    restart: always
    depends_on:
      - prometheus
    ports:
      - 4317:4317
    volumes:
      # Mount the otelcol.yml config file
      - ./otelcol.yml:/etc/otelcol/config.yaml

volumes:
  prom_data:
```

This service assumes that the following two configuration files exist alongside
`compose.yaml`:

- ```yaml {collapse=true,title=otelcol.yml}
  # Receive signals over gRPC and HTTP
  receivers:
    otlp:
      protocols:
        grpc:
        http:

  # Establish an endpoint for Prometheus to scrape from
  exporters:
    prometheus:
      endpoint: "0.0.0.0:8889"

  service:
    pipelines:
      metrics:
        receivers: [otlp]
        exporters: [prometheus]
  ```

- ```yaml {collapse=true,title=prom.yml}
  # Configure Prometheus to scrape the OpenTelemetry collector endpoint
  scrape_configs:
    - job_name: "otel-collector"
      scrape_interval: 1s
      static_configs:
        - targets: ["otelcol:8889"]
  ```

With these files in place:

1. Start the Docker Compose services:

   ```console
   $ docker compose up
   ```

2. Configure Docker CLI to export telemetry to the OpenTelemetry collector.

   ```console
   $ export DOCKER_CLI_OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
   ```

3. Run a `docker` command to trigger the CLI into sending a metric signal to
   the OpenTelemetry collector.

   ```console
   $ docker version
   ```

4. To view telemetry metrics created by the CLI, open the Prometheus expression
   browser by going to <http://localhost:9091/graph>.

5. In the **Query** field, enter `command_time_milliseconds_total`, and execute
   the query to see the telemetry data.

## Available metrics

See [available Docker CLI metrics](otel-context.md#available-metrics).
