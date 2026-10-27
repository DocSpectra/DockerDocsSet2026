---
title: Remote driver options
---



The Buildx remote driver allows for more complex custom build workloads,
allowing you to connect to externally managed BuildKit instances. This is useful
for scenarios that require manual management of the BuildKit daemon, or where a
BuildKit daemon is exposed from another source.

## Synopsis

```console
$ docker buildx create \
  --name remote \
  --driver remote \
  tcp://localhost:1234
```

The following table describes the available driver-specific options that you can
pass to `--driver-opt`:

| Parameter      | Type    | Default            | Description                                                            |
| -------------- | ------- | ------------------ | ---------------------------------------------------------------------- |
| `key`          | String  |                    | Sets the TLS client key.                                               |
| `cert`         | String  |                    | Absolute path to the TLS client certificate to present to `buildkitd`. |
| `cacert`       | String  |                    | Absolute path to the TLS certificate authority used for validation.    |
| `servername`   | String  | Endpoint hostname. | TLS server name used in requests.                                      |
| `default-load` | Boolean | `false`            | Automatically load images to the Docker Engine image store.            |


