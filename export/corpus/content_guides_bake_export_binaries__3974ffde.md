---
title: Export local and cross-platform binaries with Bake
---

Before following this task, see [Set up the Bake example project](project-setup.md).

For the shared procedures and context, see [Local exporter](/manuals/build/exporters/local-tar.md),
[Inheritance](/manuals/build/bake/inheritance.md), and [Matrices](/manuals/build/bake/matrices.md).

## Exporting build artifacts

Exporting build artifacts like binaries can be useful for deploying to
environments without Docker or Kubernetes. For example, if your programs are
meant to be run on a user's local machine.

> [!TIP]
> The techniques discussed in this section can be applied not only to build
> output like binaries, but to any type of artifacts, such as test reports.

With programming languages like Go and Rust where the compiled binaries are
usually portable, creating alternate build targets for exporting only the
binary is trivial. All you need to do is add an empty stage in the Dockerfile
containing nothing but the binary that you want to export.

First, let's add a quick way to build a binary for your local platform and
export it to `./build/local` on the local filesystem.

In the `docker-bake.hcl` file, create a new `bin` target. In this stage, set
the `output` attribute to a local filesystem path. Buildx automatically detects
that the output looks like a filepath, and exports the results to the specified
path using the [local exporter](/manuals/build/exporters/local-tar.md).

```hcl
target "bin" {
  target = "bin"
  output = ["build/bin"]
  platforms = ["local"]
}
```

Notice that this stage specifies a `local` platform. By default, if `platforms`
is unspecified, builds target the OS and architecture of the BuildKit host. If
you're using Docker Desktop, this often means builds target `linux/amd64` or
`linux/arm64`, even if your local machine is macOS or Windows, because Docker
runs in a Linux VM. Using the `local` platform forces the target platform to
match your local environment.

Next, add the `bin` stage to the Dockerfile which copies the compiled binary
from the build stage.

```dockerfile
FROM scratch AS bin
COPY --from=build "/usr/bin/bakeme" /
```

Now you can export your local platform version of the binary with `docker
buildx bake bin`. For example, on macOS, this build target generates an
executable in the [Mach-O format](https://en.wikipedia.org/wiki/Mach-O) — the
standard executable format for macOS.

```console
$ docker buildx bake bin
$ file ./build/bin/bakeme
./build/bin/bakeme: Mach-O 64-bit executable arm64
```

Next, let's add a target to build all of the platform variants of the program.
To do this, you can [inherit](/manuals/build/bake/inheritance.md) the `bin`
target that you just created, and extend it by adding the desired platforms.

```hcl
target "bin-cross" {
  inherits = ["bin"]
  platforms = [
    "linux/amd64",
    "linux/arm64",
    "linux/riscv64",
  ]
}
```

Now, building the `bin-cross` target creates binaries for all platforms.
Subdirectories are automatically created for each variant.

```console
$ docker buildx bake bin-cross
$ tree build/
build/
└── bin
    ├── bakeme
    ├── linux_amd64
    │   └── bakeme
    ├── linux_arm64
    │   └── bakeme
    └── linux_riscv64
        └── bakeme

5 directories, 4 files
```

To also generate "release" and "debug" variants, you can use a matrix. For the Dockerfile changes, see
[Configure build tags](build-tags.md). When using a matrix, you also need to
differentiate the output directory based on the matrix value, otherwise the
binary gets written to the same location for each matrix run.

```hcl
target "bin-all" {
  inherits = ["bin-cross"]
  matrix = {
    mode = ["release", "debug"]
  }
  name = "bin-${mode}"
  args = {
    BUILD_TAGS = mode
  }
  output = ["build/bin/${mode}"]
}
```

```console
$ rm -r ./build/
$ docker buildx bake bin-all
$ tree build/
build/
└── bin
    ├── debug
    │   ├── linux_amd64
    │   │   └── bakeme
    │   ├── linux_arm64
    │   │   └── bakeme
    │   └── linux_riscv64
    │       └── bakeme
    └── release
        ├── linux_amd64
        │   └── bakeme
        ├── linux_arm64
        │   └── bakeme
        └── linux_riscv64
            └── bakeme

10 directories, 6 files
```


