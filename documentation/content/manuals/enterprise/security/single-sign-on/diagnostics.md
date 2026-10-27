---
title: Inspect Docker and identity-provider errors
---

## Check for errors

If you experience SSO issues, check both Docker and your identity provider for errors first.

### Check Docker error logs

1. Sign in to [Docker Home](https://app.docker.com/) and select your organization from the top-left account drop-down.
1. Select **Admin Console**, then **SSO and SCIM**.
1. In the SSO connections table, select the **Action** menu and then **View error logs**.
1. For more details on specific errors, select **View error details** next to an error message.
1. Note any errors you see on this page for further troubleshooting.

### Check identity provider errors

1. Review your IdP’s logs or audit trails for any failed authentication or provisioning attempts.
2. Confirm that your IdP’s SSO settings match the values provided in Docker.
3. If applicable, confirm that you have configured user provisioning correctly and that it is enabled in your IdP.
4. If applicable, verify that your IdP correctly maps Docker's required user attributes.
5. Try provisioning a test user from your IdP and verify if they appear in Docker.

For further troubleshooting, check your IdP's documentation or contact their support team.
