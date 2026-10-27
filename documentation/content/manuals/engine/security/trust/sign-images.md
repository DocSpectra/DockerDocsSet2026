---
title: Sign, inspect, and revoke trusted image tags
---

## Prerequisites and scope

Read [Docker Content Trust concepts and scope](context.md), including the Docker Official Images retirement notice, and [Configure Docker and Notary clients](client-setup.md).

## Signing images with Docker Content Trust

Within the Docker CLI we can sign and push a container image with the
`$ docker trust` command syntax. This is built on top of the Notary feature
set. For more information, see the [Notary GitHub repository](https://github.com/theupdateframework/notary).

A prerequisite for signing an image is a Docker Registry with a Notary server (such as Docker Hub) attached.
Refer to [Deploying Notary](deploying_notary.md) for instructions.

> [!NOTE]
>
> Docker is retiring DCT for Docker Official Images
> (DOI). You should start planning to transition to a different image signing
> and verification solution (like [Sigstore](https://www.sigstore.dev/) or
> [Notation](https://github.com/notaryproject/notation#readme)). Timelines for the
> complete deprecation of DCT are being finalized and will be published soon.
>
> For more information, see [Retiring Docker Content Trust](https://www.docker.com/blog/retiring-docker-content-trust/).


To sign a Docker Image you will need a delegation key pair. These keys
can be generated locally using `$ docker trust key generate` or generated
by a certificate authority.

First we will add the delegation private key to the local Docker trust
repository. (By default this is stored in `~/.docker/trust/`). If you are
generating delegation keys with `$ docker trust key generate`, the private key
is automatically added to the local trust store. If you are importing a separate
key, you will need to use the
`$ docker trust key load` command.

```console
$ docker trust key generate jeff
Generating key for jeff...
Enter passphrase for new jeff key with ID 9deed25:
Repeat passphrase for new jeff key with ID 9deed25:
Successfully generated and loaded private key. Corresponding public key available: /home/ubuntu/Documents/mytrustdir/jeff.pub
```

Or if you have an existing key:

```console
$ docker trust key load key.pem --name jeff
Loading key from "key.pem"...
Enter passphrase for new jeff key with ID 8ae710e:
Repeat passphrase for new jeff key with ID 8ae710e:
Successfully imported key from key.pem
```

Next we will need to add the delegation public key to the Notary server;
this is specific to a particular image repository in Notary known as a Global
Unique Name (GUN). If this is the first time you are adding a delegation to that
repository, this command will also initiate the repository, using a local Notary
canonical root key. To understand more about initiating a repository, and the
role of delegations, head to
[delegations for content trust](trust_delegation.md).

```console
$ docker trust signer add --key cert.pem jeff registry.example.com/admin/demo
Adding signer "jeff" to registry.example.com/admin/demo...
Enter passphrase for new repository key with ID 10b5e94:
```

Finally, we will use the delegation private key to sign a particular tag and
push it up to the registry.

```console
$ docker trust sign registry.example.com/admin/demo:1
Signing and pushing trust data for local image registry.example.com/admin/demo:1, may overwrite remote trust data
The push refers to repository [registry.example.com/admin/demo]
7bff100f35cb: Pushed
1: digest: sha256:3d2e482b82608d153a374df3357c0291589a61cc194ec4a9ca2381073a17f58e size: 528
Signing and pushing trust metadata
Enter passphrase for signer key with ID 8ae710e:
Successfully signed registry.example.com/admin/demo:1
```

Alternatively, once the keys have been imported an image can be pushed with the
`$ docker push` command, by exporting the DCT environmental variable.

```console
$ export DOCKER_CONTENT_TRUST=1

$ docker push registry.example.com/admin/demo:1
The push refers to repository [registry.example.com/admin/demo:1]
7bff100f35cb: Pushed
1: digest: sha256:3d2e482b82608d153a374df3357c0291589a61cc194ec4a9ca2381073a17f58e size: 528
Signing and pushing trust metadata
Enter passphrase for signer key with ID 8ae710e:
Successfully signed registry.example.com/admin/demo:1
```

Remote trust data for a tag or a repository can be viewed by the
`$ docker trust inspect` command:

```console
$ docker trust inspect --pretty registry.example.com/admin/demo:1

Signatures for registry.example.com/admin/demo:1

SIGNED TAG          DIGEST                                                             SIGNERS
1                   3d2e482b82608d153a374df3357c0291589a61cc194ec4a9ca2381073a17f58e   jeff

List of signers and their keys for registry.example.com/admin/demo:1

SIGNER              KEYS
jeff                8ae710e3ba82

Administrative keys for registry.example.com/admin/demo:1

  Repository Key:	10b5e94c916a0977471cc08fa56c1a5679819b2005ba6a257aa78ce76d3a1e27
  Root Key:	84ca6e4416416d78c4597e754f38517bea95ab427e5f95871f90d460573071fc
```

Remote Trust data for a tag can be removed by the `$ docker trust revoke` command:

```console
$ docker trust revoke registry.example.com/admin/demo:1
Enter passphrase for signer key with ID 8ae710e:
Successfully deleted signature for registry.example.com/admin/demo:1
```
