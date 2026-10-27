---
title: "Incompatible CPU detected"
tags: [Troubleshooting]
---

Platform scope: Mac.

## Cause

Docker Desktop requires a processor (CPU) that supports virtualization and, more
specifically, the [Apple Hypervisor
framework](https://developer.apple.com/library/mac/documentation/DriversKernelHardware/Reference/Hypervisor/).

## Solution

Check that: 

 - You've installed the correct Docker Desktop for your architecture
 - Your Mac supports Apple's Hypervisor framework. To check if your Mac supports the Hypervisor framework, run the following command in a terminal window.

   ```console
   $ sysctl kern.hv_support
   ```

   If your Mac supports the Hypervisor Framework, the command prints `kern.hv_support: 1`.

   If not, the command prints `kern.hv_support: 0`.

See also, [Hypervisor Framework
Reference](https://developer.apple.com/library/mac/documentation/DriversKernelHardware/Reference/Hypervisor/)
in the Apple documentation, and Docker Desktop [Mac system requirements](/manuals/desktop/setup/install/mac-requirements.md#system-requirements).

## Diagnostics and logs

- [Collect Docker Desktop diagnostics](diagnostics.md).
- [Read Docker Desktop logs](logs.md).
