---
title: Enable image analysis for repositories
---

## Prerequisites

See [Subscriptions and features](https://www.docker.com/pricing?ref=Docs&refAction=DocsScoutAnalysis)
to learn how many Scout-enabled repositories come with each subscription tier.

Before you can activate image analysis on a repository in a third-party registry,
the registry must be integrated with Docker Scout for your Docker organization.
Docker Hub is integrated by default. For more information, see
[Container registry integrations](/manuals/scout/deep-dive/integration-types.md#container-registries)

> [!NOTE]
>
> You must have the **Editor** or **Owner** role in the Docker organization to
> activate image analysis on a repository.

## Activate image analysis

To activate image analysis:

1. Go to [Repository settings](https://scout.docker.com/settings/repos) in the Docker Scout Dashboard.
2. Select the repositories that you want to enable.
3. Select **Enable image analysis**.

If your repositories already contain images,
Docker Scout pulls and analyzes the latest images automatically.
