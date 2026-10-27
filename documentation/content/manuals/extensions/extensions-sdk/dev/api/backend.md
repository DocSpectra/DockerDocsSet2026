---
title: Extension service and command execution
description: Docker extension API
keywords: Docker, extensions, sdk, API
aliases: 
 - /desktop/extensions-sdk/dev/api/backend/
---

The `ddClient.extension.vm` object can be used to communicate with the backend defined in the [vm section](../../architecture/metadata.md#vm-section) of the extension metadata.

## Call the backend service

### get

▸ **get**(`url`): `Promise`<`unknown`\>

Performs an HTTP GET request to a backend service.

```typescript
ddClient.extension.vm.service
 .get("/some/service")
 .then((value: any) => console.log(value)
```

See [Service API Reference](/reference/api/extensions-sdk/HttpService.md) for other methods such as POST, UPDATE, and DELETE.

## Choose a command context

- `ddClient.docker.cli.exec` directly executes the `docker` command line.
- `ddClient.extension.vm.cli.exec` executes a command in the extension backend container.
- `ddClient.extension.host.cli.exec` invokes a binary on the host.

## Run a command in the extension backend container

For example, execute the command `ls -l` inside the backend container:

```typescript
await ddClient.extension.vm.cli.exec("ls", ["-l"]);
```

Stream the output of the command executed in the backend container. For example, spawn the command `ls -l` inside the backend container:

```typescript
await ddClient.extension.vm.cli.exec("ls", ["-l"], {
  stream: {
    onOutput(data) {
      if (data.stdout) {
        console.error(data.stdout);
      } else {
        console.log(data.stderr);
      }
    },
    onError(error) {
      console.error(error);
    },
    onClose(exitCode) {
      console.log("onClose with exit code " + exitCode);
    },
  },
});
```

When the extension defines its own `compose.yaml` file with multiple containers, the command is executed on the first container defined. Change the order in which containers are defined to execute commands on another container.

## Invoke an extension binary on the host

Invoke a binary on the host. The binary is typically shipped with your extension using the [host section](../../architecture/metadata.md#host-section) in the extension metadata. Note that extensions run with user access rights, this API is not restricted to binaries listed in the [host section](../../architecture/metadata.md#host-section) of the extension metadata (some extensions might install software during user interaction, and invoke newly installed binaries even if not listed in the extension metadata).

For example, execute the shipped binary `kubectl -h` command in the host:

```typescript
await ddClient.extension.host.cli.exec("kubectl", ["-h"]);
```

As long as the `kubectl` binary is shipped as part of your extension, you can spawn the `kubectl -h` command in the host and get the output stream:

```typescript
await ddClient.extension.host.cli.exec("kubectl", ["-h"], {
  stream: {
    onOutput(data: { stdout: string } | { stderr: string }): void {
      if (data.stdout) {
        console.error(data.stdout);
      } else {
        console.log(data.stderr);
      }
    },
    onError(error: any): void {
      console.error(error);
    },
    onClose(exitCode: number): void {
      console.log("onClose with exit code " + exitCode);
    },
  },
});
```

You can stream the output of the command executed in the backend container or in the host.



## Collect command results

A promise will resolve once the command finishes.

The result contains both the standard output and the standard error of the executed command:

```json
{
  "stderr": "...",
  "stdout": "..."
}
```

For convenience, the command result object also has methods to easily parse JSON command output:

- `result.lines(): string[]` splits output lines.
- `result.parseJsonObject(): any` parses a well-formed json output.
- `result.parseJsonLines(): any[]` parses each output line as a json object.

## Receive streaming output

`onOutput` is invoked when receiving output from command execution.
By default, the output is split into chunks at arbitrary boundaries.
If you prefer the output to be split into complete lines, set `splitOutputLines`
to true. The callback is then invoked once for each line.


`onError` is invoked to report an error if the executed command errors. `onClose` is invoked when the process exits and receives the process exit code.

## Docker command process lifetime

The child process created by the extension is killed (`SIGTERM`) automatically when you close the dashboard in Docker Desktop or when you exit the extension UI.
If needed, you can also use the result of the `exec(streamOptions)` call in order to kill (`SIGTERM`) the process.

```typescript
const logListener = await ddClient.docker.cli.exec("logs", ["-f", "..."], {
  stream: {
    // ...
  },
});

// when done listening to logs or before starting a new one, kill the process
logListener.close();
```

## Run commands separately

> [!NOTE]
>
> You cannot chain commands in a single `exec()` invocation, such as `cmd1 $(cmd2)` or `docker kill $(docker ps -q)`, or use a pipe between commands.
>
> Invoke `exec()` for each command and parse results to pass parameters to the next command if needed.

## Deprecated APIs

### Backend service communication

> Deprecated extension backend communication
>
> The methods below that use `window.ddClient.backend` are deprecated and will be removed in a future version. Use the methods specified above.

The `window.ddClient.backend` object can be used to communicate with the backend
defined in the [vm section](../../architecture/metadata.md#vm-section) of the
extension metadata. The client is already connected to the backend.

Example usages:

```typescript
window.ddClient.backend
  .get("/some/service")
  .then((value: any) => console.log(value));

window.ddClient.backend
  .post("/some/service", { ... })
  .then((value: any) => console.log(value));

window.ddClient.backend
  .put("/some/service", { ... })
  .then((value: any) => console.log(value));

window.ddClient.backend
  .patch("/some/service", { ... })
  .then((value: any) => console.log(value));

window.ddClient.backend
  .delete("/some/service")
  .then((value: any) => console.log(value));

window.ddClient.backend
  .head("/some/service")
  .then((value: any) => console.log(value));

window.ddClient.backend
  .request({ url: "/url", method: "GET", headers: { 'header-key': 'header-value' }, data: { ... }})
  .then((value: any) => console.log(value));
```

### Backend command execution

> Deprecated extension backend command execution
>
> This method is deprecated and will be removed in a future version. Use the specified method above.

If your extension ships with additional binaries that should be run inside the
backend container, you can use the `execInVMExtension` function:

```typescript
const output = await window.ddClient.backend.execInVMExtension(
  `cliShippedInTheVm xxx`
);
console.log(output);
```

### Host command execution

> Deprecated invocation of extension binary
>
> This method is deprecated and will be removed in a future version. Use the method specified above.

To execute a command in the host:

```typescript
window.ddClient.execHostCmd(`cliShippedOnHost xxx`).then((cmdResult: any) => {
  console.log(cmdResult);
});
```

To stream the output of the command executed in the backend container or in the host:

```typescript
window.ddClient.spawnHostCmd(
  `cliShippedOnHost`,
  [`arg1`, `arg2`],
  (data: any, err: any) => {
    console.log(data.stdout, data.stderr);
    // Once the command exits we get the status code
    if (data.code) {
      console.log(data.code);
    }
  }
);
```

