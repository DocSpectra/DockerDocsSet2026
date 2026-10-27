---
title: Containerize Next.js static export
description: Configure Next.js export output, its Dockerfile, and NGINX.
---

## Prerequisites

Complete [sample setup and Docker Init](containerize.md). Review [Node.js image choices and version caveats](/guides/node-image-context.md#choose-a-base-image).

## Configure export output

**Output export** (`output: "export"`) makes Next.js build a fully static site at build time. It generates HTML, CSS, and JavaScript into an `out` directory that can be served by any static host or CDN—no Node.js server at runtime. Use this when you don't need server-side rendering or API routes. For details, see the [Next.js output configuration documentation](https://nextjs.org/docs/app/api-reference/config/next-config-js/output).

**Configure Next.js** — Open  `next.config.ts` in your project root and add the following code:

```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
```

Choose either a Docker Hardened Image or the Docker Official Image, then replace your `Dockerfile` with the content from the selected tab below.

{{< tabs >}}
{{< tab name="Using Docker Hardened Images" >}}

Docker Hardened Images (DHIs) are available for Node.js and NGINX in the [Docker Hardened Images catalog](https://hub.docker.com/hardened-images/catalog). For more information, see the [DHI quickstart](/dhi/get-started/) guide.

1. Sign in to the DHI registry:
   ```console
   $ docker login dhi.io
   ```

2. Pull the Node.js DHI (check the catalog for available versions):
   ```console
   $ docker pull dhi.io/node:24-alpine3.22-dev
   ```

3. Pull the Nginx DHI (check the catalog for available versions):
   ```console
   $ docker pull dhi.io/nginx:1.28.0-alpine3.21-dev
   ```

4. Replace the generated Dockerfile with the following. The `FROM` instructions use Docker Hardened Images: `dhi.io/node:24-alpine3.22-dev` and `dhi.io/nginx:1.28.0-alpine3.21-dev`. Check the [Docker Hardened Images catalog](https://hub.docker.com/hardened-images/catalog) for the latest versions and update the image tags as needed for security and compatibility.

    ```dockerfile
    # ============================================
    # Stage 1: Dependencies Installation Stage
    # ============================================

    # IMPORTANT: Docker Hardened Image (DHI) Version Maintenance
    # This Dockerfile uses dhi.io/node and dhi.io/nginx. Regularly validate and update to the latest DHI versions in the catalog for security and compatibility.

    FROM dhi.io/node:24-alpine3.22-dev AS dependencies

    # Set the working directory
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
    # Stage 2: Build Next.js Application
    # ============================================

    FROM dhi.io/node:24-alpine3.22-dev AS builder

    # Set the working directory
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
    RUN --mount=type=cache,target=/app/.next/cache \
      if [ -f package-lock.json ]; then \
        npm run build; \
      elif [ -f yarn.lock ]; then \
        corepack enable yarn && yarn build; \
      elif [ -f pnpm-lock.yaml ]; then \
        corepack enable pnpm && pnpm build; \
      else \
        echo "No lockfile found." && exit 1; \
      fi

    # =========================================
    # Stage 3: Serve Static Files with Nginx
    # =========================================

    FROM dhi.io/nginx:1.28.0-alpine3.21-dev AS runner

    # Set the working directory
    WORKDIR /app

    # Next.js collects completely anonymous telemetry data about general usage.
    # Learn more here: https://nextjs.org/telemetry
    # Uncomment the following line in case you want to disable telemetry during the run time.
    # ENV NEXT_TELEMETRY_DISABLED=1

    # Copy custom Nginx config
    COPY nginx.conf /etc/nginx/nginx.conf

    # Copy the static build output from the build stage to Nginx's default HTML serving directory
    COPY --chown=nginx:nginx --from=builder /app/out /usr/share/nginx/html

    # Non-root user for security best practices
    USER nginx

    # Expose port 8080 to allow HTTP traffic
    EXPOSE 8080

    # Start Nginx directly with custom config
    ENTRYPOINT ["nginx", "-c", "/etc/nginx/nginx.conf"]
    CMD ["-g", "daemon off;"]
    ```

{{< /tab >}}
{{< tab name="Using the Docker Official Image" >}}

Create a production-ready multi-stage Dockerfile. Replace the generated Dockerfile with the following (uses `node` and `nginxinc/nginx-unprivileged`):

```dockerfile
# ============================================
# Stage 1: Dependencies Installation Stage
# ============================================

ARG NODE_VERSION=24.14.0-slim
ARG NGINXINC_IMAGE_TAG=alpine3.22

FROM node:${NODE_VERSION} AS dependencies

# Set the working directory
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
# Stage 2: Build Next.js Application
# ============================================

FROM node:${NODE_VERSION} AS builder

# Set the working directory
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
RUN --mount=type=cache,target=/app/.next/cache \
  if [ -f package-lock.json ]; then \
    npm run build; \
  elif [ -f yarn.lock ]; then \
    corepack enable yarn && yarn build; \
  elif [ -f pnpm-lock.yaml ]; then \
    corepack enable pnpm && pnpm build; \
  else \
    echo "No lockfile found." && exit 1; \
  fi

# =========================================
# Stage 3: Serve Static Files with Nginx
# =========================================

FROM nginxinc/nginx-unprivileged:${NGINXINC_IMAGE_TAG} AS runner

# Set the working directory
WORKDIR /app

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry during the run time.
# ENV NEXT_TELEMETRY_DISABLED=1

# Copy custom Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the static build output from the build stage to Nginx's default HTML serving directory
COPY --from=builder /app/out /usr/share/nginx/html

# Non-root user for security best practices
USER nginx

# Expose port 8080 to allow HTTP traffic
EXPOSE 8080

# Start Nginx directly with custom config
ENTRYPOINT ["nginx", "-c", "/etc/nginx/nginx.conf"]
CMD ["-g", "daemon off;"]
```

> [!NOTE]
> We use [nginx-unprivileged](https://hub.docker.com/r/nginxinc/nginx-unprivileged) instead of the standard NGINX image to run as a non-root user, following security best practices.

{{< /tab >}}
{{< /tabs >}}

1. **Create `nginx.conf`** (required for export output only) — Create a file named `nginx.conf` in the root of your project:

    ```nginx
    # Minimal Nginx config for static Next.js app
    worker_processes 1;

    # Store PID in /tmp (always writable)
    pid /tmp/nginx.pid;

    events {
        worker_connections 1024;
    }

    http {
        include       /etc/nginx/mime.types;
        default_type  application/octet-stream;

        # Disable logging to avoid permission issues
        access_log off;
        error_log  /dev/stderr;

        # Optimize static file serving
        sendfile        on;
        tcp_nopush      on;
        tcp_nodelay     on;
        keepalive_timeout  65;

        # Gzip compression
        gzip on;
        gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
        gzip_min_length 256;

        server {
            listen       8080;
            server_name  localhost;

            # Serve static files
            root /usr/share/nginx/html;
            index index.html;

            # Handle Next.js static export routing
            # See: https://nextjs.org/docs/app/guides/static-exports#deploying
            location / {
                try_files $uri $uri.html $uri/ =404;
            }

            # This is necessary when `trailingSlash: false` (default).
            # You can omit this when `trailingSlash: true` in next.config.
            # Handles nested routes like /blog/post -> /blog/post.html
            location ~ ^/(.+)/$ {
                rewrite ^/(.+)/$ /$1.html break;
            }

            # Serve Next.js static assets
            location ~ ^/_next/ {
                try_files $uri =404;
                expires 1y;
                add_header Cache-Control "public, immutable";
            }

            # Optional 404 handling
            error_page 404 /404.html;
            location = /404.html {
                internal;
            }
        }
    }
    ```

      > [!NOTE]
      > Export uses **port 8080**. For more details, see the [Next.js output configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/output) and [NGINX documentation](https://nginx.org/en/docs/).


## Build and run

Apply the [.dockerignore and image build steps](build-images.md), then [run the application](run.md).

## Related resources

- [Next.js output configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/output) – Learn about Next.js production optimization (standalone and export).
- [Next.js with Docker (export)](https://github.com/vercel/next.js/tree/canary/examples/with-docker-export-output) – Official Next.js example: static export with Nginx or serve.
