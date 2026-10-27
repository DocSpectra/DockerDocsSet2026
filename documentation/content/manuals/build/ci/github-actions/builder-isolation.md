---
title: Select isolated builders in GitHub Actions
---

For common setup, see [GitHub Actions prerequisites](/guides/gha.md#prerequisites) and
[repository credentials](registry-credentials.md).

## Isolated builders

The following example shows how you can select different builders for different
jobs.

An example scenario where this might be useful is when you are using a monorepo,
and you want to pinpoint different packages to specific builders. For example,
some packages may be particularly resource-intensive to build and require more
compute. Or they require a builder equipped with a particular capability or
hardware.

For more information about remote builder, see [`remote` driver](/manuals/build/builders/drivers/remote.md)
and the [append builder nodes example](builder-nodes.md#append-additional-nodes-to-the-builder).

```yaml
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Set up builder1
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
        id: builder1
      
      - name: Set up builder2
        uses: docker/setup-buildx-action@{{% param "setup_buildx_action_version" %}}
        id: builder2
      
      - name: Build against builder1
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          builder: ${{ steps.builder1.outputs.name }}
          target: mytarget1
      
      - name: Build against builder2
        uses: docker/build-push-action@{{% param "build_push_action_version" %}}
        with:
          builder: ${{ steps.builder2.outputs.name }}
          target: mytarget2
```
