---
title: Install the Docker Engine SDKs
---

After you [install Docker](/get-started/get-docker.md), you can install the Go or Python SDK and also try out the Docker Engine API.

Use the following commands to install the Go or Python SDK. Both SDKs can be
installed and coexist together.

## Go SDK

### Prerequisite

The client requires a recent version of Go. Run `go version` and ensure that you're running a currently supported version of Go.

### Install

```console
$ go get github.com/moby/moby/client
```

For more information, see [Go client reference](https://pkg.go.dev/github.com/moby/moby/client).

## Python SDK

- Recommended: Run `pip install docker`.

- If you can't use `pip`:
  1.  [Download the package directly](https://pypi.python.org/pypi/docker/).
  2.  Extract it and change to the extracted directory.
  3.  Run `python setup.py install`.

For more information, see [Docker Engine Python SDK reference](https://docker-py.readthedocs.io/).

## Docker Desktop for Linux socket

> [!NOTE]
> Docker Desktop for Linux users
>
> Docker Desktop for Linux uses a per-user socket instead of the system-wide `/var/run/docker.sock`. To use Docker SDKs with Docker Desktop for Linux, set the `DOCKER_HOST` environment variable:
>
> ```bash
> export DOCKER_HOST=unix://$HOME/.docker/desktop/docker.sock
> ```
>
> For more details, see [the Linux FAQs](/manuals/desktop/troubleshoot-and-support/faqs/linuxfaqs.md#how-do-i-use-docker-sdks-with-docker-desktop-for-linux).
