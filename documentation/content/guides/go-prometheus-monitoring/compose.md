---
title: Connecting services with Docker Compose
linkTitle: Connecting services with Docker Compose
weight: 30 #
keywords: go, golang, prometheus, grafana, containerize, monitor
description: Learn how to connect services with Docker Compose to monitor a Golang application with Prometheus and Grafana.
---

Now that you have containerized the Golang application, you will use Docker Compose to connect your services together. You will connect the Golang application, Prometheus, and Grafana services together to monitor the Golang application with Prometheus and Grafana.

## Prerequisites

[Prepare the Go monitoring sample](setup.md).

[Define the Go monitoring image](image.md).

## Creating a Docker Compose file

[Configure the Go, Prometheus, and Grafana services](configuration.md#creating-a-docker-compose-file).

## Understanding the Docker Compose file

[Service and configuration details](configuration.md#understanding-the-docker-compose-file).

## Building and running the services

Now that you have the Docker Compose file, you can build the services and run them together using Docker Compose.

To build and run the services, run the following command in the terminal:

```console
$ docker compose up
```

The `docker compose up` command builds the services defined in the Docker Compose file and runs them together. You will see the similar output in the terminal:

```console
 ✔ Network go-prometheus-monitoring_go-network  Created                                                           0.0s 
 ✔ Container grafana                            Created                                                           0.3s 
 ✔ Container go-api                             Created                                                           0.2s 
 ✔ Container prometheus                         Created                                                           0.3s 
Attaching to go-api, grafana, prometheus
go-api      | [GIN-debug] [WARNING] Creating an Engine instance with the Logger and Recovery middleware already attached.
go-api      | 
go-api      | [GIN-debug] [WARNING] Running in "debug" mode. Switch to "release" mode in production.
go-api      |  - using env:     export GIN_MODE=release
go-api      |  - using code:    gin.SetMode(gin.ReleaseMode)
go-api      | 
go-api      | [GIN-debug] GET    /metrics                  --> main.PrometheusHandler.func1 (3 handlers)
go-api      | [GIN-debug] GET    /health                   --> main.main.func1 (4 handlers)
go-api      | [GIN-debug] GET    /v1/users                 --> main.main.func2 (4 handlers)
go-api      | [GIN-debug] [WARNING] You trusted all proxies, this is NOT safe. We recommend you to set a value.
go-api      | Please check https://pkg.go.dev/github.com/gin-gonic/gin#readme-don-t-trust-all-proxies for details.
go-api      | [GIN-debug] Listening and serving HTTP on :8000
prometheus  | ts=2025-03-15T05:57:06.676Z caller=main.go:627 level=info msg="No time or size retention was set so using the default time retention" duration=15d
prometheus  | ts=2025-03-15T05:57:06.678Z caller=main.go:671 level=info msg="Starting Prometheus Server" mode=server version="(version=2.55.0, branch=HEAD, revision=91d80252c3e528728b0f88d254dd720f6be07cb8)"
grafana     | logger=settings t=2025-03-15T05:57:06.865335506Z level=info msg="Config overridden from command line" arg="default.log.mode=console"
grafana     | logger=settings t=2025-03-15T05:57:06.865337131Z level=info msg="Config overridden from Environment variable" var="GF_PATHS_DATA=/var/lib/grafana"
grafana     | logger=ngalert.state.manager t=2025-03-15T05:57:07.088956839Z level=info msg="State
.
.
grafana     | logger=plugin.angulardetectorsprovider.dynamic t=2025-03-15T05:57:07.530317298Z level=info msg="Patterns update finished" duration=440.489125ms
```

The services will start running, and you can access the Golang application at `http://localhost:8000`, Prometheus at `http://localhost:9090/health`, and Grafana at `http://localhost:3000`. You can also check the running containers using the `docker ps` command.

```console
$ docker ps
```

## Summary

In this section, you learned how to connect services together using Docker Compose. You created a Docker Compose file to run multiple services together and connect them using networks. You also learned how to build and run the services using Docker Compose.

Related information:

 - [Docker Compose overview](/manuals/compose/_index.md)
 - [Compose file reference](/reference/compose-file/_index.md)

Next, you will learn how to develop the Golang application with Docker Compose and monitor it with Prometheus and Grafana.

## Next steps

In the next section, you will learn how to develop the Golang application with Docker. You will also learn how to use Docker Compose Watch to rebuild the image whenever you make changes to the code. Lastly, you will test the application and visualize the metrics in Grafana using Prometheus as the data source.
