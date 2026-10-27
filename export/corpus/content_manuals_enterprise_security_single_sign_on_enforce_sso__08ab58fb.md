---
title: Enforce SSO
---

If SSO is not enforced, users can still sign in using Docker usernames and passwords. Enforcing SSO requires users to use SSO when signing into Docker, which centralizes authentication and enforces policies set by the IdP.

Before enforcing SSO, users accessing Docker through the CLI must [create a personal access token (PAT)](/manuals/security/access-tokens.md). The PAT replaces their username and password for authentication.

1. Sign in to [Docker Home](https://app.docker.com/) and select
   your organization or company.
1. Select **Admin Console**, then **SSO and SCIM**.
1. In the SSO connections table, select the **Action** menu, then **Enable enforcement**.
1. Follow the on-screen instructions.
1. Select **Turn on enforcement**.

When you enforce SSO, your users cannot modify their email address and
password, convert a user account to an organization, or set up 2FA through
Docker Hub. If you want to use 2FA, you must enable 2FA through your IdP.
