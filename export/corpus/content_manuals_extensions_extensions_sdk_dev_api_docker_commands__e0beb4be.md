---
title: Execute Docker commands
description: Execute Docker commands and stream logs or events from an extension.
---

## Docker commands

For execution contexts and shared behavior, see [Extension service and command execution](backend.md).

Extensions can also directly execute the `docker` command line.

### Collect command output

▸ **exec**(`cmd`, `args`): `Promise`<[`ExecResult`](/reference/api/extensions-sdk/ExecResult.md)\>

```typescript
const result = await ddClient.docker.cli.exec("info", [
  "--format",
  '"{{ json . }}"',
]);
```

For command results and parsing helpers, see [Collect command results](backend.md#collect-command-results).

### Stream container logs

▸ **exec**(`cmd`, `args`, `options`): `void`

The command above streams the output as a result of the execution of a Docker command.
This is useful if you need to get the output as a stream or the output of the command is too long.

```typescript
await ddClient.docker.cli.exec("logs", ["-f", "..."], {
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
    splitOutputLines: true,
  },
});
```

For process cleanup, see [Docker command process lifetime](backend.md#docker-command-process-lifetime).

### Listen to Docker events

This `exec(streamOptions)` API can also be used to listen to docker events:

```typescript
await ddClient.docker.cli.exec(
  "events",
  ["--format", "{{ json . }}", "--filter", "container=my-container"],
  {
    stream: {
      onOutput(data) {
        if (data.stdout) {
          const event = JSON.parse(data.stdout);
          console.log(event);
        } else {
          console.log(data.stderr);
        }
      },
      onClose(exitCode) {
        console.log("onClose with exit code " + exitCode);
      },
      splitOutputLines: true,
    },
  }
);
```

For command chaining limits, see [Run commands separately](backend.md#run-commands-separately).

See the [Exec API reference](/reference/api/extensions-sdk/Exec.md) for details about these methods.

## Deprecated execution of Docker commands

> Deprecated execution of Docker commands
>
> This method is deprecated and will be removed in a future version. Use the methods specified above.

```typescript
const output = await window.ddClient.execDockerCmd(
  "info",
  "--format",
  '"{{ json . }}"'
);

window.ddClient.spawnDockerCmd("logs", ["-f", "..."], (data, error) => {
  console.log(data.stdout);
});
```
