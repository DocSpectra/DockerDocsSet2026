---
title: Enforce sign-in with a Mac configuration profile
---

Review [sign-in enforcement behavior](enforcement-model.md) and [method precedence and troubleshooting](method-reference.md).

Configuration profiles provide the most secure enforcement method for Mac, as they're protected by Apple's System Integrity Protection.

## Configuration keys

The payload is a dictionary of key-values. Docker Desktop supports the following keys:

- `allowedOrgs`: Sets a list of organizations in one single string, where each organization is separated by a semi-colon.
- `overrideProxyHTTP`: Sets the URL of the HTTP proxy that must be used for outgoing HTTP requests.
- `overrideProxyHTTPS`: Sets the URL of the HTTP proxy that must be used for outgoing HTTPS requests.
- `overrideProxyExclude`: Bypasses proxy settings for the specified hosts and domains. Uses a comma-separated list.
- `overrideProxyPAC`: Sets the file path where the PAC file is located. It has precedence over the remote PAC file on the selected proxy.
- `overrideProxyEmbeddedPAC`: Sets the content of an in-memory PAC file. It has precedence over `overrideProxyPAC`.

Overriding at least one of the proxy settings via Configuration profiles will automatically lock the settings as they're managed by Mac.


## Create and deploy the profile

1. Create a file named `docker.mobileconfig` and include the following content:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      <key>PayloadContent</key>
      <array>
         <dict>
            <key>PayloadType</key>
            <string>com.docker.config</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>PayloadIdentifier</key>
            <string>com.docker.config</string>
            <key>PayloadUUID</key>
            <string>eed295b0-a650-40b0-9dda-90efb12be3c7</string>
            <key>PayloadDisplayName</key>
            <string>Docker Desktop Configuration</string>
            <key>PayloadDescription</key>
            <string>Configuration profile to manage Docker Desktop settings.</string>
            <key>PayloadOrganization</key>
            <string>Your Company Name</string>
            <key>allowedOrgs</key>
            <string>first_org;second_org</string>
            <key>overrideProxyHTTP</key>
            <string>http://company.proxy:port</string>
            <key>overrideProxyHTTPS</key>
            <string>https://company.proxy:port</string>
         </dict>
      </array>
      <key>PayloadType</key>
      <string>Configuration</string>
      <key>PayloadVersion</key>
      <integer>1</integer>
      <key>PayloadIdentifier</key>
      <string>com.yourcompany.docker.config</string>
      <key>PayloadUUID</key>
      <string>0deedb64-7dc9-46e5-b6bf-69d64a9561ce</string>
      <key>PayloadDisplayName</key>
      <string>Docker Desktop Config Profile</string>
      <key>PayloadDescription</key>
      <string>Config profile to enforce Docker Desktop settings for allowed organizations.</string>
      <key>PayloadOrganization</key>
      <string>Your Company Name</string>
   </dict>
   </plist>
   ```
1. Replace placeholders:
   - Change `com.yourcompany.docker.config` to your company identifier
   - Replace `Your Company Name` with your organization name
   - Replace `PayloadUUID` with a randomly generated UUID
   - Update the `allowedOrgs` value with your organization names (separated by semicolons)
   - Replace `company.proxy:port` with http/https proxy server host(or IP address) and port
1. Deploy the profile using your MDM solution.
1. Verify the profile appears in **System Settings** > **General** > **Device Management** under **Device (Managed)**. Ensure the profile is listed with the correct name and settings.

## MDM payload alternative

Some MDM solutions let you specify the payload as a plain dictionary of key-value settings without the full `.mobileconfig` wrapper:

```xml
<dict>
   <key>allowedOrgs</key>
   <string>first_org;second_org</string>
   <key>overrideProxyHTTP</key>
   <string>http://company.proxy:port</string>
   <key>overrideProxyHTTPS</key>
   <string>https://company.proxy:port</string>
</dict>
```
