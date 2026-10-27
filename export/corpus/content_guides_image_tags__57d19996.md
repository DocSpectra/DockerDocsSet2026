---
title: Image names and tags
description: Image name components, tags, and image identity.
---

## Image names

An image name is made up of slash-separated name components. Name components may
contain lowercase letters, digits, and separators. A separator is defined as a
period, one or two underscores, or one or more dashes. A name component may not
start or end with a separator.

## Tags and image identity

An image is made up of a manifest and a list of layers. In simple terms, a tag
points to a combination of these artifacts. You can have multiple tags for the
image and, in fact, most images have multiple tags.

The Docker `tag` command creates a new tag for the image. It doesn't create a
new image. The tag points to the same image and is just another way to reference
the image.

The `IMAGE ID` is a unique identifier Docker uses internally to identify the
image. Tags with the same image ID refer to the same image.
