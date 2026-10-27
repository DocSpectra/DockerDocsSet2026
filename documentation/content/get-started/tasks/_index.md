---
title: Hands-on Docker tasks
weight: 50
---

Choose a task, or follow the [Introduction](/get-started/introduction/_index.md) or [Docker workshop](/get-started/workshop/_index.md).

| Task | Shared explanation |
| --- | --- |
| [Run and explore the welcome container](run-welcome-container.md) | [What is a container?](/get-started/docker-concepts/the-basics/what-is-a-container.md) |
| [Find, pull, and inspect an image](find-and-inspect-images.md) | [What is an image?](/get-started/docker-concepts/the-basics/what-is-an-image.md) |
| [Publish the Node.js quickstart image](publish-quickstart-image.md) | [What is a registry?](/get-started/docker-concepts/the-basics/what-is-a-registry.md) |
| [Run and remove the Node.js and MySQL to-do stack](run-todo-with-compose.md) | [What is Docker Compose?](/get-started/docker-concepts/the-basics/what-is-docker-compose.md) |
| [Create image layers with container commit](create-image-layers.md) | [Image layers](/get-started/docker-concepts/building-images/understanding-image-layers.md) |
| [Write a Dockerfile for the Node.js to-do app](write-node-dockerfile.md) | [Dockerfile instructions](/get-started/docker-concepts/building-images/writing-a-dockerfile.md) |
| [Build and push the concepts to-do image](build-and-push-todo-image.md) | [Build, tag, and publish](/get-started/docker-concepts/building-images/build-tag-and-publish-an-image.md) |
| [Cache dependencies in the Node.js to-do image](cache-node-builds.md) | [Build cache](/get-started/docker-concepts/building-images/using-the-build-cache.md) |
| [Build the Spring Boot application in stages](build-java-in-stages.md) | [Multi-stage builds](/get-started/docker-concepts/building-images/multi-stage-builds.md) |
| [Publish the welcome application with CLI or Compose](publish-welcome-ports.md) | [Port publishing](/get-started/docker-concepts/running-containers/publishing-ports.md) |
| [Configure Postgres containers](configure-postgres-containers.md) | [Container defaults](/get-started/docker-concepts/running-containers/overriding-container-defaults.md) |
| [Persist and inspect Postgres data with a volume](persist-postgres-data.md) | [Data persistence](/get-started/docker-concepts/running-containers/persisting-container-data.md) |
| [Share website files with an httpd container](share-site-files.md) | [File sharing](/get-started/docker-concepts/running-containers/sharing-local-files.md) |
| [Run the Nginx, Node.js, and Redis counter stack](run-node-redis-stack.md) | [Multi-container applications](/get-started/docker-concepts/running-containers/multi-container-applications.md) |
| [Run an interactive Ubuntu container](run-interactive-ubuntu.md) | [Docker architecture](/get-started/docker-overview.md#docker-architecture) |

## Container-supported development

- [Run a local database for a non-containerized application](run-local-databases.md)
- [Mock API endpoints with WireMock](mock-api-endpoints.md)
- [Develop cloud applications locally with LocalStack](develop-cloud-locally.md)
- [Add debugging and troubleshooting containers](add-development-tools.md)

[Container-supported development concepts](/get-started/docker-concepts/container-supported-development.md).

## Labs

- [Getting started with Docker](/guides/lab-container-getting-started.md)
- [Container-supported development](/guides/lab-container-supported-development.md)
- [The containerized SDLC](/guides/lab-containerized-sdlc.md)

## More image-building examples

- [Build a Maven application for Tomcat](build-maven-tomcat-image.md)
- [Build a static React image with Nginx](build-static-react-image.md)
