---
title: Container proxy rules and PAC reference
---

## Who should use air-gapped containers?

Use air-gapped containers if:

- Your organization requires containers to communicate only with approved internal services
- You need to meet compliance standards that mandate network isolation (such as SOC 2, ISO 27001, or PCI DSS)
- You want to prevent containers from leaking data or reaching unapproved external endpoints during builds or at runtime

## How air-gapped containers work

Air-gapped containers operate by intercepting container network traffic and applying proxy rules:

1. Traffic interception: Docker Desktop intercepts all outgoing network connections from containers
1. Port filtering: Only traffic on specified ports (`transparentPorts`) is subject to proxy rules
1. Rule evaluation: PAC file rules or static proxy settings determine how to handle each connection
1. Connection handling: Traffic is allowed directly, routed through a proxy, or blocked based on the rules

Some important considerations include:

- The existing `proxy` setting continues to apply to Docker Desktop application traffic on the host
- If PAC file download fails, containers block requests to target URLs
- Hostname is available for ports 80 and 443, but only IP addresses for other ports

## Configuration parameters

The `containersProxy` setting controls network policies applied to container traffic:

| Parameter | Description | Value |
|-----------|-------------|-------|
| `locked` | Prevents developers from overriding settings | `true` (locked), `false` (default) |
| `mode` | Proxy configuration method | `system` (use system proxy), `manual` (custom) |
| `http` | HTTP proxy server | URL (e.g., `"http://proxy.company.com:8080"`) |
| `https` | HTTPS proxy server | URL (e.g., `"https://proxy.company.com:8080"`) |
| `exclude` | Bypass proxy for these addresses | Array of hostnames/IPs |
| `pac` | Proxy Auto-Configuration file URL | URL to PAC file |
| `transparentPorts` | Ports subject to proxy rules | Comma-separated ports or wildcard (`"*"`) |

## Proxy Auto-Configuration (PAC) files

PAC files provide fine-grained control over container network access by defining rules for different destinations.

### Basic PAC file structure

```javascript
function FindProxyForURL(url, host) {
	if (localHostOrDomainIs(host, 'internal.corp')) {
		return "PROXY 10.0.0.1:3128";
	}
	if (isInNet(host, "192.168.0.0", "255.255.255.0")) {
	    return "DIRECT";
	}
    return "PROXY reject.docker.internal:1234";
}
```

### General considerations

 - `FindProxyForURL` function URL parameter format is `http://host_or_ip:port` or `https://host_or_ip:port`
 - If you have an internal container trying to access `https://docs.docker.com/enterprise/security/hardened-desktop/air-gapped-containers` the Docker proxy service will submit docs.docker.com for the host value and https://docs.docker.com:443 for the url value to `FindProxyForURL`, if you are using `shExpMatch` function in your PAC file as follows:

   ```console
   if(shExpMatch(url, "https://docs.docker.com:443/enterprise/security/*")) return "DIRECT";
   ```

   `shExpMatch` function will fail, instead use:

   ```console
   if (host == docs.docker.com && url.indexOf(":443") > 0) return "DIRECT";
   ```

### PAC file return values

| Return value | Action |
|--------------|--------|
| `PROXY host:port` | Route through HTTP proxy at specified host and port |
| `SOCKS5 host:port` | Route through SOCKS5 proxy at specified host and port |
| `DIRECT` | Allow direct connection without proxy |
| `PROXY reject.docker.internal:any_port` | Block the request completely |

### Advanced PAC file example

```javascript
function FindProxyForURL(url, host) {
  // Allow access to Docker Hub for approved base images
  if (dnsDomainIs(host, ".docker.io") || host === "docker.io") {
    return "PROXY corporate-proxy.company.com:8080";
  }

  // Allow internal package repositories
  if (localHostOrDomainIs(host, 'nexus.company.com') ||
      localHostOrDomainIs(host, 'artifactory.company.com')) {
    return "DIRECT";
  }

  // Allow development tools on specific ports
  if (url.indexOf(":3000") > 0 || url.indexOf(":8080") > 0) {
    if (isInNet(host, "10.0.0.0", "255.0.0.0")) {
      return "DIRECT";
    }
  }

  // Block access to developer's localhost
  if (host === "host.docker.internal" || host === "localhost") {
    return "PROXY reject.docker.internal:1234";
  }

  // Block all other external access
  return "PROXY reject.docker.internal:1234";
}
```

## Security considerations

- Network policy enforcement: Air-gapped containers work at the Docker Desktop level. Advanced users might bypass restrictions through various means, so consider additional network-level controls for high-security environments.
- Development workflow impact: Overly restrictive policies can break legitimate development workflows. Test thoroughly and provide clear exceptions for necessary services.
- PAC file management: Host PAC files on reliable internal infrastructure. Failed PAC downloads result in blocked container network access.
- Performance considerations: Complex PAC files with many rules may impact container network performance. Keep rules simple and efficient.
