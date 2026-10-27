---
title: Create, update, and remove Swarm services
---


Swarm services use a declarative model, which means that you define the
desired state of the service, and rely upon Docker to maintain this state. The
state includes information such as (but not limited to):

- The image name and tag the service containers should run
- How many containers participate in the service
- Whether any ports are exposed to clients outside the swarm
- Whether the service should start automatically when Docker starts
- The specific behavior that happens when the service is restarted (such as
  whether a rolling restart is used)
- Characteristics of the nodes where the service can run (such as resource
  constraints and placement preferences)

For an overview of Swarm mode, see [Swarm mode key concepts](key-concepts.md).
For an overview of how services work, see
[How services work](how-swarm-mode-works/services.md).

## Create a service

To create a single-replica service with no extra configuration, you only need
to supply the image name. This command starts an Nginx service with a
randomly-generated name and no published ports. This is a naive example, since
you can't interact with the Nginx service.

```console
$ docker service create nginx
```

The service is scheduled on an available node. To confirm that the service
was created and started successfully, use the `docker service ls` command:

```console
$ docker service ls

ID                  NAME                MODE                REPLICAS            IMAGE                                                                                             PORTS
a3iixnklxuem        quizzical_lamarr    replicated          1/1                 docker.io/library/nginx@sha256:41ad9967ea448d7c2b203c699b429abe1ed5af331cd92533900c6d77490e0268
```

Created services do not always run right away. A service can be in a pending
state if its image is unavailable, if no node meets the requirements you
configure for the service, or for other reasons. See
[Pending services](how-swarm-mode-works/services.md#pending-services) for more
information.

To provide a name for your service, use the `--name` flag:

```console
$ docker service create --name my_web nginx
```

Just like with standalone containers, you can specify a command that the
service's containers should run, by adding it after the image name. This example
starts a service called `helloworld` which uses an `alpine` image and runs the
command `ping docker.com`:

```console
$ docker service create --name helloworld alpine ping docker.com
```

You can also specify an image tag for the service to use. This example modifies
the previous one to use the `alpine:3.6` tag:

```console
$ docker service create --name helloworld alpine:3.6 ping docker.com
```

## Update a service

You can change almost everything about an existing service using the
`docker service update` command. When you update a service, Docker stops its
containers and restarts them with the new configuration.

Since Nginx is a web service, it works much better if you publish port 80
to clients outside the swarm. You can specify this when you create the service,
using the `-p` or `--publish` flag. When updating an existing service, the flag
is `--publish-add`. There is also a `--publish-rm` flag to remove a port that
was previously published.

Assuming that the `my_web` service from the previous section still exists, use
the following command to update it to publish port 80.

```console
$ docker service update --publish-add 80 my_web
```

To verify that it worked, use `docker service ls`:

```console
$ docker service ls

ID                  NAME                MODE                REPLICAS            IMAGE                                                                                             PORTS
4nhxl7oxw5vz        my_web              replicated          1/1                 docker.io/library/nginx@sha256:41ad9967ea448d7c2b203c699b429abe1ed5af331cd92533900c6d77490e0268   *:0->80/tcp
```

You can update almost every configuration detail about an existing service,
including the image name and tag it runs.

## Remove a service

To remove a service, use the `docker service remove` command. You can remove a
service by its ID or name, as shown in the output of the `docker service ls`
command. The following command removes the `my_web` service.

```console
$ docker service remove my_web
```

## Service configuration details

The following sections provide details about service configuration. This topic
does not cover every flag or scenario. In almost every instance where you can
define a configuration at service creation, you can also update an existing
service's configuration in a similar way.

See the command-line references for
[`docker service create`](/reference/cli/docker/service/create/) and
[`docker service update`](/reference/cli/docker/service/update/), or run
one of those commands with the `--help` flag.

### Configure the runtime environment

You can configure the following options for the runtime environment in the
container:

* Environment variables using the `--env` flag
* The working directory inside the container using the `--workdir` flag
* The username or UID using the `--user` flag

The following service's containers have an environment variable `$MYVAR`
set to `myvalue`, run from the `/tmp/` directory, and run as the
`my_user` user.

```console
$ docker service create --name helloworld \
  --env MYVAR=myvalue \
  --workdir /tmp \
  --user my_user \
  alpine ping docker.com
```

### Update the command an existing service runs

To update the command an existing service runs, you can use the `--args` flag.
The following example updates an existing service called `helloworld` so that
it runs the command `ping docker.com` instead of whatever command it was running
before:

```console
$ docker service update --args "ping docker.com" helloworld
```
