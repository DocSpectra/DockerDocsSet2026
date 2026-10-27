---
title: "Using mounted volumes and getting runtime errors indicating an application file is not found, access to a volume mount is denied, or a service cannot start"
tags: [Troubleshooting]
---

Platform scope: All platforms.

## Cause

If your project directory is located outside your home directory (`/home/<user>`), Docker Desktop requires file sharing permissions to access it.

## Solution

Enable file sharing in Docker Desktop for Mac and Linux:

1. Navigate to **Settings**, select **Resources** and then **File sharing**.
2. Add the drive or folder that contains the Dockerfile and volume mount paths.

Enable file sharing in Docker Desktop for Windows:

1. From **Settings**, select **Shared Folders**. 
2. Share the folder that contains the Dockerfile and volume mount paths.

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
