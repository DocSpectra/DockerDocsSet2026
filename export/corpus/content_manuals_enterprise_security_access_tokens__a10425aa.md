---
title: Organization access tokens
linkTitle: Organization access tokens
description: Create and manage organization access tokens to securely authenticate automated systems and CI/CD pipelines with Docker Hub
keywords: organization access tokens, OAT, docker hub security, programmatic access, automation
aliases:
 - /security/for-admins/access-tokens/
---

{{< summary-bar feature_name="OATs" >}}

Organization access tokens (OATs) provide secure, programmatic access to Docker Hub for automated systems, CI/CD pipelines, and other business-critical tasks. Unlike personal access tokens tied to individual users, OATs are associated with your organization and can be managed by any organization owner.

> [!WARNING]
>
> Organization access tokens are incompatible with Docker Desktop, Image Access Management, and Registry Access Management. If you use these features, use [personal access tokens](/manuals/security/access-tokens.md) instead.

For use cases, benefits, and token-handling guidance, see [Organization access token uses and practices](organization-token-context.md).

## Prerequisites

To create and use organization access tokens, you must have:

- A Docker Team or Business subscription
- Owner permissions
- Repositories you want to grant access to

## Create an organization access token

Owners can create tokens with these limits:

- Team subscription: Up to 10 OATs per organization
- Business subscription: Up to 100 OATs per organization

Expired tokens count toward your total limit.

To create an OAT:

1. Sign in to [Docker Home](https://app.docker.com/) and select your
organization.
1. Select **Admin Console**, then **Access tokens**.
1. Select **Generate access token**.
1. Configure token details:
    - Label: Descriptive name indicating the token's purpose
    - Description (optional): Additional details
    - Expiration date: When the token should expire
1. Expand the **Repository** drop-down to set access permissions:
    1. Optional. Select **Read public repositories** for access to public repositories.
    1. Select **Add repository** and choose a repository from the drop-down.
    1. Set permissions for each repository: **Image Pull** or **Image Push**.
    1. Add up to 50 repositories as needed.
1. Optional. Configure organization management permissions by expanding the **Organization** drop-down and selecting the **Allow management access to this organization's resources**:
    - **Member Edit**: Edit members of the organization
    - **Member Read**: Read members of the organization
    - **Invite Edit**: Invite members to the organization
    - **Invite Read**: Read invites to the organization
    - **Group Edit**: Edit groups of the organization
    - **Group Read**: Read groups of the organization
1. Select **Generate token**. Copy the token that appears on the screen and save it. You won't be able to retrieve the token once you exit the screen.

> [!IMPORTANT]
>
> Treat organization access tokens like passwords. Store them securely in a credential manager and never commit them to source code repositories.

## Use organization access tokens

Sign in to the Docker CLI using your organization access token:

```console
$ docker login --username <YOUR_ORGANIZATION_NAME>
Password: [paste your OAT here]
```

When prompted for a password, enter your organization access token.

## Modify existing tokens

To manage existing tokens:

1. Sign in to [Docker Home](https://app.docker.com/) and select your
organization.
1. Select **Admin Console**, then **Access tokens**.
1. Select the actions menu in the token row, you can:
    - **Edit**
    - **Deactivate**
    - **Delete**
1. Select **Save** after making changes to a token.

## Organization access token best practices

Review [Organization access token best practices](organization-token-context.md#organization-access-token-best-practices).
