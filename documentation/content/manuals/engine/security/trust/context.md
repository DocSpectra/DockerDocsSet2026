---
title: Docker Content Trust concepts and scope
---


When transferring data among networked systems, trust is a central concern. In
particular, when communicating over an untrusted medium such as the internet, it
is critical to ensure the integrity and the publisher of all the data a system
operates on. You use Docker Engine to push and pull images (data) to a
public or private registry. Content trust gives you the ability to verify both
the integrity and the publisher of all the data received from a registry over
any channel.

## About Docker Content Trust (DCT)

Docker Content Trust (DCT) provides the ability to use digital signatures for
data sent to and received from remote Docker registries. These signatures allow
client-side or runtime verification of the integrity and publisher of specific
image tags.

Through DCT, image publishers can sign their images and image consumers can
ensure that the images they pull are signed. Publishers could be individuals
or organizations manually signing their content or automated software supply
chains signing content as part of their release process.

> [!NOTE]
>
> Docker is retiring DCT for Docker Official Images
> (DOI). You should start planning to transition to a different image signing
> and verification solution (like [Sigstore](https://www.sigstore.dev/) or
> [Notation](https://github.com/notaryproject/notation#readme)). Timelines for the
> complete deprecation of DCT are being finalized and will be published soon.
>
> For more information, see [Retiring Docker Content Trust](https://www.docker.com/blog/retiring-docker-content-trust/).

### Image tags and DCT

An individual image record has the following identifier:

```text
[REGISTRY_HOST[:REGISTRY_PORT]/]REPOSITORY[:TAG]
```

A particular image `REPOSITORY` can have multiple tags. For example, `latest` and
 `3.1.2` are both tags on the `mongo` image. An image publisher can build an image
 and tag combination many times changing the image with each build.

DCT is associated with the `TAG` portion of an image. Each image repository has
a set of keys that image publishers use to sign an image tag. Image publishers
have discretion on which tags they sign.

An image repository can contain an image with one tag that is signed and another
tag that is not. For example, consider [the Mongo image
repository](https://hub.docker.com/_/mongo/tags/). The `latest`
tag could be unsigned while the `3.1.6` tag could be signed. It is the
responsibility of the image publisher to decide if an image tag is signed or
not. In this representation, some image tags are signed, others are not:

![Signed tags](images/tag_signing.png)

Publishers can choose to sign a specific tag or not. As a result, the content of
an unsigned tag and that of a signed tag with the same name may not match. For
example, a publisher can push a tagged image `someimage:latest` and sign it.
Later, the same publisher can push an unsigned `someimage:latest` image. This second
push replaces the last unsigned tag `latest` but does not affect the signed `latest` version.
The ability to choose which tags they can sign, allows publishers to iterate over
the unsigned version of an image before officially signing it.

Image consumers can enable DCT to ensure that images they use were signed. If a
consumer enables DCT, they can only pull, run, or build with trusted images.
Enabling DCT is a bit like applying a "filter" to your registry. Consumers "see"
only signed image tags and the less desirable, unsigned image tags are
"invisible" to them.

![Trust view](images/trust_view.png)

To the consumer who has not enabled DCT, nothing about how they work with Docker
images changes. Every image is visible regardless of whether it is signed or
not.

### Docker Content Trust Keys

Trust for an image tag is managed through the use of signing keys. A key set is
created when an operation using DCT is first invoked. A key set consists
of the following classes of keys:

- An offline key that is the root of DCT for an image tag
- Repository or tagging keys that sign tags
- Server-managed keys such as the timestamp key, which provides freshness
	security guarantees for your repository

The following image depicts the various signing keys and their relationships:

![Content Trust components](images/trust_components.png)

> [!WARNING]
>
>The root key once lost is not recoverable. If you lose any other key, send an email to [Docker Hub Support](mailto:hub-support@docker.com). This loss also requires manual intervention from every
consumer that used a signed tag from this repository prior to the loss.

You should back up the root key somewhere safe. Given that it is only required
to create new repositories, it is a good idea to store it offline in hardware.


## Delegations


Delegations in Docker Content Trust (DCT) allow you to control who can and cannot sign
an image tag. A delegation will have a pair of private and public delegation keys. A delegation 
could contain multiple pairs of keys and contributors in order to a) allow multiple users 
to be part of a delegation, and b) to support key rotation.  

The most important delegation within Docker Content Trust is `targets/releases`.
This is seen as the canonical source of a trusted image tag, and without a 
contributor's key being under this delegation, they will be unable to sign a tag.

Fortunately when using the `$ docker trust` commands, we will automatically 
initialize a repository, manage the repository keys, and add a collaborator's key to the 
`targets/releases` delegation via `docker trust signer add`.
