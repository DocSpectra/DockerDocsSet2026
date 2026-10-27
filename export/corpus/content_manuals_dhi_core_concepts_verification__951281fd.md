---
title: DHI attestation verification tools and keys
description: Public keys and tool choices for verifying DHI attestations.
---

Docker Hardened Images (DHI) and charts include signed attestations that verify
the build process, contents, and security posture.

Docker's public key for DHI images and charts is published at:

- https://registry.scout.docker.com/keyring/dhi/latest.pub
- https://github.com/docker-hardened-images/keyring

Docker recommends using [Docker Scout](/scout/), but you can use
[`regctl`](https://github.com/regclient/regclient) and
[`cosign`](https://docs.sigstore.dev/) to retrieve and verify attestations.
Docker Scout offers several key advantages: it understands DHI attestation
structures, automatically resolves platforms, provides human-readable summaries,
validates in one step with `--verify`, and integrates tightly with Docker's
attestation infrastructure.

> [!IMPORTANT]
>
> You must authenticate to the Docker Hardened Images registry (`dhi.io`) to
> pull images. Use your Docker ID credentials (the same username and password
> you use for Docker Hub) when signing in. If you don't have a Docker account,
> [create one](../../accounts/create-account.md) for free.
>
> Run `docker login dhi.io` to authenticate.
