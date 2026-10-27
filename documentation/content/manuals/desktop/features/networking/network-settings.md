---
title: Networking mode and DNS settings for Mac and Windows
---

## Network how-tos for Mac and Windows

You can control how Docker handles container networking and DNS resolution to better support a range of environments — from IPv4-only to dual-stack and IPv6-only systems. These settings help prevent timeouts and connectivity issues caused by incompatible or misconfigured host networks.

You can set the following settings on the **Network** tab in the Docker Desktop Dashboard settings, or if you're an admin, with Settings Management via the [`admin-settings.json` file](/manuals/enterprise/security/hardened-desktop/settings-management/configure-json-file.md#networking), or the [Admin Console](/manuals/enterprise/security/hardened-desktop/settings-management/configure-admin-console.md)

> [!NOTE]
>
> These settings can be overridden on a per-network basis using CLI flags or Compose file options.

### Default networking mode

Choose the default IP protocol used when Docker creates new networks. This allows you to align Docker with your host’s network capabilities or organizational requirements, such as enforcing IPv6-only access.

| Mode                         | Description                                 |
| ---------------------------- | ------------------------------------------- |
| **Dual IPv4/IPv6 (default)** | Supports both IPv4 and IPv6. Most flexible. |
| **IPv4 only**                | Uses only IPv4 addressing.                  |
| **IPv6 only**                | Uses only IPv6 addressing.                  |

### DNS resolution behavior 

Control how Docker filters DNS records returned to containers, improving reliability in environments where only IPv4 or IPv6 is supported. This setting is especially useful for preventing apps from trying to connect using IP families that aren't actually available, which can cause avoidable delays or failures.

| Option                         | Description                                                                 |
| ------------------------------ | --------------------------------------------------------------------------- |
| **Auto (recommended)**         | Automatically filters unsupported record types. (A for IPv4, AAAA for IPv6) |
| **Filter IPv4 (A records)**    | Blocks IPv4 lookups. Only available in dual-stack mode.                     |
| **Filter IPv6 (AAAA records)** | Blocks IPv6 lookups. Only available in dual-stack mode.                     |
| **No filtering**               | Returns both A and AAAA records.                                            |

> [!IMPORTANT]
>
> Switching the default networking mode resets the DNS filter to Auto.
