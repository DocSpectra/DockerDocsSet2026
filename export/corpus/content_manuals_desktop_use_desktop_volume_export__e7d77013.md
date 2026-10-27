---
title: Export or schedule exports of a Docker Desktop volume
---

## Export a volume

You can export the content of a volume to a local file, a local image, and to an
image in Docker Hub, or to a supported cloud provider. When exporting content
from a volume used by one or more running containers, the containers are
temporarily stopped while Docker exports the content, and then restarted when
the export process is completed.

You can either [export a volume now](#export-a-volume-now) or [schedule a recurring export](#schedule-a-volume-export).

### Export a volume now

1. Sign in to Docker Desktop. You must be signed in to export a volume.
2. In the **Volumes** view, select the volume you want to export.
3. Select the **Exports** tab.
4. Select **Quick export**.
5. Select whether to export the volume to **Local or Hub storage** or **External
   cloud storage**, then specify the following additional details depending on
   your selection.

   See [Choose a volume export destination](volume-export-options.md).

6. Select **Save**.

### Schedule a volume export

1. Sign in to Docker Desktop. You must be signed in and have a paid [Docker subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopVolumes) to schedule a volume export.
2. In the **Volumes** view, select the volume you want to export.
3. Select the **Exports** tab.
4. Select **Schedule export**.
5. In **Recurrence**, select how often the export occurs, and then specify the
   following additional details based on your selection.

   - **Daily**: Specify the time that the backup occurs each day.
   - **Weekly**: Specify one or more days, and the time that the backup occurs
     each week.
   - **Monthly**: Specify which day of the month and the time that the backup
     occurs each month.

6. Select whether to export the volume to **Local or Hub storage** or **External
   cloud storage**, then specify the following additional details depending on
   your selection.
   
   See [Choose a volume export destination](volume-export-options.md).

7. Select **Save**.
