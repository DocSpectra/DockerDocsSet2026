---
title: Custom roles
description: Create tailored permission sets for your organization with custom roles
keywords: custom roles, permissions, access control, organization management, docker hub, admin console, security
---

{{< summary-bar feature_name="General admin" >}}

Custom roles allow you to create tailored permission sets that match your
organization's specific needs. This page covers custom roles and steps
to create and manage them.

## What are custom roles?

Custom roles let you create tailored permission sets for your organization. You
can assign custom roles to individual users or teams.
For the core/custom role and team permission rules, see [How roles work together](core-roles.md#how-roles-work-together).

Use custom roles when Docker's core roles don't fit your needs.

## Prerequisites

To configure custom roles, you need owner permissions in your Docker
organization.

## Create a custom role

Before you can assign a custom role to users, you must create one in the
Admin Console:

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Admin Console**.
3. Under **User management**, select **Roles** > **Create role**.
4. Create a name and describe what the role is for:
   - Provide a **Label**
   - Enter a unique **Name** identifier (can't be changed later)
   - Add an optional **Description**
5. Set permissions for the role by expanding permission categories and selecting
   the checkboxes for permissions. For a full list of available permissions, see
   the [custom roles permissions reference](custom-role-permissions.md).
6. Select **Review** to review your custom roles configuration and see a summary
   of selected permissions.
7. Select **Create**.

With a custom role created, you can now [assign custom roles to users](#assign-custom-roles).

## Edit a custom role

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Admin Console**.
3. Under **User management**, select **Roles**.
4. Find your custom role from the list, and select the **Actions menu**.
5. Select **Edit**.
6. You can edit the following custom role settings:
   - Label
   - Description
   - Permissions
7. After you have finished editing, select **Save**.

## Assign custom roles

{{< tabs >}}
{{< tab name="Individual users" >}}

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Members**.
3. Locate the member you want to assign a custom role to, then select the
   **Actions menu**.
4. In the drop-down, select **Change role**.
5. In the **Select a role** drop-down, select your custom role.
6. Select **Save**.

{{< /tab >}}
{{< tab name="Bulk users" >}}

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Members**.
3. Use the checkboxes in the username column to select all users you want
   to assign a custom role to.
4. Select **Change role**.
5. In the **Select a role** drop-down, select your custom role or a core role.
6. Select **Save**.

{{< /tab >}}
{{< tab name="Teams" >}}

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Teams**.
3. Locate the team you want to assign a custom role to, then select
   the **Actions menu**.
4. Select **Assign role**.
5. Select your custom role, then select **Assign**.

The role column will update to the newly assigned role.

{{< /tab >}}
{{< /tabs >}}

## View role assignments

To see which users and teams are assigned to roles:

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Admin Console**.
3. Under **User management**, select **Roles**.
4. In the roles list, view the **Users** and **Teams** columns to see
   assignment counts.
5. Select a specific role to view its permissions and assignments in detail.

## Reassign custom roles

{{< tabs >}}
{{< tab name="Individual users" >}}

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Members**.
3. Locate the member you want to reassign, then select the **Actions menu**.
4. Select **Change role**.
5. In the **Select a role** drop-down, select the new role.
6. Select **Save**.

{{< /tab >}}
{{< tab name="Bulk users" >}}

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Members**.
3. Use the checkboxes in the username column to select all users you want
   to reassign.
4. Select **Change role**.
5. In the **Select a role** drop-down, select the new role.
6. Select **Save**.

{{< /tab >}}
{{< tab name="Teams" >}}

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Teams**.
3. Locate the team, then select the **Actions menu**.
4. Select **Change role**.
5. In the pop-up window, select a role from the drop-down menu, then
   select **Save**.

{{< /tab >}}
{{< /tabs >}}

## Delete a custom role

Before deleting a custom role, you must reassign all users and teams to different roles.

1. Sign in to [Docker Home](https://app.docker.com).
2. Select **Admin Console**.
3. Under **User management**, select **Roles**.
4. Find your custom role from the list, and select the **Actions menu**.
5. If the role has assigned users or teams:
   - Navigate to the **Members** page and change the role for all users assigned to this custom role
   - Navigate to the **Teams** page and reassign all teams that have this custom role
6. Once no users or teams are assigned, return to **Roles**.
7. Find your custom role and select the **Actions menu**.
8. Select **Delete**.
9. In the confirmation window, select **Delete** to confirm.

## Custom roles permissions reference

See the [Custom role permissions reference](custom-role-permissions.md).
