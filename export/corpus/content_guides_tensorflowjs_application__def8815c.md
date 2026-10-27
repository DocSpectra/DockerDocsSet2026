---
title: TensorFlow.js face detection sample code
description: HTML, JavaScript, and WASM files in the face detection sample.
---

## Explore the application's code

Explore the purpose of each file and their contents in the following sections.

### The index.html file

The `index.html` file serves as the frontend for the web application that
utilizes TensorFlow.js for real-time face detection from the webcam video feed.
It incorporates several technologies and libraries to facilitate machine
learning directly in the browser. It uses several TensorFlow.js libraries,
including:

- tfjs-core and tfjs-converter for core TensorFlow.js functionality and model
  conversion.
- tfjs-backend-webgl, tfjs-backend-cpu, and the tf-backend-wasm script
  for different computational backend options that TensorFlow.js can use for
  processing. These backends allow the application to perform machine learning
  tasks efficiently by leveraging the user's hardware capabilities.
- The BlazeFace library, a TensorFlow model for face detection.

It also uses the following additional libraries:

- dat.GUI for creating a graphical interface to interact with the application's
  settings in real-time, such as switching between TensorFlow.js backends.
- Stats.min.js for displaying performance metrics (like FPS) to monitor the
  application's efficiency during operation.

{{< accordion title="index.html" >}}

```html
<style>
  body {
    margin: 25px;
  }

  .true {
    color: green;
  }

  .false {
    color: red;
  }

  #main {
    position: relative;
    margin: 50px 0;
  }

  canvas {
    position: absolute;
    top: 0;
    left: 0;
  }

  #description {
    margin-top: 20px;
    width: 600px;
  }

  #description-title {
    font-weight: bold;
    font-size: 18px;
  }
</style>

<body>
  <div id="main">
    <video
      id="video"
      playsinline
      style="
      -webkit-transform: scaleX(-1);
      transform: scaleX(-1);
      width: auto;
      height: auto;
      "
    ></video>
    <canvas id="output"></canvas>
    <video
      id="video"
      playsinline
      style="
      -webkit-transform: scaleX(-1);
      transform: scaleX(-1);
      visibility: hidden;
      width: auto;
      height: auto;
      "
    ></video>
  </div>
</body>
<script src="https://unpkg.com/@tensorflow/tfjs-core@2.1.0/dist/tf-core.js"></script>
<script src="https://unpkg.com/@tensorflow/tfjs-converter@2.1.0/dist/tf-converter.js"></script>

<script src="https://unpkg.com/@tensorflow/tfjs-backend-webgl@2.1.0/dist/tf-backend-webgl.js"></script>
<script src="https://unpkg.com/@tensorflow/tfjs-backend-cpu@2.1.0/dist/tf-backend-cpu.js"></script>
<script src="./tf-backend-wasm.js"></script>

<script src="https://unpkg.com/@tensorflow-models/blazeface@0.0.5/dist/blazeface.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.7.6/dat.gui.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/stats.js/r16/Stats.min.js"></script>
<script src="./index.js"></script>
```

{{< /accordion >}}

### The index.js file

The `index.js` file conducts the facial detection logic. It demonstrates several
advanced concepts in web development and machine learning integration. Here's a
breakdown of some of its key components and functionalities:

- Stats.js: The script starts by creating a Stats instance to monitor and
  display the frame rate (FPS) of the application in real time. This is helpful
  for performance analysis, especially when testing the impact of different
  TensorFlow.js backends on the application's speed.
- TensorFlow.js: The application allows users to switch between different
  computation backends (wasm, webgl, and cpu) for TensorFlow.js through a
  graphical interface provided by dat.GUI. Changing the backend can affect
  performance and compatibility depending on the device and browser. The
  addFlagLabels function dynamically checks and displays whether SIMD (Single
  Instruction, Multiple Data) and multithreading are supported, which are
  relevant for performance optimization in the wasm backend.
- setupCamera function: Initializes the user's webcam using the MediaDevices Web
  API. It configures the video stream to not include audio and to use the
  front-facing camera (facingMode: 'user'). Once the video metadata is loaded,
  it resolves a promise with the video element, which is then used for face
  detection.
- BlazeFace: The core of this application is the renderPrediction function,
  which performs real-time face detection using the BlazeFace model, a
  lightweight model for detecting faces in images. The function calls
  model.estimateFaces on each animation frame to detect faces from the video
  feed. For each detected face, it draws a red rectangle around the face and
  blue dots for facial landmarks on a canvas overlaying the video.

{{< accordion title="index.js" >}}

```javascript
const stats = new Stats();
stats.showPanel(0);
document.body.prepend(stats.domElement);

let model, ctx, videoWidth, videoHeight, video, canvas;

const state = {
  backend: "wasm",
};

const gui = new dat.GUI();
gui
  .add(state, "backend", ["wasm", "webgl", "cpu"])
  .onChange(async (backend) => {
    await tf.setBackend(backend);
    addFlagLabels();
  });

async function addFlagLabels() {
  if (!document.querySelector("#simd_supported")) {
    const simdSupportLabel = document.createElement("div");
    simdSupportLabel.id = "simd_supported";
    simdSupportLabel.style = "font-weight: bold";
    const simdSupported = await tf.env().getAsync("WASM_HAS_SIMD_SUPPORT");
    simdSupportLabel.innerHTML = `SIMD supported: <span class=${simdSupported}>${simdSupported}<span>`;
    document.querySelector("#description").appendChild(simdSupportLabel);
  }

  if (!document.querySelector("#threads_supported")) {
    const threadSupportLabel = document.createElement("div");
    threadSupportLabel.id = "threads_supported";
    threadSupportLabel.style = "font-weight: bold";
    const threadsSupported = await tf
      .env()
      .getAsync("WASM_HAS_MULTITHREAD_SUPPORT");
    threadSupportLabel.innerHTML = `Threads supported: <span class=${threadsSupported}>${threadsSupported}</span>`;
    document.querySelector("#description").appendChild(threadSupportLabel);
  }
}

async function setupCamera() {
  video = document.getElementById("video");

  const stream = await navigator.mediaDevices.getUserMedia({
    audio: false,
    video: { facingMode: "user" },
  });
  video.srcObject = stream;

  return new Promise((resolve) => {
    video.onloadedmetadata = () => {
      resolve(video);
    };
  });
}

const renderPrediction = async () => {
  stats.begin();

  const returnTensors = false;
  const flipHorizontal = true;
  const annotateBoxes = true;
  const predictions = await model.estimateFaces(
    video,
    returnTensors,
    flipHorizontal,
    annotateBoxes,
  );

  if (predictions.length > 0) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < predictions.length; i++) {
      if (returnTensors) {
        predictions[i].topLeft = predictions[i].topLeft.arraySync();
        predictions[i].bottomRight = predictions[i].bottomRight.arraySync();
        if (annotateBoxes) {
          predictions[i].landmarks = predictions[i].landmarks.arraySync();
        }
      }

      const start = predictions[i].topLeft;
      const end = predictions[i].bottomRight;
      const size = [end[0] - start[0], end[1] - start[1]];
      ctx.fillStyle = "rgba(255, 0, 0, 0.5)";
      ctx.fillRect(start[0], start[1], size[0], size[1]);

      if (annotateBoxes) {
        const landmarks = predictions[i].landmarks;

        ctx.fillStyle = "blue";
        for (let j = 0; j < landmarks.length; j++) {
          const x = landmarks[j][0];
          const y = landmarks[j][1];
          ctx.fillRect(x, y, 5, 5);
        }
      }
    }
  }

  stats.end();

  requestAnimationFrame(renderPrediction);
};

const setupPage = async () => {
  await tf.setBackend(state.backend);
  addFlagLabels();
  await setupCamera();
  video.play();

  videoWidth = video.videoWidth;
  videoHeight = video.videoHeight;
  video.width = videoWidth;
  video.height = videoHeight;

  canvas = document.getElementById("output");
  canvas.width = videoWidth;
  canvas.height = videoHeight;
  ctx = canvas.getContext("2d");
  ctx.fillStyle = "rgba(255, 0, 0, 0.5)";

  model = await blazeface.load();

  renderPrediction();
};

setupPage();
```

{{< /accordion >}}

### The tf-backend-wasm.js file

The `tf-backend-wasm.js` file is part of the
[TensorFlow.js library](https://github.com/tensorflow/tfjs/tree/master/tfjs-backend-wasm).
It contains initialization logic for the TensorFlow.js WASM backend, some
utilities for interacting with the WASM binaries, and functions to set custom
paths for the WASM binaries.

### The tfjs-backend-wasm-simd.wasm file

The `tfjs-backend-wasm-simd.wasm` file is part of the
[TensorFlow.js library](https://github.com/tensorflow/tfjs/tree/master/tfjs-backend-wasm).
It's a WASM binary that's used for the WebAssembly
backend, specifically optimized to utilize SIMD (Single Instruction, Multiple
Data) instructions.

