---
title: Debug the Node.js development container
description: Attach VS Code or Chrome DevTools and troubleshoot debugger connections.
---

## Prerequisites

[Configure and run the development container](develop.md). For shared container checks, see [Inspect local images and running containers](/guides/image-build-and-inspect.md).

## Debugger ports

You can connect a debugger to your application on port 9229. The Node.js inspector is enabled with `--inspect=0.0.0.0:9230` in the development script (`dev:server`).

## VS Code debugger setup

1. Create a launch configuration in `.vscode/launch.json`:

    ```json
    {
      "version": "0.2.0",
      "configurations": [
        {
          "name": "Attach to Docker Container",
          "type": "node",
          "request": "attach",
          "port": 9229,
          "address": "localhost",
          "localRoot": "${workspaceFolder}",
          "remoteRoot": "/app",
          "protocol": "inspector",
          "restart": true,
          "sourceMaps": true,
          "skipFiles": ["<node_internals>/**"]
        }
      ]
    }
    ```

1. Start your development container:

    ```console
    docker compose up app-dev --build
    ```

1. Attach the debugger:
   - Open VS Code
   - From the Debug panel (Ctrl/Cmd + Shift + D), select **Attach to Docker Container** from the drop-down
   - Select the green play button or press F5

## Chrome DevTools (alternative)

You can also use Chrome DevTools for debugging:

1. Start your container (if not already running):

    ```console
    docker compose up app-dev --build
    ```

1. Open Chrome and go to `chrome://inspect`.

1. From the **Configure** option, add:

    ```text
    localhost:9229
    ```

1. When your Node.js target appears, select **inspect**.

## Debugging configuration details

The debugger configuration:

- **Container port**: 9230 (internal debugger port)
- **Host port**: 9229 (mapped external port)
- **Script**: `tsx watch --inspect=0.0.0.0:9230 src/server/index.ts`

The debugger listens on all interfaces (`0.0.0.0`) inside the container on port 9230 and is accessible on port 9229 from your host machine.

## Troubleshooting debugger connection

If the debugger doesn't connect:

1. Check if the container is running:

    ```console
    docker ps
    ```

1. Check if the port is exposed:

    ```console
    docker port todoapp-dev
    ```

1. Check container logs:

    ```console
    docker compose logs app-dev
    ```

    You should see a message like:

    ```text
    Debugger listening on ws://0.0.0.0:9230/...
    ```

Now you can set breakpoints in your TypeScript source files and debug your containerized Node.js application.

For more details about Node.js debugging, see the [Node.js documentation](https://nodejs.org/en/docs/guides/debugging-getting-started).
