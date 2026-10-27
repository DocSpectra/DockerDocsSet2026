---
title: SSO authentication and user access
---

## How SSO works

When SSO is enabled, Docker supports a non-IdP-initiated flow for user sign-in.
Instead of signing in with a Docker username and password, users are redirected
to your IdP’s sign-in page. Users must initiate the SSO authentication process
by signing in to Docker Hub or Docker Desktop.

The following diagram illustrates how SSO operates and is managed between
Docker Hub, Docker Desktop, and your IdP.

![SSO architecture](images/SSO.png)

Once configuration is complete, users can sign in to Docker services using
their company email address. After signing in, users are added to your company,
assigned to an organization, and added to a team.

> [!IMPORTANT]
>
> Docker plans to deprecate CLI password-based sign-in in future releases.
> Using a PAT ensures continued CLI access. For more information, see the
> [security announcement](/manuals/security/security-announcements.md#deprecation-of-password-logins-on-cli-when-sso-enforced).
