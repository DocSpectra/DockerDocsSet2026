---
title: Test and lint the Bake example project
---

Before following this task, see [Set up the Bake example project](project-setup.md).

For shared procedure and context, see [Bake targets](/manuals/build/bake/targets.md) and
[Cache mounts](/manuals/build/cache/optimize.md#use-cache-mounts).

## Testing and linting

Bake isn't just for defining build configurations and running builds. You can
also use Bake to run your tests, effectively using BuildKit as a task runner.
Running your tests in containers is great for ensuring reproducible results.
This section shows how to add two types of tests:

- Unit testing with `go test`.
- Linting for style violations with `golangci-lint`.

In Test-Driven Development (TDD) fashion, start by adding a new `test` target
to the Bake file:

```hcl
target "test" {
  target = "test"
  output = ["type=cacheonly"]
}
```

> [!TIP]
> Using `type=cacheonly` ensures that the build output is effectively
> discarded; the layers are saved to BuildKit's cache, but Buildx will not
> attempt to load the result to the Docker Engine's image store.
>
> For test runs, you don't need to export the build output — only the test
> execution matters.

To execute this Bake target, run `docker buildx bake test`. At this time,
you'll receive an error indicating that the `test` stage does not exist in the
Dockerfile.

```console
$ docker buildx bake test
[+] Building 1.2s (6/6) FINISHED
 => [internal] load local bake definitions
...
ERROR: failed to solve: target stage "test" could not be found
```

To satisfy this target, add the corresponding Dockerfile target. The `test`
stage here is based on the same base stage as the build stage.

```dockerfile
FROM base AS test
RUN --mount=target=. \
    --mount=type=cache,target=/go/pkg/mod \
    go test .
```

> [!TIP]
> The [`--mount=type=cache` directive](/manuals/build/cache/optimize.md#use-cache-mounts)
> caches Go modules between builds, improving build performance by avoiding the
> need to re-download dependencies. This shared cache ensures that the same
> dependency set is available across build, test, and other stages.

Now, running the `test` target with Bake will evaluate the unit tests for this
project. If you want to verify that it works, you can make an arbitrary change
to `main_test.go` to cause the test to fail.

Next, to enable linting, add another target to the Bake file, named `lint`:

```hcl
target "lint" {
  target = "lint"
  output = ["type=cacheonly"]
}
```

And in the Dockerfile, add the build stage. This stage will use the official
`golangci-lint` image on Docker Hub.

> [!TIP]
> Because this stage relies on executing an external dependency, it's generally
> a good idea to define the version you want to use as a build argument. This
> lets you more easily manage version upgrades in the future by collocating
> dependency versions to the beginning of the Dockerfile.

```dockerfile {hl_lines=[2,"6-8"]}
ARG GO_VERSION="1.23"
ARG GOLANGCI_LINT_VERSION="1.61"

#...

FROM golangci/golangci-lint:v${GOLANGCI_LINT_VERSION}-alpine AS lint
RUN --mount=target=.,rw \
    golangci-lint run
```

Lastly, to enable running both tests simultaneously, you can use the `groups`
construct in the Bake file. A group can specify multiple targets to run with a
single invocation.

```hcl
group "validate" {
  targets = ["test", "lint"]
}
```

Now, running both tests is as simple as:

```console
$ docker buildx bake validate
```


