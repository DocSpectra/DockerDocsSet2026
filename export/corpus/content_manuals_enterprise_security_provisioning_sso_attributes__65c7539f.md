---
title: SSO attributes and SAML mapping
---

## SSO attributes

When a user signs in through SSO, Docker obtains several attributes from your IdP to manage the user's identity and permissions. These attributes include:

- Email address: The unique identifier for the user
- Full name: The user's complete name
- Groups: Optional. Used for group-based access control
- Docker Org: Optional. Specifies the organization the user belongs to
- Docker Team: Optional. Defines the team the user belongs to within the organization
- Docker Role: Optional. Determines the user's permissions within Docker
- Docker session minutes: Optional. Sets the session duration before users must re-authenticate with their IdP. Must be a positive integer greater than 0. If not provided, default session timeouts apply

> [!NOTE]
>
> Default session timeouts apply when Docker session minutes is not specified. Docker Desktop sessions expire after 90 days or 30 days of inactivity. Docker Hub and Docker Home sessions expire after 24 hours.

## SAML attribute mapping

If your organization uses SAML for SSO, Docker retrieves these attributes from the SAML assertion message. Different IdPs may use different names for these attributes.

| SSO Attribute	| SAML Assertion Message Attributes |
| :--- | :--- |
| Email address |	`"http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier"`, `"http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"`, `"http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"`, `email` |
| Full name	| `"http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"`, `name`, `"http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"`, `"http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname"` |
| Groups (optional) |	`"http://schemas.xmlsoap.org/claims/Group"`, `"http://schemas.microsoft.com/ws/2008/06/identity/claims/groups"`, `Groups`, `groups` |
| Docker Org (optional)	| `dockerOrg` |
| Docker Team (optional) |	`dockerTeam` |
| Docker Role (optional) |	`dockerRole` |
| Docker session minutes (optional) | `dockerSessionMinutes`, must be a positive integer > 0 |
