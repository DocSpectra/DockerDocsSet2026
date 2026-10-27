---
title: Run an application with Compose
description: Foreground and background startup and shutdown for a Compose application.
---

## Run in the foreground

In the application directory, run:

```console
$ docker compose up --build
```

Press `ctrl`+`c` in the terminal to stop the application.

## Run in the background

You can run the application detached from the terminal by adding the `-d`
option. In the application directory, run:

```console
$ docker compose up --build -d
```

## Stop the background application

In the terminal, run:

```console
$ docker compose down
```

For Compose commands, see the [Compose CLI reference](/reference/cli/docker/compose/).
