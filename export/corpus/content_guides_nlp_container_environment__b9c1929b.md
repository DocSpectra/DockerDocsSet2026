---
title: Docker-NLP container environment
description: Dockerfile walkthrough for the Docker-NLP sample applications.
---

## Explore the Docker-NLP Dockerfile

You'll use Docker to run the application in a container. Docker lets you
containerize the application, providing a consistent and isolated environment
for running it. This means the application will operate as intended within its
Docker container, regardless of the underlying system differences.

To run the application in a container, a Dockerfile is required. A Dockerfile is
a text document that contains all the commands you would call on the command
line to assemble an image. An image is a read-only template with instructions
for creating a Docker container.

The sample application already contains a `Dockerfile`. Open the `Dockerfile` in a code or text editor to explore its contents.

The following steps explain each part of the `Dockerfile`. For more details, see the [Dockerfile reference](/reference/dockerfile/).

1. Specify the base image.

   ```dockerfile
   FROM python:3.8-slim
   ```

   This command sets the foundation for the build. `python:3.8-slim` is a
   lightweight version of the Python 3.8 image, optimized for size and speed.
   Using this slim image reduces the overall size of your Docker image, leading
   to quicker downloads and less surface area for security vulnerabilities. This
   is particularly useful for a Python-based application where you might not
   need the full standard Python image.

2. Set the working directory.

   ```dockerfile
   WORKDIR /app
   ```

   `WORKDIR` sets the current working directory within the Docker image. By
   setting it to `/app`, you ensure that all subsequent commands in the
   Dockerfile (like `COPY` and `RUN`) are executed in this directory. This also
   helps in organizing your Docker image, as all application-related files are
   contained in a specific directory.

3. Copy the requirements file into the image.

   ```dockerfile
   COPY requirements.txt /app
   ```

   The `COPY` command transfers the `requirements.txt` file from
   your local machine into the Docker image. This file lists all Python
   dependencies required by the application. Copying it into the container
   lets the next command (`RUN pip install`) install these dependencies
   inside the image environment.

4. Install the Python dependencies in the image.

   ```dockerfile
   RUN pip install --no-cache-dir -r requirements.txt
   ```

   This line uses `pip`, Python's package installer, to install the packages
   listed in `requirements.txt`. The `--no-cache-dir` option disables
   the cache, which reduces the size of the Docker image by not storing the
   unnecessary cache data.

5. Run additional commands.

   ```dockerfile
   RUN python -m spacy download en_core_web_sm
   ```

   This step is specific to NLP applications that require the spaCy library. It downloads the `en_core_web_sm` model, which is a small English language model for spaCy.

6. Copy the application code into the image.

   ```dockerfile
   COPY *.py /app
   COPY entrypoint.sh /app
   ```

   These commands copy your Python scripts and the `entrypoint.sh` script into
   the image's `/app` directory. This is crucial because the container needs
   these scripts to run the application. The `entrypoint.sh` script is
   particularly important as it dictates how the application starts inside the
   container.

7. Set permissions for the `entrypoint.sh` script.

   ```dockerfile
   RUN chmod +x /app/entrypoint.sh
   ```

   This command modifies the file permissions of `entrypoint.sh`, making it
   executable. This step is necessary to ensure that the Docker container can
   run this script to start the application.

8. Set the entry point.

   ```dockerfile
   ENTRYPOINT ["/app/entrypoint.sh"]
   ```

   The `ENTRYPOINT` instruction configures the container to run `entrypoint.sh`
   as its default executable. This means that when the container starts, it
   automatically executes the script.

   You can explore the `entrypoint.sh` script by opening it in a code or text
   editor. As the sample contains several applications, the script lets you
   specify which application to run when the container starts.

