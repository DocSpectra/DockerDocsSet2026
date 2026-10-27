---
title: "Prepare the Go monitoring sample"
description: "Prepare the Go monitoring sample"
---

## Prerequisites

- A good understanding of Golang is assumed.
- You must me familiar with Prometheus and creating dashboards in Grafana.
- You must have familiarity with Docker concepts like containers, images, and Dockerfiles. If you are new to Docker, you can start with the [Docker basics](/get-started/docker-concepts/the-basics/what-is-a-container.md) guide.

[Git client](../prerequisites.md#git-client).

## Getting the sample application

Clone the sample application to use with this guide. Open a terminal, change
directory to a directory that you want to work in, and run the following
command to clone the repository:

```console
$ git clone https://github.com/dockersamples/go-prometheus-monitoring.git 
```

Once you cloned you will see the following content structure inside `go-prometheus-monitoring` directory,

```text
go-prometheus-monitoring
├── CONTRIBUTING.md
├── Docker
│   ├── grafana.yml
│   └── prometheus.yml
├── dashboard.json
├── Dockerfile
├── LICENSE
├── README.md
├── compose.yaml
├── go.mod
├── go.sum
└── main.go
```

- **main.go** - The entry point of the application.
- **go.mod and go.sum** - Go module files.
- **Dockerfile** - Dockerfile used to build the app.
- **Docker/** - Contains the Docker Compose configuration files for Grafana and Prometheus.
- **compose.yaml** - Compose file to launch everything (Golang app, Prometheus, and Grafana).
- **dashboard.json** - Grafana dashboard configuration file.
- Other files are for licensing and documentation purposes.
