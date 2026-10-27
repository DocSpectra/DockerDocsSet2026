---
title: Certificates in Zscaler-proxied Docker environments
---

## The role of certificates in Docker

When Docker builds or runs containers, it often needs to fetch resources from
the internet—whether it's pulling a base image from a registry, downloading
dependencies, or communicating with external services. In a proxied
environment, Zscaler intercepts HTTPS traffic and replaces the remote server's
certificate with its own. However, Docker doesn't trust this Zscaler
certificate by default, leading to SSL errors.

```plaintext
x509: certificate signed by unknown authority
```

These errors occur because Docker cannot verify the validity of the certificate
presented by Zscaler. To avoid this, you must configure Docker to trust
Zscaler's certificate.

## Conclusion

Embedding the Zscaler root certificate directly into your Docker images ensures
that containers run smoothly within Zscaler-proxied environments. By using this
approach, you reduce potential runtime errors and create a consistent,
auditable configuration that allows for smooth Docker operations within a
monitored network.
