---
description: Containerize a Golang application and monitor it with Prometheus and Grafana.
keywords: golang, prometheus, grafana, monitoring, containerize
title: Monitor a Golang application with Prometheus and Grafana
summary: |
  Learn how to containerize a Golang application and monitor it with Prometheus and Grafana.
linkTitle: Monitor with Prometheus and Grafana
languages: [go]
params:
  time: 45 minutes
---

The guide teaches you how to containerize a Golang application and monitor it with Prometheus and Grafana. 

> **Acknowledgment**
>
> Docker would like to thank [Pradumna Saraf](https://twitter.com/pradumna_saraf) for his contribution to this guide.

## Overview

[Prometheus and Grafana context](../observability-context.md#prometheus-and-grafana).

In this guide, you will be creating a Golang server with some endpoints to simulate a real-world application. Then you will expose metrics from the server using Prometheus. Finally, you will visualize the metrics using Grafana. You will containerize the Golang application, and using the Docker Compose file, you will connect all the services: Golang, Prometheus, and Grafana.

## What will you learn?

* Create a Golang application with custom Prometheus metrics.
* Containerize a Golang application.
* Use Docker Compose to run multiple services and connect them together to monitor a Golang application with Prometheus and Grafana.
* Visualize the metrics using Grafana dashboards.

## Prerequisites

[Prepare the Go monitoring sample](setup.md).

## Next steps

You will create a Golang server and expose metrics using Prometheus.

## Tasks

- [Run the application and inspect its metrics](application.md)
- [Build and run the image](containerize.md)
- [Run the services with Compose](compose.md)
- [Develop with Watch and visualize metrics](develop.md)
