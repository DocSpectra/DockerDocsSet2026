---
title: MSI properties, reboots, and analytics
---

## Configuration options

In addition to the following custom properties, the Docker Desktop MSI installer also supports the standard [Windows Installer command line options](https://learn.microsoft.com/en-us/windows/win32/msi/standard-installer-command-line-options).

| Property                           | Description                                                                                                                                                                                                                                                                                   | Default                 |
| :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
| `ENABLEDESKTOPSHORTCUT`            | Creates a desktop shortcut.                                                                                                                                                                                                                                                                   | 1                       |
| `INSTALLFOLDER`                    | Specifies a custom location where Docker Desktop will be installed.                                                                                                                                                                                                                           | C:\Program Files\Docker |
| `ADMINSETTINGS`                    | Automatically creates an `admin-settings.json` file which is used to [control certain Docker Desktop settings](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md) on client machines within organizations. It must be used together with the `ALLOWEDORG` property. | None                    |
| `ALLOWEDORG`                       | Requires the user to sign in and be part of the specified Docker Hub organization when running the application. This creates a registry key called `allowedOrgs` in `HKLM\Software\Policies\Docker\Docker Desktop`.                                                                           | None                    |
| `ALWAYSRUNSERVICE`                 | Lets users switch to Windows containers without needing admin rights                                                                                                                                                                                                                          | 0                       |
| `DISABLEWINDOWSCONTAINERS`         | Disables the Windows containers integration                                                                                                                                                                                                                                                   | 0                       |
| `ENGINE`                           | Sets the Docker Engine that's used to run containers. This can be either `wsl` , `hyperv`, or `windows`                                                                                                                                                                                       | `wsl`                   |
| `PROXYENABLEKERBEROSNTLM`          | When set to 1, enables support for Kerberos and NTLM proxy authentication.                                                                                                                                                                                                                    | 0                       |
| `PROXYHTTPMODE`                    | Sets the HTTP Proxy mode. This can be either `system` or `manual`                                                                                                                                                                                                                             | `system`                |
| `OVERRIDEPROXYHTTP`                | Sets the URL of the HTTP proxy that must be used for outgoing HTTP requests.                                                                                                                                                                                                                  | None                    |
| `OVERRIDEPROXYHTTPS`               | Sets the URL of the HTTP proxy that must be used for outgoing HTTPS requests.                                                                                                                                                                                                                 | None                    |
| `OVERRIDEPROXYEXCLUDE`             | Bypasses proxy settings for the hosts and domains. Uses a comma-separated list.                                                                                                                                                                                                               | None                    |
| `OVERRIDEPROXYPAC`                 | Sets the PAC file URL. This setting takes effect only when using `manual` proxy mode.                                                                                                                                                                                                         | None                    |
| `OVERRIDEPROXYEMBEDDEDPAC`         | Specifies an embedded PAC (Proxy Auto-config) script. This setting takes effect only when using `manual` proxy mode and has precedence over the `OVERRIDEPROXYPAC` flag.                                                                                                                      | None                    |
| `HYPERVDEFAULTDATAROOT`            | Specifies the default location for the Hyper-V VM disk.                                                                                                                                                                                                                                       | None                    |
| `WINDOWSCONTAINERSDEFAULTDATAROOT` | Specifies the default location for Windows containers.                                                                                                                                                                                                                                        | None                    |
| `WSLDEFAULTDATAROOT`               | Specifies the default location for the WSL distribution disk.                                                                                                                                                                                                                                 | None                    |
| `DISABLEANALYTICS`                 | When set to 1, analytics collection will be disabled for the MSI. For more information, see [Analytics](#analytics).                                                                                                                                                                          | 0                       |
| `REMOVEEXISTINGINSTALL`            | When set to 1, any existing EXE installations are removed. Existing settings and content are preserved. Available with Docker Desktop version 4.61 and later.   | 1 |

Additionally, you can also use `/norestart` or `/forcerestart` to control reboot behaviour.

By default, the installer reboots the machine after a successful installation. When run silently, the reboot is automatic and the user is not prompted.

## Analytics

The MSI installer collects anonymous usage statistics relating to installation only. This is to better understand user behaviour and to improve the user experience by identifying and addressing issues or optimizing popular features.

### How to opt-out

{{< tabs >}}
{{< tab name="From the GUI" >}}

When you install Docker Desktop from the default installer GUI, select the **Disable analytics** checkbox located on the bottom-left corner of the **Welcome** dialog.

{{< /tab >}}
{{< tab name="From the command line" >}}

When you install Docker Desktop from the command line, use the `DISABLEANALYTICS` property.

```powershell
msiexec /i "win\msi\bin\en-US\DockerDesktop.msi" /L*V ".\msi.log" DISABLEANALYTICS=1
```

{{< /tab >}}
{{< /tabs >}}

### Persistence

If you decide to disable analytics for an installation, your choice is persisted in the registry and honoured across future upgrades and uninstalls.

However, the key is removed when Docker Desktop is uninstalled and must be configured again via one of the previous methods.

The registry key is as follows:

```powershell
SOFTWARE\Docker Inc.\Docker Desktop\DisableMsiAnalytics
```

When analytics is disabled, this key is set to `1`.
