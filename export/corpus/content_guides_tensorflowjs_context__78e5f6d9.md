---
title: TensorFlow.js, Docker, and browser backends
description: TensorFlow.js context and the WASM, WebGL, and CPU backends.
---

## What is TensorFlow.js?

[TensorFlow.js](https://www.tensorflow.org/js) is an open-source JavaScript
library for machine learning that enables you to train and deploy ML models in
the browser or on Node.js. It supports creating new models from scratch or using
pre-trained models, facilitating a wide range of ML applications directly in web
environments. TensorFlow.js offers efficient computation, making sophisticated
ML tasks accessible to web developers without deep ML expertise.

## Why Use TensorFlow.js and Docker together?

- Environment consistency and simplified deployment: Docker packages
  TensorFlow.js applications and their dependencies into containers, ensuring
  consistent runs across all environments and simplifying deployment.
- Efficient development and easy scaling: Docker enhances development efficiency
  with features like hot reloading and facilitates easy scaling of -
  TensorFlow.js applications using orchestration tools like Kubernetes.
- Isolation and enhanced security: Docker isolates TensorFlow.js applications in
  secure environments, minimizing conflicts and security vulnerabilities while
  running applications with limited permissions.

## Browser backends

In the context of TensorFlow.js or similar web-based machine learning
frameworks, the WASM, WebGL, and CPU backends can be used to
execute operations. Each of these backends utilizes different resources and
technologies available in modern browsers and has its strengths and limitations.
The following sections are a brief breakdown of the different backends.

### WASM

WebAssembly (WASM) is a low-level, assembly-like language with a compact binary
format that runs at near-native speed in web browsers. It allows code written in
languages like C/C++ to be compiled into a binary that can be executed in the
browser.

It's a good choice when high performance is required, and either the WebGL
backend is not supported or you want consistent performance across all devices
without relying on the GPU.

### WebGL

WebGL is a browser API that allows for GPU-accelerated usage of physics and
image processing and effects as part of the web page canvas.

WebGL is well-suited for operations that are parallelizable and can
significantly benefit from GPU acceleration, such as matrix multiplications and
convolutions commonly found in deep learning models.

### CPU

The CPU backend uses pure JavaScript execution, utilizing the device's central
processing unit (CPU). This backend is the most universally compatible and
serves as a fallback when neither WebGL nor WASM backends are available or
suitable.

