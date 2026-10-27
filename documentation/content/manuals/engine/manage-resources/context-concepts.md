---
title: Docker context properties and selection
---

## Introduction {#introduction}

This guide shows how you can use contexts to manage Docker daemons from a single client.

Each context contains all information required to manage resources on the daemon.
The `docker context` command makes it easy to configure these contexts and switch between them.

As an example, a single Docker client might be configured with two contexts:

- A default context running locally
- A remote, shared context

Once these contexts are configured,
you can use the `docker context use <context-name>` command
to switch between them.

## The anatomy of a context {#the-anatomy-of-a-context}

A context is a combination of several properties. These include:

- Name and description
- Endpoint configuration
- TLS info

To list available contexts, use the `docker context ls` command.

```console
$ docker context ls
NAME        DESCRIPTION                               DOCKER ENDPOINT               ERROR
default *                                             unix:///var/run/docker.sock
```

This shows a single context called "default".
It's configured to talk to a daemon through the local `/var/run/docker.sock` Unix socket.

The asterisk in the `NAME` column indicates that this is the active context.
This means all `docker` commands run against this context,
unless overridden with environment variables such as `DOCKER_HOST` and `DOCKER_CONTEXT`,
or on the command-line with the `--context` and `--host` flags.

Dig a bit deeper with `docker context inspect`.
The following example shows how to inspect the context called `default`.

```console
$ docker context inspect default
[
    {
        "Name": "default",
        "Metadata": {},
        "Endpoints": {
            "docker": {
                "Host": "unix:///var/run/docker.sock",
                "SkipTLSVerify": false
            }
        },
        "TLSMaterial": {},
        "Storage": {
            "MetadataPath": "\u003cIN MEMORY\u003e",
            "TLSPath": "\u003cIN MEMORY\u003e"
        }
    }
]
```

