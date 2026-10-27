---
title: Commit a container
---

## Before you start

- [Install Docker and the SDKs](install.md).
- [Choose an API version](../versioning.md#choose-an-api-version).
- [Review Unix socket and cURL requirements](../http-socket.md).

## Example

Commit a container to create an image from its contents:

{{< tabs group="lang" >}}
{{< tab name="Go" >}}

```go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/moby/moby/api/types/container"
	"github.com/moby/moby/client"
)

func main() {
	ctx := context.Background()
	apiClient, err := client.New(client.FromEnv, client.WithUserAgent("my-application/1.0.0"))
	if err != nil {
		log.Fatal(err)
	}
	defer apiClient.Close()

	createResp, err := apiClient.ContainerCreate(ctx, client.ContainerCreateOptions{
		Config: &container.Config{
			Cmd: []string{"touch", "/helloworld"},
		},
		Image: "alpine",
	})
	if err != nil {
		log.Fatal(err)
	}

	if _, err := apiClient.ContainerStart(ctx, createResp.ID, client.ContainerStartOptions{}); err != nil {
		log.Fatal(err)
	}

	wait := apiClient.ContainerWait(ctx, createResp.ID, client.ContainerWaitOptions{})
	select {
	case err := <-wait.Error:
		if err != nil {
			log.Fatal(err)
		}
	case <-wait.Result:
	}

	commitResp, err := apiClient.ContainerCommit(ctx, createResp.ID, client.ContainerCommitOptions{Reference: "helloworld"})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(commitResp.ID)
}
```

{{< /tab >}}
{{< tab name="Python" >}}

```python
import docker
client = docker.from_env()
container = client.containers.run("alpine", ["touch", "/helloworld"], detach=True)
container.wait()
image = container.commit("helloworld")
print(image.id)
```

{{< /tab >}}
{{< tab name="HTTP" >}}

```console
$ docker run -d alpine touch /helloworld
0888269a9d584f0fa8fc96b3c0d8d57969ceea3a64acf47cd34eebb4744dbc52
$ curl --unix-socket /var/run/docker.sock\
  -X POST "http://localhost/v{{% param "latest_engine_api_version" %}}/commit?container=0888269a9d&repo=helloworld"
{"Id":"sha256:6c86a5cd4b87f2771648ce619e319f3e508394b5bfc2cdbd2d60f59d52acda6c"}
```

{{< /tab >}}
{{< /tabs >}}
