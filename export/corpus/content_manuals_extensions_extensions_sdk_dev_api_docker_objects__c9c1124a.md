---
title: List Docker containers and images
description: List Docker objects from an extension.
---

## Docker objects

### List containers

▸ **listContainers**(`options?`): `Promise`<`unknown`\>

To get the list of containers:

```typescript
const containers = await ddClient.docker.listContainers();
```

### List images

▸ **listImages**(`options?`): `Promise`<`unknown`\>

To get the list of local container images:

```typescript
const images = await ddClient.docker.listImages();
```

See the [Docker API reference](/reference/api/extensions-sdk/Docker.md) for details about these methods.

## Deprecated access to Docker objects

> Deprecated access to Docker objects
>
> The methods below are deprecated and will be removed in a future version. Use the methods specified above.

```typescript
const containers = await window.ddClient.listContainers();

const images = await window.ddClient.listImages();
```

