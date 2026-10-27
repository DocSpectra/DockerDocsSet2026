---
title: Configure Next.js component tests
description: Install and configure Vitest and React Testing Library for a custom Next.js project.
---

## Prerequisites

Use your custom project. The [sample project](https://github.com/kristiyan-velkov/docker-nextjs-sample) already includes Vitest tests at `app/page.test.tsx`. For the container test procedure, see [Use a development image for Compose tests](/guides/compose-test-services.md).

## Install Vitest and React Testing Library

If you're using a custom project and haven't already added the necessary testing tools, install them by running:

```console
$ npm install --save-dev vitest @vitejs/plugin-react @testing-library/react @testing-library/dom jsdom
```

Then, update the scripts section of your `package.json` file to include:

```json
"scripts": {
  "test": "vitest",
  "test:run": "vitest run"
}
```

## Configure Vitest

If you're using a custom project, create a `vitest.config.ts` file in your project root (matching the [sample project](https://github.com/kristiyan-velkov/docker-nextjs-sample)):

```ts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    setupFiles: "./vitest.setup.ts",
    globals: true,
  },
});
```

Create a `vitest.setup.ts` file in your project root:

```ts
import "@testing-library/jest-dom/vitest";
```

> [!NOTE]
> Vitest works well with Next.js and provides fast execution and ESM support. For more details, see the [Next.js testing documentation](https://nextjs.org/docs/app/building-your-application/testing) and [Vitest docs](https://vitest.dev/).
