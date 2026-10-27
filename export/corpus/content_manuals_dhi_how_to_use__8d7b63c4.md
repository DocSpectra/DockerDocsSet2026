---
title: Use a Docker Hardened Image
linktitle: Use an image
description: Learn how to pull, run, and reference Docker Hardened Images in Dockerfiles, CI pipelines, and standard development workflows.
keywords: use hardened image, docker pull secure image, non-root containers, multi-stage dockerfile, dev image variant
weight: 30
aliases:
  - /dhi/how-to/els/
  - /dhi/how-to/k8s/
---

You can use a Docker Hardened Image (DHI) just like any other image on Docker
Hub. DHIs follow the same familiar usage patterns. Pull them with `docker pull`,
reference them in your Dockerfile, and run containers with `docker run`.

The key difference is that DHIs are security-focused and intentionally minimal
to reduce the attack surface. This means some variants don't include a shell or
package manager, and may run as a non-root user by default.

> [!IMPORTANT]
>
> You must authenticate to the Docker Hardened Images registry (`dhi.io`) to
> pull DHI Community images. You can authenticate using either of the following:
>
> - **Docker ID and password:** Use your Docker Hub username and password. If
>   you don't have a Docker account, [create one](../../accounts/create-account.md)
>   for free.
> - **Access token:** Use a [personal access token
>   (PAT)](../../security/access-tokens.md) for personal accounts, or an
>   [organization access token
>   (OAT)](../../enterprise/security/access-tokens.md) with your organization
>   name as the username.
>
> Run `docker login dhi.io` to authenticate.

## Considerations when adopting DHIs

Docker Hardened Images are intentionally minimal to improve security. If you're
updating existing Dockerfiles or frameworks to use DHIs, keep in mind that
runtime images don't include shells or package managers, run as non-root users
by default, and may have different configurations than images you're familiar
with.

For a comprehensive checklist of migration considerations and detailed guidance,
see [Migrate to Docker Hardened Images](../migration/_index.md).

Choose a task:

- [Pull, run, and reference an image](#pull-run-and-reference-dhis)
- [Use an image in CI/CD](#use-a-dhi-in-cicd-pipelines) or [discover attestations with ORAS](#discover-attestations-with-oras)
- [Run compiled executables](#use-a-static-image-for-compiled-executables) or [build framework-based applications](#use-dev-variants-for-framework-based-applications)
- [Use compliance and ELS variants](#use-compliance-and-els-variants)
- [Deploy to Kubernetes](./kubernetes.md) or [use Helm](./helm.md)

## Pull, run, and reference DHIs

Docker Hardened Images use different image references depending on your
subscription:

| Subscription        | Image reference            | Authentication        |
|---------------------|----------------------------|-----------------------|
| Community           | `dhi.io/<image>:<tag>`     | `docker login dhi.io` |
| Select & Enterprise | `<your-org>/<image>:<tag>` | `docker login`        |

Select and Enterprise users should [mirror](./mirror.md) repositories to their
Docker Hub organization to access compliance variants and customization
features.

After authenticating, use the image reference in standard Docker commands and
Dockerfiles. For example:

```console
$ docker pull dhi.io/python:3.13
$ docker run --rm dhi.io/python:3.13 python -c "print('Hello from DHI')"
```

```dockerfile
FROM dhi.io/python:3.13
COPY . /app
CMD ["python", "/app/main.py"]
```

For multi-stage builds:
- Use a `-dev` tag for build stages that need a shell or package manager. See
  [Use dev variants for framework-based
  applications](#use-dev-variants-for-framework-based-applications).
- Use the `static` image for compiled executables with minimal runtime
  dependencies. See [Use a static image for compiled
  executables](#use-a-static-image-for-compiled-executables).

To learn how to search for available variants, see [Search and evaluate
images](./explore.md).

## Use a DHI in CI/CD pipelines

Docker Hardened Images work just like any other image in your CI/CD pipelines.
You can reference them in Dockerfiles, pull them as part of a pipeline step, or
run containers based on them during builds and tests.

Unlike typical container images, DHIs also include signed
[attestations](../core-concepts/attestations.md) such as SBOMs and provenance
metadata. You can incorporate these into your pipeline to support supply chain
security, policy checks, or audit requirements if your tooling supports it.

To strengthen your software supply chain, consider adding your own attestations
when building images from DHIs. This lets you document how the image was built,
verify its integrity, and enable downstream validation and policy enforcement
using tools like Docker Scout.

To learn how to attach attestations during the build process, see [Docker Build
Attestations](/manuals/build/metadata/attestations.md).

For Docker Scout's provenance requirements when scanning images built from a
DHI, see [Scan child images and CI builds](./scan-child-images.md).

### Discover attestations with ORAS

You can use [ORAS](https://oras.land/) to discover and inspect the attestations
attached to Docker Hardened Images. This is particularly useful in CI/CD
pipelines for supply chain security validation and compliance checks.

For automated workflows, authenticate using an [organization access token
(OAT)](../../enterprise/security/access-tokens.md). OATs are owned by the
organization rather than an individual user, making them better suited for CI/CD
pipelines.

To discover attestations with ORAS:

1. [Generate an organization access
   token](../../enterprise/security/access-tokens.md) with **Read public
   repositories** scope.

   The following example shows how to discover attestations on DHI community
   images from `dhi.io`. If you're discovering attestations on images mirrored to
   your organization, generate an OAT scoped to read from your mirrored repository
   instead of **Read public repositories**.

2. Sign in to `dhi.io` using your organization name as the username and the OAT
   as the password.

   > [!WARNING]
   >
   > The following examples export credentials directly on the command line for
   > demonstration purposes. This exposes sensitive tokens in your shell history
   > and process list. In production environments, use secure methods such as
   > reading from files with restricted permissions, environment files loaded
   > at runtime, or secret management tools.

    ```console
    $ oras login dhi.io -u <YOUR_ORGANIZATION_NAME>
    ```

   Or non-interactively in a CI/CD pipeline, set your organization name and token:

   ```console
   $ export DOCKER_ORG="YOUR_ORGANIZATION_NAME"
   $ export OAT="YOUR_ORGANIZATION_ACCESS_TOKEN"
   $ echo $OAT | oras login dhi.io -u "$DOCKER_ORG" --password-stdin
   ```

3. Discover attestations on a DHI image:

   ```console
   $ oras discover dhi.io/node:24-dev --platform linux/amd64
   ```

   > [!NOTE]
   >
   > The `--platform` flag is required. Without it, `oras discover` resolves to
   > the multi-arch image index, which returns only an index-level signature
   > rather than the full set of per-platform attestations.

   A successful response lists the attestations attached to the image,
   including SBOMs, provenance, vulnerability reports, and changelog metadata.

## Use a static image for compiled executables

Docker Hardened Images include a `static` image repository designed specifically
for running compiled executables in an extremely minimal and secure runtime.
Unlike a non-hardened `FROM scratch` image, the DHI `static` image includes
attestations and essential packages like `ca-certificates`.

Use a `-dev` or other builder image to compile your binary, then copy the output
into a `static` image:

```dockerfile
FROM dhi.io/golang:1.22-dev AS build
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o myapp

FROM dhi.io/static:20230311
COPY --from=build /app/myapp /myapp
ENTRYPOINT ["/myapp"]
```

For more multi-stage build patterns, see the [Go migration
example](../migration/examples/go.md).

## Use dev variants for framework-based applications

If you're building applications with frameworks that require package managers or
build tools (such as Python, Node.js, or Go), use a `-dev` variant during the
development or build stage. These variants include essential utilities like
shells, compilers, and package managers to support local iteration and CI
workflows.

Use `-dev` images in your inner development loop or in isolated CI stages to
maximize productivity. Once you're ready to produce artifacts for production,
switch to a smaller runtime variant to reduce the attack surface and image size.

For detailed multi-stage Dockerfile examples using dev variants, see the
migration examples:
- [Go](../migration/examples/go.md)
- [Python](../migration/examples/python.md)
- [Node.js](../migration/examples/node.md)

## Use compliance and ELS variants

{{< summary-bar feature_name="Docker Hardened Images" >}}

With a DHI Select or DHI Enterprise subscription, you can access additional
image variants:

- Compliance variants: FIPS-enabled and STIG-ready images for regulatory
  requirements
- ELS (Extended Lifecycle Support) variants (requires add-on): Security patches
  for end-of-life image versions

To access these variants, [mirror](./mirror.md) the repository to your Docker
Hub organization. For ELS, enable **Mirror end-of-life images** when setting up
mirroring. Once mirrored, use the compliance or EOL tags like any other image
tag.

## Use with Kubernetes

For image pull secrets, registry selection, a test pod, and cleanup steps, see
[Use Docker Hardened Images with Kubernetes](./kubernetes.md). For
OpenShift-specific steps, see [Use Docker Hardened Images with Red Hat
OpenShift](/guides/dhi-openshift/).

### Create an image pull secret

See [Create an image pull secret](./kubernetes.md#create-an-image-pull-secret)
for registry selection and authentication options.

#### Using an access token

See [Using an access token](./kubernetes.md#using-an-access-token).

#### Using Docker Desktop credentials

See [Using Docker Desktop credentials](./kubernetes.md#using-docker-desktop-credentials).

### Test the image pull secret

See [Test the image pull secret](./kubernetes.md#test-the-image-pull-secret)
for the test pod, expected output, and cleanup.
