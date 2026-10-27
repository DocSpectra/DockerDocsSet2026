---
title: Explore the Builds view in Docker Desktop
linkTitle: Builds
description: Understand how to use the Builds view in Docker Desktop
keywords: Docker Dashboard, manage, gui, dashboard, builders, builds
weight: 40
---

The **Builds** view provides an interactive interface for inspecting build history, monitoring active builds, and managing builders directly in Docker Desktop.

By default, the **Build history** tab displays a list of completed builds, sorted by date (newest first). Switch to the **Active builds** tab to view ongoing builds.

If you're connected to a cloud builder through [Docker Build Cloud](../../build-cloud/_index.md),
the Builds view also lists any active or completed cloud builds by other team members
connected to the same cloud builder.

> [!NOTE]
>
> Windows container image builds use the legacy builder and do not appear in the **Builds** view. Only BuildKit-powered builds are shown here.

## Show build list

Open the **Builds** view from the Docker Dashboard to access:

- **Build history**: Completed builds with access to logs, dependencies, traces, and more
- **Active builds**: Builds currently in progress

Only builds from active, running builders are listed. Builds from removed or stopped builders are not shown.

### Builder settings

The top-right corner shows the name of your currently selected builder, and the
**Builder settings** button lets you [manage builders](#manage-builders) in the
Docker Desktop settings.

### Import builds

The **Import builds** button lets you import build records for builds by other
people, or builds in a CI environment. When you've imported a build record, it
gives you full access to the logs, traces, and other data for that build,
directly in Docker Desktop. 

The [build summary](/manuals/build/ci/github-actions/build-summary.md)
for the `docker/build-push-action` and `docker/bake-action` GitHub Actions
includes a link to download the build records, for inspecting CI jobs with
Docker Desktop.

## Inspect builds

To inspect a build, select the build that you want to view in the list.
The inspection view contains a number of tabs.

See [Build inspection tabs and metrics](build-inspection-reference.md) for the **Info**, **Source**, **Error**, **Logs**, and **History** tabs.

### Build timing

See [Build timing](build-inspection-reference.md#build-timing).

### Build dependencies

See [Build dependencies](build-inspection-reference.md#build-dependencies).

### Arguments, secrets, and other parameters

See [Arguments, secrets, and other parameters](build-inspection-reference.md#arguments-secrets-and-other-parameters).

### Outputs and artifacts

See [Outputs and artifacts](build-inspection-reference.md#outputs-and-artifacts).

### Dockerfile source and errors

See [Dockerfile source and errors](build-inspection-reference.md#dockerfile-source-and-errors).

### Build logs

See [Build logs](build-inspection-reference.md#build-logs).

### Build history

See [Build history](build-inspection-reference.md#build-history).

## Inspect build traces with Jaeger

See [Inspect a build trace with Jaeger](build-traces.md).

## Manage builders

The **Builder** tab in **Settings** lets you:

- Inspect the state and configuration of active builders
- Start and stop a builder
- Delete build history
- Add or remove builders (or connect and disconnect, in the case of cloud builders)

For more information about managing builders, see [Change settings](/manuals/desktop/settings-and-maintenance/builders.md)
