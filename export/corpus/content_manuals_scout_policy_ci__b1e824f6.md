---
title: Evaluate policy compliance in CI
description: |
  Configure your continuous integration pipelines to fail
  when Policy Evaluation for an image is worse compared to baseline
keywords: scout, supply chain, policy, ci
---

## Prerequisites and comparison behavior

See [Image comparison and policy evaluation in CI](/manuals/scout/deep-dive/ci-comparison.md) for the baseline strategy, image-loading requirements, authentication, and pull request permissions.

## Example

The following example on how to run policy evaluation in CI uses the [Docker
Scout GitHub Action](https://github.com/marketplace/actions/docker-scout) to
execute the `compare` command on an image built in CI. The compare command has
a `to-env` input, which will run the comparison against an environment called
`production`. The `exit-on` input is set to `policy`, meaning that the
comparison fails only if policy compliance has worsened.

For authentication, runner image-store limitations, and pull request comment permissions, see [GitHub Actions example requirements](/manuals/scout/deep-dive/ci-comparison.md#github-actions-example-requirements).

```yaml
name: Docker

on:
  push:
    tags: ["*"]
    branches:
      - "main"
  pull_request:
    branches: ["**"]

env:
  REGISTRY: docker.io
  IMAGE_NAME: <IMAGE_NAME>
  DOCKER_ORG: <ORG>

jobs:
  build:
    permissions:
      pull-requests: write

    runs-on: ubuntu-latest
    steps:
      - name: Log into registry ${{ env.REGISTRY }}
        uses: docker/login-action@{{% param "login_action_version" %}}
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ secrets.REGISTRY_USER }}
          password: ${{ secrets.REGISTRY_TOKEN }}
      
      - name: Setup Docker buildx
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@{{% param "metadata_action_version" %}}
        with:
          images: ${{ env.IMAGE_NAME }}

      - name: Build image
        id: build-and-push
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          sbom: ${{ github.event_name != 'pull_request' }}
          provenance: ${{ github.event_name != 'pull_request' }}
          push: ${{ github.event_name != 'pull_request' }}
          load: ${{ github.event_name == 'pull_request' }}

      - name: Authenticate with Docker
        uses: docker/login-action@{{% param "login_action_version" %}}
        with:
          username: ${{ secrets.DOCKER_USER }}
          password: ${{ secrets.DOCKER_PAT }}

      - name: Compare
        if: ${{ github.event_name == 'pull_request' }}
        uses: docker/scout-action@v1
        with:
          command: compare
          image: ${{ steps.meta.outputs.tags }}
          to-env: production
          platform: "linux/amd64"
          ignore-unchanged: true
          only-severities: critical,high
          organization: ${{ env.DOCKER_ORG }}
          exit-on: policy
```

The following screenshot shows what the GitHub PR comment looks like when a
policy evaluation check fails because policy has become worse in the PR image
compared to baseline.

![Policy evaluation comment in GitHub PR](../images/scout-policy-eval-ci.webp)

This example has demonstrated how to run policy evaluation in CI with GitHub
Actions. Docker Scout also supports other CI platforms. For more information,
see [Docker Scout CI
integrations](../integrations/_index.md#continuous-integration).
