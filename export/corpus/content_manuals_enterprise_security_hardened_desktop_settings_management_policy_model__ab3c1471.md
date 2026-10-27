---
title: Settings Management policies and constraints
---

## Who should use Settings Management?

Settings Management is designed for organizations that:

- Need centralized control over Docker Desktop configurations
- Want to standardize Docker Desktop environments across teams
- Operate in regulated environments and must enforce compliance policies

## How Settings Management works

Administrators can define settings using one of these methods:

- Admin Console: Create and assign settings policies through the
  Docker Admin Console. This provides a web-based interface for managing settings
  across your organization.
- `admin-settings.json` file: Place a configuration file on the
  user's machine to enforce settings. This method works well for automated
  deployments and scripted installations.

Enforced settings override user-defined configurations and can't be modified by developers.

## Configurable settings

Settings Management supports a wide range of Docker Desktop features, including:

- Proxy configurations
- Network settings
- Container isolation options
- Registry access controls
- Resource limits
- Security policies
- Cloud policies

For a complete list of settings you can enforce, see the [Settings reference](/manuals/enterprise/security/hardened-desktop/settings-management/settings-reference.md).

## Policy precedence

When multiple policies exist, Docker Desktop applies them in this order:

1. User-specific policies: Highest priority
1. Organization default policy: Applied when no user-specific policy exists
1. Local `admin-settings.json` file: Lowest priority, overridden by Admin Console policies
1. [Configuration profiles](/manuals/enterprise/security/enforce-sign-in/mac-profiles.md): Super-set of Docker Admin Console policies.

## Developer experience

When settings are enforced:

- Settings options appear grayed out in Docker Desktop and can't be modified through the Dashboard, CLI, or configuration files
- If Enhanced Container Isolation is enabled, developers can't use privileged containers or similar methods to alter enforced settings within the Docker Desktop Linux VM

This ensures consistent environments while maintaining a clear visual indication of which settings are managed by administrators.

## Limitations

Settings Management has the following limitations:

- Doesn't work in air-gapped or offline environments
- Not compatible with environments that restrict authentication with Docker Hub
