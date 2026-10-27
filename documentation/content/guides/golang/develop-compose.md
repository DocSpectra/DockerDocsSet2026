---
title: Run the Go development stack with Compose
description: Run the Go development stack with Compose.
---

## Prerequisites

Start with [Connect the Go application to CockroachDB](develop-application.md), including winding down the containers. See [Go guide prerequisites](prerequisites.md).

For storage and networking context, see [Volumes](/manuals/engine/storage/volumes.md) and [Networking in Compose](/manuals/compose/how-tos/networking.md).

## Better productivity with Docker Compose

At this point, you might be wondering if there is a way to avoid having to deal with long lists of arguments to the `docker` command. The toy example you used in this series requires five environment variables to define the connection to the database. A real application might need many, many more. Then there is also a question of dependencies. Ideally, you want to make sure that the database is started before your application is run. And spinning up the database instance may require another Docker command with many options. But there is a better way to orchestrate these deployments for local development purposes.

In this section, you'll create a Docker Compose file to start your `docker-gs-ping-roach` application and CockroachDB database engine with a single command.

## Configure Docker Compose

In your application's directory, create a new text file named `compose.yaml` with the following content.

```yaml
version: "3.8"

services:
  docker-gs-ping-roach:
    depends_on:
      - roach
    build:
      context: .
    container_name: rest-server
    hostname: rest-server
    networks:
      - mynet
    ports:
      - 80:8080
    environment:
      - PGUSER=${PGUSER:-totoro}
      - PGPASSWORD=${PGPASSWORD:?database password not set}
      - PGHOST=${PGHOST:-db}
      - PGPORT=${PGPORT:-26257}
      - PGDATABASE=${PGDATABASE:-mydb}
    deploy:
      restart_policy:
        condition: on-failure
  roach:
    image: cockroachdb/cockroach:latest-v25.4
    container_name: roach
    hostname: db
    networks:
      - mynet
    ports:
      - 26257:26257
      - 8080:8080
    volumes:
      - roach:/cockroach/cockroach-data
    command: start-single-node --insecure

volumes:
  roach:

networks:
  mynet:
    driver: bridge
```

This Docker Compose configuration is super convenient as you don't have to type all the parameters to pass to the `docker run` command. You can declaratively do that in the Docker Compose file. The [Docker Compose documentation pages](/manuals/compose/_index.md) are quite extensive and include a full reference for the Docker Compose file format.

## The `.env` file {#the-env-file}

Docker Compose will automatically read environment variables from a `.env` file if it's available. Since your Compose file requires `PGPASSWORD` to be set, add the following content to the `.env` file:

```bash
PGPASSWORD=whatever
```

The exact value doesn't really matter for this example, because you run CockroachDB in insecure mode. Make sure you set the variable to some value to avoid getting an error.

## Merging Compose files

The file name `compose.yaml` is the default file name which `docker compose` command recognizes if no `-f` flag is provided. This means you can have multiple Docker Compose files if your environment has such requirements. Furthermore, Docker Compose files are... composable (pun intended), so multiple files can be specified on the command line to merge parts of the configuration together. The following list is just a few examples of scenarios where such a feature would be very useful:

- Using a bind mount for the source code for local development but not when running the CI tests;
- Switching between using a pre-built image for the frontend for some API application vs creating a bind mount for source code;
- Adding additional services for integration testing;
- And many more...

You aren't going to cover any of these advanced use cases here.

## Variable substitution in Docker Compose

One of the really cool features of Docker Compose is [variable substitution](/reference/compose-file/interpolation.md). You can see some examples in the Compose file, `environment` section. By means of an example:

- `PGUSER=${PGUSER:-totoro}` means that inside the container, the environment variable `PGUSER` shall be set to the same value as it has on the host machine where Docker Compose is run. If there is no environment variable with this name on the host machine, the variable inside the container gets the default value of `totoro`.
- `PGPASSWORD=${PGPASSWORD:?database password not set}` means that if the environment variable `PGPASSWORD` isn't set on the host, Docker Compose will display an error. This is OK, because you don't want to hard-code default values for the password. You set the password value in the `.env` file, which is local to your machine. It is always a good idea to add `.env` to `.gitignore` to prevent the secrets being checked into the version control.

Other ways of dealing with undefined or empty values exist, as documented in the [variable substitution](/reference/compose-file/interpolation.md) section of the Docker documentation.

## Validating Docker Compose configuration

Before you apply changes made to a Compose configuration file, there is an opportunity to validate the content of the configuration file with the following command:

```console
$ docker compose config
```

When this command is run, Docker Compose reads the file `compose.yaml`, parses it into a data structure in memory, validates where possible, and prints back the reconstruction of that configuration file from its internal representation. If this isn't possible due to errors, Docker prints an error message instead.

## Build and run the application using Docker Compose

Start your application and confirm that it's running.

```console
$ docker compose up --build
```

You passed the `--build` flag so Docker will compile your image and then start it.

> [!NOTE]
>
> Docker Compose is a useful tool, but it has its own quirks. For example, no rebuild is triggered on the update to the source code unless the `--build` flag is provided. It is a very common pitfall to edit one's source code, and forget to use the `--build` flag when running `docker compose up`.

Since your set-up is now run by Docker Compose, it has assigned it a project name, so you get a new volume for your CockroachDB instance. This means that your application will fail to connect to the database, because the database doesn't exist in this new volume. The terminal displays an authentication error for the database:

```text
# ... omitted output ...
rest-server             | 2021/05/10 00:54:25 failed to initialise the store: pq: password authentication failed for user totoro
roach                   | *
roach                   | * INFO: Replication was disabled for this cluster.
roach                   | * When/if adding nodes in the future, update zone configurations to increase the replication factor.
roach                   | *
roach                   | CockroachDB node starting at 2021-05-10 00:54:26.398177 +0000 UTC (took 3.0s)
roach                   | build:               CCL v20.1.15 @ 2021/04/26 16:11:58 (go1.13.9)
roach                   | webui:               http://db:8080
roach                   | sql:                 postgresql://root@db:26257?sslmode=disable
roach                   | RPC client flags:    /cockroach/cockroach <client cmd> --host=db:26257 --insecure
roach                   | logs:                /cockroach/cockroach-data/logs
roach                   | temp dir:            /cockroach/cockroach-data/cockroach-temp349434348
roach                   | external I/O path:   /cockroach/cockroach-data/extern
roach                   | store[0]:            path=/cockroach/cockroach-data
roach                   | storage engine:      rocksdb
roach                   | status:              initialized new cluster
roach                   | clusterID:           b7b1cb93-558f-4058-b77e-8a4ddb329a88
roach                   | nodeID:              1
rest-server exited with code 0
rest-server             | 2021/05/10 00:54:25 failed to initialise the store: pq: password authentication failed for user totoro
rest-server             | 2021/05/10 00:54:26 failed to initialise the store: pq: password authentication failed for user totoro
rest-server             | 2021/05/10 00:54:29 failed to initialise the store: pq: password authentication failed for user totoro
rest-server             | 2021/05/10 00:54:25 failed to initialise the store: pq: password authentication failed for user totoro
rest-server             | 2021/05/10 00:54:26 failed to initialise the store: pq: password authentication failed for user totoro
rest-server             | 2021/05/10 00:54:29 failed to initialise the store: pq: password authentication failed for user totoro
rest-server exited with code 1
# ... omitted output ...
```

Because of the way you set up your deployment using `restart_policy`, the failing container is being restarted every 20 seconds. So, in order to fix the problem, you need to log in to the database engine and create the user. You've done it before in [Configure the database engine](develop-database.md#configure-the-database-engine).

This isn't a big deal. All you have to do is to connect to CockroachDB instance and run the three SQL commands to create the database and the user, as described in [Configure the database engine](develop-database.md#configure-the-database-engine).

So, log in to the database engine from another terminal:

```console
$ docker exec -it roach ./cockroach sql --insecure
```

And run the same commands as before to create the database `mydb`, the user `totoro`, and to grant that user necessary permissions. Once you do that (and the example application container is automatically restarts), the `rest-service` stops failing and restarting and the console goes quiet.

It would have been possible to connect the volume that you had previously used, but for the purposes of this example it's more trouble than it's worth and it also provided an opportunity to show how to introduce resilience into your deployment via the `restart_policy` Compose file feature.

## Testing the application

Now, test your API endpoint. In the new terminal, run the following command:

```console
$ curl http://localhost/
```

You should receive the following response:

```json
Hello, Docker! (0)
```

## Shutting down

To stop the containers started by Docker Compose, press `ctrl+c` in the terminal where you ran `docker compose up`. To remove those containers after they've been stopped, run `docker compose down`.

## Detached mode

You can run containers started by the `docker compose` command in detached mode, just as you would with the `docker` command, by using the `-d` flag.

To start the stack, defined by the Compose file in detached mode, run:

```console
$ docker compose up --build -d
```

Then, you can use `docker compose stop` to stop the containers and `docker compose down` to remove them.

## Further exploration

You can run `docker compose` to see what other commands are available.

## Wrap up

There are some tangential, yet interesting points that were purposefully not covered in this chapter. For the more adventurous reader, this section offers some pointers for further study.

## Persistent storage

A managed volume isn't the only way to provide your container with persistent storage. It is highly recommended to get acquainted with available storage options and their use cases, covered in [Manage data in Docker](/manuals/engine/storage/_index.md).

## CockroachDB clusters

You ran a single instance of CockroachDB, which was enough for this example. But, it's possible to run a CockroachDB cluster, which is made of multiple instances of CockroachDB, each instance running in its own container. Since CockroachDB engine is distributed by design, it would have taken surprisingly little change to your procedure to run a cluster with multiple nodes.

Such distributed set-up offers interesting possibilities, such as applying Chaos Engineering techniques to simulate parts of the cluster failing and evaluating your application's ability to cope with such failures.

If you are interested in experimenting with CockroachDB clusters, check out:

- [Start a CockroachDB Cluster in Docker](https://www.cockroachlabs.com/docs/v20.2/start-a-local-cluster-in-docker-mac.html) article; and
- Documentation for Docker Compose keywords [`deploy`](/reference/compose-file/legacy-versions.md) and [`replicas`](/reference/compose-file/legacy-versions.md).

## Other databases

Since you didn't run a cluster of CockroachDB instances, you might be wondering whether you could have used a non-distributed database engine. The answer is 'yes', and if you were to pick a more traditional SQL database, such as [PostgreSQL](https://www.postgresql.org/), the process described in this chapter would have been very similar.

## Next steps

In this module, you set up a containerized development environment with your application and the database engine running in different containers. You also wrote a Docker Compose file which links the two containers together and provides for easy starting up and tearing down of the development environment.

In the next module, you'll take a look at one possible approach to running functional tests in Docker.
