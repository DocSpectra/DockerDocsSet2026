---
title: Create and manage a team
linkTitle: Teams
weight: 20
description: Learn how to create and manage teams for your organization
keywords: docker, registry, teams, organizations, plans, Dockerfile, Docker
  Hub, docs, documentation, repository permissions, configure repository access, team management
aliases:
  - /docker-hub/manage-a-team/
  - /admin/organization/manage-a-team/
---

{{< summary-bar feature_name="Admin orgs" >}}

You can create teams for your organization in the Admin Console or Docker Hub,
and configure team repository access in Docker Hub.

A team is a group of Docker users that belong to an organization. An
organization can have multiple teams. An organization owner can create new
teams and add members to an existing team using their Docker ID or email
address. Members aren't required to be part of a team to be associated with an
organization.

The organization owner can add additional organization owners to help them
manage users, teams, and repositories in the organization by assigning them
the owner role.

## What is an organization owner?

An organization owner is an administrator who has the following permissions:

- Manage repositories and add team members to the organization
- Access private repositories, all teams, billing information, and
  organization settings
- Specify [permissions](#permissions-reference) for each team in the
  organization
- Enable [SSO](/manuals/enterprise/security/single-sign-on/_index.md) for the
  organization

When SSO is enabled for your organization, the organization owner can
also manage users. Docker can auto-provision Docker IDs for new end-users or
users who'd like to have a separate Docker ID for company use through SSO
enforcement.

Organization owners can add others with the owner role to help them
manage users, teams, and repositories in the organization.

For more information on roles, see
[Roles and permissions](/manuals/enterprise/security/roles-and-permissions/_index.md).

## Create a team

1. Sign in to [Docker Home](https://app.docker.com) and select your
   organization.
1. Select **Teams**.

## Set team repository permissions

Follow [Set team repository permissions](team-repository-permissions.md#set-team-repository-permissions).

### Permissions reference

See [Team repository permission levels](team-repository-permissions.md#permissions-reference), including cumulative permissions and the verified-email requirement.

## Delete a team

Organization owners can delete a team. When you remove a team from your
organization, this action revokes member access to the team's permitted
resources. It won't remove users from other teams that they belong to, and it
won't delete any resources.

1. Sign in to [Docker Home](https://app.docker.com/) and select your
   organization.
1. Select **Teams**.
1. Select the **Actions** icon next to the name of the team you want to delete.
1. Select **Delete team**.
1. Review the confirmation message, then select **Delete**.

## More resources

- [Video: Docker Teams](https://youtu.be/WKlT1O-4Du8?feature=shared&t=348)
- [Video: Roles, teams, and repositories](https://youtu.be/WKlT1O-4Du8?feature=shared&t=435)
