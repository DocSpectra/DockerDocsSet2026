---
title: "Install Docker Desktop on Mac interactively"
---

Before installing, review [Mac requirements](mac-requirements.md), [Mac permission requirements](mac-permission-requirements.md), and [installation preparation](mac-preparation.md).

{{< button text="Docker Desktop for Mac with Apple silicon" url="https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64" >}}
{{< button text="Docker Desktop for Mac with Intel chip" url="https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-amd64" >}}

*For checksums, see [Release notes](/manuals/desktop/release-notes.md).*

## Install interactively

1. Download the installer using the download buttons at the top of the page, or from the [release notes](/manuals/desktop/release-notes.md).

2. Double-click `Docker.dmg` to open the installer, then drag the Docker icon to the **Applications** folder. By default, Docker Desktop is installed at `/Applications/Docker.app`.

3. Double-click `Docker.app` in the **Applications** folder to start Docker.

4. The Docker menu displays the Docker Subscription Service Agreement.

    Review the [Docker Desktop license agreement](/manuals/subscription/desktop-license.md) for free-use conditions, paid-subscription requirements, government use, and included subscriptions.

5. Select **Accept** to continue. 

   Note that Docker Desktop won't run if you do not agree to the terms. You can choose to accept the terms at a later date by opening Docker Desktop.

   For more information, see [Docker Desktop Subscription Service Agreement](https://www.docker.com/legal/docker-subscription-service-agreement). It is recommended that you also read the [FAQs](https://www.docker.com/pricing/faq).

6. From the installation window, select either: 
   - **Use recommended settings (Requires password)**. This lets Docker Desktop automatically set the necessary configuration settings. 
   - **Use advanced settings**. You can then set the location of the Docker CLI tools either in the system or user directory, enable the default Docker socket, and enable privileged port mapping. See [Settings](/manuals/desktop/settings-and-maintenance/settings.md#advanced), for more information and how to set the location of the Docker CLI tools.
7. Select **Finish**. If you have applied any of the previous configurations that require a password in step 6, enter your password to confirm your choice.
