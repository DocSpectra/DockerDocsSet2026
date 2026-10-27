---
title: Compose lifecycle hook behavior
description: Lifecycle hook privileges, execution timing, and stop exceptions.
---

{{< summary-bar feature_name="Compose lifecycle hooks" >}}

## Services lifecycle hooks

When Docker Compose runs a container, it uses two elements, 
[ENTRYPOINT and COMMAND](/manuals/engine/containers/run.md#default-command-and-options), 
to manage what happens when the container starts and stops.

However, it can sometimes be easier to handle these tasks separately with lifecycle hooks - 
commands that run right after the container starts or just before it stops.

Lifecycle hooks are particularly useful because they can have special privileges 
(like running as the root user), even when the container itself runs with lower privileges 
for security. This means that certain tasks requiring higher permissions can be done without 
compromising the overall security of the container.

### Post-start hooks

Post-start hooks are commands that run after the container has started, but there's no 
set time for when exactly they will execute. The hook execution timing is not assured during 
the execution of the container's `entrypoint`.


### Pre-stop hooks

Pre-stop hooks are commands that run before the container is stopped by a specific 
command (like `docker compose down` or stopping it manually with `Ctrl+C`). 
These hooks won't run if the container stops by itself or gets killed suddenly.
