---
description: Understand what you can do with the Volumes view on Docker Dashboard
keywords: Docker Desktop Dashboard, manage, containers, gui, dashboard, volumes, user manual
title: Explore the Volumes view in Docker Desktop
linkTitle: Volumes
weight: 30
---

The **Volumes** view in Docker Desktop lets you create, inspect, delete, clone, empty, export, and import [Docker volumes](/manuals/engine/storage/volumes.md). You can also browse files and folders in volumes and see which containers are using them.

## View your volumes

You can view the following information about your volumes:

- Name: The name of the volume.
- Status: Whether the volume is in-use by a container or not.
- Created: How long ago the volume was created.
- Size: The size of the volume.
- Scheduled exports: Whether a scheduled export is active or not.

By default, the **Volumes** view displays a list of all the volumes.

You can filter and sort volumes as well as modify which columns are displayed by
doing the following:

- Filter volumes by name: Use the **Search** field.
- Filter volumes by status: To the right of the search bar, filter volumes by
  **In use** or **Unused**.
- Sort volumes: Select a column name to sort the volumes.
- Customize columns: To the right of the search bar, choose what volume
  information to display.

## Create a volume

See [Create a volume in Docker Desktop](volume-create.md).

## Inspect a volume

To explore the details of a specific volume, select a volume from the list. This
opens the detailed view.

The **Container in-use** tab displays the name of the container using the
volume, the image name, the port number used by the container, and the target. A
target is a path inside a container that gives access to the files in the
volume.

The **Stored data** tab displays the files and folders in the volume and the
file size. To save a file or a folder, right-click on the file or folder to
display the options menu, select **Save as...**, and then specify a location to
download the file.

To delete a file or a folder from the volume, right-click on the file or folder
to display the options menu, select **Delete**, and then select **Delete** again
to confirm.

The **Exports** tab lets you [export the volume](volume-export.md).

## Clone a volume

See [Clone a volume](volume-data.md#clone-a-volume).

## Delete one or more volumes

Deleting a volume deletes the volume and all its data. When a container is using
a volume, you can't delete the volume, even if the container is stopped.
You must first stop and remove any containers
using the volume before you can delete the volume.

To delete a volume:

1. In the **Volumes** view, select **Delete** icon in the **Actions** column for
   the volume you want to delete.
2. In the **Delete volume?** modal, select **Delete forever**.

To delete multiple volumes:

1. In the **Volumes** view, select the checkbox next to all the volumes you want
   to delete.
2. Select **Delete**.
3. In the **Delete volumes?** modal, select **Delete forever**.

## Empty a volume

See [Empty a volume](volume-data.md#empty-a-volume).

## Export a volume

See [Export or schedule exports](volume-export.md).

### Export a volume now

See [Export a volume now](volume-export.md#export-a-volume-now).

### Schedule a volume export

See [Schedule a volume export](volume-export.md#schedule-a-volume-export).

## Import a volume

See [Import a volume](volume-data.md#import-a-volume).

## Additional resources

- [Persisting container data](/get-started/docker-concepts/running-containers/persisting-container-data.md)
- [Use volumes](/manuals/engine/storage/volumes.md)
