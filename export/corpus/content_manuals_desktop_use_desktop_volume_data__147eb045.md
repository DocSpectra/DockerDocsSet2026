---
title: Clone, empty, or import a Docker Desktop volume
---

For volume storage concepts, see [Use volumes](/manuals/engine/storage/volumes.md).

## Clone a volume

Cloning a volume creates a new volume with a copy of all of the data from the
cloned volume. When cloning a volume used by one or more running containers, the
containers are temporarily stopped while Docker clones the data, and then
restarted when the cloning process is completed.

To clone a volume:

1. Sign in to Docker Desktop. You must be signed in to clone a volume.
2. In the **Volumes** view, select the **Clone** icon in the **Actions** column
   for the volume you want to clone.
3. In the **Clone a volume** modal, specify a **Volume name**, and then select
   **Clone**.

## Empty a volume

Emptying a volume deletes all a volume's data, but doesn't delete the volume.
When emptying a volume used by one or more running containers, the containers
are temporarily stopped while Docker empties the data, and then restarted when
the emptying process is completed.

To empty a volume:

1. Sign in to Docker Desktop. You must be signed in to empty a volume.
2. In the **Volumes** view, select the volume you want to empty.
3. Next to **Import**, select the **More volume actions** icon, and then select **Empty volume**.
4. In the **Empty a volume?** modal, select **Empty**.

## Import a volume

You can import a local file, a local image, or an image from Docker Hub. Any
existing data in the volume is replaced by the imported content. When importing
content to a volume used by one or more running containers, the containers are
temporarily stopped while Docker imports the content, and then restarted when
the import process is completed.

To import a volume:

1. Sign in to Docker Desktop. You must be signed in to import a volume.
2. Optionally, [create](volume-create.md#create-a-volume) a new volume to import the content
   into.
3. Select the volume you want to import content in to.
4. Select **Import**.
5. Select where the content is coming from and then specify the following
   additional details depending on your selection:

   - **Local file**: Select the file that contains the content.
   - **Local image**: Select the local image that contains the content.
   - **Registry**: Specify the image from Docker Hub that contains the content.

6. Select **Import**.
