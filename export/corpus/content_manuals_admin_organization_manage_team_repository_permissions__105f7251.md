---
title: Team repository access
description: Configure repository access for teams and review permission levels.
---

## Set team repository permissions

You must create a team before you are able to configure repository permissions.

To set team repository permissions:

1. Sign in to [Docker Hub](https://hub.docker.com).
1. Select **My Hub** > **Repositories**.

   A list of your repositories appears.

1. Select a repository.

   The **General** page for the repository appears.

1. Select the **Permissions** tab.
1. Add, modify, or remove a team's repository permissions.
   - Add: Specify the **Team**, select the **Permission**, and then select **Add**.
   - Modify: Specify the new permission next to the team.
   - Remove: Select the **Remove permission** icon next to the team.

### Permissions reference

- `Read-only` access lets users view, search, and pull a private repository
  in the same way as they can a public repository.
- `Read & Write` access lets users pull, push, and view a repository. In
  addition, it lets users view, cancel, retry or trigger builds.
- `Admin` access lets users pull, push, view, edit, and delete a
  repository. You can also edit build settings and update the repository’s
  description, collaborator permissions, public/private visibility, and delete.

Permissions are cumulative. For example, if you have "Read & Write" permissions,
you automatically have "Read-only" permissions.

The following table shows what each permission level allows users to do:

|             Action              | Read-only | Read & Write | Admin |
| :-----------------------------: | :-------: | :----------: | :---: |
|        Pull a Repository        |    ✅     |      ✅      |  ✅   |
|        View a Repository        |    ✅     |      ✅      |  ✅   |
|        Push a Repository        |    ❌     |      ✅      |  ✅   |
|        Edit a Repository        |    ❌     |      ❌      |  ✅   |
|       Delete a Repository       |    ❌     |      ❌      |  ✅   |
| Update a Repository Description |    ❌     |      ❌      |  ✅   |
|           View Builds           |    ✅     |      ✅      |  ✅   |
|          Cancel Builds          |    ❌     |      ✅      |  ✅   |
|          Retry Builds           |    ❌     |      ✅      |  ✅   |
|         Trigger Builds          |    ❌     |      ✅      |  ✅   |
|       Edit Build Settings       |    ❌     |      ❌      |  ✅   |

> [!NOTE]
>
> A user who hasn't verified their email address only has `Read-only` access to
> the repository, regardless of the rights their team membership has given them.

