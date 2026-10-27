---
title: Create and manage synchronized file shares
linkTitle: Synchronized file shares
weight: 70
description: Get started with Synchronized file shares on Docker Desktop.
keyword: mutagen, file sharing, docker desktop, bind mounts
aliases:
- /desktop/synchronized-file-sharing/
---

{{< summary-bar feature_name="Synchronized file sharing" >}}

Synchronized file shares is an alternative file sharing mechanism that provides fast and flexible host-to-VM file sharing, enhancing bind mount performance through the use of synchronized filesystem caches. 
 
## Who is it for?

See [Intended workloads](file-sharing-context.md#who-is-it-for).

## How does Synchronized file shares work?

See [Synchronization behavior and supported environments](file-sharing-context.md#how-does-synchronized-file-shares-work).

## Before you begin

See [Synchronized file sharing behavior and limitations](file-sharing-context.md) for intended workloads, supported environments, and known issues.

## Create a file share instance 

To create a file share instance:
1. Sign in to Docker Desktop.
2. In **Settings**, navigate to the **File sharing** tab within the **Resources** section. 
3. In the **Synchronized file shares** section, select **Create share**.
4. Select a host folder to share. The synchronized file share should initialize and be usable.

File shares take a few seconds to initialize as files are copied into the Docker Desktop VM. During this time, the status indicator displays **Preparing**. There is also a status icon in the footer of the Docker Desktop Dashboard that keeps you updated.

When the status indicator displays **Watching for filesystem changes**, your files are available to the VM through all the standard bind mount mechanisms, whether that's `-v` in the command line or specified in your `compose.yml` file.

> [!NOTE]
>
> When you create a new service, setting the [bind mount option consistency](/reference/cli/docker/service/create/#options-for-bind-mounts) to `:consistent` bypasses Synchronized file shares. 

## Explore your file share instance

The **Synchronized file shares** section displays all your file share instances and provides useful information about each instance including:
- The origin of the file share content
- A status update
- How much space each file share is using
- The number of filesystem entry counts
- The number of symbolic links
- Which container(s) is using the file share instance

Selecting a file share instance expands the dropdown and exposes this information.

## Use `.syncignore`

You can use a `.syncignore` file at the root of each file share, to exclude local files from your file share instance. It supports the same syntax as `.dockerignore` files and excludes, and/or re-includes, paths from synchronization. `.syncignore` files are ignored at any location other than the root of the file share.
 
Some example of things you might want to add to your `.syncignore` file are:
- Large dependency directories, for example `node_modules` and `composer` directories (unless you rely on accessing them via a bind mount)
- `.git` directories (again, unless you need them)

In general, use your `.syncignore` file to exclude items that aren't critical to your workflow, especially those that would be slow to sync or use significant storage.

## Known issues

See [Known issues](file-sharing-context.md#known-issues).
