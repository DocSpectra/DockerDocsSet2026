---
title: Using Gordon via CLI
linkTitle: CLI
description: Access and use Gordon through the docker ai command
weight: 20
---

{{< summary-bar feature_name="Gordon" >}}

The `docker ai` command provides a Terminal User Interface (TUI) for Gordon,
integrating AI assistance directly into your terminal.

Before starting, review the [prerequisites](../_index.md#prerequisites) and [permissions](permissions.md).

## On this page

- [Launch the TUI or pass a prompt](#basic-usage)
- [Set the working directory](#working-directory)
- [Disable Gordon](#disabling-gordon)
- [Check version or send feedback](#commands)

## Basic usage

Launch the interactive TUI:

```console
$ docker ai
```

This opens Gordon's terminal interface where you can type prompts, approve
actions, and continue conversations with full context.

<script src="https://asciinema.org/a/9kvZFH9LO9ZVDpwS.js" id="asciicast-9kvZFH9LO9ZVDpwS" async="true"></script>

Pass a prompt directly as an argument:

```console
$ docker ai "list my running containers"
```

Exit the TUI with `/exit` or <kbd>Ctrl+C</kbd>.

## Working directory

The working directory sets the default context for Gordon's file operations.

Gordon uses your current shell directory as the working directory:

```console
$ cd ~/my-project
$ docker ai
```

Override with `-C` or `--working-dir`:

```console
$ docker ai -C ~/different-project
```

For working directory access caveats, see [Security considerations](permissions.md#security-considerations).

## Disabling Gordon

Gordon CLI is part of Docker Desktop. To disable it, follow the
[Docker Desktop steps](docker-desktop.md#disabling-gordon).

## Commands

The `docker ai` command includes several subcommands:

Interactive mode (default):

```console
$ docker ai
```

Opens the TUI for conversational interaction.

Version:

```console
$ docker ai version
```

Displays the Gordon version.

Feedback:

```console
$ docker ai feedback
```

Opens a feedback form in your browser.
