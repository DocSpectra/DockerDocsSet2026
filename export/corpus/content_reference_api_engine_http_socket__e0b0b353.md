---
title: Connect to the API over a Unix socket
---

When using cURL to connect over a Unix socket, the hostname is not important. The examples use `localhost`, but any hostname would work.

> [!IMPORTANT]
>
> The run-a-container and quickstart examples assume you're using cURL 7.50.0 or above. Older versions of
> cURL used a [non-standard URL notation](https://github.com/moby/moby/issues/17960)
> when using a socket connection.
>
> If you're' using an older version of cURL, use `http:/<API version>/` instead,
> for example: `http:/v{{% param "latest_engine_api_version" %}}/containers/1c6594faf5/start`.
