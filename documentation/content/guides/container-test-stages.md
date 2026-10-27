---
title: Test stages in Docker builds
description: Testing context, build-stage selection, and test output.
---

## Testing context

Testing is an essential part of modern software development. Testing can mean a
lot of things to different development teams. There are unit tests, integration
tests and end-to-end testing.

## Run tests during a build

The `CMD` instruction runs when the container runs, and the `RUN` instruction
runs when the image is being built. When using `RUN` to run tests, the build
will fail if the tests fail.

## Select a stage and view results

Use `--target` to target the test stage, `--progress plain` (or
`--progress=plain`) to view build output, and `--no-cache` to ensure the tests
always run.

For stage selection, see [Stop at a specific build stage](/manuals/build/building/multi-stage.md#stop-at-a-specific-build-stage).
