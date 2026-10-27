---
title: Pin Buildx and BuildKit versions in GitHub Actions
---

For common setup, see [GitHub Actions prerequisites](/guides/gha.md#prerequisites) and
[repository credentials](registry-credentials.md).

## Version pinning

By default, the action will attempt to use the latest version of [Buildx](https://github.com/docker/buildx)
available on the GitHub Runner (the build client) and the latest release of
[BuildKit](https://github.com/moby/buildkit) (the build server).

To pin to a specific version of Buildx, use the `version` input. For example,
to pin to Buildx v0.10.0:

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
  with:
    version: v0.10.0
```

To pin to a specific version of BuildKit, use the `image` option in the
`driver-opts` input. For example, to pin to BuildKit v0.11.0:

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
  with:
    driver-opts: image=moby/buildkit:v0.11.0
```

