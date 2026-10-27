---
title: "Instrument the Node.js sample with OpenTelemetry"
description: "Instrument the Node.js sample with OpenTelemetry"
---

## Prerequisites

[Docker Compose](/compose/): Recommended for managing multi-container Docker applications.

Basic knowledge of Node.js and Docker.

[OpenTelemetry and OTLP context](observability-context.md#opentelemetry-and-otlp).

## Project Structure

Create the project directory:
```bash
mkdir otel-js-app
cd otel-js-app
```

```bash
otel-js-app/
├── docker-compose.yaml
├── collector-config.yaml
├── app/
│   ├── package.json
│   ├── app.js
│   └── tracer.js
```

## Create a Simple Node.js App

Initialize a basic Node.js app:

```bash
mkdir app && cd app
npm init -y
npm install express @opentelemetry/api @opentelemetry/sdk-node \
            @opentelemetry/auto-instrumentations-node \
            @opentelemetry/exporter-trace-otlp-http
```

Now, add the application logic:

```js
// app/app.js
const express = require('express');
require('./tracer'); // Initialize OpenTelemetry

const app = express();

app.get('/', (req, res) => {
  res.send('Hello from OpenTelemetry demo app!');
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`App listening at http://localhost:${PORT}`);
});
```

## Configure OpenTelemetry Tracing

Create the tracer configuration file:

```js
// app/tracer.js
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({
    url: 'http://collector:4318/v1/traces',
  }),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();
```
