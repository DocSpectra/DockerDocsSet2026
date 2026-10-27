---
title: "Define the Go monitoring image"
description: "Define the Go monitoring image"
---

[Multi-stage builds](/manuals/build/building/multi-stage.md).

[Build cache](/manuals/build/cache/_index.md).

## Creating a Dockerfile

Create a new file named `Dockerfile` in the root directory of your Golang application. The Dockerfile contains instructions to build and run the application in a container.

The following is a Dockerfile for a Golang application. You will also find this file in the `go-prometheus-monitoring` directory.

```dockerfile
# Use the official Golang image as the base
FROM golang:1.24-alpine AS builder

# Set environment variables
ENV CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

# Set working directory inside the container
WORKDIR /build

# Copy go.mod and go.sum files for dependency installation
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download

# Copy the entire application source
COPY . .

# Build the Go binary
RUN go build -o /app .

# Final lightweight stage
FROM alpine:3.21 AS final

# Copy the compiled binary from the builder stage
COPY --from=builder /app /bin/app

# Expose the application's port
EXPOSE 8000

# Run the application
CMD ["bin/app"]
```

## Understanding the Dockerfile

The Dockerfile consists of two stages:

1. **Build stage**: This stage uses the official Golang image as the base and sets the necessary environment variables. It also sets the working directory inside the container, copies the `go.mod` and `go.sum` files for dependency installation, downloads the dependencies, copies the entire application source, and builds the Go binary.

    You use the `golang:1.24-alpine` image as the base image for the build stage. The `CGO_ENABLED=0` environment variable disables CGO, which is useful for building static binaries. You also set the `GOOS` and `GOARCH` environment variables to `linux` and `amd64`, respectively, to build the binary for the Linux platform.

2. **Final stage**: This stage uses the official Alpine image as the base and copies the compiled binary from the build stage. It also exposes the application's port and runs the application.

    You use the `alpine:3.21` image as the base image for the final stage. You copy the compiled binary from the build stage to the final image. You expose the application's port using the `EXPOSE` instruction and run the application using the `CMD` instruction.

    Apart from the multi-stage build, the Dockerfile also follows best practices such as using the official images, setting the working directory, and copying only the necessary files to the final image. You can further optimize the Dockerfile by other best practices.
