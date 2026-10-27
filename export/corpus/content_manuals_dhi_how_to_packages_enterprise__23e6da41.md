---
title: Configure the enterprise hardened package repository
description: Install enterprise packages using secret-mounted build credentials.
---

Before you begin, review [hardened package access](../core-concepts/packages.md) and [CLI setup](cli.md).

## Enterprise repository

{{< summary-bar feature_name="Docker Hardened Images Enterprise" >}}

With DHI Enterprise, you have access to an additional package
repository that includes hardened packages for compliance variants such as FIPS,
as well as additional security patches.

The configuration process involves five steps:

1. Install the [signing key](https://github.com/docker-hardened-images/keyring)
2. Configure the base package repository
3. Install the enterprise configuration package
4. Configure package installation with authentication
5. Build the image passing credentials as a secret using the DHI CLI

  > [!NOTE]
  >
  > You must have the Docker Hardened Images CLI installed and configured. For
  > more information, see [Use the DHI CLI](./cli.md).

The following example shows how to configure the Alpine package manager in your
Dockerfile to use Docker's enterprise hardened package repository:

```dockerfile
FROM alpine:3.23

# Install the signing key
RUN cd /etc/apk/keys && \
    wget https://dhi.io/keyring/dhi-apk@docker-0F81AD7700D99184.rsa.pub

# Replace the default repositories with the hardened package repository
RUN echo "https://dhi.io/apk/alpine/v3.23/main" > /etc/apk/repositories

# Update and install the enterprise configuration package to add the security repository
RUN apk update && \
    apk add dhi-enterprise-conf

# Install packages from the security repository with authentication
RUN --mount=type=secret,id=http_auth \
    HTTP_AUTH="$(cat /run/secrets/http_auth)" \
    apk update && \
    apk add openssl-fips
```

Build the image with authentication passed securely as a build secret:

```console
$ dhictl auth apk > http_auth.txt
$ docker build --secret id=http_auth,src=http_auth.txt -t myapp-enterprise:latest .
$ rm http_auth.txt
```

The `--secret` flag securely mounts the authentication credentials during build
without storing them in the image layers or metadata.
