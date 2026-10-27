---
title: "Certificates not set up correctly"
tags: [Troubleshooting]
---

Platform scope: All platforms.

## Error message 

When attempting to pull from a registry using `docker run`, you may encounter the following error:

```console
Error response from daemon: Get http://192.168.203.139:5858/v2/: malformed HTTP response "\x15\x03\x01\x00\x02\x02"
```

Additionally, logs from the registry may show:

```console
2017/06/20 18:15:30 http: TLS handshake error from 192.168.203.139:52882: tls: client didn't provide a certificate
2017/06/20 18:15:30 http: TLS handshake error from 192.168.203.139:52883: tls: first record does not look like a TLS handshake
```

## Possible causes 

- Docker Desktop ignores certificates listed under insecure registries.
- Client certificates are not sent to insecure registries, causing handshake failures.

## Solution 

- Ensure that your registry is properly configured with valid SSL certificates.
- If your registry is self-signed, configure Docker to trust the certificate by adding it to Docker’s certificates directory (/etc/docker/certs.d/ on Linux).
- If the issue persists, check your Docker daemon configuration and enable TLS authentication.

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
