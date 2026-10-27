---
title: Open an external URL
description: Open a URL in the system default browser from an extension.
---

## Open a URL

This function opens an external URL with the system default browser.

▸ **openExternal**(`url`): `void`

```typescript
ddClient.host.openExternal("https://docker.com");
```

> The URL must have the protocol `http` or `https`.

For more details about method parameters and the return types available, see [Desktop host API reference](/reference/api/extensions-sdk/Host.md).

> Deprecated URL opening
>
> This method is deprecated and will be removed in a future version. Use the methods specified above.

```typescript
window.ddClient.openExternal("https://docker.com");
```


For UI runtime policies, see [Extension security](../../architecture/security.md#policies-enforced-for-the-front-end-code).
