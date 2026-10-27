---
title: Update the application
weight: 30
linkTitle: "Part 2: Update the application"
keywords: get started, setup, orientation, quickstart, intro, concepts, containers,
  docker desktop
description: Making changes to your application
aliases:
 - /get-started/03_updating_app/
 - /guides/workshop/03_updating_app/
---

## Before you begin

- [Workshop prerequisites](/get-started/shared/workshop-prerequisites.md)
- [Workshop sequence](/get-started/workshop/_index.md#workshop-steps)
- [Build and tag images](/get-started/docker-concepts/building-images/build-tag-and-publish-an-image.md)


In [part 1](./02_our_app.md), you containerized a todo application. In this part, you'll update the application and image. You'll also learn how to stop and remove a container.

## Update the source code

In the following steps, you'll change the "empty text" when you don't have any todo list items to "You have no todo items yet! Add one above!"


1. In the `src/static/js/app.js` file, update line 56 to use the new empty text.

   ```diff
   - <p className="text-center">No items yet! Add one above!</p>
   + <p className="text-center">You have no todo items yet! Add one above!</p>
   ```

2. Build your updated version of the image, using the `docker build` command.

   ```console
   $ docker build -t getting-started .
   ```

3. Start a new container using the updated code.

   ```console
   $ docker run -dp 127.0.0.1:3000:3000 getting-started
   ```

You probably saw an error like this:

```console
docker: Error response from daemon: driver failed programming external connectivity on endpoint laughing_burnell 
(bb242b2ca4d67eba76e79474fb36bb5125708ebdabd7f45c8eaf16caaabde9dd): Bind for 127.0.0.1:3000 failed: port is already allocated.
```

The error occurred because you aren't able to start the new container while your old container is still running. The reason is that the old container is already using the host's port 3000 and only one process on the machine (containers included) can listen to a specific port. To fix this, you need to remove the old container.

## Remove the old container

[Stop and remove the old container using the CLI or Docker Desktop](/get-started/shared/stop-and-remove-containers.md).

## Start the updated app container

1. Now, start your updated app using the `docker run` command.

   ```console
   $ docker run -dp 127.0.0.1:3000:3000 getting-started
   ```

2. Refresh your browser on [http://localhost:3000](http://localhost:3000) and you should see your updated help text.

## Summary

In this section, you learned how to update and rebuild an image, as well as how to stop and remove a container.

Related information:
 - [docker CLI reference](/reference/cli/docker/)

## Next steps

Next, you'll learn how to share images with others.

{{< button text="Share the application" url="04_sharing_app.md" >}}
