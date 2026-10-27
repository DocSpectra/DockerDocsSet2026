---
title: "Docker commands failing in Git Bash"
tags: [Troubleshooting]
---

Platform scope: Windows.

## Error message

```console
$ docker run --rm -ti -v C:\Users\user\work:/work alpine
docker: Error response from daemon: mkdir C:UsersUserwork: Access is denied.
```

```console
$ docker run --rm -ti -v $(pwd):/work alpine
docker: Error response from daemon: OCI runtime create failed: invalid mount {Destination:\Program Files\Git\work Type:bind Source:/run/desktop/mnt/host/c/Users/user/work;C Options:[rbind rprivate]}: mount destination \Program Files\Git\work not absolute: unknown.
```

## Cause

Git Bash (or MSYS) provides a Unix-like environment on Windows. These tools apply their own
preprocessing on the command line. 

This affects `$(pwd)`, colon-separated paths, and tilde (`~`)

Also, the `\` character has a special meaning in Git Bash. 

## Solution

 - Disable Git Bash path conversion temporarily. For example, run the command with MSYS path conversion disable:
    ```console
    $ MSYS_NO_PATHCONV=1 docker run --rm -ti -v $(pwd):/work alpine
    ```
 - Use proper path formatting:
    - Use double forward and backslashes (`\\` `//`) instead of single (`\` `/`).
    - If referencing `$(pwd)`, add an extra `/`:

Portability of the scripts is not affected as Linux treats multiple `/` as a single entry.

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
