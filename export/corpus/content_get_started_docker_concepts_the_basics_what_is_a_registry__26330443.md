---
title: What is a registry?
weight: 30
keywords: concepts, build, images, container, docker desktop
aliases:
- /guides/walkthroughs/run-hub-images/
- /guides/walkthroughs/publish-your-image/
- /guides/docker-concepts/the-basics/what-is-a-registry/
---

{{< youtube-embed 2WDl10Wv5rs >}}

## Explanation

Now that you know what a container image is and how it works, you might wonder - where do you store these images? 

Well, you can store your container images on your computer system, but what if you want to share them with your friends or use them on another machine? That's where the image registry comes in.

An image registry is a centralized location for storing and sharing your container images. It can be either public or private. [Docker Hub](https://hub.docker.com) is a public registry that anyone can use and is the default registry. 

While Docker Hub is a popular option, there are many other available container registries available today, including [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/), [Azure Container Registry (ACR)](https://azure.microsoft.com/en-in/products/container-registry), and [Google Container Registry (GCR)](https://cloud.google.com/artifact-registry). You can even run your private registry on your local system or inside your organization. For example, Harbor, JFrog Artifactory, GitLab Container registry etc.

### Registry vs. repository

While you're working with registries, you might hear the terms _registry_ and _repository_ as if they're interchangeable. Even though they're related, they're not quite the same thing.

A _registry_ is a centralized location that stores and manages container images, whereas a _repository_ is a collection of related container images within a registry. Think of it as a folder where you organize your images based on projects. Each repository contains one or more container images.

The following diagram shows the relationship between a registry, repositories, and images.

```goat {class="text-sm"}
+---------------------------------------+
|               Registry                |
|---------------------------------------|
|                                       |
|    +-----------------------------+    |
|    |        Repository A         |    |
|    |-----------------------------|    |
|    |   Image: project-a:v1.0     |    |
|    |   Image: project-a:v2.0     |    |
|    +-----------------------------+    |
|                                       |
|    +-----------------------------+    |
|    |        Repository B         |    |
|    |-----------------------------|    |
|    |   Image: project-b:v1.0     |    |
|    |   Image: project-b:v1.1     |    |
|    |   Image: project-b:v2.0     |    |
|    +-----------------------------+    |
|                                       |
+---------------------------------------+
```

> [!TIP]
>
>A Docker Personal plan gives you one private repository and unlimited public repositories. To get unlimited private repositories, upgrade to the [Docker Team plan](https://www.docker.com/pricing?ref=Docs&refAction=DocsConceptsRegistry).

## Images and Docker Hub

### Container images

If you’re new to container images, think of them as a standardized package that contains everything needed to run an application, including its files, configuration, and dependencies. These packages can then be distributed and shared with others.

### Docker Hub

To share your Docker images, you need a place to store them. This is where registries come in. While there are many registries, Docker Hub is the default and go-to registry for images. Docker Hub provides both a place for you to store your own images and to find images from others to either run or use as the bases for your own images.

When choosing base images, Docker Hub offers two categories of trusted, Docker-maintained images:

- [Docker Official Images (DOI)](/manuals/docker-hub/image-library/trusted-content.md#docker-official-images) – Curated images for popular software, following best practices and regularly updated.
- [Docker Hardened Images (DHI)](/manuals/dhi/_index.md) – Minimal, secure, production-ready images with near-zero CVEs, designed to reduce attack surface and simplify compliance. DHI images are free and open source under Apache 2.0.

Explore the full catalog of trusted content on Docker Hub:

- [Docker Official Images](https://hub.docker.com/search?badges=official) – Curated images for popular software
- [Docker Hardened Images](https://hub.docker.com/hardened-images/catalog) – Security-hardened, minimal production images (also available at [dhi.io](https://dhi.io))
- [Docker Verified Publishers](https://hub.docker.com/search?badges=verified_publisher) – Images from verified software vendors
- [Docker Sponsored Open Source](https://hub.docker.com/search?badges=open_source) – Images from sponsored OSS projects

## Distribution and access

- Docker Hub is the go-to registry for finding trusted content. Docker provides a collection of trusted content, composed of Docker Official Images, Docker Verified Publishers, and Docker Sponsored Open Source Software, to use directly or as bases for your own images.

- Docker Hub provides a marketplace to distribute your own applications. Anyone can create an account and distribute images. While you are publicly distributing the image you created, private repositories can ensure your images are accessible to only authorized users.

> **Usage of other registries**
>
> While Docker Hub is the default registry, registries are standardized and made 
> interoperable through the [Open Container Initiative](https://opencontainers.org/). This allows companies and 
> organizations to run their own private registries. Quite often, trusted content 
> is mirrored (or copied) from Docker Hub into these private registries.
>

## Account and repository procedure

[Sign in and create a Docker Hub repository](/get-started/shared/docker-hub-access.md).

## Additional resources

- [Docker Hub Quickstart](/docker-hub/quickstart/)
- [Manage Docker Hub Repositories](/docker-hub/repos/)
