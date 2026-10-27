---
title: Binary installation caveats and upgrades
---

> [!IMPORTANT]
>
> This page contains information on how to install Docker using binaries. These
> instructions are mostly suitable for testing purposes. We do not recommend
> installing Docker using binaries in production environments as they don't have automatic security updates. The Linux binaries described on this
> page are statically linked, which means that vulnerabilities in build-time
> dependencies are not automatically patched by security updates of your Linux
> distribution.
>
> Updating binaries is also slightly more involved when compared to Docker packages
> installed using a package manager or through Docker Desktop, as it requires
> (manually) updating the installed version whenever there is a new release of
> Docker.
>
> Also, static binaries may not include all functionalities provided by the dynamic
> packages.
>
> On Windows and Mac, we recommend that you install [Docker Desktop](/manuals/desktop/_index.md)
> instead. For Linux, we recommend that you follow the instructions specific for
> your distribution.

If you want to try Docker or use it in a testing environment, but you're not on
a supported platform, you can try installing from static binaries. If possible,
you should use packages built for your operating system, and use your operating
system's package management system to manage Docker installation and upgrades.

Static binaries for the Docker daemon binary are only available for Linux (as
`dockerd`) and Windows (as `dockerd.exe`).
Static binaries for the Docker client are available for Linux, Windows, and macOS (as `docker`).

## Upgrade static binaries {#upgrade-static-binaries}

To upgrade your manual installation of Docker Engine, first stop any
`dockerd` or `dockerd.exe`  processes running locally, then follow the
regular installation steps to install the new version on top of the existing
version.

