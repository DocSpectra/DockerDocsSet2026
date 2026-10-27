---
title: Native Node.js addons and DHI runtime customizations
description: Separate native-addon build tools from runtime libraries and hardened language runtimes.
---

Any Node.js application that depends on native addons (such as `bcrypt`,
`sharp`, `sqlite3`, or `node-canvas`) faces the challenge of compiling native
Node.js modules at install time.

See [image hardening](hardening.md) and [customization capabilities](customizations.md) for shared context.

> [!IMPORTANT]
>
> When creating a customization, only add what your application needs at runtime:
>
> - **System packages** - add shared libraries (such as `sqlite-libs`) and
>   language runtimes from the DHI catalog (such as `python-3.14`).
>   Do not add build tools (such as `g++`, `make`, or `python3` from Alpine).
> - **Build tools** - keep these in the `-dev` build stage only. Never add them
>   to the runtime customization.
>
> Language runtimes installed from the DHI hardened package feed are patched and
> tracked in the image SBOM, which is why they are acceptable as system packages.
> Build tools from Alpine or Debian package feeds are not hardened and should
> never appear in the runtime image.
