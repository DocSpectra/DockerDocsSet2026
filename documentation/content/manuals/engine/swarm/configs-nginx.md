---
title: Configure Nginx with configs and rotate its configuration
---

## Prerequisites and caveats

See [Docker config lifecycle and platform support](configs-context.md), including example scope and Windows differences.

This example is divided into two parts.
[The first part](#generate-the-site-certificate) is all about generating
the site certificate and does not directly involve Docker configs at all, but
it sets up [the second part](#configure-the-nginx-container), where you store
and use the site certificate as a series of secrets and the Nginx configuration
as a config. The example shows how to set options on the config, such as the
target location within the container and the file permissions (`mode`).

## Generate the site certificate

Follow [Generate a site certificate](site-certificate.md), including the Let's Encrypt alternative and key protection caveat.

## Configure the Nginx container

1.  Produce a very basic Nginx configuration that serves static files over HTTPS.
    The TLS certificate and key are stored as Docker secrets so that they
    can be rotated easily.

    In the current directory, create a new file called `site.conf` with the
    following contents:

    ```nginx
    server {
        listen                443 ssl;
        server_name           localhost;
        ssl_certificate       /run/secrets/site.crt;
        ssl_certificate_key   /run/secrets/site.key;

        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
        }
    }
    ```

2.  Create two secrets, representing the key and the certificate. You can store
    any file as a secret as long as it is smaller than 500 KB. This allows you
    to decouple the key and certificate from the services that use them.
    In these examples, the secret name and the file name are the same.

    ```console
    $ docker secret create site.key site.key

    $ docker secret create site.crt site.crt
    ```

3.  Save the `site.conf` file in a Docker config. The first parameter is the
    name of the config, and the second parameter is the file to read it from.

    ```console
    $ docker config create site.conf site.conf
    ```

    List the configs:

    ```console
    $ docker config ls

    ID                          NAME                CREATED             UPDATED
    4ory233120ccg7biwvy11gl5z   site.conf           4 seconds ago       4 seconds ago
    ```


4.  Create a service that runs Nginx and has access to the two secrets and the
    config. Set the mode to `0440` so that the file is only readable by its
    owner and that owner's group, not the world.

    ```console
    $ docker service create \
         --name nginx \
         --secret site.key \
         --secret site.crt \
         --config source=site.conf,target=/etc/nginx/conf.d/site.conf,mode=0440 \
         --publish published=3000,target=443 \
         nginx:latest \
         sh -c "exec nginx -g 'daemon off;'"
    ```

    Within the running containers, the following three files now exist:

    - `/run/secrets/site.key`
    - `/run/secrets/site.crt`
    - `/etc/nginx/conf.d/site.conf`

5.  Verify that the Nginx service is running.

    ```console
    $ docker service ls

    ID            NAME   MODE        REPLICAS  IMAGE
    zeskcec62q24  nginx  replicated  1/1       nginx:latest

    $ docker service ps nginx

    NAME                  IMAGE         NODE  DESIRED STATE  CURRENT STATE          ERROR  PORTS
    nginx.1.9ls3yo9ugcls  nginx:latest  moby  Running        Running 3 minutes ago
    ```

6.  Verify that the service is operational: you can reach the Nginx
    server, and that the correct TLS certificate is being used.

    ```console
    $ curl --cacert root-ca.crt https://0.0.0.0:3000

    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    <style>
        body {
            width: 35em;
            margin: 0 auto;
            font-family: Tahoma, Verdana, Arial, sans-serif;
        }
    </style>
    </head>
    <body>
    <h1>Welcome to nginx!</h1>
    <p>If you see this page, the nginx web server is successfully installed and
    working. Further configuration is required.</p>

    <p>For online documentation and support, refer to
    <a href="https://nginx.org">nginx.org</a>.<br/>
    Commercial support is available at
    <a href="https://www.nginx.com">www.nginx.com</a>.</p>

    <p><em>Thank you for using nginx.</em></p>
    </body>
    </html>
    ```

    ```console
    $ openssl s_client -connect 0.0.0.0:3000 -CAfile root-ca.crt

    CONNECTED(00000003)
    depth=1 /C=US/ST=CA/L=San Francisco/O=Docker/CN=Swarm Secret Example CA
    verify return:1
    depth=0 /C=US/ST=CA/L=San Francisco/O=Docker/CN=localhost
    verify return:1
    ---
    Certificate chain
     0 s:/C=US/ST=CA/L=San Francisco/O=Docker/CN=localhost
       i:/C=US/ST=CA/L=San Francisco/O=Docker/CN=Swarm Secret Example CA
    ---
    Server certificate
    -----BEGIN CERTIFICATE-----
    …
    -----END CERTIFICATE-----
    subject=/C=US/ST=CA/L=San Francisco/O=Docker/CN=localhost
    issuer=/C=US/ST=CA/L=San Francisco/O=Docker/CN=Swarm Secret Example CA
    ---
    No client certificate CA names sent
    ---
    SSL handshake has read 1663 bytes and written 712 bytes
    ---
    New, TLSv1/SSLv3, Cipher is AES256-SHA
    Server public key is 4096 bit
    Secure Renegotiation IS supported
    Compression: NONE
    Expansion: NONE
    SSL-Session:
        Protocol  : TLSv1
        Cipher    : AES256-SHA
        Session-ID: A1A8BF35549C5715648A12FD7B7E3D861539316B03440187D9DA6C2E48822853
        Session-ID-ctx:
        Master-Key: F39D1B12274BA16D3A906F390A61438221E381952E9E1E05D3DD784F0135FB81353DA38C6D5C021CB926E844DFC49FC4
        Key-Arg   : None
        Start Time: 1481685096
        Timeout   : 300 (sec)
        Verify return code: 0 (ok)
    ```

7.  Unless you are going to continue to the next example, clean up after running
    this example by removing the `nginx` service and the stored secrets and
    config.

    ```console
    $ docker service rm nginx

    $ docker secret rm site.crt site.key

    $ docker config rm site.conf
    ```

You have now configured a Nginx service with its configuration decoupled from
its image. You could run multiple sites with exactly the same image but
separate configurations, without the need to build a custom image at all.

## Example: Rotate a config

To rotate a config, you first save a new config with a different name than the
one that is currently in use. You then redeploy the service, removing the old
config and adding the new config at the same mount point within the container.
This example builds upon the previous one by rotating the `site.conf`
configuration file.

1.  Edit the `site.conf` file locally. Add `index.php` to the `index` line, and
    save the file.

    ```nginx
    server {
        listen                443 ssl;
        server_name           localhost;
        ssl_certificate       /run/secrets/site.crt;
        ssl_certificate_key   /run/secrets/site.key;

        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm index.php;
        }
    }
    ```

2.  Create a new Docker config using the new `site.conf`, called `site-v2.conf`.

    ```bah
    $ docker config create site-v2.conf site.conf
    ```

3.  Update the `nginx` service to use the new config instead of the old one.

    ```console
    $ docker service update \
      --config-rm site.conf \
      --config-add source=site-v2.conf,target=/etc/nginx/conf.d/site.conf,mode=0440 \
      nginx
    ```

4.  Verify that the `nginx` service is fully re-deployed, using
    `docker service ps nginx`. When it is, you can remove the old `site.conf`
    config.

    ```console
    $ docker config rm site.conf
    ```

5.  To clean up, you can remove the `nginx` service, as well as the secrets and
    configs.

    ```console
    $ docker service rm nginx

    $ docker secret rm site.crt site.key

    $ docker config rm site-v2.conf
    ```

You have now updated your `nginx` service's configuration without the need to
rebuild its image.
