---
title: Configure Next.js standalone output
linkTitle: Standalone output
weight: 11
description: Configure Next.js standalone output using the Dockerfiles from the Next.js containerization guide.
---

[Next.js guide](_index.md) / [Containerize](containerize.md)

On this page:

- [Prerequisites](#prerequisites)
- [Configure standalone output](#21-nextjs-with-standalone-output)
- [Configure next.config.ts](#configure-nextconfigts)
- [Choose a Dockerfile](#choose-a-dockerfile)
- [Return to shared build and run steps](#next-steps)

## Prerequisites

Start with the [containerization prerequisites](containerize.md#prerequisites), [sample application](containerize.md#get-the-sample-application), and [generated Dockerfile](containerize.md#generate-a-dockerfile). Review [base image selection](containerize.md#step-2-configure-nextjs-output-and-dockerfile).

> [!IMPORTANT]
> This guide uses stable Node.js LTS image tags that are considered secure when the guide is written. Because new releases and security patches are published regularly, always review the [official Node.js Docker images](https://hub.docker.com/_/node) and select a secure, up-to-date version before building or deploying.

## 2.1 Next.js with standalone output

**Standalone output** (`output: "standalone"`) makes Next.js build a self-contained output that includes only the files and dependencies needed to run the application. A single `node server.js` can serve the app, which is ideal for Docker and supports server-side rendering, API routes, and incremental static regeneration. For details, see the [Next.js output configuration documentation](https://nextjs.org/docs/app/api-reference/config/next-config-js/output) (including the "standalone" option).

The container runs the Next.js server with Node.js on **port 3000**.

### Configure next.config.ts

**Configure Next.js** — Open or create `next.config.ts` in your project root:

```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
};

export default nextConfig;
```

### Choose a Dockerfile

Choose either a Docker Hardened Image or the Docker Official Image, then create or replace your `Dockerfile` with the content from the selected tab below.

{{< tabs >}}
{{< tab name="Using Docker Hardened Images" >}}

Docker Hardened Images (DHIs) are available for Node.js in the [Docker Hardened Images catalog](https://hub.docker.com/hardened-images/catalog/dhi/node). For more information, see the [DHI quickstart](/dhi/get-started/) guide.

1. Sign in to the DHI registry:
   ```console
   $ docker login dhi.io
   ```

2. Pull the Node.js DHI (check the catalog for available versions):
   ```console
   $ docker pull dhi.io/node:24-alpine3.22-dev
   ```

3. Replace the generated Dockerfile with the following. The `FROM` instructions use `dhi.io/node:24-alpine3.22-dev`. Check the [Docker Hardened Images catalog](https://hub.docker.com/hardened-images/catalog) for the latest versions and update the image tags as needed for security and compatibility.

    ```dockerfile
    # ============================================
    # Stage 1: Dependencies Installation Stage
    # ============================================

    # IMPORTANT: Docker Hardened Image (DHI) Version Maintenance
    # This Dockerfile uses dhi.io/node. Regularly validate and update to the latest DHI versions in the catalog for security and compatibility.

    FROM dhi.io/node:24-alpine3.22-dev AS dependencies

    # Set working directory
    WORKDIR /app

    # Copy package-related files first to leverage Docker's caching mechanism
    COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* .npmrc* ./

    # Install project dependencies with frozen lockfile for reproducible builds
    RUN --mount=type=cache,target=/root/.npm \
        --mount=type=cache,target=/usr/local/share/.cache/yarn \
        --mount=type=cache,target=/root/.local/share/pnpm/store \
      if [ -f package-lock.json ]; then \
        npm ci --no-audit --no-fund; \
      elif [ -f yarn.lock ]; then \
        corepack enable yarn && yarn install --frozen-lockfile --production=false; \
      elif [ -f pnpm-lock.yaml ]; then \
        corepack enable pnpm && pnpm install --frozen-lockfile; \
      else \
        echo "No lockfile found." && exit 1; \
      fi

    # ============================================
    # Stage 2: Build Next.js application in standalone mode
    # ============================================

    FROM dhi.io/node:24-alpine3.22-dev AS builder

    # Set working directory
    WORKDIR /app

    # Copy project dependencies from dependencies stage
    COPY --from=dependencies /app/node_modules ./node_modules

    # Copy application source code
    COPY . .

    ENV NODE_ENV=production

    # Next.js collects completely anonymous telemetry data about general usage.
    # Learn more here: https://nextjs.org/telemetry
    # Uncomment the following line in case you want to disable telemetry during the build.
    # ENV NEXT_TELEMETRY_DISABLED=1

    # Build Next.js application
    # If you want to speed up Docker rebuilds, you can cache the build artifacts
    # by adding: --mount=type=cache,target=/app/.next/cache
    # This caches the .next/cache directory across builds, but it also prevents
    # .next/cache/fetch-cache from being included in the final image, meaning
    # cached fetch responses from the build won't be available at runtime.
    RUN if [ -f package-lock.json ]; then \
        npm run build; \
      elif [ -f yarn.lock ]; then \
        corepack enable yarn && yarn build; \
      elif [ -f pnpm-lock.yaml ]; then \
        corepack enable pnpm && pnpm build; \
      else \
        echo "No lockfile found." && exit 1; \
      fi

    # ============================================
    # Stage 3: Run Next.js application
    # ============================================

    FROM dhi.io/node:24-alpine3.22-dev AS runner

    # Set working directory
    WORKDIR /app

    # Set production environment variables
    ENV NODE_ENV=production
    ENV PORT=3000
    ENV HOSTNAME="0.0.0.0"

    # Next.js collects completely anonymous telemetry data about general usage.
    # Learn more here: https://nextjs.org/telemetry
    # Uncomment the following line in case you want to disable telemetry during the run time.
    # ENV NEXT_TELEMETRY_DISABLED=1

    # Copy production assets
    COPY --from=builder --chown=node:node /app/public ./public

    # Set the correct permission for prerender cache
    RUN mkdir .next
    RUN chown node:node .next

    # Automatically leverage output traces to reduce image size
    # https://nextjs.org/docs/advanced-features/output-file-tracing
    COPY --from=builder --chown=node:node /app/.next/standalone ./
    COPY --from=builder --chown=node:node /app/.next/static ./.next/static

    # If you want to persist the fetch cache generated during the build so that
    # cached responses are available immediately on startup, uncomment this line:
    # COPY --from=builder --chown=node:node /app/.next/cache ./.next/cache

    # Switch to non-root user for security best practices
    USER node

    # Expose port 3000 to allow HTTP traffic
    EXPOSE 3000

    # Start Next.js standalone server
    CMD ["node", "server.js"]
    ```

{{< /tab >}}
{{< tab name="Using the Docker Official Image" >}}

Create a production-ready multi-stage Dockerfile. Replace the generated Dockerfile with the following (uses `node`):

```dockerfile
  # ============================================
  # Stage 1: Dependencies Installation Stage
  # ============================================

  ARG NODE_VERSION=24.14.0-slim

  FROM node:${NODE_VERSION} AS dependencies

  # Set working directory
  WORKDIR /app

  # Copy package-related files first to leverage Docker's caching mechanism
  COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* .npmrc* ./

  # Install project dependencies with frozen lockfile for reproducible builds
  RUN --mount=type=cache,target=/root/.npm \
      --mount=type=cache,target=/usr/local/share/.cache/yarn \
      --mount=type=cache,target=/root/.local/share/pnpm/store \
    if [ -f package-lock.json ]; then \
      npm ci --no-audit --no-fund; \
    elif [ -f yarn.lock ]; then \
      corepack enable yarn && yarn install --frozen-lockfile --production=false; \
    elif [ -f pnpm-lock.yaml ]; then \
      corepack enable pnpm && pnpm install --frozen-lockfile; \
    else \
      echo "No lockfile found." && exit 1; \
    fi

  # ============================================
  # Stage 2: Build Next.js application in standalone mode
  # ============================================

  FROM node:${NODE_VERSION} AS builder

  # Set working directory
  WORKDIR /app

  # Copy project dependencies from dependencies stage
  COPY --from=dependencies /app/node_modules ./node_modules

  # Copy application source code
  COPY . .

  ENV NODE_ENV=production

  # Next.js collects completely anonymous telemetry data about general usage.
  # Learn more here: https://nextjs.org/telemetry
  # Uncomment the following line in case you want to disable telemetry during the build.
  # ENV NEXT_TELEMETRY_DISABLED=1

  # Build Next.js application
  # If you want to speed up Docker rebuilds, you can cache the build artifacts
  # by adding: --mount=type=cache,target=/app/.next/cache
  # This caches the .next/cache directory across builds, but it also prevents
  # .next/cache/fetch-cache from being included in the final image, meaning
  # cached fetch responses from the build won't be available at runtime.
  RUN if [ -f package-lock.json ]; then \
      npm run build; \
    elif [ -f yarn.lock ]; then \
      corepack enable yarn && yarn build; \
    elif [ -f pnpm-lock.yaml ]; then \
      corepack enable pnpm && pnpm build; \
    else \
      echo "No lockfile found." && exit 1; \
    fi

  # ============================================
  # Stage 3: Run Next.js application
  # ============================================

  FROM node:${NODE_VERSION} AS runner

  # Set working directory
  WORKDIR /app

  # Set production environment variables
  ENV NODE_ENV=production
  ENV PORT=3000
  ENV HOSTNAME="0.0.0.0"

  # Next.js collects completely anonymous telemetry data about general usage.
  # Learn more here: https://nextjs.org/telemetry
  # Uncomment the following line in case you want to disable telemetry during the run time.
  # ENV NEXT_TELEMETRY_DISABLED=1

  # Copy production assets
  COPY --from=builder --chown=node:node /app/public ./public

  # Set the correct permission for prerender cache
  RUN mkdir .next
  RUN chown node:node .next

  # Automatically leverage output traces to reduce image size
  # https://nextjs.org/docs/advanced-features/output-file-tracing
  COPY --from=builder --chown=node:node /app/.next/standalone ./
  COPY --from=builder --chown=node:node /app/.next/static ./.next/static

  # If you want to persist the fetch cache generated during the build so that
  # cached responses are available immediately on startup, uncomment this line:
  # COPY --from=builder --chown=node:node /app/.next/cache ./.next/cache

  # Switch to non-root user for security best practices
  USER node

  # Expose port 3000 to allow HTTP traffic
  EXPOSE 3000

  # Start Next.js standalone server
  CMD ["node", "server.js"]
```

> [!NOTE]
> This Dockerfile uses three stages: **dependencies**, **builder**, and **runner**. The final image runs `node server.js` and listens on port 3000.

{{< /tab >}}
{{< /tabs >}}

## Next steps

Return to the containerization guide to [configure .dockerignore](containerize.md#step-3-configure-the-dockerignore-file), [build the image](containerize.md#step-4-build-the-nextjs-application-image), and [run the application](containerize.md#run-the-containerized-application).
