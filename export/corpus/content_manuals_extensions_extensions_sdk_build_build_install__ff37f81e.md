---
title: Build, install, and update an extension
description: Build and install an extension locally.
---

## Prerequisites

See [Development prerequisites](../prerequisites.md).

## Build and install

Now that you have configured the extension, you need to build the extension image that Docker Desktop will use to
install it.

```console
$ docker build --tag=awesome-inc/my-extension:latest .
```

This built an image tagged `awesome-inc/my-extension:latest`, you can run `docker inspect awesome-inc/my-extension:latest` to see more details about it.

Finally, you can install the extension and see it appearing in the Docker Desktop Dashboard.

```console
$ docker extension install awesome-inc/my-extension:latest
```

## Rebuild and update

Since you have modified the code or configuration of the extension, you must build the extension again.

```bash
docker build --tag=awesome-inc/my-extension:latest .
```

Once built, you need to update it, or install it if you haven't already done so.

```bash
docker extension update awesome-inc/my-extension:latest
```

