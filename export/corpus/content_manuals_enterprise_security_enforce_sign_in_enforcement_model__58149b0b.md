---
title: Docker Desktop sign-in and SSO enforcement
---

## How sign-in enforcement works

When Docker Desktop detects a registry key, `.plist` file, or
`registry.json` file:

- A `Sign in required!` prompt appears, requiring users to sign
  in as organization members to use Docker Desktop.
- If users sign in with accounts that aren't organization members, they're
  automatically signed out and can't use Docker Desktop. They can select **Sign in**
  to try again with a different account.
- When users sign in with organization member accounts, they can use Docker
  Desktop normally.
- When users sign out, the `Sign in required!` prompt reappears and they can
  no longer use Docker Desktop unless they sign back in.

> [!NOTE]
>
> Enforcing sign-in for Docker Desktop doesn't affect Docker CLI access. CLI access is only restricted for organizations that enforce single sign-on (SSO).

## Enforcing sign-in versus enforcing single sign-on (SSO)

Enforcing Docker Desktop sign-in and [enforcing SSO](/manuals/enterprise/security/single-sign-on/enforce-sso.md) are different features that serve different purposes:


| Enforcement                       | Description                                                     | Benefits                                                                                                                                                                                                                                                   |
|:----------------------------------|:----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enforce sign-in only              | Users must sign in before using Docker Desktop                 | Ensures users receive the benefits of your subscription and ensures security features are applied. In addition, you gain insights into users’ activity.                                                                                                    |
| Enforce single sign-on (SSO) only | If users sign in, they must sign in using SSO                  | Centralizes authentication and enforces unified policies set by the identity provider.                                                                                                                                                                     |
| Enforce both                      | Users must sign in using SSO before using Docker Desktop       | Ensures users receive the benefits of your subscription and ensures security features are applied. In addition, you gain insights into users’ activity. It also centralizes authentication and enforces unified policies set by the identity provider. |
| Enforce neither                   | If users sign in, they can use SSO or their Docker credentials | Lets users access Docker Desktop without barriers, at the cost of reduced security and insights.                                                                                                                                                  |
