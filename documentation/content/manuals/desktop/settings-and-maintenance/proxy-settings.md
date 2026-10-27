---
title: Docker Desktop proxy settings and authentication
---

## Proxies

Docker Desktop supports HTTP/HTTPS and SOCKS5 proxies. SOCKS5 requires a Business subscription.

To prevent developers from accidentally changing the proxy settings, see
[Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md#what-features-can-i-configure-with-settings-management).

### Docker Desktop proxy

Used for signing in to Docker, pulling and pushing images, fetching artifacts during image builds, and reporting error diagnostics.

| Proxy mode | Description |
|------------|-------------|
| **System proxy** | Use the proxy configured on the host (static or Proxy Auto-Configuration (PAC)). Docker Desktop reads this automatically. |
| **No proxy** | Connect directly without a proxy. |
| **Manual configuration** | Enter a **Web Server (HTTP)** and **Secure Web Server (HTTPS)** URL manually. Use the format `http://proxy:port` or `https://proxy:port`. You can also specify hosts and domains that should bypass the proxy, for example: `registry-1.docker.com,*.docker.com,10.0.0.0/8`. |

> [!NOTE]
>
> If you use a PAC file hosted on a web server, add the MIME type `application/x-ns-proxy-autoconfig` for the `.pac` extension. Without this, the PAC file may not parse correctly. See [Hardened Docker Desktop](/manuals/enterprise/security/hardened-desktop/air-gapped-containers.md#proxy-auto-configuration-files).

### Containers proxy

Used for outbound traffic from running containers.

| Proxy mode | Description |
|------------|-------------|
| **Same as host proxy** | Use the same proxy configuration as the Docker Desktop proxy. |
| **System proxy** | Use the proxy configured on the host. |
| **No proxy** | Connect directly without a proxy. |
| **Manual configuration** | Enter a **Web Server (HTTP)** and **Secure Web Server (HTTPS)** URL manually. Use the format `http://proxy:port` or `https://proxy:port`. You can also specify hosts and domains that should bypass the proxy, for example: `registry-1.docker.com,*.docker.com,10.0.0.0/8`. |

> [!NOTE]
>
> The HTTPS proxy used for image scanning is configured using the `HTTPS_PROXY` environment variable.

### Proxy authentication

| Method |  Behavior | Notes |
|--------|-----------| ----- |
| **Basic** | Docker Desktop prompts for credentials and caches them in the OS credential store. | Use an `https://` proxy URL to protect passwords in transit. Supports TLS 1.3. |
| **Kerberos / NTLM** |  Centralizes authentication — developers aren't prompted for credentials, reducing the risk of account lockouts. If the proxy returns multiple schemes in a 407 response, Docker Desktop defaults to Basic. | Requires a Business subscription. To enable Kerberos or NTLM proxy authentication you must pass the `--proxy-enable-kerberosntlm` installer flag during installation via the command line, and ensure your proxy server is properly configured for Kerberos or NTLM authentication. |
