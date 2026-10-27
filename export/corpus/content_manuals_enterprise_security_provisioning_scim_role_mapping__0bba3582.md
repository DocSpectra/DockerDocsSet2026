---
title: Map Docker roles, organizations, and teams
---

You can assign [Docker roles](/manuals/enterprise/security/roles-and-permissions/core-roles.md) to
users by adding optional SCIM attributes in your IdP. These attributes override
default role and team values set in your SSO configuration.

> [!NOTE]
>
> Role mappings are supported for both SCIM and Just-in-Time (JIT)
> provisioning. For JIT, role mapping applies only when the user is first
> provisioned.

The following table lists the supported optional user-level attributes:

| Attribute    | Possible values                          | Notes                                                                                                                                                                                                                                                            |
| ------------ | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dockerRole` | `member`, `editor`, or `owner`           | If not set, the user defaults to the `member` role. Setting this attribute overrides the default.<br><br>For role definitions, see [Roles and permissions](/manuals/enterprise/security/roles-and-permissions/core-roles.md).                                        |
| `dockerOrg`  | Docker `organizationName` (e.g., `moby`) | Overrides the default organization configured in your SSO connection.<br><br>If unset, the user is provisioned to the default organization. If `dockerOrg` and `dockerTeam` are both set, the user is provisioned to the team within the specified organization. |
| `dockerTeam` | Docker `teamName` (e.g., `developers`)   | Provisions the user to the specified team in the default or specified organization. If the team doesn't exist, it is automatically created.<br><br>You can still use [group mapping](/manuals/enterprise/security/provisioning/scim/group-mapping-reference.md) to assign users to multiple teams across organizations.   |

The external namespace used for these attributes is: `urn:ietf:params:scim:schemas:extension:docker:2.0:User`.
This value is required in your identity provider when creating custom SCIM attributes for Docker.

{{< tabs >}}
{{< tab name="Okta" >}}

### Step one: Set up role mapping in Okta

1. Setup SSO and SCIM first.
1. In the Okta admin portal, go to **Directory**, select **Profile Editor**,
   and then **User (Default)**.
1. Select **Add Attribute** and configure the values for the role, organization,
   or team you want to add. Exact naming isn't required.
1. Return to the **Profile Editor** and select your application.
1. Select **Add Attribute** and enter the required values. The **External Name**
   and **External Namespace** must be exact.
   - The external name values for organization/team/role mapping are
     `dockerOrg`, `dockerTeam`, and `dockerRole` respectively, as listed in the previous table.
   - The external namespace is the same for all of them:
     `urn:ietf:params:scim:schemas:extension:docker:2.0:User`.
1. After creating the attributes, navigate to the top of the page and select
   **Mappings**, then **Okta User to YOUR APP**.
1. Go to the newly created attributes and map the variable names to the external
   names, then select **Save Mappings**. If you're using JIT provisioning, continue
   to the following steps.
1. Navigate to **Applications** and select **YOUR APP**.
1. Select **General**, then **SAML Settings**, and **Edit**.
1. Select **Step 2** and configure the mapping from the user attribute to the
   Docker variables.

### Step two: Assign roles by user

1. In the Okta Admin portal, select **Directory**, then **People**.
1. Select **Profile**, then **Edit**.
1. Select **Attributes** and update the attributes to the desired values.

### Step three: Assign roles by group

1. In the Okta Admin portal, select **Directory**, then **People**.
1. Select **YOUR GROUP**, then **Applications**.
1. Open **YOUR APPLICATION** and select the **Edit** icon.
1. Update the attributes to the desired values.

If a user doesn't already have attributes set up, users who are added to the
group will inherit these attributes upon provisioning.

{{< /tab >}}
{{< tab name="Entra ID/Azure AD (SAML 2.0 and OIDC)" >}}

### Step one: Configure attribute mappings

1. Complete the SCIM provisioning setup.
1. In the Azure Portal, open **Microsoft Entra ID** >
   **Enterprise Applications**, and select your SCIM application.
1. Go to **Provisioning** > **Mappings** >
   **Provision Azure Active Directory Users**.
1. Add or update the following mappings:
   - `userPrincipalName` -> `userName`
   - `mail` -> `emails.value`
   - Optional. Map `dockerRole`, `dockerOrg`, or `dockerTeam` using one of the
     [mapping methods](/manuals/enterprise/security/provisioning/scim/role-mapping.md).
1. Remove any unsupported attributes to prevent sync errors.
1. Optional. Go to **Mappings** > **Provision Azure Active Directory Groups**:
   - If group provisioning causes errors, set **Enabled** to **No**.
   - If enabling, test group mappings carefully.
1. Select **Save** to apply mappings.

### Step two: Choose a role mapping method

You can map `dockerRole`, `dockerOrg`, or `dockerTeam` using one of the
following methods:

#### Expression mapping

Use this method if you only need to assign Docker roles like `member`, `editor`,
or `owner`.

1. In the **Edit Attribute** view, set the mapping type to **Expression**.
1. In the **Expression** field:
   1. If your App Roles match Docker roles exactly, use:
      SingleAppRoleAssignment([appRoleAssignments])
   1. If they don't match, use a switch expression: `Switch(SingleAppRoleAssignment([appRoleAssignments]), "My Corp Admins", "owner", "My Corp Editors", "editor", "My Corp Users", "member")`
1. Set:
   - **Target attribute**: `urn:ietf:params:scim:schemas:extension:docker:2.0:User:dockerRole`
   - **Match objects using this attribute**: No
   - **Apply this mapping**: Always
1. Save your changes.

> [!WARNING]
>
> You can't use `dockerOrg` or `dockerTeam` with this method. Expression mapping
> is only compatible with one attribute.

#### Direct mapping

Use this method if you need to map multiple attributes (`dockerRole` +
`dockerTeam`).

1. For each Docker attribute, choose a unique Entra extension attribute
   (`extensionAttribute1`, `extensionAttribute2`, etc.).
1. In the **Edit Attribute** view:
   - Set mapping type to **Direct**.
   - Set **Source attribute** to your selected extension attribute.
   - Set **Target attribute** to one of:
     - `dockerRole: urn:ietf:params:scim:schemas:extension:docker:2.0:User:dockerRole`
     - `dockerOrg: urn:ietf:params:scim:schemas:extension:docker:2.0:User:dockerOrg`
     - `dockerTeam: urn:ietf:params:scim:schemas:extension:docker:2.0:User:dockerTeam`
   - Set **Apply this mapping** to **Always**.
1. Save your changes.

To assign values, you'll need to use the Microsoft Graph API.

### Step three: Assign users and groups

For either mapping method:

1. In the SCIM app, go to **Users and Groups** > **Add user/group**.
1. Select the users or groups to provision to Docker.
1. Select **Assign**.

If you're using expression mapping:

1. Go to **App registrations** > your SCIM app > **App Roles**.
1. Create App Roles that match Docker roles.
1. Assign users or groups to App Roles under **Users and Groups**.

If you're using direct mapping:

1. Go to [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
   and sign in as a tenant admin.
1. Use Microsoft Graph API to assign attribute values. Example PATCH request:

```bash
PATCH https://graph.microsoft.com/v1.0/users/{user-id}
Content-Type: application/json

{
  "extensionAttribute1": "owner",
  "extensionAttribute2": "moby",
  "extensionAttribute3": "developers"
}
```

> [!NOTE]
>
> You must use a different extension attribute for each SCIM field.

{{< /tab >}}
{{< /tabs >}}

See the documentation for your IdP for additional details:

- [Okta](https://help.okta.com/en-us/Content/Topics/users-groups-profiles/usgp-add-custom-user-attributes.htm)
- [Entra ID/Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/app-provisioning/customize-application-attributes#provisioning-a-custom-extension-attribute-to-a-scim-compliant-application)
