---
title: Secrets in Compose
description: Secret access, file mounts, and environment variable risks in Compose.
---

A secret is any piece of data, such as a password, certificate, or API key, that shouldn’t be transmitted over a network or stored unencrypted in a Dockerfile or in your application’s source code.

{{% include "compose/secrets.md" %}}

Environment variables are often available to all processes, and it can be difficult to track access. They can also be printed in logs when debugging errors without your knowledge. Using secrets mitigates these risks.

## Use secrets

Secrets are mounted as a file in `/run/secrets/<secret_name>` inside the container.

Getting a secret into a container is a two-step process. First, define the secret using the [top-level secrets element in your Compose file](/reference/compose-file/secrets.md). Next, update your service definitions to reference the secrets they require with the [secrets attribute](/reference/compose-file/services.md#secrets). Compose grants access to secrets on a per-service basis.

Unlike the other methods, this permits granular access control within a service container via standard filesystem permissions.
