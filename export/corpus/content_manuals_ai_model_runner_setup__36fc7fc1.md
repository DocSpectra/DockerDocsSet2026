---
title: Enable and update Docker Model Runner
description: Enable Model Runner in Docker Desktop or install and update it in Docker Engine.
---

## Before you begin

Review the [platform requirements](requirements.md).

## Enable Docker Model Runner

You can enable DMR using Docker Desktop or Docker Engine. Follow the instructions below based on your setup.

### Docker Desktop

1. In the settings view, go to the **AI** tab.
1. Select the **Enable Docker Model Runner** setting.
1. If you use Windows with a supported NVIDIA GPU, you also see and can select
   **Enable GPU-backed inference**.
1. Optional: To enable TCP support, select **Enable host-side TCP support**.
   1. In the **Port** field, type the port you want to use.
   1. If you interact with Model Runner from a local frontend web app, in
      **CORS Allows Origins**, select the origins that Model Runner should
      accept requests from. An origin is the URL where your web app runs, for
      example `http://localhost:3131`.

You can now use the `docker model` command in the CLI and view and interact
with your local models in the **Models** tab in the Docker Desktop Dashboard.

### Docker Engine

1. Ensure you have installed [Docker Engine](/engine/install/).
1. Docker Model Runner is available as a package. To install it, run:

   {{< tabs >}}
   {{< tab name="Ubuntu/Debian">}}

   ```bash
   $ sudo apt-get update
   $ sudo apt-get install docker-model-plugin
   ```

   {{< /tab >}}
   {{< tab name="RPM-base distributions">}}

   ```bash
   $ sudo dnf update
   $ sudo dnf install docker-model-plugin
   ```

   {{< /tab >}}
   {{< /tabs >}}

1. Test the installation:

   ```bash
   $ docker model version
   $ docker model run ai/smollm2
   ```

> [!NOTE]
> TCP support is enabled by default for Docker Engine on port `12434`.

### Update DMR in Docker Engine

To update Docker Model Runner in Docker Engine, uninstall it with
[`docker model uninstall-runner`](/reference/cli/docker/model/uninstall-runner/)
then reinstall it:

```bash
docker model uninstall-runner --images && docker model install-runner
```

> [!NOTE]
> With the above command, local models are preserved.
> To delete the models during the upgrade, add the `--models` option to the
> `uninstall-runner` command.

