---
title: Enforce sign-in with registry.json
---

Review [sign-in enforcement behavior](enforcement-model.md) and [method precedence and troubleshooting](method-reference.md).

The registry.json method works across all platforms and offers flexible deployment options.

## File locations

Create the `registry.json` file (UTF-8 without BOM) at the appropriate location:

| Platform | Location |
| --- | --- |
| Windows | `/ProgramData/DockerDesktop/registry.json` |
| Mac | `/Library/Application Support/com.docker.docker/registry.json` |
| Linux | `/usr/share/docker-desktop/registry/registry.json` |

## Basic setup

{{< tabs >}}
{{< tab name="Manual creation" >}}

1. Ensure users are members of your Docker organization.
1. Create the `registry.json` file at the appropriate location for your platform.
1. Add this content, replacing organization names with your own:
      ```json
      {
         "allowedOrgs": ["myorg1", "myorg2"]
      }
      ```
1. Set file permissions to prevent user editing.
1. Restart Docker Desktop.
1. Verify the `Sign in required!` prompt appears in Docker Desktop.

> [!TIP]
>
> If users have issues starting Docker Desktop after enforcing sign-in,
> they may need to update to the latest version.

{{< /tab >}}
{{< tab name="Command line setup" >}}

### Windows (PowerShell as Administrator)

```shell
Set-Content /ProgramData/DockerDesktop/registry.json '{"allowedOrgs":["myorg1","myorg2"]}'
```

### Mac

```console
sudo mkdir -p "/Library/Application Support/com.docker.docker"
echo '{"allowedOrgs":["myorg1","myorg2"]}' | sudo tee "/Library/Application Support/com.docker.docker/registry.json"
```

### Linux

```console
sudo mkdir -p /usr/share/docker-desktop/registry
echo '{"allowedOrgs":["myorg1","myorg2"]}' | sudo tee /usr/share/docker-desktop/registry/registry.json
```

{{< /tab >}}
{{< tab name="Installation-time setup" >}}

Create the registry.json file during Docker Desktop installation:

### Windows

```shell
# PowerShell
Start-Process '.\Docker Desktop Installer.exe' -Wait 'install --allowed-org=myorg'

# Command Prompt
"Docker Desktop Installer.exe" install --allowed-org=myorg
```

### Mac

```console
sudo hdiutil attach Docker.dmg
sudo /Volumes/Docker/Docker.app/Contents/MacOS/install --allowed-org=myorg
sudo hdiutil detach /Volumes/Docker
```

{{< /tab >}}
{{< /tabs >}}
