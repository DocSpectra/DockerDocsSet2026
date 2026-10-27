---
title: Stop all running containers
---

## Before you start

- [Install Docker and the SDKs](install.md).
- [Choose an API version](../versioning.md#choose-an-api-version).
- [Review Unix socket and cURL requirements](../http-socket.md).

> [!NOTE]
>
> Don't run this on a production server. Also, if you're' using swarm
> services, the containers stop, but Docker creates new ones to keep
> the service running in its configured state.

## Example

Now that you know what containers exist, you can perform operations on them.
This example stops all running containers.

{{< tabs group="lang" >}}
{{< tab name="Go" >}}

```go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/moby/moby/client"
)

func main() {
	ctx := context.Background()
	apiClient, err := client.New(client.FromEnv, client.WithUserAgent("my-application/1.0.0"))
	if err != nil {
		log.Fatal(err)
	}
	defer apiClient.Close()

	containers, err := apiClient.ContainerList(ctx, client.ContainerListOptions{})
	if err != nil {
		log.Fatal(err)
	}

	for _, container := range containers.Items {
		fmt.Print("Stopping container ", container.ID[:10], "... ")
		noWaitTimeout := 0 // to not wait for the container to exit gracefully
		if _, err := apiClient.ContainerStop(ctx, container.ID, client.ContainerStopOptions{Timeout: &noWaitTimeout}); err != nil {
			log.Fatal(err)
		}
		fmt.Println("Success")
	}
}
```

{{< /tab >}}
{{< tab name="Python" >}}

```python
import docker
client = docker.from_env()
for container in client.containers.list():
  container.stop()
```

{{< /tab >}}
{{< tab name="HTTP" >}}

```console
$ curl --unix-socket /var/run/docker.sock http://localhost/v{{% param "latest_engine_api_version" %}}/containers/json
[{
  "Id":"ae63e8b89a26f01f6b4b2c9a7817c31a1b6196acf560f66586fbc8809ffcd772",
  "Names":["/tender_wing"],
  "Image":"bfirsh/reticulate-splines",
  ...
}]

$ curl --unix-socket /var/run/docker.sock \
  -X POST http://localhost/v{{% param "latest_engine_api_version" %}}/containers/ae63e8b89a26/stop
```

{{< /tab >}}
{{< /tabs >}}
