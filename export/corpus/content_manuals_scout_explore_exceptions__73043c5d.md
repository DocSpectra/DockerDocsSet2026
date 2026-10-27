---
title: Manage vulnerability exceptions
description: |
  Exceptions let you provide additional context and documentation for how
  vulnerabilities affect your artifacts, and provides the ability to
  suppress non-applicable vulnerabilities
keywords: scout, cves, suppress, vex, exceptions
---

For suppression behavior, creation methods, and visibility, see [Docker Scout exception behavior](/manuals/scout/deep-dive/exceptions.md).

## View exceptions in Docker Scout Dashboard or Docker Desktop

The [**Exceptions** tab](https://scout.docker.com/reports/vulnerabilities/exceptions)
of the Vulnerabilities page in Docker Scout Dashboard lists all exceptions for
for all images in your organization. From here, you can see more details about
each exception, the CVEs being suppressed, the images that exceptions apply to,
the type of exception and how it was created, and more.

For exceptions created using the GUI,
selecting the action menu lets you edit or remove the exception.

To view all exceptions for a specific image tag:

{{< tabs >}}
{{< tab name="Docker Scout Dashboard" >}}

1. Go to the [Images page](https://scout.docker.com/reports/images).
2. Select the tag that you want to inspect.
3. Open the **Exceptions** tab.

{{< /tab >}}
{{< tab name="Docker Desktop" >}}

1. Open the **Images** view in Docker Desktop.
2. Open the **Hub** tab.
3. Select the tag you want to inspect.
4. Open the **Exceptions** tab.

{{< /tab >}}
{{< /tabs >}}

## View exceptions in the CLI

{{< summary-bar feature_name="Docker Scout exceptions" >}}

Vulnerability exceptions are highlighted in the CLI when you run `docker scout
cves <image>`. If a CVE is suppressed by an exception, a `SUPPRESSED` label
appears next to the CVE ID. Details about the exception are also displayed.

![SUPPRESSED label in the CLI output](/scout/images/suppressed-cve-cli.png)

> [!IMPORTANT]
> In order to view exceptions in the CLI, you must configure the CLI to use
> the same Docker organization that you used to create the exceptions.
>
> To configure an organization for the CLI, run:
>
> ```console
> $ docker scout configure organization <organization>
> ```
>
> Replace `<organization>` with the name of your Docker organization.
>
> You can also set the organization on a per-command basis by using the
> `--org` flag:
>
> ```console
> $ docker scout cves --org <organization> <image>
> ```

To exclude suppressed CVEs from the output, use the `--ignore-suppressed` flag:

```console
$ docker scout cves --ignore-suppressed <image>
```
