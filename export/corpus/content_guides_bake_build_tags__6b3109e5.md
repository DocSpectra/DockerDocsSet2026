---
title: Configure build tags in the Bake example Dockerfile
---

For the example project, see [Set up the Bake example project](project-setup.md).

Finally, update the Dockerfile to consume the `BUILD_TAGS` argument during the
compilation stage. When the `-tags="${BUILD_TAGS}"` option evaluates to
`-tags="debug"`, the compiler uses the `configureLogging` function in the
[`debug.go`](https://github.com/dvdksn/bakeme/blob/75c8a41e613829293c4bd3fc3b4f0c573f458f42/debug.go#L1)
file.

```diff {title=Dockerfile}
 # build compiles the program
 FROM base AS build
-ARG TARGETOS TARGETARCH
+ARG TARGETOS TARGETARCH BUILD_TAGS
 ENV GOOS=$TARGETOS
 ENV GOARCH=$TARGETARCH
 RUN --mount=target=. \
        --mount=type=cache,target=/go/pkg/mod \
-       go build -o "/usr/bin/bakeme" .
+       go build -tags="${BUILD_TAGS}" -o "/usr/bin/bakeme" .
```


