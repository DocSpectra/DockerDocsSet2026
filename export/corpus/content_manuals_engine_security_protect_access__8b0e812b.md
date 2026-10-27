---
description: How to setup and run Docker with SSH or HTTPS
keywords: docker, docs, article, example, ssh, https, daemon, tls, ca,  certificate
title: Protect the Docker daemon socket
aliases:
- /articles/https/
- /engine/articles/https/
- /engine/security/https/
---

By default, Docker runs through a non-networked UNIX socket. It can also
optionally communicate using SSH or a TLS (HTTPS) socket.

## Use SSH to protect the Docker daemon socket

See [Connect to the Docker daemon with SSH](connect-ssh.md).

### SSH Tips

See [SSH connection reuse](connect-ssh.md#ssh-tips).

## Use TLS (HTTPS) to protect the Docker daemon socket

See [Protect Docker daemon connections with TLS](connect-tls.md).

### Create a CA, server and client keys with OpenSSL

See [Create CA, server, and client keys](tls-certificates.md).

### Secure by default

See [Secure client connections by default](connect-tls.md#secure-by-default).

### Other modes

See [Other TLS modes](connect-tls.md#other-modes).

#### Daemon modes

See [Daemon TLS modes](connect-tls.md#daemon-modes).

#### Client modes

See [Client TLS modes](connect-tls.md#client-modes).

#### Connecting to the secure Docker port using `curl`

See [Test the secure port with curl](connect-tls.md#connecting-to-the-secure-docker-port-using-curl).

## Related information

* [Using certificates for repository client verification](certificates.md)
* [Use trusted images](trust/_index.md)
