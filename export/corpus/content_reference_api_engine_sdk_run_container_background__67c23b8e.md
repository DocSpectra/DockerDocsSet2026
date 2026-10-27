---
title: Run a container in the background
---

## Before you start

- [Install Docker and the SDKs](install.md).
- [Choose an API version](../versioning.md#choose-an-api-version).
- [Review Unix socket and cURL requirements](../http-socket.md).

## Example

You can also run containers in the background, the equivalent of typing
`docker run -d bfirsh/reticulate-splines`:

{{< tabs group="lang" >}}
{{< tab name="Go" >}}

```go
package main

import (
	"context"
	"fmt"
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

	imageName := "bfirsh/reticulate-splines"

	out, err := apiClient.ImagePull(ctx, imageName, client.ImagePullOptions{})
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()

	io.Copy(os.Stdout, out)

	resp, err := apiClient.ContainerCreate(ctx, client.ContainerCreateOptions{
		Image: imageName,
	})
	if err != nil {
		log.Fatal(err)
	}

	if _, err := apiClient.ContainerStart(ctx, resp.ID, client.ContainerStartOptions{}); err != nil {
		log.Fatal(err)
	}

	fmt.Println(resp.ID)
}
```

{{< /tab >}}
{{< tab name="Python" >}}

```python
import docker
client = docker.from_env()
container = client.containers.run("bfirsh/reticulate-splines", detach=True)
print(container.id)
```

{{< /tab >}}
{{< tab name="HTTP" >}}

```console
$ curl --unix-socket /var/run/docker.sock -H "Content-Type: application/json" \
  -d '{"Image": "bfirsh/reticulate-splines"}' \
  -X POST http://localhost/v{{% param "latest_engine_api_version" %}}/containers/create
{"Id":"1c6594faf5","Warnings":null}

$ curl --unix-socket /var/run/docker.sock -X POST http://localhost/v{{% param "latest_engine_api_version" %}}/containers/1c6594faf5/start
```

{{< /tab >}}
{{< /tabs >}}
