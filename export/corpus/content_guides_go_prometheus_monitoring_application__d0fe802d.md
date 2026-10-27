---
title: Building the application
linkTitle: Understand the application
weight: 10 #
keywords: go, golang, prometheus, grafana, containerize, monitor
description: Learn how to create a Golang server to register metrics with Prometheus.
---

## Prerequisites

[Prepare the Go monitoring sample](setup.md).

You will be creating a Golang server with some endpoints to simulate a real-world application. Then you will expose metrics from the server using Prometheus.

## Getting the sample application

[Prepare the Go monitoring sample](setup.md#getting-the-sample-application).

## Understanding the application

[Go application metrics and middleware](metrics.md).

## Running the application

Make sure you are still inside `go-prometheus-monitoring` directory in the terminal, and run the following command. Install the dependencies by running `go mod tidy` and then build and run the application by running `go run main.go`. Then visit `http://localhost:8000/health` or `http://localhost:8000/v1/users`. You should see the output `{"message": "Up and running!"}` or `{"message": "Hello from /v1/users"}`. If you are able to see this then your app is successfully up and running. 


Now, check your application's metrics by accessing the `/metrics` endpoint. 
Open `http://localhost:8000/metrics` in your browser. You should see similar output to the following.

```sh
# HELP api_http_request_error_total Total number of errors returned by the API
# TYPE api_http_request_error_total counter
api_http_request_error_total{path="/",status="404"} 1
api_http_request_error_total{path="//v1/users",status="404"} 1
api_http_request_error_total{path="/favicon.ico",status="404"} 1
# HELP api_http_request_total Total number of requests processed by the API
# TYPE api_http_request_total counter
api_http_request_total{path="/health",status="200"} 2
api_http_request_total{path="/v1/users",status="200"} 1
```

In the terminal, press `ctrl` + `c` to stop the application.

> [!Note]
> If you don't want to run the application locally, and want to run it in a Docker container, skip to [containerizing the application](containerize.md), where you create a Dockerfile.

## Summary

In this section, you learned how to create a Golang app to register metrics with Prometheus. By implementing middleware functions, you were able to increment the counters based on the request path and status codes.

## Next steps

In the next section, you'll learn how to containerize your application.
