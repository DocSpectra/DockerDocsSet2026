---
title: GitHub Actions cache requirements
---


This page contains examples on using the cache storage backends with GitHub
Actions.

> [!NOTE]
>
> See [Cache storage backends](../../cache/backends/_index.md) for more
> details about cache storage backends.


## Cache backend API

{{< summary-bar feature_name="Cache backend API" >}}

The [GitHub Actions cache exporter](../../cache/backends/gha.md)
backend uses the [GitHub Cache service API](https://github.com/tonistiigi/go-actions-cache)
to fetch and upload cache blobs. That's why you should only use this cache
backend in a GitHub Action workflow, as the `url` (`$ACTIONS_RESULTS_URL`) and
`token` (`$ACTIONS_RUNTIME_TOKEN`) attributes only get populated in a workflow
context.

> [!IMPORTANT]
>
> As of April 15th, 2025, [only GitHub Cache service API v2 is supported.](https://gh.io/gha-cache-sunset). The legacy v1 API has been shut down.
>
> If you encounter the following error during your build:
>
> ```console
> ERROR: failed to solve: This legacy service is shutting down, effective April 15, 2025. Migrate to the new service ASAP. For more information: https://gh.io/gha-cache-sunset
> ```
>
> You're probably using outdated tools that only support the legacy GitHub
> Cache service API v1. Here are the minimum versions you need to upgrade to
> depending on your use case:
> * Docker Buildx >= v0.21.0
> * BuildKit >= v0.20.0
> * Docker Compose >= v2.33.1
> * Docker Engine >= v28.0.0 (if you're building using the Docker driver with containerd image store enabled)
>
> If you're building using the `docker/build-push-action` or `docker/bake-action`
> actions on GitHub hosted runners, Docker Buildx and BuildKit are already up
> to date but on self-hosted runners, you may need to update them yourself.
> Alternatively, you can use the `docker/setup-buildx-action` action to install
> the latest version of Docker Buildx:
>
> ```yaml
> - name: Set up Docker Buildx
>   uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
>   with:
>    version: latest
> ```
>
> If you're building using Docker Compose, you can use the
> `docker/setup-compose-action` action:
>
> ```yaml
> - name: Set up Docker Compose
>   uses: docker/setup-compose-action@{{% param "setup_compose_action_version" %}}
>   with:
>    version: latest
> ```
>
> If you're building using the Docker Engine with the containerd image store
> enabled, you can use the `docker/setup-docker-action` action:
>
> ```yaml
> -
>   name: Set up Docker
>   uses: docker/setup-docker-action@{{% param "setup_docker_action_version" %}}
>   with:
>     version: latest
>     daemon-config: |
>       {
>         "features": {
>           "containerd-snapshotter": true
>         }
>       }
> ```


