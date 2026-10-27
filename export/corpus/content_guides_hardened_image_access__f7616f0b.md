---
title: "Authenticate to pull Docker Hardened Images"
description: "Authenticate to pull Docker Hardened Images"
---

> [!NOTE]
>
> [Docker Hardened Images (DHIs)](https://docs.docker.com/dhi/) are minimal, secure, and production-ready container base and application images maintained by Docker. DHIs are recommended whenever it is possible for better security. They are designed to reduce vulnerabilities and simplify compliance, freely available to everyone with no subscription required, no usage restrictions, and no vendor lock-in.

## Authenticate

You must authenticate to dhi.io before you can pull Docker Hardened Images. Run `docker login dhi.io` to authenticate.

```bash
$ docker login dhi.io
```
