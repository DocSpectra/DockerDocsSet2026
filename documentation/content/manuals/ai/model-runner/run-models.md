---
title: Pull and run a model
description: Pull and run models with the Docker Desktop Models view or the Docker CLI.
---

## Prerequisites

Review the [platform requirements](requirements.md) and [enable Docker Model Runner](setup.md#enable-docker-model-runner).

## Pull a model

Models are cached locally.

> [!NOTE]
>
> When you use the Docker CLI, you can also pull models directly from
> [HuggingFace](https://huggingface.co/).

{{< tabs group="release" >}}
{{< tab name="From Docker Desktop">}}

1. Select **Models** and select the **Docker Hub** tab.
1. Find the model you want and select **Pull**.

![Screenshot showing the Docker Hub view.](./images/dmr-catalog.png)

{{< /tab >}}
{{< tab name="From the Docker CLI">}}

Use the [`docker model pull` command](/reference/cli/docker/model/pull/).
For example:

```bash {title="Pulling from Docker Hub"}
docker model pull ai/smollm2:360M-Q4_K_M
```

```bash {title="Pulling from HuggingFace"}
docker model pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```

{{< /tab >}}
{{< /tabs >}}

## Run a model

{{< tabs group="release" >}}
{{< tab name="From Docker Desktop">}}

1. Select **Models** and select the **Local** tab.
1. Select the play button. The interactive chat screen opens.

![Screenshot showing the Local view.](./images/dmr-run.png)

{{< /tab >}}
{{< tab name="From the Docker CLI" >}}

Use the [`docker model run` command](/reference/cli/docker/model/run/).

{{< /tab >}}
{{< /tabs >}}

