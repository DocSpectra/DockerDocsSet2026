---
title: Build and publish service images
description: Use the Compose build and image example with shared build rules.
---

## Build rules and caveats

See [build paths and syntax](build.md), [pull policy](services.md#pull_policy), and [build attributes](build.md#attributes).

## Illustrative example

The following example illustrates Compose Build Specification concepts with a concrete sample application. The sample is non-normative.

```yaml
services:
  frontend:
    image: example/webapp
    build: ./webapp

  backend:
    image: example/database
    build:
      context: backend
      dockerfile: ../backend.Dockerfile

  custom:
    build: ~/custom
```

When used to build service images from source, the Compose file creates three Docker images:

- `example/webapp`: A Docker image is built using `webapp` sub-directory, within the Compose file's folder, as the Docker build context. Lack of a `Dockerfile` within this folder returns an error.
- `example/database`: A Docker image is built using `backend` sub-directory within the Compose file's folder. `backend.Dockerfile` file is used to define build steps, this file is searched relative to the context path, which means `..` resolves to the Compose file's folder, so `backend.Dockerfile` is a sibling file.
- A Docker image is built using the `custom` directory with the user's `$HOME` as the Docker context. Compose displays a warning about the non-portable path used to build image.

On push, both `example/webapp` and `example/database` Docker images are pushed to the default registry. The `custom` service image is skipped as no `image` attribute is set and Compose displays a warning about this missing attribute.

