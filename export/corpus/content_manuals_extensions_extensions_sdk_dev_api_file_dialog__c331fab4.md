---
title: Open a file selection dialog
description: Select a file or folder from an extension.
---

## Open a file selection dialog

This function opens a file selector dialog that asks the user to select a file or folder.

▸ **showOpenDialog**(`dialogProperties`): `Promise`<[`OpenDialogResult`](/reference/api/extensions-sdk/OpenDialogResult.md)\>:

The `dialogProperties` parameter is a list of flags passed to Electron to customize the dialog's behaviour. For example, you can pass `multiSelections` to allow a user to select multiple files. See [Electron's documentation](https://www.electronjs.org/docs/latest/api/dialog) for a full list.

```typescript
const result = await ddClient.desktopUI.dialog.showOpenDialog({
  properties: ["openDirectory"],
});
if (!result.canceled) {
  console.log(result.paths);
}
```


For UI runtime policies, see [Extension security](../../architecture/security.md#policies-enforced-for-the-front-end-code).
