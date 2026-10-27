---
title: Try Gordon in Docker Desktop or the CLI
description: Start a Gordon session, review its proposed actions, and try example prompts.
---

## Prerequisites

Review the [Gordon access requirements](requirements.md).

## Quick start

{{< tabs >}}
{{< tab name="Docker Desktop" >}}

1. Open Docker Desktop.
2. Select **Gordon** in the sidebar.
3. Select your project directory.
4. Type a question: "What containers are running?"

   ![Gordon running in Docker Desktop](./images/gordon_gui.avif)

5. Review Gordon's proposed actions and approve.

{{< /tab >}}
{{< tab name="CLI" >}}

1. Open your terminal and run:

   ```console
   $ docker ai
   ```

   This opens the Terminal User Interface (TUI) for Gordon.

2. Type a question: "what containers are running?" and press <kbd>Enter</kbd>.

   ![Gordon running in the terminal](./images/gordon_tui.avif?border=true)

3. Review Gordon's proposed actions and approve by typing `y`.

{{< /tab >}}
{{< /tabs >}}

## Permissions

By default, Gordon asks for approval before executing actions. You can approve
individual actions or allow all actions for the current session.

![Gordon permission request](./images/permissions.avif)

Permissions reset for each session. To configure default permissions or enable
auto-approve mode, see [Permissions](./how-to/permissions.md).

## Try these examples

Container inspection:

```console
$ docker ai "show me logs from my nginx container"
```

Dockerfile review:

```console
$ docker ai "review my Dockerfile for best practices"
```

Image management:

```console
$ docker ai "list my local images and their sizes"
```
