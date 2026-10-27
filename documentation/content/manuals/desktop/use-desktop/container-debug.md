---
title: Run commands or debug a container in Docker Desktop
---

For the Containers view and quick actions, see [Container views, actions, and resource statistics](container-reference.md).

## Exec/Debug

If you have not enabled Docker Debug in settings, the **Exec** tab displays. It lets you quickly run commands within your running container.

Using the **Exec** tab is the same as running one of the following commands:

- `docker exec -it <container-id> /bin/sh`
- `docker exec -it <container-id> cmd.exe` when accessing Windows containers

For more details, see the [`docker exec` CLI reference](/reference/cli/docker/container/exec/).

If you have enabled Docker Debug in settings, or toggled on **Debug mode** to the right of the tab options, the **Debug** tab displays. 

Debug mode has several advantages, such as:

- A customizable toolbox. The toolbox comes with many standard Linux tools
  pre-installed, such as `vim`, `nano`, `htop`, and `curl`. For more details, see the [`docker debug` CLI reference](/reference/cli/docker/debug/).
- The ability to access containers that don't have a shell, for example, slim or
  distroless containers.

To use debug mode:

- Hover over your running container and under the **Actions** column, select the **Show container actions**
menu. From the drop-down menu, select **Use Docker Debug**.
- Or, select the container and then select the **Debug** tab. 

To use debug mode by default, navigate to
the **General** tab in **Settings** and select the **Enable Docker Debug by
default** option.
