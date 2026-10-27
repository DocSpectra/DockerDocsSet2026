---
title: "Install Docker Desktop on Mac from the command line"
---

Before installing, review [Mac requirements](mac-requirements.md), [Mac permission requirements](mac-permission-requirements.md), and [installation preparation](mac-preparation.md).

{{< button text="Docker Desktop for Mac with Apple silicon" url="https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64" >}}
{{< button text="Docker Desktop for Mac with Intel chip" url="https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-amd64" >}}

*For checksums, see [Release notes](/manuals/desktop/release-notes.md).*

## Install from the command line

After downloading `Docker.dmg` from either the download buttons at the top of the page or from the [release notes](/manuals/desktop/release-notes.md), run the following commands in a terminal to install Docker Desktop in the **Applications** folder:

```console
$ sudo hdiutil attach Docker.dmg
$ sudo /Volumes/Docker/Docker.app/Contents/MacOS/install
$ sudo hdiutil detach /Volumes/Docker
```

By default, Docker Desktop is installed at `/Applications/Docker.app`. As macOS typically performs security checks the first time an application is used, the `install` command can take several minutes to run.


## Installer flags

See [Mac installer flags](installer-options.md#mac-installer-flags).
