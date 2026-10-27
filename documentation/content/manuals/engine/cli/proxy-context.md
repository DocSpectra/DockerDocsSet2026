---
title: Docker proxy configuration scope
---

## Container and build proxy variables {#container-and-build-proxy-variables}

The Docker CLI can configure proxies via environment variables in containers.

These settings are used to configure proxy environment variables for containers
only, and not used as proxy settings for the Docker CLI or the Docker Engine
itself. Builds and containers use the configuration specified in
`~/.docker/config.json`.

## Daemon proxy settings {#daemon-proxy-settings}

If your organization uses a proxy server to connect to the internet, you may
need to configure the Docker daemon to use the proxy server. The daemon uses
a proxy server to access images stored on Docker Hub and other registries,
and to reach other nodes in a Docker swarm.


## Docker Desktop {#docker-desktop}

> [!IMPORTANT]
>
> Proxy configurations specified in the `daemon.json` are ignored by Docker
> Desktop. If you use Docker Desktop, you can configure proxies using the
> [Docker Desktop settings](/manuals/desktop/settings-and-maintenance/settings.md#proxies).

## Proxy environment variable conventions {#proxy-environment-variable-conventions}

> [!NOTE]
>
> Unfortunately, there's no standard that defines how web clients should handle proxy 
> environment variables, or the format for defining them.
>
> If you're interested in the history of these variables, check out this blog
> post on the subject, by the GitLab team:
> [We need to talk: Can we standardize NO_PROXY?](https://about.gitlab.com/blog/2021/01/27/we-need-to-talk-no-proxy/).

