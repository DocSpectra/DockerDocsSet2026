---
title: Monitor DHI customization builds
description: Use Docker Hub or the CLI to view build details and logs.
---

Before you begin, review [customization capabilities](../core-concepts/customizations.md), [mirroring requirements](../core-concepts/mirroring.md), and [CLI setup](cli.md).

## Monitor customization builds

{{< tabs >}}
{{< tab name="Docker Hub" >}}

1. Sign in to [Docker Hub](https://hub.docker.com).
2. Select **My Hub**.
3. In the namespace drop-down, select your organization.
4. Select **Hardened Images** > **Manage**.
5. Select the **Customizations** tab.

{{< /tab >}}
{{< tab name="CLI" >}}

List builds for a customization:

```console
$ docker dhi customization build list my-org/dhi-golang "golang with git" --org my-org
```

Get details of a specific build:

```console
$ docker dhi customization build get my-org/dhi-golang "golang with git" <build-id> --org my-org
```

View build logs:

```console
$ docker dhi customization build logs my-org/dhi-golang "golang with git" <build-id> --org my-org
```

{{< /tab >}}
{{< /tabs >}}
