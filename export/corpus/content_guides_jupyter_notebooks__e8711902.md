---
title: "Save and access Jupyter notebooks in a volume"
description: "Save and access Jupyter notebooks in a volume"
---

## Prerequisites

[Latest Docker Desktop](prerequisites.md#latest-docker-desktop).

[JupyterLab and Docker concepts](jupyter-context.md).

## Save and access notebooks

When you remove a container, all data in that container is deleted. To save
notebooks outside of the container, you can use a [volume](/engine/storage/volumes/).

### Run a JupyterLab container with a volume

To start the container with a volume, open a terminal and run the following command

```console
$ docker run --rm -p 8889:8888 -v jupyter-data:/home/jovyan/work quay.io/jupyter/base-notebook start-notebook.py --NotebookApp.token='my-token'
```

The `-v` option tells Docker to create a volume named `jupyter-data` and mount it in the container at `/home/jovyan/work`.

To access the container, in a web browser navigate to
[localhost:8889/lab?token=my-token](http://localhost:8889/lab?token=my-token).
Notebooks can now be saved to the volume and will accessible even when
the container is deleted.

### Save a notebook to the volume

For this example, you'll use the [Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) example from scikit-learn.

1. Open a web browser and access your JupyterLab container at [localhost:8889/lab?token=my-token](http://localhost:8889/lab?token=my-token).

2. In the **Launcher**, under **Notebook**, select **Python 3**.

3. In the notebook, specify the following to install the necessary packages.

   ```console
   !pip install matplotlib scikit-learn
   ```

4. Select the play button to run the code.

5. In the notebook, specify the following code.

   ```python
   from sklearn import datasets

   iris = datasets.load_iris()
   import matplotlib.pyplot as plt

   _, ax = plt.subplots()
   scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
   ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
   _ = ax.legend(
      scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
   )
   ```

6. Select the play button to run the code. You should see a scatter plot of the
   Iris dataset.

7. In the top menu, select **File** and then **Save Notebook**.

8. Specify a name in the `work` directory to save the notebook to the volume.
   For example, `work/mynotebook.ipynb`.

9. Select **Rename** to save the notebook.

The notebook is now saved in the volume.

In the terminal, press `ctrl`+ `c` to stop the container.

Now, any time you run a Jupyter container with the volume, you'll have access to the saved notebook.

When you do run a new container, and then run the data plot code again, it'll
need to run `!pip install matplotlib scikit-learn` and download the packages.
You can avoid reinstalling packages every time you run a new container by
creating your own image with the packages already installed.
