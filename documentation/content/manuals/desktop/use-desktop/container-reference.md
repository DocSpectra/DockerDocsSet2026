---
title: Container views, actions, and resource statistics
---

The **Containers** view lists all running and stopped containers and applications. It provides a clean interface to manage the lifecycle of your containers, interact with running applications, and inspect Docker objects—including Docker Compose apps.

## Container actions

Use the **Search** field to find a specific container by name.

From the **Containers** view you can:
- Start, stop, pause, resume, or restart containers
- View image packages and CVEs
- Delete containers
- Open the application in VS code
- Open the port exposed by the container in a browser
- Copy the `docker run` command for reuse or modification
- Use Docker Debug

## Resource usage

From the **Containers** view you can monitor your containers' CPU and memory usage over time. This can help you understand if something is wrong with your containers or if you need to allocate additional resources. 

When you inspect a container, the **Stats** tab displays further information about a container's resource utilization. You can see how much CPU, memory, network and disk space your container is using over time.

## Inspect a container

You can obtain detailed information about the container when you select it.

From here, you can use the quick action buttons to perform various actions such as pause, resume, start or stop, or explore the **Logs**, **Inspect**, **Bind mounts**, **Debug**, **Files**, and **Stats** tabs. 

### Inspect

Select **Inspect** to view low-level information about the container. It displays the local path, version number of the image, SHA-256, port mapping, and other details.
