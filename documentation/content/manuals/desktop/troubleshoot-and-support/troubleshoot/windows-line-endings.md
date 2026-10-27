---
title: "Unexpected syntax errors, use Unix style line endings for files in containers"
tags: [Troubleshooting]
---

Platform scope: Windows.

## Cause 

Docker containers expect Unix-style line `\n` endings, not Windows style: `\r\n`. This includes files referenced at the command line for builds and in RUN commands in Docker files.

Keep this in mind when authoring files such as shell scripts using Windows
tools, where the default is likely to be Windows style line endings. These
commands ultimately get passed to Unix commands inside a Unix based container
(for example, a shell script passed to `/bin/sh`). If Windows style line endings
are used, `docker run` fails with syntax errors.

## Solution 

 - Convert files to Unix-style line endings using:
   
   ```console
   $ dos2unix script.sh
   ```
- In VS Code, set line endings to `LF` (Unix) instead of `CRLF` (Windows).

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
