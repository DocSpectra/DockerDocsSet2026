---
title: Authorize MCP servers with OAuth
description: Authorize and revoke MCP server access and review credential sharing across profiles.
---

## OAuth authentication

Some MCP servers require authentication to access external services like
GitHub, Notion, and Linear. The MCP Toolkit handles OAuth authentication
automatically. You authorize access through your browser, and the Toolkit
manages credentials securely. You don't need to manually create API tokens or
configure authentication for each service.

## Authorize a server with OAuth

> [!NOTE]
> This page describes the MCP Toolkit interface in Docker Desktop 4.62 and
> later. Earlier versions have a different UI. Upgrade to follow these
> instructions exactly.

1. In Docker Desktop, go to **MCP Toolkit** and select the **Catalog** tab.
2. Find and add an MCP server that requires OAuth.
3. In the server's **Configuration** tab, select the **OAuth** authentication
   method. Follow the link to begin the OAuth authorization.
4. Your browser opens the authorization page for the service. Follow the
   on-screen instructions to complete authentication.
5. Return to Docker Desktop when authentication is complete.

View all authorized services in the **OAuth** tab. To revoke access, select
**Revoke** next to the service you want to disconnect.

## Credentials across profiles

OAuth credentials are shared across all profiles. When you authorize access to
a service like GitHub or Notion, that authorization is available to any server
in any profile that needs it.

This means all profiles use the same OAuth credentials for a given service. If
you need to use different accounts for different projects, you'll need to
revoke and re-authorize between switching profiles.

