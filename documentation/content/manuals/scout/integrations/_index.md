---
description: How to setup Docker Scout with other systems.
keywords: supply chain, security, integrations, registries, ci, environments
title: Integrating Docker Scout with other systems
linkTitle: Integrations
weight: 80
---

For integration behavior, see [Integration categories](/manuals/scout/deep-dive/integration-types.md).

## Integration categories

You'll get different insights depending on where and how you choose to integrate
Docker Scout.

### Container registries

See [Container registries](/manuals/scout/deep-dive/integration-types.md#container-registries).

The following container registry integrations are available:

- [Amazon Elastic Container Registry](./registry/ecr.md)
- [Azure Container Registry](./registry/acr.md)
- [JFrog Artifactory](./registry/artifactory.md)

### Continuous Integration

See [Continuous Integration](/manuals/scout/deep-dive/integration-types.md#continuous-integration).

The following CI integrations are available:

- [GitHub Actions](./ci/gha.md)
- [GitLab](./ci/gitlab.md)
- [Microsoft Azure DevOps Pipelines](./ci/azure.md)
- [Circle CI](./ci/circle-ci.md)
- [Jenkins](./ci/jenkins.md)

### Environment monitoring

See [Environment monitoring](/manuals/scout/deep-dive/integration-types.md#environment-monitoring).

The following environment monitoring integrations are available

- [Sysdig](./environment/sysdig.md)
- [Generic environment integration with CLI](./environment/cli.md)

For more information about environment integrations, see
[Environments](./environment/_index.md).

### Code quality

See [Code quality](/manuals/scout/deep-dive/integration-types.md#code-quality).

The following code quality integrations are available:

- [SonarQube](./code-quality/sonarqube.md)

### Source code management

See [Source code management](/manuals/scout/deep-dive/integration-types.md#source-code-management).

The following source code management integrations are available:

- [GitHub](source-code-management/github.md) {{< badge color=blue text=Beta >}}

### Team collaboration

See [Team collaboration](/manuals/scout/deep-dive/integration-types.md#team-collaboration).

The following team collaboration integrations are available:

- [Slack](./team-collaboration/slack.md)
