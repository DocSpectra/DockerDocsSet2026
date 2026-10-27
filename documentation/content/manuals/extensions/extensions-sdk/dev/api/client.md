---
title: Set up the extension UI API client
description: Install and initialize the extension API client and TypeScript definitions.
---

The extensions UI runs in a sandboxed environment and doesn't have access to any
electron or nodejs APIs.

The extension UI API provides a way for the frontend to perform different actions
and communicate with the Docker Desktop dashboard or the underlying system.

JavaScript API libraries, with Typescript support, are available in order to get all the API definitions in to your extension code.

- [@docker/extension-api-client](https://www.npmjs.com/package/@docker/extension-api-client) gives access to the extension API entrypoint `DockerDesktopClient`.
- [@docker/extension-api-client-types](https://www.npmjs.com/package/@docker/extension-api-client-types) can be added as a dev dependency in order to get types auto-completion in your IDE.

## Set up the API client

To use the Extension APIs and perform actions with Docker Desktop, the extension must first import the
`@docker/extension-api-client` library. To install it, run the command below:

```bash
npm install @docker/extension-api-client
```

Then call the `createDockerDesktopClient` function to create a client object to call the extension APIs.

```js
import { createDockerDesktopClient } from '@docker/extension-api-client';

const ddClient = createDockerDesktopClient();
```

When using Typescript, you can also install `@docker/extension-api-client-types` as a dev dependency. This will
provide you with type definitions for the extension APIs and auto-completion in your IDE.

```bash
npm install @docker/extension-api-client-types --save-dev
```

![Auto completion in an IDE](../../build/images/types-autocomplete.png)

```Typescript
import { createDockerDesktopClient } from '@docker/extension-api-client';

export function App() {
  // obtain Docker Desktop client
  const ddClient = createDockerDesktopClient();
  // use ddClient to perform extension actions
}
```

For UI isolation and storage, see [Extension security](../../architecture/security.md#policies-enforced-for-the-front-end-code).

See also the [DockerDesktopClient reference](/reference/api/extensions-sdk/DockerDesktopClient.md).
