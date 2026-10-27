---
title: Show user notifications
description: Display success, warning, and error toasts from an extension.
---

## User notifications

Toasts provide a brief notification to the user. They appear temporarily and
shouldn't interrupt the user experience. They also don't require user input to disappear.

### success

▸ **success**(`msg`): `void`

Use to display a toast message of type success.

```typescript
ddClient.desktopUI.toast.success("message");
```

### warning

▸ **warning**(`msg`): `void`

Use to display a toast message of type warning.

```typescript
ddClient.desktopUI.toast.warning("message");
```

### error

▸ **error**(`msg`): `void`

Use to display a toast message of type error.

```typescript
ddClient.desktopUI.toast.error("message");
```

For more details about method parameters and the return types available, see [Toast API reference](/reference/api/extensions-sdk/Toast.md).

> Deprecated user notifications
>
> These methods are deprecated and will be removed in a future version. Use the methods specified above.

```typescript
window.ddClient.toastSuccess("message");
window.ddClient.toastWarning("message");
window.ddClient.toastError("message");
```


For UI runtime policies, see [Extension security](../../architecture/security.md#policies-enforced-for-the-front-end-code).
