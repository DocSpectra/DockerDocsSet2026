---
title: "Docker Desktop fails to start on Mac or Linux platforms"
tags: [Troubleshooting]
---

Platform scope: Mac and Linux.

## Error message 

Docker fails to start due to Unix domain socket path length limitations:

```console
[vpnkit-bridge][F] listen unix <HOME>/Library/Containers/com.docker.docker/Data/http-proxy-control.sock: bind: invalid argument
```

```console
[com.docker.backend][E] listen(vsock:4099) failed: listen unix <HOME>/Library/Containers/com.docker.docker/Data/vms/0/00000002.00001003: bind: invalid argument
```

## Cause

On Mac and Linux, Docker Desktop creates Unix domain sockets used for inter-process communication. These sockets are created under the user's home directory.

Unix domain sockets have a maximum path length:
 - 104 characters on Mac
 - 108 characters on Linux

If your home directory path is too long, Docker Desktop fails to create necessary sockets.

## Solution

Ensure your username is short enough to keep paths within the allowed limit:
 - Mac: Username should be ≤ 33 characters
 - Linux: Username should be ≤ 55 characters

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
