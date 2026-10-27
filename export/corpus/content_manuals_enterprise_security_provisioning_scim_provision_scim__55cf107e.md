---
title: Set up SCIM provisioning
linkTitle: Setup
description: Learn how System for Cross-domain Identity Management works and how to set it up.
weight: 10
aliases:
  - /enterprise/security/provisioning/scim/
---

{{< summary-bar feature_name="SSO" >}}

## Prerequisites

Review the [prerequisites for SSO provisioning](/manuals/enterprise/security/provisioning/sso-prerequisites.md) and [how SCIM works](scim-context.md#how-scim-works).

## Supported attributes

Review [SCIM attributes and JIT precedence](scim-attributes.md).

## Enable SCIM in Docker

To enable SCIM:

1. Sign in to [Docker Home](https://app.docker.com).
1. Select **Admin Console**, then **SSO and SCIM**.
1. In the **SSO connections** table, select the **Actions** icon for your
   connection, then select **Setup SCIM**.
1. Copy the **SCIM Base URL** and **API Token** and paste the values into your
   IdP.

## Enable SCIM in your IdP

The user interface for your identity provider may differ slightly from the
following steps. You can refer to the documentation for your identity provider
to verify. For additional details, see the documentation for your identity
provider:

- [Okta](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SCIM.htm)
- [Entra ID/Azure AD SAML 2.0](https://learn.microsoft.com/en-us/azure/active-directory/app-provisioning/user-provisioning)

> [!NOTE]
>
> Microsoft does not currently support SCIM and OIDC in the same non-gallery
> application in Entra ID. This page provides a verified workaround using a
> separate non-gallery app for SCIM provisioning. While Microsoft does not
> officially document this setup, it is widely used and supported in practice.

{{< tabs >}}
{{< tab name="Okta" >}}

### Step one: Enable SCIM

1. Sign in to Okta and select **Admin** to open the admin portal.
1. Open the application you created when you configured your SSO connection.
1. On the application page, select the **General** tab, then
   **Edit App Settings**.
1. Enable SCIM provisioning, then select **Save**.
1. Navigate to the **Provisioning**, then select **Edit SCIM Connection**.
1. To configure SCIM in Okta, set up your connection using the following
   values and settings:
   - SCIM Base URL: SCIM connector base URL (copied from Docker Home)
   - Unique identifier field for users: `email`
   - Supported provisioning actions: **Push New Users** and
     **Push Profile Updates**
   - Authentication Mode: HTTP Header
   - SCIM Bearer Token: HTTP Header Authorization Bearer Token
     (copied from Docker Home)
1. Select **Test Connector Configuration**.
1. Review the test results and select **Save**.

### Step two: Enable synchronization

1. In Okta, select **Provisioning**.
1. Select **To App**, then **Edit**.
1. Enable **Create Users**, **Update User Attributes**, and **Deactivate Users**.
1. Select **Save**.
1. Remove unnecessary mappings. The necessary mappings are:
   - Username
   - Given name
   - Family name
   - Email

Next, [set up role mapping](#set-up-role-mapping).

{{< /tab >}}
{{< tab name="Entra ID (OIDC)" >}}

Microsoft does not support SCIM and OIDC in the same non-gallery application.
You must create a second non-gallery application in Entra ID for SCIM
provisioning.

### Step one: Create a separate SCIM app

1. In the Azure Portal, go to **Microsoft Entra ID** >
   **Enterprise Applications** > **New application**.
1. Select **Create your own application**.
1. Name your application and choose
   **Integrate any other application you don't find in the gallery**.
1. Select **Create**.

### Step two: Configure SCIM provisioning

1. In your new SCIM application, go to **Provisioning** > **Get started**.
1. Set **Provisioning Mode** to **Automatic**.
1. Under **Admin Credentials**:
   - **Tenant URL**: Paste the **SCIM Base URL** from Docker Home.
   - **Secret Token**: Paste the **SCIM API token** from Docker Home.
1. Select **Test Connection** to verify.
1. Select **Save** to store credentials.

Next, [set up role mapping](#set-up-role-mapping).

{{< /tab >}}
{{< tab name="Entra ID (SAML 2.0)" >}}

1. In the Azure Portal, go to **Microsoft Entra ID** >
   **Enterprise Applications**, and select your Docker SAML app.
1. Select **Provisioning** > **Get started**.
1. Set **Provisioning Mode** to **Automatic**.
1. Under **Admin Credentials**:
   - **Tenant URL**: Paste the **SCIM Base URL** from Docker Home.
   - **Secret Token**: Paste the **SCIM API token** from Docker Home.
1. Select **Test Connection** to verify.
1. Select **Save** to store credentials.

Next, [set up role mapping](#set-up-role-mapping).

{{< /tab >}}
{{< /tabs >}}

## Set up role mapping

Follow [Map Docker roles, organizations, and teams](role-mapping.md).

## Test SCIM provisioning

After completing role mapping, you can test the configuration manually.

{{< tabs >}}
{{< tab name="Okta" >}}

1. In the Okta admin portal, go to **Directory > People**.
1. Select a user you've assigned to your SCIM application.
1. Select **Provision User**.
1. Wait a few seconds, then check the Docker
   [Admin Console](https://app.docker.com/admin) under **Members**.
1. If the user doesn't appear, review logs in **Reports > System Log** and
   confirm SCIM settings in the app.

{{< /tab >}}
{{< tab name="Entra ID/Azure AD (OIDC and SAML 2.0)" >}}

1. In the Azure Portal, go to **Microsoft Entra ID** > **Enterprise Applications**,
   and select your SCIM app.
1. Go to **Provisioning** > **Provision on demand**.
1. Select a user or group and choose **Provision**.
1. Confirm that the user appears in the Docker
   [Admin Console](https://app.docker.com/admin) under **Members**.
1. If needed, check **Provisioning logs** for errors.

{{< /tab >}}
{{< /tabs >}}

## Disable SCIM

If SCIM is disabled, any user provisioned through SCIM will remain in the
organization. Future changes for your users will not sync from your IdP.
User de-provisioning is only possible when manually removing the user from the
organization.

To disable SCIM:

1. Sign in to [Docker Home](https://app.docker.com).
1. Select **Admin Console**, then **SSO and SCIM**.
1. In the **SSO connections** table, select the **Actions** icon.
1. Select **Disable SCIM**.

## Next steps

- Set up [Group mapping](/manuals/enterprise/security/provisioning/scim/group-mapping.md).
- [Troubleshoot provisioning](/manuals/enterprise/security/provisioning/troubleshoot-provisioning.md).
