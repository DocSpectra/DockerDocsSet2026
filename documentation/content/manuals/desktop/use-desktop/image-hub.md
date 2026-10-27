---
title: Pull, push, and browse Docker Hub images in Docker Desktop
---

For image metadata and status definitions, see [Docker Desktop image views and metadata](image-reference.md).

## Pull the latest image from Docker Hub

Select the image from the list, select the **More options** button and select **Pull**.

> [!NOTE]
>
> The repository must exist on Docker Hub in order to pull the latest version of an image. You must be signed in to pull private images.

## Push an image to Docker Hub

Select the image from the list, select the **More options** button and select **Push to Hub**.

> [!NOTE]
>
> You can only push an image to Docker Hub if the image belongs to your Docker ID or your organization. That is, the image must contain the correct username/organization in its tag to be able to push it to Docker Hub.

## Docker Hub repositories

The **Images** view also allows you to manage and interact with images in Docker Hub repositories.
By default, when you go to **Images** in Docker Desktop, you see a list of images that exist in your local image store.
The **Local** and **Docker Hub repositories** tabs near the top toggles between viewing images in your local image store,
and images in remote Docker Hub repositories that you have access to.

Switching to the **Docker Hub repositories** tab prompts you to sign in to your Docker Hub account, if you're not already signed in.
When signed in, it shows you a list of images in Docker Hub organizations and repositories that you have access to.

Select an organization from the drop-down to view a list of repositories for that organization.

If you have enabled [Docker Scout](../../scout/_index.md) on the repositories,
image analysis results (and [health scores](/manuals/scout/policy/scores.md) if
your Docker organization is eligible) appear next to the image tags.

Hovering over an image tag reveals two options:

- **Pull**: Pull the latest version of the image from Docker Hub.
- **View in Hub**: Open the Docker Hub page and display detailed information about the image.
