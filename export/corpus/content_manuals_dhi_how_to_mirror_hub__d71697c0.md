---
title: Mirror DHI repositories to a Docker Hub organization
description: Start, list, and stop organization mirrors with Docker Hub, CLI, or Terraform.
---

Before you begin, review [mirroring requirements](../core-concepts/mirroring.md) and [CLI installation and configuration](cli.md).

## Mirror a DHI repository to your organization

To mirror repositories, you must be an organization owner or editor, or use a
personal access token (PAT) or organization access token (OAT). See the CLI and
Terraform tabs in the following sections for required permission scopes.

- Image repositories: Mirroring lets you customize images by adding packages,
  OCI artifacts (such as custom certificates or additional tools), environment
  variables, labels, and other configuration settings. For more details, see
  [Image customization context](../core-concepts/customizations.md).

- Chart repositories: Mirroring lets you customize image references within
  the chart. This is particularly useful when using customized images or when
  you've mirrored images to a third-party registry and need the chart to
  reference those custom locations. For more details, see [Chart customization context](../core-concepts/customizations.md).

{{< tabs >}}
{{< tab name="Docker Hub" >}}

1. Go to [Docker Hub](https://hub.docker.com) and sign in.
2. Select **My Hub**.
3. In the namespace drop-down, select your organization.
4. Select **Hardened Images** > **Catalog**.
5. Select a DHI repository to view its details.
6. Mirror the repository:
    - To mirror an image repository, select **Use this image** > **Mirror
      repository**, and then follow the on-screen instructions. If you have the ELS add-on, you can also
      select **Enable support for end-of-life versions**.
    - To mirror a Helm chart repository, select **Get Helm chart**, and then follow the on-screen instructions.

It may take a few minutes for all the tags to finish mirroring.

{{< /tab >}}
{{< tab name="CLI" >}}

Authenticate with `docker login` using your Docker credentials, a [personal
access token (PAT)](../../security/access-tokens.md) with **Read & Write**
permissions, or an [organization access token
(OAT)](../../enterprise/security/access-tokens.md). When using an OAT, the
available operations depend on the token's permission scope:

- To list mirrored repositories, the OAT must have read (pull) access to the
  relevant repositories. Results are scoped to repositories the OAT can access.
- To create a mirror to an existing destination repository, the OAT must have
  push access to that repository. To create a mirror to a new destination
  repository that doesn't yet exist, the OAT must have org-wide repository
  access (for example, `<org>/*` with pull or push). Repository-scoped access to
  the future repository name is not sufficient.
- To stop mirroring, the OAT must have push access to the relevant repository.
- OATs with public repository read-only access cannot list or manage mirrored
  repositories.

Use the [`docker dhi mirror`](/reference/cli/docker/dhi/mirror/) command:

```console
$ docker dhi mirror start --org my-org \
  -r dhi/golang,my-org/dhi-golang \
  -r dhi/nginx,my-org/dhi-nginx \
  -r dhi/prometheus-chart,my-org/dhi-prometheus-chart
```

Mirror with dependencies:

```console
$ docker dhi mirror start --org my-org -r dhi/golang,my-org/dhi-golang --dependencies
```

List mirrored images in your organization:

```console
$ docker dhi mirror list --org my-org
```

Filter mirrored images by name or type:

```console
$ docker dhi mirror list --org my-org --filter python
$ docker dhi mirror list --org my-org --type image
$ docker dhi mirror list --org my-org --type helm-chart
```

{{< /tab >}}
{{< tab name="Terraform" >}}

You can manage DHI mirrors as infrastructure-as-code using the [DHI Terraform
provider](https://registry.terraform.io/providers/docker-hardened-images/dhi/latest/docs).

First, install and configure the provider:

```hcl
terraform {
  required_providers {
    dhi = {
      source = "docker-hardened-images/dhi"
    }
  }
}

provider "dhi" {
  docker_hub_username = var.docker_username
  docker_hub_password = var.docker_password
  organization        = var.org_name
}
```

> [!NOTE]
>
> Instead of specifying credentials in the provider block, you can set the
> `DOCKER_USERNAME`, `DOCKER_PASSWORD`, and `DHI_ORG` environment variables. You
> can also authenticate using an organization access token (OAT) in place of a
> password. Set `DOCKER_USERNAME` to your organization namespace and
> `DOCKER_PASSWORD` to the OAT. When using an OAT, the same permission scopes
> apply as with the CLI: read (pull) access is required to list mirrors, and
> push access is required to create or delete them.

Then, define a `dhi_mirror` resource for each repository you want to mirror:

```hcl
resource "dhi_mirror" "golang" {
  source_namespace = "dhi"
  source_name      = "golang"
  destination_name = "dhi-golang"
}

resource "dhi_mirror" "nginx" {
  source_namespace = "dhi"
  source_name      = "nginx"
  destination_name = "dhi-nginx"
}
```

To enable Extended Lifecycle Support (ELS) variants, set the `els` attribute:

```hcl
resource "dhi_mirror" "golang" {
  source_namespace = "dhi"
  source_name      = "golang"
  destination_name = "dhi-golang"
  els              = true
}
```

Run `terraform apply` to create the mirrors.

For the full list of resource attributes, see the [Terraform Registry
documentation](https://registry.terraform.io/providers/docker-hardened-images/dhi/latest/docs/resources/mirror).

{{< /tab >}}
{{< /tabs >}}

After mirroring, the repository appears in your organization's repository list,
prefixed by `dhi-`, and continues to receive updated images. It behaves like any
other Docker Hub repository, so you can manage access and permissions, configure
webhooks, and use other standard Hub features. See [Docker Hub
repositories](/manuals/docker-hub/repos/_index.md) for details.

### Stop mirroring a repository

After you stop mirroring, the repository remains, but it no longer receives
updates. You can still use the last images or charts that were mirrored.

> [!NOTE]
>
> If you only want to stop mirroring ELS versions, you can clear the ELS
> option in the mirrored repository's **Settings** tab.

{{< tabs >}}
{{< tab name="Docker Hub" >}}

1. Go to [Docker Hub](https://hub.docker.com) and sign in.
2. Select **My Hub**.
3. In the namespace drop-down, select your organization that has access to DHI.
4. Select **Hardened Images** > **Manage**.
5. Select the **Mirrored Images** or **Mirrored Helm charts** tab.
6. In the far right column of the repository you want to stop mirroring, select the menu icon.
7. Select **Stop mirroring**.

{{< /tab >}}
{{< tab name="CLI" >}}

Authenticate with `docker login` using your Docker credentials, a [personal
access token (PAT)](../../security/access-tokens.md) with **Read & Write**
permissions, or an [organization access token
(OAT)](../../enterprise/security/access-tokens.md) with push access to the
relevant repository.

Use the [`docker dhi mirror`](/reference/cli/docker/dhi/mirror/) command:

```console
$ docker dhi mirror stop --org my-org dhi-golang
```

{{< /tab >}}
{{< tab name="Terraform" >}}

To stop mirroring, remove the `dhi_mirror` resource from your Terraform
configuration and run `terraform apply`. The repository remains in your
organization but no longer receives updates.

{{< /tab >}}
{{< /tabs >}}
