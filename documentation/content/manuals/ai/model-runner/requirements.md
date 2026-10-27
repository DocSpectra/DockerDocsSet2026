---
title: Docker Model Runner platform requirements
description: Hardware, operating system, and driver requirements for Model Runner.
---

## Requirements

Docker Model Runner is supported on the following platforms:

{{< tabs >}}
{{< tab name="Windows">}}

Windows(amd64):
-  NVIDIA GPUs
-  NVIDIA drivers 576.57+

Windows(arm64):
- OpenCL for Adreno
- Qualcomm Adreno GPU (6xx series and later)

  > [!NOTE]
  > Some llama.cpp features might not be fully supported on the 6xx series.

{{< /tab >}}
{{< tab name="MacOS">}}

- Apple Silicon

{{< /tab >}}
{{< tab name="Linux">}}

Docker Engine only:

- Supports CPU, NVIDIA (CUDA), AMD (ROCm), and Vulkan backends
- Requires NVIDIA driver 575.57.08+ when using NVIDIA GPUs

{{< /tab >}}
{{</tabs >}}

