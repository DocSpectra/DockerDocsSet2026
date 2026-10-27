---
title: "Build and run a custom JupyterLab environment"
description: "Build and run a custom JupyterLab environment"
---

## Prerequisites

[Latest Docker Desktop](prerequisites.md#latest-docker-desktop).

[JupyterLab and Docker concepts](jupyter-context.md).

## Customize your JupyterLab environment

You can create your own JupyterLab environment and build it into an image using
Docker. By building your own image, you can customize your JupyterLab
environment with the packages and tools you need, and ensure that it's
consistent and reproducible across different deployments. Building your own
image also makes it easier to share your JupyterLab environment with others, or
to use it as a base for further development.

### Define your environment in a Dockerfile

In the previous Iris Dataset example from [Save a notebook to the volume](jupyter-notebooks.md#save-a-notebook-to-the-volume), you had to install the dependencies, `matplotlib` and `scikit-learn`, every time you ran a new container. While the dependencies in that small example download and
install quickly, it may become a problem as your list of dependencies grow.
There may also be other tools, packages, or files that you always want in your
environment.

In this case, you can install the dependencies as part of the environment in the
image. Then, every time you run your container, the dependencies will always be
installed.

You can define your environment in a Dockerfile. A Dockerfile is a text file
that instructs Docker how to create an image of your JupyterLab environment. An
image contains everything you want and need when running JupyterLab, such as
files, packages, and tools.

In a directory of your choice, create a new text file named `Dockerfile`. Open the `Dockerfile` in an IDE or text editor and then add the following contents.

```dockerfile
# syntax=docker/dockerfile:1

FROM quay.io/jupyter/base-notebook
RUN pip install --no-cache-dir matplotlib scikit-learn
```

This Dockerfile uses the `quay.io/jupyter/base-notebook` image as the base, and then runs `pip` to install the dependencies. For more details about the instructions in the Dockerfile, see the [Dockerfile reference](/reference/dockerfile/).

Before you proceed, save your changes to the `Dockerfile`.

### Build your environment into an image

After you have a `Dockerfile` to define your environment, you can use `docker
build` to build an image using your `Dockerfile`.

Open a terminal, change directory to the directory where your `Dockerfile` is
located, and then run the following command.

```console
$ docker build -t my-jupyter-image .
```

The command builds a Docker image from your `Dockerfile` and a context. The
`-t` option specifies the name and tag of the image, in this case
`my-jupyter-image`. The `.` indicates that the current directory is the context,
which means that the files in that directory can be used in the image creation
process.

You can verify that the image was built by viewing the `Images` view in Docker Desktop, or by running the `docker image ls` command in a terminal. You should see an image named `my-jupyter-image`.

## Run your image as a container

To run your image as a container, you use the `docker run` command. In the
`docker run` command, you'll specify your own image name.

```console
$ docker run --rm -p 8889:8888 my-jupyter-image start-notebook.py --NotebookApp.token='my-token'
```

To access the container, in a web browser navigate to
[localhost:8889/lab?token=my-token](http://localhost:8889/lab?token=my-token).

You can now use the packages without having to install them in your notebook.

1. In the **Launcher**, under **Notebook**, select **Python 3**.

2. In the notebook, specify the following code.

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

3. Select the play button to run the code. You should see a scatter plot of the Iris dataset.

In the terminal, press `ctrl`+ `c` to stop the container.
