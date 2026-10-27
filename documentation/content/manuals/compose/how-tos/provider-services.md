---
title: Use provider services
description: Learn how to use provider services in Docker Compose to integrate external capabilities into your applications
keywords: compose, docker compose, provider, services, platform capabilities, integration, model runner, ai
weight: 112
---

{{< summary-bar feature_name="Compose provider services" >}}

See [Provider service behavior](../intro/provider-services.md) for platform capabilities, provisioning, provider types, and injected environment variables.

## What are provider services?

See [Provider services](../intro/provider-services.md#what-are-provider-services).

## Using provider services

To use a provider service in your Compose file, you need to:

1. Define a service with the `provider` attribute
2. Specify the `type` of provider you want to use
3. Configure any provider-specific options
4. Declare dependencies from your application services to the provider service

Here's a basic example:

```yaml
services:
  database:
    provider:
      type: awesomecloud
      options:
        type: mysql
        foo: bar  
  app:
    image: myapp 
    depends_on:
       - database
```

Notice the dedicated `provider` attribute in the `database` service.
This attribute specifies that the service is managed by a provider and lets you define options specific to that provider type.

The `depends_on` attribute in the `app` service specifies that it depends on the `database` service.
This means that the `database` service will be started before the `app` service, allowing the provider information
to be injected into the `app` service.

## How it works

See [Provisioning and environment variables](../intro/provider-services.md#how-it-works).

## Provider types

See [Provider type resolution](../intro/provider-services.md#provider-types).

## Benefits of using provider services

See [Provider service benefits](../intro/provider-services.md#benefits-of-using-provider-services).

## Creating your own provider

If you want to create your own provider to extend Compose with custom capabilities, you can implement a Compose plugin that registers provider types.

For detailed information on how to create and implement your own provider, refer to the [Compose Extensions documentation](https://github.com/docker/compose/blob/main/docs/extension.md).   
This guide explains the extension mechanism that allows you to add new provider types to Compose.

## Reference

- [Docker Model Runner documentation](/manuals/ai/model-runner/_index.md)
- [Compose Extensions documentation](https://github.com/docker/compose/blob/main/docs/extension.md)