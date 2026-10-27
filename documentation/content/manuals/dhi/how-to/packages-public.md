---
title: Configure the public hardened package repository
description: Configure Alpine signing keys and repositories, then build and check an image.
---

Before you begin, review [hardened package access](../core-concepts/packages.md).

## Public repository

To use Docker's public hardened package repository in your own images, configure
the Alpine package manager in your Dockerfile.

The configuration process involves three steps:

1. Install the [signing key](https://github.com/docker-hardened-images/keyring)
2. Configure the package repository
3. Update and install packages

The following example shows how to configure the Alpine package manager in your
Dockerfile to use Docker's public hardened package repository:

```dockerfile
FROM alpine:3.23

# Install the signing key
RUN cd /etc/apk/keys && \
    wget https://dhi.io/keyring/dhi-apk@docker-0F81AD7700D99184.rsa.pub

# Replace the default repositories with the hardened package repository
RUN echo "https://dhi.io/apk/alpine/v3.23/main" > /etc/apk/repositories

# Update and install packages
RUN apk update && \
    apk add libpng
```

Replace `3.23` with your Alpine version in both the base image tag and repository URL.

To verify the configuration, build and run the image:

```console
$ docker build -t myapp:latest .
$ docker run -it myapp:latest sh
```

Inside the container, check the configured repositories:

```console
/ # cat /etc/apk/repositories
https://dhi.io/apk/alpine/v3.23/main
```

This ensures all packages are installed from Docker's hardened repository.

All packages installed from the Docker Hardened Images repository are built from
source by Docker and include full provenance.
