---
title: Configure Next.js lint scripts and ESLint
description: Install and configure linting for a custom Next.js project.
---

## Prerequisites

Use your custom project. The [sample project](https://github.com/kristiyan-velkov/docker-nextjs-sample) already includes ESLint. For the container test and lint procedure, see [Use a development image for Compose tests](/guides/compose-test-services.md).

## Configure lint

For lint, add a `lint` script (and optionally `lint:fix`). For example, with [ESLint](https://eslint.org/):

```json
"scripts": {
  "test": "vitest",
  "test:run": "vitest run",
  "lint": "eslint .",
  "lint:fix": "eslint . --fix"
}
```

The sample project uses `eslint` and `eslint-config-next` for Next.js. Install them in a custom project with:

```console
$ npm install --save-dev eslint eslint-config-next @eslint/eslintrc
```

Create an ESLint config file (e.g. `eslint.config.cjs`) in your project root with Next.js rules and global ignores:

```js
const { defineConfig, globalIgnores } = require("eslint/config");
const { FlatCompat } = require("@eslint/eslintrc");

const compat = new FlatCompat({ baseDirectory: __dirname });

module.exports = defineConfig([
  ...compat.extends(
    "eslint-config-next/core-web-vitals",
    "eslint-config-next/typescript"
  ),
  globalIgnores([
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
    "node_modules/**",
    "eslint.config.cjs",
  ]),
]);
```
