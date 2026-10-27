---
title: SSO authentication with JIT enabled or disabled
---

## SSO authentication with JIT provisioning enabled

When a user signs in with SSO and you have JIT provisioning enabled, the following steps occur automatically:

1. The system checks if a Docker account exists for the user's email address.
   - If an account exists: The system uses the existing account and updates the user's full name if necessary.
   - If no account exists: A new Docker account is created using basic user attributes (email, name, and surname). A unique username is generated based on the user's email, name, and random numbers to ensure all usernames are unique across the platform.

2. The system checks for any pending invitations to the SSO organization.
   - Invitation found: The invitation is automatically accepted.
   - Invitation includes a specific group: The user is added to that group within the SSO organization.

3. The system verifies if the IdP has shared group mappings during authentication.
   - Group mappings provided: The user is assigned to the relevant organizations and teams.
   - No group mappings provided: The system checks if the user is already part of the organization. If not, the user is added to the default organization and team configured in the SSO connection.

The following graphic provides an overview of SSO authentication with JIT enabled:

![JIT provisioning enabled workflow](../images/jit-enabled-flow.svg)

## SSO authentication with JIT provisioning disabled

When JIT provisioning is disabled, the following actions occur during SSO authentication:

1. The system checks if a Docker account exists for the user's email address.
   - If an account exists: The system uses the existing account and updates the user's full name if necessary.
   - If no account exists: A new Docker account is created using basic user attributes (email, name, and surname). A unique username is generated based on the user's email, name, and random numbers to ensure all usernames are unique across the platform.

2. The system checks for any pending invitations to the SSO organization.
   - Invitation found: If the user is a member of the organization or has a pending invitation, sign-in is successful, and the invitation is automatically accepted.
   - No invitation found: If the user is not a member of the organization and has no pending invitation, the sign-in fails, and an `Access denied` error appears. The user must contact an administrator to be invited to the organization.

With JIT disabled, group mapping is only available if you have [SCIM enabled](scim/scim-context.md). If SCIM is not enabled, users won't be auto-provisioned to groups.

The following graphic provides an overview of SSO authentication with JIT disabled:

![JIT provisioning disabled workflow](../images/jit-disabled-flow.svg)
