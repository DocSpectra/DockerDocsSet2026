---
title: Discover DHI attestations with ORAS
description: Authenticate and discover per-platform attestations with ORAS.
---

See [DHI in CI/CD pipelines](../core-concepts/ci.md) for context.

## Discover attestations with ORAS

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
