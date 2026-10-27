---
title: Extension security
linkTitle: Security
description: Aspects of the security model of extensions
keywords: Docker, extensions, sdk, security
aliases:
 - /desktop/extensions-sdk/guides/security/
 - /desktop/extensions-sdk/architecture/security/
---

## Extension capabilities

An extension can have the following optional parts: 
* A user interface in HTML or JavaScript, displayed in Docker Desktop Dashboard
* A backend part that runs as a container
* Executables deployed on the host machine.

Extensions are executed with the same permissions as the Docker Desktop user. Extension capabilities include running any Docker commands (including running containers and mounting folders), running extension binaries, and accessing files on your machine that are accessible by the user running Docker Desktop.
Note that extensions are not restricted to execute binaries that they list in the [host section](../architecture/metadata.md#host-section) of the extension metadata: since these binaries can contain any code running as user, they can in turn execute any other commands as long as the user has rights to execute them.

The Extensions SDK provides a set of JavaScript APIs to invoke commands or invoke these binaries from the extension UI code. Extensions can also provide a backend part that starts a long-lived running container in the background.

> [!IMPORTANT]
>
> Make sure you trust the publisher or author of the extension when you install it, as the extension has the same access rights as the user running Docker Desktop.

## Policies enforced for the front-end code

Extension UI code is rendered in a separate electron session and doesn't have a node.js environment initialized, nor direct access to the electron APIs. 

This is to limit the possible unexpected side effects to the overall Docker Dashboard.

The extension UI code can't perform privileged tasks, such as making changes to the system, or spawning sub-processes, except by using the SDK APIs provided with the extension framework.
The Extension UI code can also perform interactions with Docker Desktop, such as navigating to various places in the Dashboard, only through the extension SDK APIs.

Extensions UI parts are isolated from each other and extension UI code is running in its own session for each extension. Extensions can't access other extensions’ session data.

`localStorage` is one of the mechanisms of a browser’s web storage. It allows users to save data as key-value pairs in the browser for later use. `localStorage` doesn't clear data when the browser (the extension pane) closes. This makes it ideal for persisting data when navigating out of the extension to other parts of Docker Desktop.

If your extension uses `localStorage` to store data, other extensions running in Docker Desktop can't access the local storage of your extension. The extension’s local storage is persisted even after Docker Desktop is stopped or restarted. When an extension is upgraded, its local storage is persisted, whereas when it is uninstalled, its local storage is completely removed.

