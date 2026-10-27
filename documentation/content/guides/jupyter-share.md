---
title: "Share a JupyterLab image and notebook volume"
description: "Share a JupyterLab image and notebook volume"
---

## Prerequisites

[Latest Docker Desktop](prerequisites.md#latest-docker-desktop).

[JupyterLab and Docker concepts](jupyter-context.md).

[Build the JupyterLab image](jupyter-customize.md) and [save notebooks to a volume](jupyter-notebooks.md).

## Share your work

By sharing your image and notebook, you create a portable and replicable
research environment that can be easily accessed and used by other data
scientists. This process not only facilitates collaboration but also ensures
that your work is preserved in an environment where it can be run without
compatibility issues.

To share your image and data, you'll use [Docker Hub](https://hub.docker.com/). Docker Hub is a cloud-based registry service that lets you share and distribute container images.

### Share your image

1. [Sign up](https://www.docker.com/pricing?ref=Docs&refAction=DocsGuidesJupyter) or sign in to [Docker Hub](https://hub.docker.com).

2. Rename your image so that Docker knows which repository to push it to. Open a
   terminal and run the following `docker tag` command. Replace `YOUR-USER-NAME`
   with your Docker ID.

   ```console
   $ docker tag my-jupyter-image YOUR-USER-NAME/my-jupyter-image
   ```

3. Run the following `docker push` command to push the image to Docker Hub.
   Replace `YOUR-USER-NAME` with your Docker ID.

   ```console
   $ docker push YOUR-USER-NAME/my-jupyter-image
   ```

4. Verify that you pushed the image to Docker Hub.
   1. Go to [Docker Hub](https://hub.docker.com).
   2. Select **My Hub** > **Repositories**.
   3. View the **Last pushed** time for your repository.

Other users can now download and run your image using the `docker run` command. They need to replace `YOUR-USER-NAME` with your Docker ID.

```console
$ docker run --rm -p 8889:8888 YOUR-USER-NAME/my-jupyter-image start-notebook.py --NotebookApp.token='my-token'
```

### Share your volume

This example uses the Docker Desktop graphical user interface. Alternatively, in the command line interface you can [back up the volume](/engine/storage/volumes/#back-up-a-volume) and then [push it using the ORAS CLI](/manuals/docker-hub/repos/manage/hub-images/oci-artifacts.md#push-a-volume).

1. Sign in to Docker Desktop.
2. In the Docker Dashboard, select **Volumes**.
3. Select the **jupyter-data** volume by selecting the name.
4. Select the **Exports** tab.
5. Select **Quick export**.
6. For **Location**, select **Registry**.
7. In the text box under **Registry**, specify your Docker ID, a name for the
   volume, and a tag. For example, `YOUR-USERNAME/jupyter-data:latest`.
8. Select **Save**.
9. Verify that you exported the volume to Docker Hub.
   1. Go to [Docker Hub](https://hub.docker.com).
   2. Select **My Hub** > **Repositories**.
   3. View the **Last pushed** time for your repository.

Other users can now download and import your volume. To import the volume and then run it with your image:

1. Sign in to Docker Desktop.
2. In the Docker Dashboard, select **Volumes**.
3. Select **Create** to create a new volume.
4. Specify a name for the new volume. For this example, use `jupyter-data-2`.
5. Select **Create**.
6. In the list of volumes, select the **jupyter-data-2** volume by selecting the
   name.
7. Select **Import**.
8. For **Location**, select **Registry**.
9. In the text box under **Registry**, specify the same name as the repository
   that you exported your volume to. For example,
   `YOUR-USERNAME/jupyter-data:latest`.
10. Select **Import**.
11. In a terminal, run `docker run` to run your image with the imported volume.
   Replace `YOUR-USER-NAME` with your Docker ID.

   ```console
   $ docker run --rm -p 8889:8888 -v jupyter-data-2:/home/jovyan/work YOUR-USER-NAME/my-jupyter-image start-notebook.py --NotebookApp.token='my-token'
   ```
