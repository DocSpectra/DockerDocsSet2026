---
description: How PKI works in swarm mode
keywords: swarm, security, tls, pki,
title: Manage swarm security with public key infrastructure (PKI)
---

See [Swarm node identity and certificate lifecycle](../pki-context.md) for TLS authentication, join tokens, and certificate renewal.

For token handling and rotation, see [View and rotate join tokens](../join-tokens.md).

## Rotating the CA certificate

> [!NOTE]
>
> Mirantis Kubernetes Engine (MKE), formerly known as Docker UCP, provides an external
> certificate manager service for the swarm. If you run swarm on MKE, you shouldn't
> rotate the CA certificates manually. Instead, contact Mirantis support if you need
> to rotate a certificate.

In the event that a cluster CA key or a manager node is compromised, you can
rotate the swarm root CA so that none of the nodes trust certificates
signed by the old root CA anymore.

Run `docker swarm ca --rotate` to generate a new CA certificate and key. If you
prefer, you can pass the `--ca-cert` and `--external-ca` flags to specify the
root certificate and to use a root CA external to the swarm. Alternately,
you can pass the `--ca-cert` and `--ca-key` flags to specify the exact
certificate and key you would like the swarm to use.

When you issue the `docker swarm ca --rotate` command, the following things
happen in sequence:

1.  Docker generates a cross-signed certificate. This means that a version of
    the new root CA certificate is signed with the old root CA certificate.
    This cross-signed certificate is used as an intermediate certificate for all
    new node certificates. This ensures that nodes that still trust the old root
    CA can still validate a certificate signed by the new CA.

2.  Docker also tells all nodes to immediately renew their TLS certificates.
    This process may take several minutes, depending on the number of nodes in
    the swarm.

3.  After every node in the swarm has a new TLS certificate signed by the new CA,
    Docker forgets about the old CA certificate and key material, and tells
    all the nodes to trust the new CA certificate only.

    This also causes a change in the swarm's join tokens. The previous
    join tokens are no longer valid.

From this point on, all new node certificates issued are signed with the new
root CA, and do not contain any intermediates.

## Learn More

* Read about how [nodes](nodes.md) work.
* Learn how Swarm mode [services](services.md) work.
