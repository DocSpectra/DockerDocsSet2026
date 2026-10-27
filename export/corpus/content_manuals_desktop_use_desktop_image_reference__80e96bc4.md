---
title: Docker Desktop image views and metadata
---

The **Images** view displays a list of your Docker images and allows you to run an image as a container, pull the latest version of an image from Docker Hub, and inspect images. It also displays a summary of image vulnerabilities. In addition, the **Images** view contains clean-up options to remove unwanted images from the disk to reclaim space. If you are logged in, you can also see the images you and your organization have shared on Docker Hub.

The **Images** view lets you manage Docker images without having to use the CLI. By default, it displays a list of all Docker images on your local disk. 

You can also view Hub images once you have signed in to Docker Hub. This allows you to collaborate with your team and manage your images directly through Docker Desktop.

The **Images** view lets you perform core operations such as running an image as a container, pulling the latest version of an image from Docker Hub, pushing the image to Docker Hub, and inspecting images.

It also displays metadata about the image such as the:
- Tag
- Image ID
- Date created
- Size of the image.

An **In Use** tag displays next to images used by running and stopped containers. You can choose what information you want displayed by selecting the **More options** menu to the right of the search bar, and then use the toggle switches according to your preferences. 

The **Images on disk** status bar displays the number of images and the total disk space used by the images and when this information was last refreshed.


## Unused and dangling images

An unused image is an image which is not used by any running or stopped containers. An image becomes dangling when you build a new version of the image with the same tag.
