---
title: Use a config with Redis
---

## Prerequisites and caveats

See [Docker config lifecycle and platform support](configs-context.md), including example scope and Windows differences.

## Steps

This simple example shows how configs work in just a few commands. For a
real-world example, continue to
[Advanced example: Use configs with a Nginx service](configs-nginx.md).

1.  Add a config to Docker. The `docker config create` command reads standard
    input because the last argument, which represents the file to read the
    config from, is set to `-`.

    ```console
    $ echo "This is a config" | docker config create my-config -
    ```

2.  Create a `redis` service and grant it access to the config. By default,
    the container can access the config at `/my-config`, but
    you can customize the file name on the container using the `target` option.

    ```console
    $ docker service create --name redis --config my-config redis:alpine
    ```

3.  Verify that the task is running without issues using `docker service ps`. If
    everything is working, the output looks similar to this:

    ```console
    $ docker service ps redis

    ID            NAME     IMAGE         NODE              DESIRED STATE  CURRENT STATE          ERROR  PORTS
    bkna6bpn8r1a  redis.1  redis:alpine  ip-172-31-46-109  Running        Running 8 seconds ago
    ```

4.  Get the ID of the `redis` service task container using `docker ps`, so that
    you can use `docker container exec` to connect to the container and read the contents
    of the config data file, which defaults to being readable by all and has the
    same name as the name of the config. The first command below illustrates
    how to find the container ID, and the second and third commands use shell
    completion to do this automatically.

    ```console
    $ docker ps --filter name=redis -q

    5cb1c2348a59

    $ docker container exec $(docker ps --filter name=redis -q) ls -l /my-config

    -r--r--r--    1 root     root            12 Jun  5 20:49 my-config

    $ docker container exec $(docker ps --filter name=redis -q) cat /my-config

    This is a config
    ```

5.  Try removing the config. The removal fails because the `redis` service is
    running and has access to the config.

    ```console

    $ docker config ls

    ID                          NAME                CREATED             UPDATED
    fzwcfuqjkvo5foqu7ts7ls578   hello               31 minutes ago      31 minutes ago


    $ docker config rm my-config

    Error response from daemon: rpc error: code = 3 desc = config 'my-config' is
    in use by the following service: redis
    ```

6.  Remove access to the config from the running `redis` service by updating the
    service.

    ```console
    $ docker service update --config-rm my-config redis
    ```

7.  Repeat steps 3 and 4 again, verifying that the service no longer has access
    to the config. The container ID is different, because the
    `service update` command redeploys the service.

    ```console
    $ docker container exec -it $(docker ps --filter name=redis -q) cat /my-config

    cat: can't open '/my-config': No such file or directory
    ```

8.  Stop and remove the service, and remove the config from Docker.

    ```console
    $ docker service rm redis

    $ docker config rm my-config
    ```
