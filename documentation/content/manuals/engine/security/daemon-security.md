---
title: Docker daemon attack surface
---

## Docker daemon attack surface

Running containers (and applications) with Docker implies running the
Docker daemon. This daemon requires `root` privileges unless you opt-in
to [Rootless mode](rootless/context.md), and you should therefore be aware of
some important details.

First of all, only trusted users should be allowed to control your
Docker daemon. This is a direct consequence of some powerful Docker
features. Specifically, Docker allows you to share a directory between
the Docker host and a guest container; and it allows you to do so
without limiting the access rights of the container. This means that you
can start a container where the `/host` directory is the `/` directory
on your host; and the container can alter your host filesystem
without any restriction. This is similar to how virtualization systems
allow filesystem resource sharing. Nothing prevents you from sharing your
root filesystem (or even your root block device) with a virtual machine.

This has a strong security implication: for example, if you instrument Docker
from a web server to provision containers through an API, you should be
even more careful than usual with parameter checking, to make sure that
a malicious user cannot pass crafted parameters causing Docker to create
arbitrary containers.

For this reason, the REST API endpoint (used by the Docker CLI to
communicate with the Docker daemon) changed in Docker 0.5.2, and now
uses a Unix socket instead of a TCP socket bound on 127.0.0.1 (the
latter being prone to cross-site request forgery attacks if you happen to run
Docker directly on your local machine, outside of a VM). You can then
use traditional Unix permission checks to limit access to the control
socket.

You can also expose the REST API over HTTP if you explicitly decide to do so.
However, if you do that, be aware of the above mentioned security implications.
Note that even if you have a firewall to limit accesses to the REST API 
endpoint from other hosts in the network, the endpoint can be still accessible
from containers, and it can easily result in the privilege escalation.
Therefore it is *mandatory* to secure API endpoints with 
[HTTPS and certificates](protect-access.md).
Exposing the daemon API over HTTP without TLS is not permitted,
and such a configuration causes the daemon to fail early on startup, see
[Unauthenticated TCP connections](../deprecated.md#unauthenticated-tcp-connections).
It is also recommended to ensure that it is reachable only from a trusted
network or VPN.

You can also use `DOCKER_HOST=ssh://USER@HOST` or `ssh -L /path/to/docker.sock:/var/run/docker.sock`
instead if you prefer SSH over TLS.

The daemon is also potentially vulnerable to other inputs, such as image
loading from either disk with `docker load`, or from the network with
`docker pull`. As of Docker 1.3.2, images are now extracted in a chrooted
subprocess on Linux/Unix platforms, being the first-step in a wider effort
toward privilege separation. As of Docker 1.10.0, all images are stored and
accessed by the cryptographic checksums of their contents, limiting the
possibility of an attacker causing a collision with an existing image.

Finally, if you run Docker on a server, it is recommended to run
exclusively Docker on the server, and move all other services within
containers controlled by Docker. Of course, it is fine to keep your
favorite admin tools (probably at least an SSH server), as well as
existing monitoring/supervision processes, such as NRPE and collectd.
