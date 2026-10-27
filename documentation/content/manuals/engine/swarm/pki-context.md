---
title: Swarm node identity and certificate lifecycle
---


The Swarm mode public key infrastructure (PKI) system built into Docker
makes it simple to securely deploy a container orchestration system. The nodes
in a swarm use mutual Transport Layer Security (TLS) to authenticate, authorize,
and encrypt the communications with other nodes in the swarm.

When you create a swarm by running `docker swarm init`, Docker designates itself
as a manager node. By default, the manager node generates a new root Certificate
Authority (CA) along with a key pair, which are used to secure communications
with other nodes that join the swarm. If you prefer, you can specify your own
externally-generated root CA, using the `--external-ca` flag of the
[docker swarm init](/reference/cli/docker/swarm/init/) command.

The manager node also generates two tokens to use when you join additional nodes
to the swarm: one worker token and one manager token. Each token
includes the digest of the root CA's certificate and a randomly generated
secret. When a node joins the swarm, the joining node uses the digest to
validate the root CA certificate from the remote manager. The remote manager
uses the secret to ensure the joining node is an approved node.

Each time a new node joins the swarm, the manager issues a certificate to the
node. The certificate contains a randomly generated node ID to identify the node
under the certificate common name (CN) and the role under the organizational
unit (OU). The node ID serves as the cryptographically secure node identity for
the lifetime of the node in the current swarm.

The diagram below illustrates how manager nodes and worker nodes encrypt
communications using a minimum of TLS 1.2.

![TLS diagram](/engine/swarm/images/tls.webp?w=600)

The example below shows the information from a certificate from a worker node:

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            3b:1c:06:91:73:fb:16:ff:69:c3:f7:a2:fe:96:c1:73:e2:80:97:3b
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: CN=swarm-ca
        Validity
            Not Before: Aug 30 02:39:00 2016 GMT
            Not After : Nov 28 03:39:00 2016 GMT
        Subject: O=ec2adilxf4ngv7ev8fwsi61i7, OU=swarm-worker, CN=dw02poa4vqvzxi5c10gm4pq2g
...snip...
```

By default, each node in the swarm renews its certificate every three months.
You can configure this interval by running the `docker swarm update
--cert-expiry <TIME PERIOD>` command. The minimum rotation value is 1 hour.
Refer to the
[docker swarm update](/reference/cli/docker/swarm/update/) CLI
reference for details.
