---
title: Proxy variables in a systemd drop-in file
---

## Set HTTP and HTTPS proxy variables {#set-http-and-https-proxy-variables}

Add the `HTTP_PROXY` environment variable to the drop-in file:

```systemd
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:3128"
```

To proxy HTTPS requests, set the `HTTPS_PROXY` environment
variable:

```systemd
[Service]
Environment="HTTPS_PROXY=http://proxy.example.com:3128"
```

Multiple environment variables can be set; to set both an HTTP and an
HTTPS proxy;

```systemd
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:3128"
Environment="HTTPS_PROXY=http://proxy.example.com:3128"
```

> [!NOTE]
>
> Special characters in the proxy value, such as `#?!()[]{}`, must be double
> escaped using `%%`. For example:
>
> ```systemd
> [Service]
> Environment="HTTP_PROXY=http://domain%%5Cuser:complex%%23pass@proxy.example.com:3128/"
> ```

## Exclude hosts from proxying {#exclude-hosts-from-proxying}

If you have internal Docker registries that you need to contact without
proxying, you can specify them via the `NO_PROXY` environment variable.

The `NO_PROXY` variable specifies a string that contains comma-separated
values for hosts that should be excluded from proxying. These are the options
you can specify to exclude hosts:

- IP address prefix (`1.2.3.4`)
- Domain name, or a special DNS label (`*`)
- A domain name matches that name and all subdomains. A domain name with a
  leading "." matches subdomains only. For example, given the domains
  `foo.example.com` and `example.com`:
  - `example.com` matches `example.com` and `foo.example.com`, and
  - `.example.com` matches only `foo.example.com`
- A single asterisk (`*`) indicates that no proxying should be done
- Literal port numbers are accepted by IP address prefixes (`1.2.3.4:80`) and
  domain names (`foo.example.com:80`)

Example:

```systemd
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:3128"
Environment="HTTPS_PROXY=http://proxy.example.com:3128"
Environment="NO_PROXY=localhost,127.0.0.1,docker-registry.example.com,.corp"
```
