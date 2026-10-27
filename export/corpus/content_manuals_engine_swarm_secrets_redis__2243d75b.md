---
title: Use a secret with Redis
---

## Prerequisites and caveats

See [Docker secret lifecycle and platform support](secrets-context.md), including example scope and Windows differences.

## Steps

This simple example shows how secrets work in just a few commands. For a
real-world example, continue to
[Intermediate example: Use secrets with a Nginx service](secrets-nginx.md).

1.  Add a secret to Docker. The `docker secret create` command reads standard
    input because the last argument, which represents the file to read the
    secret from, is set to `-`.

    ```console
    $ printf "This is a secret" | docker secret create my_secret_data -
    ```

2.  Create a `redis` service and grant it access to the secret. By default,
    the container can access the secret at `/run/secrets/<secret_name>`, but
    you can customize the file name on the container using the `target` option.

    ```console
    $ docker service  create --name redis --secret my_secret_data redis:alpine
    ```

3.  Verify that the task is running without issues using `docker service ps`. If
    everything is working, the output looks similar to this:

    ```console
    $ docker service ps redis

    ID            NAME     IMAGE         NODE              DESIRED STATE  CURRENT STATE          ERROR  PORTS
    bkna6bpn8r1a  redis.1  redis:alpine  ip-172-31-46-109  Running        Running 8 seconds ago  
    ```

    If there were an error, and the task were failing and repeatedly restarting,
    you would see something like this:

    ```console
    $ docker service ps redis

    NAME                      IMAGE         NODE  DESIRED STATE  CURRENT STATE          ERROR                      PORTS
    redis.1.siftice35gla      redis:alpine  moby  Running        Running 4 seconds ago                             
     \_ redis.1.whum5b7gu13e  redis:alpine  moby  Shutdown       Failed 20 seconds ago      "task: non-zero exit (1)"  
     \_ redis.1.2s6yorvd9zow  redis:alpine  moby  Shutdown       Failed 56 seconds ago      "task: non-zero exit (1)"  
     \_ redis.1.ulfzrcyaf6pg  redis:alpine  moby  Shutdown       Failed about a minute ago  "task: non-zero exit (1)"  
     \_ redis.1.wrny5v4xyps6  redis:alpine  moby  Shutdown       Failed 2 minutes ago       "task: non-zero exit (1)"
    ```

4.  Get the ID of the `redis` service task container using `docker ps` , so that
    you can use `docker container exec` to connect to the container and read the contents
    of the secret data file, which defaults to being readable by all and has the
    same name as the name of the secret. The first command below illustrates
    how to find the container ID, and the second and third commands use shell
    completion to do this automatically.

    ```console
    $ docker ps --filter name=redis -q

    5cb1c2348a59

    $ docker container exec $(docker ps --filter name=redis -q) ls -l /run/secrets

    total 4
    -r--r--r--    1 root     root            17 Dec 13 22:48 my_secret_data

    $ docker container exec $(docker ps --filter name=redis -q) cat /run/secrets/my_secret_data

    This is a secret
    ```

5.  Verify that the secret is not available if you commit the container.

    ```console
    $ docker commit $(docker ps --filter name=redis -q) committed_redis

    $ docker run --rm -it committed_redis cat /run/secrets/my_secret_data

    cat: can't open '/run/secrets/my_secret_data': No such file or directory
    ```

6.  Try removing the secret. The removal fails because the `redis` service is
    running and has access to the secret.

    ```console
    $ docker secret ls

    ID                          NAME                CREATED             UPDATED
    wwwrxza8sxy025bas86593fqs   my_secret_data      4 hours ago         4 hours ago


    $ docker secret rm my_secret_data

    Error response from daemon: rpc error: code = 3 desc = secret
    'my_secret_data' is in use by the following service: redis
    ```

7.  Remove access to the secret from the running `redis` service by updating the
    service.

    ```console
    $ docker service update --secret-rm my_secret_data redis
    ```

8.  Repeat steps 3 and 4 again, verifying that the service no longer has access
    to the secret. The container ID is different, because the
    `service update` command redeploys the service.

    ```console
    $ docker container exec -it $(docker ps --filter name=redis -q) cat /run/secrets/my_secret_data

    cat: can't open '/run/secrets/my_secret_data': No such file or directory
    ```

9.  Stop and remove the service, and remove the secret from Docker.

    ```console
    $ docker service rm redis

    $ docker secret rm my_secret_data
    ```
