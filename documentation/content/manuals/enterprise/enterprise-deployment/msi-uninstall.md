---
title: Uninstall Docker Desktop with MSI
---

For MSI command-line properties and reboot behavior, see the [MSI reference](msi-reference.md).

When uninstalling Docker Desktop, you need to use the same `.msi` file that was originally used to install the application.

If you no longer have the original `.msi` file, you need to use the product code associated with the installation. To find the product code, run:

```powershell
Get-WmiObject Win32_Product | Select-Object IdentifyingNumber, Name | Where-Object {$_.Name -eq "Docker Desktop"}
```

It should return output similar to the following:

```text
IdentifyingNumber                      Name
-----------------                      ----
{10FC87E2-9145-4D7D-B493-2E99E8D8E103} Docker Desktop
```

> [!NOTE]
>
> This command may take some time, depending on the number of installed applications.

`IdentifyingNumber` is the applications product code and can be used to uninstall Docker Desktop. For example:

```powershell
msiexec /x {10FC87E2-9145-4D7D-B493-2E99E8D8E103} /L*V ".\msi.log" /quiet
```

## Uninstall interactively with verbose logging

```powershell
msiexec /x "DockerDesktop.msi" /L*V ".\msi.log"
```

## Uninstall interactively without verbose logging

```powershell
msiexec /x "DockerDesktop.msi"
```

## Uninstall non-interactively with verbose logging

```powershell
msiexec /x "DockerDesktop.msi" /L*V ".\msi.log" /quiet
```

## Uninstall non-interactively without verbose logging

```powershell
msiexec /x "DockerDesktop.msi" /quiet
```
