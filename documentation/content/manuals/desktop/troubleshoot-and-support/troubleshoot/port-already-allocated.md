---
title: "`port already allocated` errors"
tags: [Troubleshooting]
---

Platform scope: All platforms.

## Error message

When starting a container, you may see an error like:

```text
Bind for 0.0.0.0:8080 failed: port is already allocated
```

Or

```text
listen tcp:0.0.0.0:8080: bind: address is already in use
```

## Cause

- Another application on your system is already using the specified port.
- A previously running container was not stopped properly and is still bound to the port.

## Solution

To discover the identity of this software, either:
- Use the `resmon.exe` GUI, select **Network** and then **Listening Ports**
- In PowerShell, use `netstat -aon | find /i "listening "` to discover the PID of the process
currently using the port (the PID is the number in the rightmost column). 

Then, decide whether to shut the other process down, or to use a different port in your
Docker app.

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
