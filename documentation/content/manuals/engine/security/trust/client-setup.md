---
title: Configure Docker and Notary clients for content trust
---

See [Docker Content Trust concepts and scope](context.md).

## Configuring the Docker client

By default, the `$ docker trust` commands expect the notary server URL to be the
same as the registry URL specified in the image tag (following a similar logic to
`$ docker push`). When using Docker Hub or DTR, the notary
server URL is the same as the registry URL. However, for self-hosted
environments or 3rd party registries, you will need to specify an alternative
URL of the notary server. This is done with:

```console
$ export DOCKER_CONTENT_TRUST_SERVER=https://<URL>:<PORT>
```

If you do not export this variable in self-hosted environments, you may see 
errors such as: 

```console
$ docker trust signer add --key cert.pem jeff registry.example.com/admin/demo
Adding signer "jeff" to registry.example.com/admin/demo...
<...>
Error: trust data missing for remote repository registry.example.com/admin/demo or remote repository not found: timestamp key trust data unavailable.  Has a notary repository been initialized?

$ docker trust inspect registry.example.com/admin/demo --pretty
WARN[0000] Error while downloading remote metadata, using cached timestamp - this might not be the latest version available remotely
<...>
```

If you have enabled authentication for your notary server, or are using DTR, you will need to log in 
before you can push data to the notary server. 

```console
$ docker login registry.example.com/user/repo
Username: admin
Password:

Login Succeeded

$ docker trust signer add --key cert.pem jeff registry.example.com/user/repo
Adding signer "jeff" to registry.example.com/user/repo...
Initializing signed repository for registry.example.com/user/repo...
Successfully initialized "registry.example.com/user/repo"
Successfully added signer: jeff to registry.example.com/user/repo
```

If you do not log in, you will see:

```console
$ docker trust signer add --key cert.pem jeff registry.example.com/user/repo
Adding signer "jeff" to registry.example.com/user/repo...
Initializing signed repository for registry.example.com/user/repo...
you are not authorized to perform this operation: server returned 401.

Failed to add signer to: registry.example.com/user/repo
```

## Configuring the Notary client

Some of the more advanced features of DCT require the Notary CLI. To install and 
configure the Notary CLI:

1. Download the [client](https://github.com/theupdateframework/notary/releases) and ensure that it is available on your path.

2. Create a configuration file at `~/.notary/config.json` with the following content:

```json
{
  "trust_dir" : "~/.docker/trust",
  "remote_server": {
    "url": "https://registry.example.com",
    "root_ca": "../.docker/ca.pem"
  }
}
```

The newly created configuration file contains information about the location of your local Docker trust data and the notary server URL.

For more detailed information about how to use notary outside of the
Docker Content Trust use cases, refer to the [Notary CLI documentation](https://github.com/theupdateframework/notary/blob/master/docs/command_reference.md)
