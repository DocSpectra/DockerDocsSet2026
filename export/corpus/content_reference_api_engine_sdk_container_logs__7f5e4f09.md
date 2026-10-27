---
title: Print the logs of a specific container
---

## Before you start

- [Install Docker and the SDKs](install.md).
- [Choose an API version](../versioning.md#choose-an-api-version).
- [Review Unix socket and cURL requirements](../http-socket.md).

You need to modify the code before running it to change the hard-coded ID of
the container to print the logs for.

## Example

You can also perform actions on individual containers. This example prints the
logs of a container given its ID.

{{< tabs group="lang" >}}
{{< tab name="Go" >}}

```go
package main

import (
	"context"
	"io"
	"log"
	"os"

	"github.com/moby/moby/client"
)

func main() {
	ctx := context.Background()
	apiClient, err := client.New(client.FromEnv, client.WithUserAgent("my-application/1.0.0"))
	if err != nil {
		log.Fatal(err)
	}
	defer apiClient.Close()

	options := client.ContainerLogsOptions{ShowStdout: true}
	// Replace this ID with a container that really exists
	out, err := apiClient.ContainerLogs(ctx, "f1064a8a4c82", options)
	if err != nil {
		log.Fatal(err)
	}

	io.Copy(os.Stdout, out)
}
```

{{< /tab >}}
{{< tab name="Python" >}}

```python
import docker
client = docker.from_env()
container = client.containers.get('f1064a8a4c82')
print(container.logs())
```

{{< /tab >}}
{{< tab name="HTTP" >}}

```console
$ curl --unix-socket /var/run/docker.sock "http://localhost/v{{% param "latest_engine_api_version" %}}/containers/ca5f55cdb/logs?stdout=1"
Reticulating spline 1...
Reticulating spline 2...
Reticulating spline 3...
Reticulating spline 4...
Reticulating spline 5...
```

{{< /tab >}}
{{< /tabs >}}
