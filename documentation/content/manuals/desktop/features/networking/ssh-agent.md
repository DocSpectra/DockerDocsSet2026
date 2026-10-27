---
title: Forward the host SSH agent into a container
---

For host and VM networking context, see [Networking on Docker Desktop](_index.md).

## Network how-tos for Mac and Linux

### SSH agent forwarding

Docker Desktop for Mac and Linux lets you use the host’s SSH agent inside a container. To do this:

1. Bind mount the SSH agent socket by adding the following parameter to your `docker run` command:

   ```console
   $--mount type=bind,src=/run/host-services/ssh-auth.sock,target=/run/host-services/ssh-auth.sock
   ```

2. Add the `SSH_AUTH_SOCK` environment variable in your container:

    ```console
    $ -e SSH_AUTH_SOCK="/run/host-services/ssh-auth.sock"
    ```

To enable the SSH agent in Docker Compose, add the following flags to your service:

 ```yaml
services:
  web:
    image: nginx:alpine
    volumes:
      - type: bind
        source: /run/host-services/ssh-auth.sock
        target: /run/host-services/ssh-auth.sock
    environment:
      - SSH_AUTH_SOCK=/run/host-services/ssh-auth.sock
 ```
