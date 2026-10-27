---
title: Container-supported development concepts
---

Containers offer a consistent way to build, share, and run applications across different environments. While containers are typically used to containerize your application, they also make it incredibly easy to run essential services needed for development. Instead of installing or connecting to a remote database, you can easily launch your own database. But the possibilities don't stop there.

With container-supported development, you use containers to enhance your development environment by emulating or running your own instances of the services your app needs. This provides faster feedback loops, less coupling with remote services, and a greater ability to test error states.

And best of all, you can have these benefits regardless of whether the main app under development is running in containers.

## Who's this for?

- Teams that want to reduce the coupling they have on shared or deployed infrastructure or remote API endpoints
- Teams that want to reduce the complexity and costs associated with using cloud services directly during development
- Developers that want to make it easier to visualize what's going on in their databases, queues, etc.
- Teams that want to reduce the complexity of setting up their development environment without impacting the development of the app itself


## Tools integration

Works well with Docker Compose and Testcontainers.

## What is container-supported development?

Container-supported development is the idea of using containers to enhance your development environment by running local instances or emulators of the services your application relies on. Once you're using containers, it's easy to add additional services to visualize or troubleshoot what's going on in your services.

{{< youtube-embed pNcrto_wGi0 >}}
