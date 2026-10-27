---
title: Pull an image with authentication
---

## Before you start

- [Install Docker and the SDKs](install.md).
- [Choose an API version](../versioning.md#choose-an-api-version).
- [Review Unix socket and cURL requirements](../http-socket.md).

## Example

Pull an image, like `docker pull`, with authentication:

> [!NOTE]
>
> Credentials are sent in the clear. Docker's official registries use
> HTTPS. Private registries should also be configured to use HTTPS.

{{< tabs group="lang" >}}
{{< tab name="Go" >}}

```go
package main

import (
	"context"
	"io"
	"log"
	"os"

	"github.com/moby/moby/api/pkg/authconfig"
	"github.com/moby/moby/api/types/registry"
	"github.com/moby/moby/client"
)

func main() {
	ctx := context.Background()
	apiClient, err := client.New(client.FromEnv, client.WithUserAgent("my-application/1.0.0"))
	if err != nil {
		log.Fatal(err)
	}
	defer apiClient.Close()

	authStr, err := authconfig.Encode(registry.AuthConfig{
		Username: "username",
		Password: "password",
	})
	if err != nil {
		log.Fatal(err)
	}

	out, err := apiClient.ImagePull(ctx, "alpine", client.ImagePullOptions{RegistryAuth: authStr})
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()

	io.Copy(os.Stdout, out)
}
```

{{< /tab >}}
{{< tab name="Python" >}}

The Python SDK retrieves authentication information from the [credentials
store](/reference/cli/docker/login/#credential-stores) file and
integrates with [credential
helpers](https://github.com/docker/docker-credential-helpers). It's possible to override these credentials, but that's out of
scope for this example guide. After using `docker login`, the Python SDK
uses these credentials automatically.

```python
import docker
client = docker.from_env()
image = client.images.pull("alpine")
print(image.id)
```

{{< /tab >}}
{{< tab name="HTTP" >}}

This example leaves the credentials in your shell's history, so consider
this a naive implementation. The credentials are passed as a Base-64-encoded
JSON structure.

```console
$ JSON=$(echo '{"username": "string", "password": "string", "serveraddress": "string"}' | base64)

$ curl --unix-socket /var/run/docker.sock \
  -H "Content-Type: application/tar"
  -X POST "http://localhost/v{{% param "latest_engine_api_version" %}}/images/create?fromImage=alpine"
  -H "X-Registry-Auth"
  -d "$JSON"
{"status":"Pulling from library/alpine","id":"3.1"}
{"status":"Pulling fs layer","progressDetail":{},"id":"8f13703509f7"}
{"status":"Downloading","progressDetail":{"current":32768,"total":2244027},"progress":"[\u003e                                                  ] 32.77 kB/2.244 MB","id":"8f13703509f7"}
...
```

{{< /tab >}}
{{< /tabs >}}
