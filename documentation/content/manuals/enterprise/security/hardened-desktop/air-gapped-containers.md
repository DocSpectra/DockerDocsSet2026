---
title: Air-gapped containers
description: Restrict outbound container traffic using proxy rules, PAC files, and network isolation with Docker Desktop air-gapped containers
keywords: air gapped containers, network security, proxy configuration, container isolation, docker desktop, PAC file, network isolation
aliases:
 - /desktop/hardened-desktop/settings-management/air-gapped-containers/
 - /desktop/hardened-desktop/air-gapped-containers/
 - /security/for-admins/hardened-desktop/air-gapped-containers/
weight: 30
---

{{< summary-bar feature_name="Air-gapped containers" >}}

Air-gapped containers let you restrict container network access by controlling where containers can send and receive data. This feature applies custom proxy rules to container network traffic, helping secure environments where containers shouldn't have unrestricted internet access.

Docker Desktop can configure container network traffic to accept connections, reject connections, or tunnel through HTTP or SOCKS proxies. You control which TCP ports the policy applies to and whether to use a single proxy or per-destination policies via Proxy Auto-Configuration (PAC) files.

For traffic handling and caveats, review [Container proxy rules and PAC reference](container-proxy-reference.md).

## Prerequisites

Before configuring air-gapped containers, you must have:

- [Enforce sign-in](/manuals/enterprise/security/enforce-sign-in/_index.md) enabled to ensure users authenticate with your organization
- A Docker Business subscription
- Configured [Settings Management](/manuals/enterprise/security/hardened-desktop/settings-management/_index.md) with the `admin-settings.json` file to manage organization policies

## Configure air-gapped containers

Add the container proxy to your [`admin-settings.json` file](/manuals/enterprise/security/hardened-desktop/settings-management/settings-file-deployment.md). For example:

```json
{
  "configurationFileVersion": 2,
  "containersProxy": {
    "locked": true,
    "mode": "manual",
    "http": "",
    "https": "",
    "exclude": [],
    "pac": "http://192.168.1.16:62039/proxy.pac",
    "transparentPorts": "*"
  }
}
```

### Configuration parameters

See [Configuration parameters](container-proxy-reference.md#configuration-parameters).

### Configuration examples

Block all external access:

```json
"containersProxy": {
  "locked": true,
  "mode": "manual",
  "http": "",
  "https": "",
  "exclude": [],
  "transparentPorts": "*"
}
```

Allow specific internal services:

```json
"containersProxy": {
  "locked": true,
  "mode": "manual",
  "http": "",
  "https": "",
  "exclude": ["internal.company.com", "10.0.0.0/8"],
  "transparentPorts": "80,443"
}
```

Route through corporate proxy:

```json
"containersProxy": {
  "locked": true,
  "mode": "manual",
  "http": "http://corporate-proxy.company.com:8080",
  "https": "http://corporate-proxy.company.com:8080",
  "exclude": ["localhost", "*.company.local"],
  "transparentPorts": "*"
}
```

## Proxy Auto-Configuration (PAC) files

See [PAC files](container-proxy-reference.md#proxy-auto-configuration-pac-files) for rule examples, return values, and URL matching caveats.

## Verify air-gapped container configuration

After applying the configuration, test that container network restrictions work:

Test blocked access:

```console
$ docker run --rm alpine wget -O- https://www.google.com
# Should fail or timeout based on your proxy rules
```

Test allowed access:

```console
$ docker run --rm alpine wget -O- https://internal.company.com
# Should succeed if internal.company.com is in your exclude list or PAC rules
```

Test proxy routing:

```console
$ docker run --rm alpine wget -O- https://docker.io
# Should succeed if routed through approved proxy
```

## Security considerations

Review [Security considerations](container-proxy-reference.md#security-considerations).

## Next steps

- [Explore Enhanced Container Isolation](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/_index.md) to further restrict what containers can do at runtime
- [Understand how Docker Desktop handles host and container networking](/manuals/desktop/features/networking/_index.md)
