---
title: View and rotate Swarm join tokens
---

## View the join command or update a swarm join token

Nodes require a secret token to join the swarm. The token for worker nodes is
different from the token for manager nodes. Nodes only use the join-token at the
moment they join the swarm. Rotating the join token after a node has already
joined a swarm does not affect the node's swarm membership. Token rotation
ensures an old token cannot be used by any new nodes attempting to join the
swarm.

To retrieve the join command including the join token for worker nodes, run:

```console
$ docker swarm join-token worker

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
    192.168.99.100:2377

This node joined a swarm as a worker.
```

To view the join command and token for manager nodes, run:

```console
$ docker swarm join-token manager

To add a manager to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-59egwe8qangbzbqb3ryawxzk3jn97ifahlsrw01yar60pmkr90-bdjfnkcflhooyafetgjod97sz \
    192.168.99.100:2377
```

Pass the `--quiet` flag to print only the token:

```console
$ docker swarm join-token --quiet worker

SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c
```

Be careful with the join tokens because they are the secrets necessary to join
the swarm. In particular, checking a secret into version control is a bad
practice because it would allow anyone with access to the application source
code to add new nodes to the swarm. Manager tokens are especially sensitive
because they allow a new manager node to join and gain control over the whole
swarm.

We recommend that you rotate the join tokens in the following circumstances:

* If a token was checked-in by accident into a version control system, group
chat or accidentally printed to your logs.
* If you suspect a node has been compromised.
* If you wish to guarantee that no new nodes can join the swarm.

Additionally, it is a best practice to implement a regular rotation schedule for
any secret including swarm join tokens. We recommend that you rotate your tokens
at least every 6 months.

Run `swarm join-token --rotate` to invalidate the old token and generate a new
token. Specify whether you want to rotate the token for `worker` or `manager`
nodes:

```console
$ docker swarm join-token  --rotate worker

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-2kscvs0zuymrsc9t0ocyy1rdns9dhaodvpl639j2bqx55uptag-ebmn5u927reawo27s3azntd44 \
    192.168.99.100:2377
```
