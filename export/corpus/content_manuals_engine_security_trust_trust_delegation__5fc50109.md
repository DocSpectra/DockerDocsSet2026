---
description: Delegations for content trust
keywords: trust, security, delegations, keys, repository
title: Delegations for content trust
aliases:
- /ee/dtr/user/access-dtr/configure-your-notary-client/
---
See [Delegation concepts](context.md#delegations), [client setup](client-setup.md), and [creating delegation keys](delegation-keys.md) before managing delegations.

## Configuring the Docker client

See [Configure the Docker client](client-setup.md#configuring-the-docker-client).

## Configuring the Notary client

See [Configure the Notary client](client-setup.md#configuring-the-notary-client).

## Creating delegation keys

See [Create and inspect delegation keys](delegation-keys.md).

### Using Docker Trust to generate keys

See [Generate keys with Docker Trust](delegation-keys.md#using-docker-trust-to-generate-keys).

### Manually generating keys

See [Manually generate keys](delegation-keys.md#manually-generating-keys).

### Viewing local delegation keys

See [View local delegation keys](delegation-keys.md#viewing-local-delegation-keys).

## Managing delegations in a Notary Server

When the first delegation is added to the Notary Server using `$ docker trust`,
we automatically initiate trust data for the repository. This includes creating 
the notary target and snapshots keys, and rotating the snapshot key to be 
managed by the notary server. More information on these keys can be found in
[Manage keys for content trust](trust_key_mng.md).

When initiating a repository, you will need the key and the passphrase of a local
Notary Canonical Root Key. If you have not initiated a repository before, and 
therefore don't have a Notary root key, `$ docker trust` will create one for you.

> [!IMPORTANT]
>
> Be sure to protect and back up your [Notary Canonical Root Key](trust_key_mng.md).

### Initiating the repository

To upload the first key to a delegation, at the same time initiating a 
repository, you can use the `$ docker trust signer add` command. This will add 
the contributor's public key to the `targets/releases` delegation, and create a 
second `targets/<name>` delegation. 

For DCT the name of the second delegation, in the below example
`jeff`, is there to help you keep track of the owner of the keys. In more 
advanced use cases of Notary additional delegations are used for hierarchy. 

```console
$ docker trust signer add --key cert.pem jeff registry.example.com/admin/demo

Adding signer "jeff" to registry.example.com/admin/demo...
Initializing signed repository for registry.example.com/admin/demo...
Enter passphrase for root key with ID f6c6a4b: 
Enter passphrase for new repository key with ID b0014f8: 
Repeat passphrase for new repository key with ID b0014f8: 
Successfully initialized "registry.example.com/admin/demo"
Successfully added signer: jeff to registry.example.com/admin/demo
```

You can see which keys have been pushed to the Notary server for each repository
with the `$ docker trust inspect` command. 

```console
$ docker trust inspect --pretty registry.example.com/admin/demo

No signatures for registry.example.com/admin/demo


List of signers and their keys for registry.example.com/admin/demo

SIGNER              KEYS
jeff                1091060d7bfd

Administrative keys for registry.example.com/admin/demo

  Repository Key:	b0014f8e4863df2d028095b74efcb05d872c3591de0af06652944e310d96598d
  Root Key:	64d147e59e44870311dd2d80b9f7840039115ef3dfa5008127d769a5f657a5d7
```

You could also use the Notary CLI to list delegations and keys. Here you can 
clearly see the keys were attached to `targets/releases` and `targets/jeff`.

```console
$ notary delegation list registry.example.com/admin/demo

ROLE                PATHS             KEY IDS                                                             THRESHOLD
----                -----             -------                                                             ---------
targets/jeff        "" <all paths>    1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1    1
                                          
targets/releases    "" <all paths>    1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1    1 
```

### Adding additional signers

Docker Trust allows you to configure multiple delegations per repository, 
allowing you to manage the lifecycle of delegations. When adding additional 
delegations with `$ docker trust` the collaborators key is once again added to 
the `targets/release` role.

> Note you will need the passphrase for the repository key; this would have been
> configured when you first initiated the repository.

```console
$ docker trust signer add --key ben.pub ben registry.example.com/admin/demo

Adding signer "ben" to registry.example.com/admin/demo...
Enter passphrase for repository key with ID b0014f8: 
Successfully added signer: ben to registry.example.com/admin/demo
```

Check to prove that there are now 2 delegations (Signer).

```console
$ docker trust inspect --pretty registry.example.com/admin/demo

No signatures for registry.example.com/admin/demo

List of signers and their keys for registry.example.com/admin/demo

SIGNER              KEYS
ben                 afa404703b25
jeff                1091060d7bfd

Administrative keys for registry.example.com/admin/demo

  Repository Key:	b0014f8e4863df2d028095b74efcb05d872c3591de0af06652944e310d96598d
  Root Key:	64d147e59e44870311dd2d80b9f7840039115ef3dfa5008127d769a5f657a5d7
```

### Adding keys to an existing delegation

To support things like key rotation and expiring / retiring keys you can publish
multiple contributor keys per delegation. The only prerequisite here is to make
sure you use the same the delegation name, in this case `jeff`. Docker trust 
will automatically handle adding this new key to `targets/releases`. 

> [!NOTE]
>
> You will need the passphrase for the repository key; this would have been
> configured when you first initiated the repository.

```console
$ docker trust signer add --key cert2.pem jeff registry.example.com/admin/demo

Adding signer "jeff" to registry.example.com/admin/demo...
Enter passphrase for repository key with ID b0014f8: 
Successfully added signer: jeff to registry.example.com/admin/demo
```

Check to prove that the delegation (Signer) now contains multiple Key IDs. 

```console
$ docker trust inspect --pretty registry.example.com/admin/demo

No signatures for registry.example.com/admin/demo


List of signers and their keys for registry.example.com/admin/demo

SIGNER              KEYS
jeff                1091060d7bfd, 5570b88df073

Administrative keys for registry.example.com/admin/demo

  Repository Key:	b0014f8e4863df2d028095b74efcb05d872c3591de0af06652944e310d96598d
  Root Key:	64d147e59e44870311dd2d80b9f7840039115ef3dfa5008127d769a5f657a5d7
```

### Removing a delegation

If you need to remove a delegation, including the contributor keys that are 
attached to the `targets/releases` role, you can use the 
`$ docker trust signer remove` command.

> [!NOTE]
>
> Tags that were signed by the removed delegation will need to be resigned 
> by an active delegation

```console
$ docker trust signer remove ben registry.example.com/admin/demo
Removing signer "ben" from registry.example.com/admin/demo...
Enter passphrase for repository key with ID b0014f8: 
Successfully removed ben from registry.example.com/admin/demo
```

#### Troubleshooting

1) If you see an error that there are no usable keys in `targets/releases`, you 
   will need to add additional delegations using `docker trust signer add` before 
   resigning images.

   ```text
   WARN[0000] role targets/releases has fewer keys than its threshold of 1; it will not be usable until keys are added to it
   ```

2) If you have added additional delegations already and are seeing an error 
   message that there are no valid signatures in `targets/releases`, you will need
   to resign the `targets/releases` delegation file with the Notary CLI.

   ```text
   WARN[0000] Error getting targets/releases: valid signatures did not meet threshold for targets/releases 
   ```

   Resigning the delegation file is done with the `$ notary witness` command

   ```console
   $ notary witness registry.example.com/admin/demo targets/releases --publish
   ```

   For more information on the `notary witness` command, refer to the
   [Notary client advanced usage guide](https://github.com/theupdateframework/notary/blob/master/docs/advanced_usage.md#recovering-a-delegation)

### Removing a contributor's key from a delegation

As part of rotating keys for a delegation, you may want to remove an individual 
key but retain the delegation. This can be done with the Notary CLI.

Remember you will have to remove the key from both the `targets/releases` role 
and the role specific to that signer `targets/<name>`.

1) We will need to grab the Key ID from the Notary Server

   ```console
   $ notary delegation list registry.example.com/admin/demo

   ROLE                PATHS             KEY IDS                                                             THRESHOLD
   ----                -----             -------                                                             ---------
   targets/jeff        "" <all paths>    8fb597cbaf196f0781628b2f52bff6b3912e4e8075720378fda60d17232bbcf9    1
                                         1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1    
   targets/releases    "" <all paths>    8fb597cbaf196f0781628b2f52bff6b3912e4e8075720378fda60d17232bbcf9    1
                                         1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1    
   ```

2) Remove from the `targets/releases` delegation

   ```console
   $ notary delegation remove registry.example.com/admin/demo targets/releases 1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1 --publish
   
   Auto-publishing changes to registry.example.com/admin/demo
   Enter username: admin
   Enter password: 
   Enter passphrase for targets key with ID b0014f8: 
   Successfully published changes for repository registry.example.com/admin/demo
   ```

3) Remove from the `targets/<name>` delegation

   ```console
   $ notary delegation remove registry.example.com/admin/demo targets/jeff 1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1 --publish
   
   Removal of delegation role targets/jeff with keys [5570b88df0736c468493247a07e235e35cf3641270c944d0e9e8899922fc6f99], to repository "registry.example.com/admin/demo" staged for next publish.
   
   Auto-publishing changes to registry.example.com/admin/demo
   Enter username: admin    
   Enter password: 
   Enter passphrase for targets key with ID b0014f8: 
   Successfully published changes for repository registry.example.com/admin/demo
   ```

4) Check the remaining delegation list 

   ```console
   $ notary delegation list registry.example.com/admin/demo
   
   ROLE                PATHS             KEY IDS                                                             THRESHOLD
   ----                -----             -------                                                             ---------
   targets/jeff        "" <all paths>    8fb597cbaf196f0781628b2f52bff6b3912e4e8075720378fda60d17232bbcf9    1    
   targets/releases    "" <all paths>    8fb597cbaf196f0781628b2f52bff6b3912e4e8075720378fda60d17232bbcf9    1    
   ```

### Removing a local delegation private key

As part of rotating delegation keys, you may need to remove a local delegation
key from the local Docker trust store. This is done with the Notary CLI, using
the `$ notary key remove` command.

1) We will need to get the Key ID from the local Docker Trust store

   ```console
   $ notary key list
   
   ROLE       GUN                          KEY ID                                                              LOCATION
   ----       ---                          ------                                                              --------
   root                                    f6c6a4b00fefd8751f86194c7d87a3bede444540eb3378c4a11ce10852ab1f96    /home/ubuntu/.docker/trust/private
   admin                                   8fb597cbaf196f0781628b2f52bff6b3912e4e8075720378fda60d17232bbcf9    /home/ubuntu/.docker/trust/private
   jeff                                    1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1    /home/ubuntu/.docker/trust/private
   targets    ...example.com/admin/demo    c819f2eda8fba2810ec6a7f95f051c90276c87fddfc3039058856fad061c009d    /home/ubuntu/.docker/trust/private
   ```

2) Remove the key from the local Docker Trust store

   ```console
   $ notary key remove 1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1
   
   Are you sure you want to remove 1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1 (role jeff) from /home/ubuntu/.docker/trust/private?  (yes/no)  y
   
   Deleted 1091060d7bfd938dfa5be703fa057974f9322a4faef6f580334f3d6df44c02d1 (role jeff) from /home/ubuntu/.docker/trust/private.
   ```

## Removing all trust data from a repository

You can remove all trust data from a repository, including repository, target, 
snapshot and all delegations keys using the Notary CLI.

This is often required by a container registry before a particular repository
can be deleted. 

```console
$ notary delete registry.example.com/admin/demo --remote

Deleting trust data for repository registry.example.com/admin/demo
Enter username: admin
Enter password: 
Successfully deleted local and remote trust data for repository registry.example.com/admin/demo

$ docker trust inspect --pretty registry.example.com/admin/demo

No signatures or cannot access registry.example.com/admin/demo
```

## Related information

* [Content trust in Docker](context.md)
* [Manage keys for content trust](trust_key_mng.md)
* [Automation with content trust](trust_automation.md)
* [Play in a content trust sandbox](trust_sandbox.md)
