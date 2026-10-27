---
title: Configure BuildKit registry certificates
---

Before following these steps, see [Apply a BuildKit configuration](configuration.md).

## Setting registry certificates

If you specify registry certificates in the BuildKit configuration, the daemon
copies the files into the container under `/etc/buildkit/certs`. The following
steps show adding a self-signed registry certificate to the BuildKit
configuration.

1. Add the following configuration to `/etc/buildkitd.toml`:

   ```toml
   # /etc/buildkitd.toml
   debug = true
   [registry."myregistry.com"]
     ca=["/etc/certs/myregistry.pem"]
     [[registry."myregistry.com".keypair]]
       key="/etc/certs/myregistry_key.pem"
       cert="/etc/certs/myregistry_cert.pem"
   ```

   This tells the builder to push images to the `myregistry.com` registry using
   the certificates in the specified location (`/etc/certs`).

2. Create a `docker-container` builder that uses this configuration:

   ```console
   $ docker buildx create --use --bootstrap \
     --name mybuilder \
     --driver docker-container \
     --buildkitd-config /etc/buildkitd.toml
   ```

3. Inspect the builder's configuration file (`/etc/buildkit/buildkitd.toml`), it
   shows that the certificate configuration is now configured in the builder.

   ```console
   $ docker exec -it buildx_buildkit_mybuilder0 cat /etc/buildkit/buildkitd.toml
   ```

   ```toml
   debug = true

   [registry]

     [registry."myregistry.com"]
       ca = ["/etc/buildkit/certs/myregistry.com/myregistry.pem"]

       [[registry."myregistry.com".keypair]]
         cert = "/etc/buildkit/certs/myregistry.com/myregistry_cert.pem"
         key = "/etc/buildkit/certs/myregistry.com/myregistry_key.pem"
   ```

4. Verify that the certificates are inside the container:

   ```console
   $ docker exec -it buildx_buildkit_mybuilder0 ls /etc/buildkit/certs/myregistry.com/
   myregistry.pem    myregistry_cert.pem   myregistry_key.pem
   ```

Now you can push to the registry using this builder, and it will authenticate
using the certificates:

```console
$ docker buildx build --push --tag myregistry.com/myimage:latest .
```


