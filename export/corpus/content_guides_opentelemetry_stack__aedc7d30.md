---
title: "Run the OpenTelemetry Collector and visualize traces"
description: "Run the OpenTelemetry Collector and visualize traces"
---

## Prerequisites

[Docker Compose](/compose/): Recommended for managing multi-container Docker applications.

Basic knowledge of Node.js and Docker.

[Instrument the Node.js sample](opentelemetry-app.md).

[OpenTelemetry and OTLP context](observability-context.md#opentelemetry-and-otlp).

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## Configure the OpenTelemetry Collector

Create a collector-config.yaml file at the root:

```yaml
# collector-config.yaml
receivers:
  otlp:
    protocols:
      http:

exporters:
  logging:
    loglevel: debug
  jaeger:
    endpoint: jaeger:14250
    tls:
      insecure: true

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [logging, jaeger]
```

## Add Docker Compose Configuration

Create the `docker-compose.yaml` file:

```yaml
version: '3.9'

services:
  app:
    build: ./app
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
    depends_on:
      - collector

  collector:
    image: otel/opentelemetry-collector:latest
    volumes:
      - ./collector-config.yaml:/etc/otelcol/config.yaml
    command: ["--config=/etc/otelcol/config.yaml"]
    ports:
      - "4318:4318" # OTLP

  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "16686:16686" # UI
      - "14250:14250" # Collector gRPC
```

Now, add the `Dockerfile` inside the `app/` folder:

```dockerfile
# app/Dockerfile
FROM node:18

WORKDIR /usr/src/app
COPY . .
RUN npm install

CMD ["node", "app.js"]
```

## Start the Stack

Start all services with Docker Compose:

```bash
docker compose up --build
```

Once the services are running:

Visit your app at [http://localhost:3000](http://localhost:3000)

View traces at [http://localhost:16686](http://localhost:16686) in the Jaeger UI

## Verify Traces in Jaeger

After visiting your app's root endpoint, open Jaeger’s UI, search for the service (default is usually `unknown_service` unless explicitly named), and check the traces.

You should see spans for the HTTP request, middleware, and auto-instrumented libraries.
