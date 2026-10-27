---
title: "Docker Desktop fails to start when anti-virus software is installed"
tags: [Troubleshooting]
---

Platform scope: Windows.

## Cause

Some anti-virus software may be incompatible with Hyper-V and Microsoft
Windows builds. The conflict
typically occurs after a Windows update and
manifests as an error response from the Docker daemon and a Docker Desktop start failure.

## Solution

For a temporary workaround, uninstall the anti-virus software, or
add Docker to the exclusions/exceptions in your antivirus software.

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
