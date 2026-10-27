---
title: Diagnose Docker Model Runner issues
description: View model logs, inspect requests and responses, and diagnose plugin discovery.
---

## Troubleshooting

### Display the logs

To troubleshoot issues, display the logs:

{{< tabs group="release" >}}
{{< tab name="From Docker Desktop">}}

Select **Models** and select the **Logs** tab.

![Screenshot showing the Models view.](./images/dmr-logs.png)

{{< /tab >}}
{{< tab name="From the Docker CLI">}}

Use the [`docker model logs` command](/reference/cli/docker/model/logs/).

{{< /tab >}}
{{< /tabs >}}

### Inspect requests and responses

Inspecting requests and responses helps you diagnose model-related issues.
For example, you can evaluate context usage to verify you stay within the model's context
window or display the full body of a request to control the parameters you are passing to your models
when developing with a framework.

In Docker Desktop, to inspect the requests and responses for each model:

1. Select **Models** and select the **Requests** tab. This view displays all the requests to all models:
   - The time the request was sent.
   - The model name and version
   - The prompt/request
   - The context usage
   - The time it took for the response to be generated.
1. Select one of the requests to display further details:
   - In the **Overview** tab, view the token usage, response metadata and generation speed, and the actual prompt and response.
   - In the **Request**  and **Response** tabs, view the full JSON payload of the request and the response.

> [!NOTE]
> You can also display the requests for a specific model when you select a model and then select the **Requests** tab.


## Known issues

### `docker model` is not recognised

If you run a Docker Model Runner command and see:

```text
docker: 'model' is not a docker command
```

It means Docker can't find the plugin because it's not in the expected CLI plugins directory.

To fix this, create a symlink so Docker can detect it:

```console
$ ln -s /Applications/Docker.app/Contents/Resources/cli-plugins/docker-model ~/.docker/cli-plugins/docker-model
```

Once linked, rerun the command.

