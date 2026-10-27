---
title: Group mapping behavior, naming, and attributes
---

Group mapping automatically synchronizes user groups from your identity provider (IdP) with teams in your Docker organization. For example, when you add a developer to the "backend-team" group in your IdP, they're automatically added to the corresponding team in Docker

This page explains how group mapping works, and how to set up group mapping.

> [!TIP]
>
> Group mapping is ideal for adding users to multiple organizations or multiple teams within one organization. If you don't need to set up multi-organization or multi-team assignment, SCIM [user-level attributes](role-mapping.md) may be a better fit for your needs.

## How group mapping works

Group mapping keeps your Docker Teams synchronized with your IdP groups through these key components:

- Authentication flow: When users sign in through SSO, your IdP shares user attributes with Docker including email, name, and group memberships.
- Automatic updates: Docker uses these attributes to create or update user profiles and manage team assignments based on IdP group changes.
- Unique identification: Docker uses email addresses as unique identifiers, so each Docker account must have a unique email address.
- Team synchronization: Users' team memberships in Docker automatically reflect changes made in your IdP groups.

## Set up group mapping

Group mapping setup involves configuring your identity provider to share group
information with Docker. This requires:

- Creating groups in your IdP using Docker's naming format
- Configuring attributes so your IdP sends group data during authentication
- Adding users to the appropriate groups
- Testing the connection to ensure groups sync properly

You can use group mapping with SSO only, or with both SSO and SCIM for enhanced
user lifecycle management.

### Group naming format

Create groups in your IdP using the format: `organization:team`.

For example:

- For the "developers" team in the "moby" organization: `moby:developers`
- For multi-organization access: `moby:backend` and `whale:desktop`

Docker creates teams automatically if they don't already exist when groups sync.

### Supported attributes

| Attribute | Description |
|:--------- | :---------- |
| `id` | Unique ID of the group in UUID format. This attribute is read-only. |
| `displayName` | Name of the group following the group mapping format: `organization:team`. |
| `members` | A list of users that are members of this group. |
| `members(x).value` | Unique ID of the user that is a member of this group. Members are referenced by ID. |
