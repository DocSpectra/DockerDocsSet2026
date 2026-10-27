---
title: Troubleshoot Docker Offload
linktitle: Troubleshoot
weight: 800
description: Learn how to troubleshoot issues with Docker Offload.
keywords: cloud, troubleshooting, cloud mode, Docker Desktop, cloud builder, usage
tags: [Troubleshooting]
---

{{< summary-bar feature_name="Docker Offload" >}}

## Before you begin

See [Docker Offload prerequisites and access requirements](requirements.md), including connection requirements and the minimum Docker Desktop version.

## Diagnose builds, containers, and sessions

Docker Desktop uses Offload to run both builds and containers in the cloud.
If builds or containers are failing to run, falling back to local, or reporting
session errors, use the following steps to help resolve the issue.

1. Ensure Docker Offload is enabled in Docker Desktop: follow [Configure settings in Docker Desktop](configuration.md#configure-settings-in-docker-desktop) and ensure that **Enable Docker Offload** is toggled on.

2. Use the following command to check if the connection is active:

   ```console
   $ docker offload status
   ```

3. To get more information, run the following command:

   ```console
   $ docker offload diagnose
   ```

4. If you're not connected, start a new session:

   ```console
   $ docker offload start
   ```

5. Verify authentication with `docker login`.

6. If needed, you can sign out and then sign in again:

   ```console
   $ docker logout
   $ docker login
   ```

7. Verify your usage. For more information, see [Docker Offload usage](/offload/usage/).