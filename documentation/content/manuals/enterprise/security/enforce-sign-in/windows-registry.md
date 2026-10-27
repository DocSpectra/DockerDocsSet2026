---
title: Enforce sign-in with a Windows registry key
---

Review [sign-in enforcement behavior](enforcement-model.md) and [method precedence and troubleshooting](method-reference.md).

## Configure the registry key

{{< tabs >}}
{{< tab name="Manual setup" >}}

To configure the registry key method manually:

1. Create the registry key:

   ```console
   $ HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Docker\Docker Desktop
   ```
1. Create a multi-string value name `allowedOrgs`.
1. Use your organization names as string data. You can add multiple organizations:
   - Use lowercase letters only
   - Add each organization on a separate line
   - Do not use spaces or commas as separators
1. Restart Docker Desktop.
1. Verify the `Sign in required!` prompt appears in Docker Desktop.

{{< /tab >}}
{{< tab name="Group Policy deployment" >}}

Deploy the registry key across your organization using Group Policy:

1. Create a registry script with the required key structure.
1. In Group Policy Management, create or edit a GPO.
1. Navigate to **Computer Configuration** > **Preferences** > **Windows Settings** > **Registry**.
1. Right-click **Registry** > **New** > **Registry Item**.
1. Configure the registry item:
   - Action: **Update**
   - Path: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Docker\Docker Desktop`
   - Value name: `allowedOrgs`
   - Value data: Your organization names
1. Link the GPO to the target Organizational Unit.
1. Test on a small group using `gpupdate/force`.
1. Deploy organization-wide after verification.

{{< /tab >}}
{{< /tabs >}}
