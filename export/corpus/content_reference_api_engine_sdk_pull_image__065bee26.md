---
title: Pull an image
---

## Before you start

- [Install Docker and the SDKs](install.md).
- [Choose an API version](../versioning.md#choose-an-api-version).
- [Review Unix socket and cURL requirements](../http-socket.md).

## Example

Pull an image, like `docker pull`:

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

	out, err := apiClient.ImagePull(ctx, "alpine", client.ImagePullOptions{})
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()

	io.Copy(os.Stdout, out)
}
```

{{< /tab >}}
{{< tab name="Python" >}}

```python
import docker
client = docker.from_env()
image = client.images.pull("alpine")
print(image.id)
```

{{< /tab >}}
{{< tab name="HTTP" >}}

```console
$ curl --unix-socket /var/run/docker.sock \
  -X POST "http://localhost/v{{% param "latest_engine_api_version" %}}/images/create?fromImage=alpine"
{"status":"Pulling from library/alpine","id":"3.1"}
{"status":"Pulling fs layer","progressDetail":{},"id":"8f13703509f7"}
{"status":"Downloading","progressDetail":{"current":32768,"total":2244027},"progress":"[\u003e                                                  ] 32.77 kB/2.244 MB","id":"8f13703509f7"}
...
```

{{< /tab >}}
{{< /tabs >}}
