---
title: Contribute an image definition to the DHI catalog
description: Task-specific definition steps and examples.
---

See the [catalog layout and image definitions](../core-concepts/definitions.md).

## Contribute to the catalog

Docker Hardened Images is an open source project. You can contribute new image
definitions or improve existing ones by submitting a pull request to the
[catalog repository](https://github.com/docker-hardened-images/catalog).

To contribute a new image:

1. Fork the catalog repository.
2. Create a directory under `image/` following the naming convention:
   `image/<image-name>/<distribution>/`.
3. Add your YAML definition files (one per variant).
4. Add an `info.yaml` with display name, description, and categories.
5. Add an `overview.md` describing the image.
6. Add a `logo.svg` for the image icon.
7. Add a `guides.md` with usage documentation.
8. Open a pull request against the `main` branch.

For more details, read the
[contributing guide](https://github.com/docker-hardened-images/catalog/blob/main/CONTRIBUTING.md)
in the catalog repository.
