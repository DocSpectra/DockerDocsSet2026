---
title: Stop and remove containers
---

## Stop and remove a container

To remove a container, you first need to stop it. Once it has stopped, you can remove it. You can remove a container using the CLI or Docker Desktop's graphical interface. Choose the option that you're most comfortable with.

{{< tabs >}}
{{< tab name="CLI" >}}

### Remove a container using the CLI

1. Get the ID of the container by using the `docker ps` command.

   ```console
   $ docker ps
   ```

2. Use the `docker stop` command to stop the container. Replace `<the-container-id>` with the ID from `docker ps`.

   ```console
   $ docker stop <the-container-id>
   ```

3. Once the container has stopped, you can remove it by using the `docker rm` command.

   ```console
   $ docker rm <the-container-id>
   ```

> [!NOTE]
>
> You can stop and remove a container in a single command by adding the `force` flag to the `docker rm` command. For example: `docker rm -f <the-container-id>`

{{< /tab >}}
{{< tab name="Docker Desktop" >}}

### Remove a container using Docker Desktop

1. Open Docker Desktop to the **Containers** view.
2. Select the trash can icon under the **Actions** column for the container that you want to delete.
3. In the confirmation dialog, select **Delete forever**.

{{< /tab >}}
{{< /tabs >}}

