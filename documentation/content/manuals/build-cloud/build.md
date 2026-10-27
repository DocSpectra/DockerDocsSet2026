---
title: Build an image with Docker Build Cloud
---

Before following this task, see [Docker Build Cloud setup](setup.md).



For loading and platform choices, see [Outputs and platforms](outputs.md).
For builder selection, see [Select the cloud builder](select-builder.md).

To build using Docker Build Cloud, invoke a build command and specify the name of the
builder using the `--builder` flag.

```console
$ docker buildx build --builder cloud-<ORG>-<BUILDER_NAME> --tag <IMAGE> .
```

