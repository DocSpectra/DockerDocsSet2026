---
title: Docker CLI OpenTelemetry concepts
---

## What is OpenTelemetry? {#what-is-opentelemetry}

OpenTelemetry, or OTel for short, is an open observability framework for
creating and managing telemetry data, such as traces, metrics, and logs.
OpenTelemetry is vendor- and tool-agnostic, meaning that it can be used with a
broad variety of Observability backends.

Support for OpenTelemetry instrumentation in the Docker CLI means that the CLI can emit
information about events that take place, using the protocols and conventions
defined in the Open Telemetry specification.

## How it works {#how-it-works}

The Docker CLI doesn't emit telemetry data by default. Only if you've set an
environment variable on your system will Docker CLI attempt to emit OpenTelemetry
metrics, to the endpoint that you specify.

```bash
DOCKER_CLI_OTEL_EXPORTER_OTLP_ENDPOINT=<endpoint>
```

The variable specifies the endpoint of an OpenTelemetry collector, where telemetry data
about `docker` CLI invocation should be sent. To capture the data, you'll need
an OpenTelemetry collector listening on that endpoint.

The purpose of a collector is to receive the telemetry data, process it, and
exports it to a backend. The backend is where the telemetry data gets stored.
You can choose from a number of different backends, such as Prometheus or
InfluxDB.

Some backends provide tools for visualizing the metrics directly.
Alternatively, you can also run a dedicated frontend with support for
generating more useful graphs, such as Grafana.

## Available metrics {#available-metrics}

Docker CLI exports a single metric, `command.time`, which measures
the execution duration of a command in milliseconds. This metric has the
following attributes:

- `command.name`: the name of the command
- `command.status.code`: the exit code of the command
- `command.stderr.isatty`: true if stderr is attached to a TTY
- `command.stdin.isatty`: true if stdin is attached to a TTY
- `command.stdout.isatty`: true if stdout is attached to a TTY
