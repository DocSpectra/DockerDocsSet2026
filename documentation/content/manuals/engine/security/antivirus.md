---
title: Antivirus software and Docker
description: General guidelines for using antivirus software with Docker
keywords: antivirus, security
---

## Docker commands hang during scanning

When antivirus software scans files used by Docker, these files may be locked
in a way that causes Docker commands to hang.

## Exclude the data directory and schedule scans

One way to reduce these problems is to add the Docker data directory
(`/var/lib/docker` on Linux, `%ProgramData%\docker` on Windows Server, or `$HOME/Library/Containers/com.docker.docker/` on Mac) to the
antivirus's exclusion list. However, this comes with the trade-off that viruses
or malware in Docker images, writable layers of containers, or volumes are not
detected. If you do choose to exclude Docker's data directory from background
virus scanning, you may want to schedule a recurring task that stops Docker,
scans the data directory, and restarts Docker.


For security context, see [Docker daemon attack surface](daemon-security.md).
