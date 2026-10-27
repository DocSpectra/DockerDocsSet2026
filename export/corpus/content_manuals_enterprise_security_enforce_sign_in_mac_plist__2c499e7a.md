---
title: Enforce sign-in with a Mac plist file
---

Review [sign-in enforcement behavior](enforcement-model.md) and [method precedence and troubleshooting](method-reference.md).

## Create and deploy the plist file

{{< tabs >}}
{{< tab name="Manual creation" >}}

1. Create the file `/Library/Application Support/com.docker.docker/desktop.plist`.
1. Add this content, replacing `myorg1` and `myorg2` with your organization names:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
     <dict>
	     <key>allowedOrgs</key>
	     <array>
             <string>myorg1</string>
             <string>myorg2</string>
         </array>
     </dict>
   </plist>
   ```
1. Set file permissions to prevent editing by non-administrator users.
1. Restart Docker Desktop.
1. Verify the `Sign in required!` prompt appears in Docker Desktop.

{{< /tab >}}
{{< tab name="Shell script deployment" >}}

Create and deploy a script for organization-wide distribution:

```bash
#!/bin/bash

# Create directory if it doesn't exist
sudo mkdir -p "/Library/Application Support/com.docker.docker"

# Write the plist file
sudo defaults write "/Library/Application Support/com.docker.docker/desktop.plist" allowedOrgs -array "myorg1" "myorg2"

# Set appropriate permissions
sudo chmod 644 "/Library/Application Support/com.docker.docker/desktop.plist"
sudo chown root:admin "/Library/Application Support/com.docker.docker/desktop.plist"
```

Deploy this script using SSH, remote support tools, or your preferred deployment method.

{{< /tab >}}
{{< /tabs >}}
