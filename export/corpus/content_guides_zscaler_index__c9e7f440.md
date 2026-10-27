---
title: Using Docker with Zscaler
tags: [networking, admin]
summary: |
  This guide explains how to embed Zscaler’s root certificate into Docker
  images, allowing containers to operate securely with Zscaler proxies and
  avoid SSL errors.
params:
  time: 10 minutes
---

In many corporate environments, network traffic is intercepted and monitored
using HTTPS proxies, such as Zscaler. While Zscaler ensures security compliance
and network control, it can cause issues for developers using Docker,
particularly during build processes, where SSL certificate validation errors
might occur. This guide outlines how to configure Docker containers and builds
to properly handle Zscaler's custom certificates, ensuring smooth operation in
monitored environments.

## Certificate context

Review [Certificates in Zscaler-proxied Docker environments](/guides/zscaler-certificate-context.md), including the SSL validation error.

## Configure Zscaler proxy for Docker Desktop

Depending on how Zscaler is deployed, you may need to configure Docker Desktop
proxy settings manually to use the Zscaler proxy.

If you're using Zscaler as a system-level proxy via the [Zscaler Client Connector](https://help.zscaler.com/zscaler-client-connector/what-is-zscaler-client-connector),
all traffic on the device is automatically routed through Zscaler, so Docker
Desktop uses the Zscaler proxy automatically with no additional configuration
necessary.

If you are not using Zscaler as a system-level proxy, manually configure proxy
settings in Docker Desktop. Set up proxy settings for all clients in the
organization using [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md),
or edit proxy configuration in the Docker Desktop GUI under [**Settings > Resources > Proxies**](/manuals/desktop/settings-and-maintenance/settings.md#proxies).

## Install root certificates in Docker images

Review the [image certificate installation procedure](/guides/proxy-root-certificates.md) before building.

### Obtaining the root certificate

The easiest way to obtain the root certificate is to export it from a machine
where an administrator has already installed it. You can use either a web
browser or the system's certificate management service (for example, Windows
Certificate Store).

#### Example: Exporting the certificate using Google Chrome

1. In Google Chrome, navigate to `chrome://certificate-manager/`.
2. Under **Local certificates**, select **View imported certificates**.
3. Find the Zscaler root certificate, often labeled **Zscaler Root CA**.
4. Open the certificate details and select **Export**.
5. Save the certificate in ASCII PEM format.
6. Open the exported file in a text editor to confirm it includes `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.

When you have obtained the certificate, store it in an accessible repository,
such as JFrog Artifactory or a Git repository. Alternatively, use generic
storage like AWS S3.

### Build with the certificate

Follow [Install a proxy root certificate in Docker images](/guides/proxy-root-certificates.md) for local certificates, artifact downloads with checksum verification, and multi-stage builds.

