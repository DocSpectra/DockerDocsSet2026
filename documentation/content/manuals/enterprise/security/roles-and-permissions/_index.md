---
title: Roles and permissions
linkTitle: Roles and permissions
description: Control access to content, registry, and organization management with Docker's role system
keywords: roles, permissions, custom roles, core roles, access control, organization management, docker hub, admin console, security
tags: [admin]
aliases:
  - /admin/organization/roles/
  - /security/for-admins/roles-and-permissions/
grid:
  - title: "Core roles"
    description: Learn about Docker's built-in Member, Editor, and Owner roles with predefined permissions.
    icon: "admin_panel_settings"
    link: /enterprise/security/roles-and-permissions/core-roles/
  - title: "Custom roles"
    description: Create tailored permission sets that match your organization's specific needs.
    icon: "tune"
    link: /enterprise/security/roles-and-permissions/custom-roles/
weight: 40
---

{{< summary-bar feature_name="General admin" >}}

Roles control what users can do in your Docker organization. When you invite users or create teams, you assign them roles that determine their permissions for repositories, teams, and organization settings.

Docker provides two types of roles to meet different organizational needs:

- [Core roles](/manuals/enterprise/security/roles-and-permissions/core-roles.md) with predefined permissions
- [Custom roles](/manuals/enterprise/security/roles-and-permissions/custom-roles.md) that you can tailor to your specific requirements

## Docker roles

### Core roles

For the Member, Editor, and Owner definitions and permission tables, see [Core roles](core-roles.md).

### Custom roles

Custom roles allow you to create tailored permission sets by selecting specific permissions from categories like user management, team management, billing, and Hub permissions. Use custom roles when Docker's core roles don't fit your needs.

## When to use each role

Use core roles when:

- Docker's predefined permission sets match your organizational structure
- You want simple, straightforward role assignments
- You're getting started with Docker organization management
- Your access control needs are standard and don't require fine-grained permissions

Use custom roles when:

- You need specific permission combinations not available in core roles
- You want to create specialized roles like billing administrators, security auditors, or repository managers
- You need department-specific access control
- You want to implement the principle of least privilege with precise permission grants

## How roles work together

See [How roles work together](core-roles.md#how-roles-work-together) for role and team permission rules.

## Next steps

Choose the role type that best fits your organization's needs:

{{< grid >}}
