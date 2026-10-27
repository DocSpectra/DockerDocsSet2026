---
description: Learn how to deploy pre-trained models in a TensorFlow.js web applications to perform face detection.
keywords: tensorflow.js, machine learning, ml, mediapipe, blazeface, face detection
title: Face detection with TensorFlow.js
summary: |
  This guide explains how to run TensorFlow.js in Docker containers.
tags: [ai]
languages: [js]
aliases:
  - /guides/use-case/tensorflowjs/
params:
  time: 20 minutes
---

This guide introduces the seamless integration of TensorFlow.js with Docker to
perform face detection. In this guide, you'll explore how to:

- Run a containerized TensorFlow.js application using Docker.
- Implement face detection in a web application with TensorFlow.js.
- Construct a Dockerfile for a TensorFlow.js web application.
- Use Docker Compose for real-time application development and updates.
- Share your Docker image on Docker Hub to facilitate deployment and extend
  reach.

> **Acknowledgment**
>
> Docker would like to thank [Harsh Manvar](https://github.com/harsh4870) for
> his contribution to this guide.

## Prerequisites

- You have installed the latest version of
  [Docker Desktop](/get-started/get-docker.md).
- Review the [Git client prerequisite](prerequisites.md#git-client).

## TensorFlow.js and Docker

See [TensorFlow.js, Docker, and browser backends](tensorflowjs-context.md).

## Get and run the sample application

In a terminal, clone the sample application using the following command.

```console
$ git clone https://github.com/harsh4870/TensorJS-Face-Detection
```

After cloning the application, you'll notice the application has a `Dockerfile`.
This Dockerfile lets you build and run the application locally with nothing more
than Docker.

Before you run the application as a container, you must build it into an image.
Run the following command inside the `TensorJS-Face-Detection` directory to
build an image named `face-detection-tensorjs`.

```console
$ docker build -t face-detection-tensorjs .
```

The command builds the application into an image. Depending on your network
connection, it can take several minutes to download the necessary components the
first time you run the command.

To run the image as a container, run the following command in a terminal.

```console
$ docker run -p 80:80 face-detection-tensorjs
```

The command runs the container and maps port 80 in the container to port 80 on
your system.

Once the application is running, open a web browser and access the application
at [http://localhost:80](http://localhost:80). You may need to grant access to
your webcam for the application.

In the web application, you can change the backend to use one of the following:

- WASM
- WebGL
- CPU

To stop the application, press `ctrl`+`c` in the terminal.

## About the application

The sample application performs real-time face detection using
[MediaPipe](https://developers.google.com/mediapipe/), a comprehensive framework
for building multimodal machine learning pipelines. It's specifically using the
BlazeFace model, a lightweight model for detecting faces in images.

See [browser backends](tensorflowjs-context.md#browser-backends) for WASM, WebGL, and CPU context.

## Explore the application's code

See the [face detection sample code reference](tensorflowjs-application.md).

## Explore the Dockerfile

See [Dockerfiles and images](genai-container-assets.md#dockerfiles-and-images) for the role of these assets.

The following is the Dockerfile for this project.

```dockerfile
FROM nginx:stable-alpine3.17-slim
WORKDIR /usr/share/nginx/html
COPY . .
```

This Dockerfile defines an image that serves static content using Nginx from an
Alpine Linux base image.

## Develop with Compose

Docker Compose is a tool for defining and running multi-container Docker
applications. With Compose, you use a YAML file to configure your application's
services, networks, and volumes. In this case, the application isn't a
multi-container application, but Docker Compose has other useful features for
development, like [Compose Watch](/manuals/compose/how-tos/file-watch.md).

The sample application doesn't have a Compose file yet. To create a Compose
file, in the `TensorJS-Face-Detection` directory, create a text file named
`compose.yaml` and then add the following contents.

```yaml
services:
  server:
    build:
      context: .
    ports:
      - 80:80
    develop:
      watch:
        - action: sync
          path: .
          target: /usr/share/nginx/html
```

This Compose file defines a service that is built using the Dockerfile in the
same directory. It maps port 80 on the host to port 80 in the container. It also
has a `develop` subsection with the `watch` attribute that defines a list of
rules that control automatic service updates based on local file changes. For
more details about the Compose instructions, see the
[Compose file reference](/reference/compose-file/_index.md).

Save the changes to your `compose.yaml` file and then run the following command to run the application.

```console
$ docker compose watch
```

Once the application is running, open a web browser and access the application
at [http://localhost:80](http://localhost:80). You may need to grant access to
your webcam for the application.

Now you can make changes to the source code and see the changes automatically
reflected in the container without having to rebuild and rerun the container.

Open the `index.js` file and update the landmark points to be green instead of
blue on line 83.

```diff
-        ctx.fillStyle = "blue";
+        ctx.fillStyle = "green";
```

Save the changes to the `index.js` file and then refresh the browser page. The
landmark points should now appear green.

To stop the application, press `ctrl`+`c` in the terminal.

## Share your image

Publishing your Docker image on Docker Hub streamlines deployment processes for
others, enabling seamless integration into diverse projects. It also promotes
the adoption of your containerized solutions, broadening their impact across the
developer ecosystem. To share your image:

1. [Sign up](https://www.docker.com/pricing?ref=Docs&refAction=DocsGuidesTensorflowjs) or sign in to [Docker Hub](https://hub.docker.com).

2. Rebuild your image to include the changes to your application. This time,
   prefix the image name with your Docker ID. Docker uses the name to determine
   which repository to push it to. Open a terminal and run the following
   command in the `TensorJS-Face-Detection` directory. Replace `YOUR-USER-NAME`
   with your Docker ID.

   ```console
   $ docker build -t YOUR-USER-NAME/face-detection-tensorjs .
   ```

3. Run the following `docker push` command to push the image to Docker Hub.
   Replace `YOUR-USER-NAME` with your Docker ID.

   ```console
   $ docker push YOUR-USER-NAME/face-detection-tensorjs
   ```

4. Verify that you pushed the image to Docker Hub.
   1. Go to [Docker Hub](https://hub.docker.com).
   2. Select **My Hub** > **Repositories**.
   3. View the **Last pushed** time for your repository.

Other users can now download and run your image using the `docker run` command. They need to replace `YOUR-USER-NAME` with your Docker ID.

```console
$ docker run -p 80:80 YOUR-USER-NAME/face-detection-tensorjs
```

## Summary

This guide demonstrated leveraging TensorFlow.js and Docker for face detection
in web applications. It highlighted the ease of running containerized
TensorFlow.js applications, and developing with Docker Compose for real-time
code changes. Additionally, it covered how sharing your Docker image on Docker
Hub can streamline deployment for others, enhancing the application's reach
within the developer community.

Related information:

- [TensorFlow.js website](https://www.tensorflow.org/js)
- [MediaPipe website](https://developers.google.com/mediapipe/)
- [Dockerfile reference](/reference/dockerfile/)
- [Compose file reference](/reference/compose-file/_index.md)
- [Docker CLI reference](/reference/cli/docker/)
- [Docker Blog: Accelerating Machine Learning with TensorFlow.js](https://www.docker.com/blog/accelerating-machine-learning-with-tensorflow-js-using-pretrained-models-and-docker/)
