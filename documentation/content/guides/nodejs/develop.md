---
title: Use containers for Node.js development
linkTitle: Develop your app
weight: 30
keywords: node, node.js, development
description: Learn how to develop your Node.js application locally using containers.
aliases:
  - /get-started/nodejs/develop/
  - /language/nodejs/develop/
  - /guides/language/nodejs/develop/
---

## Prerequisites

Complete [sample setup](containerize.md), [image building](build-images.md), and [startup verification](run.md).

For shared file-update requirements and behavior, see [Use Compose Watch](/manuals/compose/how-tos/file-watch.md).

## Overview

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Adding a local database and persisting data
- Configuring your container to run a development environment
- Debugging your containerized application

## Add a local database and persist data

Follow [Add PostgreSQL and verify Todo data persistence](persist-data.md).

## Configure and run a development container

You can use a bind mount to mount your source code into the container. The container can then see the changes you make to the code immediately, as soon as you save a file. This means that you can run processes, like nodemon, in the container that watch for filesystem changes and respond to them. To learn more about bind mounts, see [Storage overview](/manuals/engine/storage/_index.md).

In addition to adding a bind mount, you can configure your Dockerfile and `compose.yaml` file to install development dependencies and run development tools.

### Update your Dockerfile for development

Your Dockerfile should be configured as a multi-stage build with separate stages for development, production, and testing. If you followed the previous section, your Dockerfile already includes a development stage that has all development dependencies and runs the application with hot reload enabled.

Here's the development stage from your multi-stage Dockerfile:

```dockerfile {hl_lines="5-26",collapse=true,title=Dockerfile}
# ========================================
# Development Stage
# ========================================
FROM build-deps AS development

# Set environment
ENV NODE_ENV=development \
    NPM_CONFIG_LOGLEVEL=warn

# Copy source files
COPY . .

# Ensure all directories have proper permissions
RUN mkdir -p /app/node_modules/.vite && \
    chown -R nodejs:nodejs /app && \
    chmod -R 755 /app

# Switch to non-root user
USER nodejs

# Expose ports
EXPOSE 3000 5173 9229

# Start development server
CMD ["npm", "run", "dev:docker"]
```

The development stage:

- Installs all dependencies including dev dependencies
- Exposes ports for the API server (3000), Vite dev server (5173), and Node.js debugger (9229)
- Runs `npm run dev` which starts both the Express server and Vite dev server concurrently
- Includes health checks for monitoring container status

Next, you'll need to update your Compose file to use the new stage.

### Update your Compose file for development

Update your `compose.yml` file to run the development stage with bind mounts for hot reloading:

```yaml {hl_lines=[5,8-10,20-27],collapse=true,title=compose.yml}
services:
  app-dev:
    build:
      context: .
      dockerfile: Dockerfile
      target: development
    container_name: todoapp-dev
    ports:
      - '${APP_PORT:-3000}:3000' # API server
      - '${VITE_PORT:-5173}:5173' # Vite dev server
      - '${DEBUG_PORT:-9229}:9229' # Node.js debugger
    environment:
      NODE_ENV: development
      DOCKER_ENV: 'true'
      POSTGRES_HOST: db
      POSTGRES_PORT: 5432
      POSTGRES_DB: todoapp
      POSTGRES_USER: todoapp
      POSTGRES_PASSWORD: '${POSTGRES_PASSWORD:-todoapp_password}'
      ALLOWED_ORIGINS: '${ALLOWED_ORIGINS:-http://localhost:3000,http://localhost:5173}'
    volumes:
      - ./src:/app/src:ro
      - ./package.json:/app/package.json
      - ./vite.config.ts:/app/vite.config.ts:ro
      - ./tailwind.config.js:/app/tailwind.config.js:ro
      - ./postcss.config.js:/app/postcss.config.js:ro
    depends_on:
      db:
        condition: service_healthy
    develop:
      watch:
        - action: sync
          path: ./src
          target: /app/src
          ignore:
            - '**/*.test.*'
            - '**/__tests__/**'
        - action: rebuild
          path: ./package.json
        - action: sync
          path: ./vite.config.ts
          target: /app/vite.config.ts
        - action: sync
          path: ./tailwind.config.js
          target: /app/tailwind.config.js
        - action: sync
          path: ./postcss.config.js
          target: /app/postcss.config.js
    restart: unless-stopped
    networks:
      - todoapp-network
```

Key features of the development configuration:

- **Multi-port exposure**: API server (3000), Vite dev server (5173), and debugger (9229)
- **Comprehensive bind mounts**: Source code, configuration files, and package files for hot reloading
- **Environment variables**: Configurable through `.env` file or defaults
- **PostgreSQL database**: Production-ready database with persistent storage
- **Docker Compose watch**: Automatic file synchronization and container rebuilds
- **Health checks**: Database health monitoring with automatic dependency management

### Run your development container and debug your application

Run the following command to run your application with the development configuration:

```console
$ docker compose up app-dev --build
```

Or with file watching for automatic updates:

```console
$ docker compose up app-dev --watch
```

For local development without Docker:

```console
$ npm run dev:with-db
```

Or start services separately:

```console
$ npm run db:start    # Start PostgreSQL container
$ npm run dev         # Start both server and client
```

The application will start with both the Express API server and Vite development server:

- **API Server**: [http://localhost:3000](http://localhost:3000) - Express.js backend with REST API
- **Frontend**: [http://localhost:5173](http://localhost:5173) - Vite dev server with hot module replacement
- **Health Check**: [http://localhost:3000/health](http://localhost:3000/health) - Application health status

Any changes to the application's source files on your local machine will now be immediately reflected in the running container thanks to the bind mounts.

Try making a change to test hot reloading:

1. Open `src/client/components/TodoApp.tsx` in an IDE or text editor.
1. Update the main heading text:

    ```diff
    - <h1 className="text-3xl font-bold text-gray-900 mb-8">
    -   Modern Todo App
    - </h1>
    + <h1 className="text-3xl font-bold text-gray-900 mb-8">
    +   My Todo App
    + </h1>
    ```

1. Save the file and the Vite dev server will automatically reload the page with your changes.

## Debug the application

Follow [Debug the Node.js development container](debug.md) for VS Code, Chrome DevTools, port settings, and connection troubleshooting.

## Task Runner alternative

See [Run Node.js sample tasks with Task Runner](tasks.md).

## Summary

You've set up your Compose file with a PostgreSQL database and data persistence. You also created a multi-stage Dockerfile and configured bind mounts for development.

Related information:

- [Volumes top-level element](/reference/compose-file/volumes/)
- [Services top-level element](/reference/compose-file/services/)
- [Multi-stage builds](/manuals/build/building/multi-stage.md)

## Next steps

In the next section, you'll learn how to run unit tests using Docker.

[Run tests](run-tests.md).
