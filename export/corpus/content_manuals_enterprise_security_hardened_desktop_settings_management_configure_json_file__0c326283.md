---
title: Configure Settings Management with a JSON file
linkTitle: Use a JSON file
description: Configure and enforce Docker Desktop settings using an admin-settings.json file
keywords: admin controls, settings management, configuration, enterprise, docker desktop, json file
weight: 10
aliases:
  - /desktop/hardened-desktop/settings-management/configure/
  - /security/for-admins/hardened-desktop/settings-management/configure/
  - /security/for-admins/hardened-desktop/settings-management/configure-json-file/
---

{{< summary-bar feature_name="Hardened Docker Desktop" >}}

Settings Management lets you configure and enforce Docker Desktop settings across your organization using an `admin-settings.json` file. This standardizes Docker Desktop environments and ensures consistent configurations for all users.

## Prerequisites

Before you begin, make sure you have:

- [Enforce sign-in](/manuals/enterprise/security/enforce-sign-in/_index.md) for
  your organization
- A Docker Business subscription

The presence of the `admin-settings.json` file enforces sign-in on Docker Desktop. This is intended for business features that require authentication.

Users must be signed in and part of a Docker Business organization. If either condition isn't met, the settings file is ignored.

## Step one: Create the settings file

Follow [Create and distribute admin-settings.json](settings-file-deployment.md).

## Step two: Configure settings

> [!TIP]
>
> For a complete list of available settings, their supported platforms, and which configuration methods they work with, see the [Settings reference](settings-reference.md).

Review the [locking and grouped-setting rules](json-file-reference.md#locking-and-grouped-settings).

### Example `admin-settings.json` file

The following sample is an `admin-settings.json` file with common enterprise settings configured. You can use this example as a template with the [`admin-settings.json` configurations](json-file-reference.md#admin-settingsjson-configurations):

```json {collapse=true}
{
  "configurationFileVersion": 2,
  "exposeDockerAPIOnTCP2375": {
    "locked": true,
    "value": false
  },
  "proxy": {
    "locked": true,
    "mode": "system",
    "http": "",
    "https": "",
    "exclude": [],
    "windowsDockerdPort": 65000,
    "enableKerberosNtlm": false,
    "pac": "",
    "embeddedPac": ""
  },
  "containersProxy": {
    "locked": true,
    "mode": "manual",
    "http": "",
    "https": "",
    "exclude": [],
    "pac": "",
    "embeddedPac": "",
    "transparentPorts": ""
  },
  "enhancedContainerIsolation": {
    "locked": true,
    "value": true,
    "dockerSocketMount": {
      "imageList": {
        "images": [
          "docker.io/localstack/localstack:*",
          "docker.io/testcontainers/ryuk:*"
        ]
      },
      "commandList": {
        "type": "deny",
        "commands": ["push"]
      }
    }
  },
  "linuxVM": {
    "wslEngineEnabled": {
      "locked": false,
      "value": false
    },
    "dockerDaemonOptions": {
      "locked": false,
      "value": "{\"debug\": false}"
    },
    "vpnkitCIDR": {
      "locked": false,
      "value": "192.168.65.0/24"
    }
  },
  "kubernetes": {
    "locked": false,
    "enabled": false,
    "showSystemContainers": false,
    "imagesRepository": ""
  },
  "windowsContainers": {
    "dockerDaemonOptions": {
      "locked": false,
      "value": "{\"debug\": false}"
    }
  },
  "disableUpdate": {
    "locked": false,
    "value": false
  },
  "analyticsEnabled": {
    "locked": false,
    "value": true
  },
  "extensionsEnabled": {
    "locked": true,
    "value": false
  },
  "scout": {
    "locked": false,
    "sbomIndexing": true,
    "useBackgroundIndexing": true
  },
  "allowBetaFeatures": {
    "locked": false,
    "value": false
  },
  "blockDockerLoad": {
    "locked": false,
    "value": true
  },
  "filesharingAllowedDirectories": [
    {
      "path": "$HOME",
      "sharedByDefault": true
    },
    {
      "path": "$TMP",
      "sharedByDefault": false
    }
  ],
  "useVirtualizationFrameworkVirtioFS": {
    "locked": true,
    "value": true
  },
  "useVirtualizationFrameworkRosetta": {
    "locked": true,
    "value": true
  },
  "useGrpcfuse": {
    "locked": true,
    "value": true
  },
  "displayedOnboarding": {
    "locked": true,
    "value": true
  },
  "desktopTerminalEnabled": {
    "locked": false,
    "value": false
  },
  "enableInference": {
    "locked": false,
    "value": true
  },
  "enableInferenceTCP": {
    "locked": false,
    "value": true
  },
  "enableInferenceTCPPort": {
    "locked": true,
    "value": 12434
  },
  "enableInferenceCORS": {
    "locked": true,
    "value": ""
  },
  "enableInferenceGPUVariant": {
    "locked": true,
    "value": true
  },
  "portBindingBehavior": {
    "locked": true,
    "value": "default-port-binding"
  }
}
```

## Step three: Apply the settings

Follow [Apply and inspect managed settings](apply-settings.md#apply-settings).

## `admin-settings.json` configurations

See the [JSON configuration tables](json-file-reference.md#admin-settingsjson-configurations).
