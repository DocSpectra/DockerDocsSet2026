---
title: Install Docker Desktop from the Microsoft Store on Windows
linkTitle: MS Store
description: Install Docker Desktop for Windows through the Microsoft Store. Understand its update behavior and limitations. 
keywords: microsoft store, windows, docker desktop, install, deploy, configure, admin, mdm, intune, winget
tags: [admin]
weight: 30
aliases: 
 - /desktop/setup/install/enterprise-deployment/ms-store/
---

You can deploy Docker Desktop for Windows through the [Microsoft app store](https://apps.microsoft.com/detail/xp8cbj40xlbwkx?hl=en-GB&gl=GB).

The Microsoft Store version of Docker Desktop provides the same functionality as the standard installer but has a different update behavior depending on whether your developers install it themselves or if installation is handled by an MDM tool such as Intune. This is described in the following section. 

Choose the installation method that best aligns with your environment's requirements and management practices.

## Update behavior

Review [Microsoft Store update behavior](installer-updates.md#microsoft-store-installations) for developer-managed and Intune-managed installations.

## WSL considerations

Docker Desktop for Windows integrates closely with WSL. When updating Docker Desktop installed from the Microsoft Store:
- Make sure you have quit Docker Desktop and that it is no longer running so updates can complete successfully
- In some environments, virtual hard disk (VHDX) file locks may prevent the update from completing.

## Recommendations for Intune management

If using Intune to manage Docker Desktop for Windows:
- Ensure your Intune policies are configured to handle application updates
- Be aware that the update process uses WinGet APIs rather than direct Store mechanisms
- Consider testing the update process in a controlled environment to verify proper functionality
