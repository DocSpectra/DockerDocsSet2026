---
title: Protect Docker daemon connections with TLS
---

See [Docker daemon attack surface](daemon-security.md) for access context.

## Use TLS (HTTPS) to protect the Docker daemon socket

If you need Docker to be reachable through HTTP rather than SSH in a safe manner,
you can enable TLS (HTTPS) by specifying the `tlsverify` flag and pointing Docker's
`tlscacert` flag to a trusted CA certificate.

In the daemon mode, it only allows connections from clients
authenticated by a certificate signed by that CA. In the client mode,
it only connects to servers with a certificate signed by that CA.

> [!IMPORTANT]
>
> Using TLS and managing a CA is an advanced topic. Familiarize yourself
> with OpenSSL, x509, and TLS before using it in production.

### Create a CA, server and client keys with OpenSSL

Follow [Create CA, server, and client keys](tls-certificates.md), including key permissions and cleanup.

Now you can make the Docker daemon only accept connections from clients
providing a certificate trusted by your CA:

```console
$ dockerd \
    --tlsverify \
    --tlscacert=ca.pem \
    --tlscert=server-cert.pem \
    --tlskey=server-key.pem \
    -H=0.0.0.0:2376
```

To connect to Docker and validate its certificate, provide your client keys,
certificates and trusted CA:

> [!TIP]
>
> This step should be run on your Docker client machine. As such, you
> need to copy your CA certificate, your server certificate, and your client
> certificate to that machine.

> [!NOTE]
>
> Replace all instances of `$HOST` in the following example with the
> DNS name of your Docker daemon's host.

```console
$ docker --tlsverify \
    --tlscacert=ca.pem \
    --tlscert=cert.pem \
    --tlskey=key.pem \
    -H=$HOST:2376 version
```

> [!NOTE]
>
> Docker over TLS should run on TCP port 2376.

> [!WARNING]
>
> As shown in the example above, you don't need to run the `docker` client
> with `sudo` or the `docker` group when you use certificate authentication.
> That means anyone with the keys can give any instructions to your Docker
> daemon, giving them root access to the machine hosting the daemon. Guard
> these keys as you would a root password!

### Secure by default

If you want to secure your Docker client connections by default, you can move
the files to the `.docker` directory in your home directory --- and set the
`DOCKER_HOST` and `DOCKER_TLS_VERIFY` variables as well (instead of passing
`-H=tcp://$HOST:2376` and `--tlsverify` on every call).

```console
$ mkdir -pv ~/.docker
$ cp -v {ca,cert,key}.pem ~/.docker

$ export DOCKER_HOST=tcp://$HOST:2376 DOCKER_TLS_VERIFY=1
```

Docker now connects securely by default:

    $ docker ps

### Other modes

If you don't want to have complete two-way authentication, you can run
Docker in various other modes by mixing the flags.

#### Daemon modes

 - `tlsverify`, `tlscacert`, `tlscert`, `tlskey` set: Authenticate clients
 - `tls`, `tlscert`, `tlskey`: Do not authenticate clients

#### Client modes

 - `tls`: Authenticate server based on public/default CA pool
 - `tlsverify`, `tlscacert`: Authenticate server based on given CA
 - `tls`, `tlscert`, `tlskey`: Authenticate with client certificate, do not
   authenticate server based on given CA
 - `tlsverify`, `tlscacert`, `tlscert`, `tlskey`: Authenticate with client
   certificate and authenticate server based on given CA

If found, the client sends its client certificate, so you just need
to drop your keys into `~/.docker/{ca,cert,key}.pem`. Alternatively,
if you want to store your keys in another location, you can specify that
location using the environment variable `DOCKER_CERT_PATH`.

```console
$ export DOCKER_CERT_PATH=~/.docker/zone1/
$ docker --tlsverify ps
```

#### Connecting to the secure Docker port using `curl`

To use `curl` to make test API requests, you need to use three extra command line
flags:

```console
$ curl https://$HOST:2376/images/json \
  --cert ~/.docker/cert.pem \
  --key ~/.docker/key.pem \
  --cacert ~/.docker/ca.pem
```
