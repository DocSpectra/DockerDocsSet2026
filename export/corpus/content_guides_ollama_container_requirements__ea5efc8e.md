---
title: GPU prerequisites for an Ollama container
description: GPU platform, performance, and driver prerequisites for the Ollama tutorial containers.
---

When running Ollama in a container, you should have a CUDA-supported GPU. While you can run Ollama in a container without a supported GPU, the performance may not be acceptable. Only Linux and Windows 11 support GPU access to containers.

## Install GPU prerequisites

- For Docker Engine on Linux, install the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit).
- For Docker Desktop on Windows 10/11, install the latest [NVIDIA driver](https://www.nvidia.com/Download/index.aspx) and make sure you are using the [WSL2 backend](/manuals/desktop/features/wsl/enable-wsl.md#turn-on-docker-desktop-wsl-2)
