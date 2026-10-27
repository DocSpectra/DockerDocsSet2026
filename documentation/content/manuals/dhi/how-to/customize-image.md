---
title: Customize a Docker Hardened Image
description: Create and manage image customizations with Docker Hub, CLI, and Terraform.
---

Before you begin, review [customization capabilities](../core-concepts/customizations.md), [mirroring requirements](../core-concepts/mirroring.md), and [CLI setup](cli.md).

## Customize a Docker Hardened Image

To add a customized Docker Hardened Image to your organization, an organization
owner must first [mirror](mirror-hub.md) the DHI repository to your organization
on Docker Hub. Once the repository is mirrored, any user with access to the
mirrored DHI repository can create a customized image.

You can create customizations using either the DHI CLI or the Docker Hub web interface.

{{< tabs >}}
{{< tab name="Docker Hub" >}}

1. Sign in to [Docker Hub](https://hub.docker.com).
1. Select **My Hub**.
1. In the namespace drop-down, select your organization that has a mirrored DHI
   repository.
1. Select **Hardened Images** > **Manage** > **Mirrored Images**.
1. For the mirrored DHI repository you want to customize, select the menu icon in the far right column.
1. Select **Customize**.

   At this point, the on-screen instructions will guide you through the
   customization process. You can continue with the following steps for more
   details.

1. Select one or more images or Helm charts and versions you want to customize.

   When selecting multiple images and versions, all selections must share the
   same distribution and distribution version. For example, you can select
   `dhi-node:22_alpine3.23` and `dhi-python:3.13_alpine3.23` together (both
   Alpine 3.23), but you cannot mix `dhi-node:22_debian` with Alpine images, or
   mix different Alpine versions like `alpine3.23` and `alpine3.22`.

   Alternatively, you can select multiple Helm chart versions to apply the same
   customization to all of them. You cannot mix images and Helm charts in the
   same customization.

1. Select **Next**.
1. Optional. Add packages.

   1. In the packages drop-down, select the packages you want to add to the
      image.

      The packages available in the drop-down are OS system packages for the
      selected image variant. For version 3.23 Alpine-based images, these are
      hardened packages that have been built from source by Docker with
      cryptographic signatures and full supply chain security. For version 3.22
      Alpine-based images and Debian-based images, these are standard system
      packages.

   1. In the **OCI artifacts** drop-down, first, select the repository that
      contains the OCI artifact image. Then, select the tag you want to use from
      that repository. Finally, specify the specific paths you want to include
      from the OCI artifact image.

      The OCI artifacts are images that you have previously
      built and pushed to a repository in the same namespace as the mirrored
      DHI. For example, you can add a custom root CA certificate or another
      image that contains a tool you need, like adding Python to a Node.js
      image. For more details on how to create an OCI artifact image, see
      [Create an OCI artifact image](create-oci-artifacts.md#create-an-oci-artifact-image-for-image-customization).

      You can add multiple OCI artifact images to a single customization. When
      you add more than one, they're applied in the order you add them in the
      **OCI artifacts** drop-down. If multiple images contain directories or
      files with the same path, images added later overwrite files from images
      added earlier. To manage this, you must select paths to include and
      optionally exclude from each OCI artifact image. This allows you to
      control which files are included in the final customized image.

      By default, no files are included from the OCI artifact image. You must
      explicitly include the paths you want. After including a path, you can
      then explicitly exclude files or directories underneath it.

      > [!NOTE]
      >
      > When files necessary for runtime are overwritten by OCI artifacts, the
      > image build still succeeds, but you may have issues when running the
      > image.

   1. In the **Scripts** section, you can add, edit, or remove scripts.

      Scripts let you add files to the container image that you can access at runtime. They are not executed during
      the build process. This is useful for services that require pre-start initialization, such as setup scripts or
      file writes to directories like `/var/lock` or `/out`.

      You must specify the following:

      - The path where the script will be placed
      - The script content
      - The UID and GID ownership of the script
      - The octal file permissions of the script

1. Select **Next: Configure** to configure the following image settings:

   > [!NOTE]
   >
   > When customizing multiple images at once, many of these configuration
   > options are limited by default and may not be available.

   1. Specify the [environment variables](/reference/dockerfile/#env) and their
      values that the image will contain.
   1. Add [labels](/reference/dockerfile/#label) to the image.
   1. Add [annotations](/build/metadata/annotations/) to the image.
   1. Specify the users to add to the image. When you add a user, a home
      directory is automatically created for that user with 0755 permissions.
   1. Specify the user groups to add to the image.
   1. Select which [user](/reference/dockerfile/#user) to run the images as.
   1. Add [`ENTRYPOINT`](/reference/dockerfile/#entrypoint) arguments to the
      image. These arguments are appended to the base image's entrypoint.
   1. Add [`CMD`](/reference/dockerfile/#cmd) arguments to the image. These
      arguments are appended to the base image's command.
   1. Override the default (`/`) [working
      directory](/reference/dockerfile/#workdir) for the image.
   1. Specify a suffix for the customization name that is appended to the
      customized image's tag. For example, if you specify `custom` when
      customizing the `dhi-python:3.13` image, the customized image will be
      tagged as `dhi-python:3.13_custom`.
   1. Select the compression format for the image layers. You can choose between
      **ZSTD** (default) or **GZIP** compression. **ZSTD** typically provides
      faster image pulls and better compression ratios, but may have
      compatibility issues with older software. If you need compatibility with
      older Docker versions, use **GZIP**.
   1. Select the platforms you want to build the image for. You must select at
      least one platform.

1. Select **Next: Review customization**.

1. Select **Create Customization**.

   A summary of the customization appears. It may take some time for the image
   to build. Once built, it will appear in the **Tags** tab of the repository,
   and your team members can pull it like any other image.

{{< /tab >}}
{{< tab name="CLI" >}}

Authenticate with `docker login` using your Docker credentials, a [personal
access token (PAT)](../../security/access-tokens.md) with **Read & Write**
permissions, or an [organization access token
(OAT)](../../enterprise/security/access-tokens.md). When using an OAT, the
available operations depend on the token's permission scope:

- To list or get customizations, or to view build logs, the OAT must have read
  (pull) access to the destination repository. Results are scoped to
  repositories the OAT can access.
- To create, update, or delete a customization, the OAT must have push access to
  the destination repository. Bulk operations require push access to every
  referenced destination repository.

Use the [`docker dhi customization`](/reference/cli/docker/dhi/customization/) command:

```console
# Prepare a customization scaffold
$ docker dhi customization prepare golang 1.25 \
  --org my-org \
  --destination my-org/dhi-golang \
  --name "golang with git" \
  --output my-customization.yaml

# Create a customization
$ docker dhi customization create my-customization.yaml --org my-org

# List customizations
$ docker dhi customization list --org my-org

# Filter customizations by name, repository, or source
$ docker dhi customization list --org my-org --filter git
$ docker dhi customization list --org my-org --repo dhi-golang
$ docker dhi customization list --org my-org --source golang

# Get a customization
$ docker dhi customization get my-org/dhi-golang "golang with git" --org my-org --output my-customization.yaml

# Update a customization
$ docker dhi customization edit my-customization.yaml --org my-org

# Delete a customization
$ docker dhi customization delete my-org/dhi-golang "golang with git" --org my-org

# Delete without confirmation prompt
$ docker dhi customization delete my-org/dhi-golang "golang with git" --org my-org --yes
```

{{< /tab >}}
{{< tab name="Terraform" >}}

You can manage DHI customizations as infrastructure-as-code using the [DHI
Terraform
provider](https://registry.terraform.io/providers/docker-hardened-images/dhi/latest/docs).
If you haven't configured the provider yet, see the Terraform tab in [Mirror a
repository](mirror-hub.md) for setup instructions.

Define a `dhi_customization` resource for each customization:

```hcl
resource "dhi_customization" "golang_with_git" {
  repository = "dhi-golang"
  name       = "golang with git"

  contents {
    packages = ["git", "curl"]
  }

  platform {
    os           = "linux"
    architecture = "amd64"
  }
}
```

The `dhi_customization` resource also supports optional configuration blocks
for `accounts`, `files`, `labels`, `annotations`, `environment`, `entrypoint`,
`cmd`, `user`, `workdir`, and `stop_signal`.

Run `terraform apply` to create the customization.

To edit a customization, update the resource configuration and run `terraform
apply`. To delete a customization, remove the resource and run `terraform apply`.

For the full list of resource attributes, see the [Terraform Registry
documentation](https://registry.terraform.io/providers/docker-hardened-images/dhi/latest/docs/resources/customization).

> [!NOTE]
>
> Monitoring customization builds is not available through the Terraform
> provider. Use the Docker Hub web interface or the DHI CLI to monitor builds.

{{< /tab >}}
{{< /tabs >}}
