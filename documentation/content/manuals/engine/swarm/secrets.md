---
title: Manage sensitive data with Docker secrets
description: How to securely store, retrieve, and use sensitive data with Docker services
keywords: swarm, secrets, credentials, sensitive strings, sensitive data, security,
  encryption, encryption at rest
tags: [Secrets]
---

## About secrets

See [Docker secret lifecycle and platform support](secrets-context.md).

### Windows support

See [Secret support on Windows](secrets-context.md#windows-support).

## How Docker manages secrets

See [Secret storage, access, and lifecycle](secrets-context.md#how-docker-manages-secrets).

See [Rotate a secret](secrets.md#example-rotate-a-secret) for a way to remove a secret without disrupting running services.

## Read more about `docker secret` commands

Use these links to read about specific commands, or continue to the
[example about using secrets with a service](secrets.md#simple-example-get-started-with-secrets).

- [`docker secret create`](/reference/cli/docker/secret/create/)
- [`docker secret inspect`](/reference/cli/docker/secret/inspect/)
- [`docker secret ls`](/reference/cli/docker/secret/ls/)
- [`docker secret rm`](/reference/cli/docker/secret/rm/)
- [`--secret`](/reference/cli/docker/service/create/#secret) flag for `docker service create`
- [`--secret-add` and `--secret-rm`](/reference/cli/docker/service/update/#secret-add) flags for `docker service update`

## Examples

This section includes three graduated examples which illustrate how to use
Docker secrets. The images used in these examples have been updated to make it
easier to use Docker secrets. To find out how to modify your own images in
a similar way, see
[Build support for Docker Secrets into your images](#build-support-for-docker-secrets-into-your-images).

> [!NOTE]
>
> These examples use a single-Engine swarm and unscaled services for
> simplicity. The examples use Linux containers, but Windows containers also
> support secrets. See [Windows support](#windows-support).

### Defining and using secrets in compose files

Both the `docker-compose` and `docker stack` commands support defining secrets
in a compose file. See
[the Compose file reference](/reference/compose-file/legacy-versions.md) for details.

### Simple example: Get started with secrets

See [Use a secret with Redis](secrets-redis.md).

### Simple example: Use secrets in a Windows service

See [Use a secret with IIS on Windows](secrets-windows.md).

### Intermediate example: Use secrets with a Nginx service

See [Use TLS secrets with Nginx](secrets-nginx.md).

#### Generate the site certificate

See [Generate the site certificate](secrets-nginx.md#generate-the-site-certificate).

#### Configure the Nginx container

See [Configure Nginx](secrets-nginx.md#configure-the-nginx-container).

### Advanced example: Use secrets with a WordPress service

In this example, you create a single-node MySQL service with a custom root
password, add the credentials as secrets, and create a single-node WordPress
service which uses these credentials to connect to MySQL. The
[next example](#example-rotate-a-secret) builds on this one and shows you how to
rotate the MySQL password and update the services so that the WordPress service
can still connect to MySQL.

This example illustrates some techniques to use Docker secrets to avoid saving
sensitive credentials within your image or passing them directly on the command
line.

> [!NOTE]
>
> This example uses a single-Engine swarm for simplicity, and uses a
> single-node MySQL service because a single MySQL server instance cannot be
> scaled by simply using a replicated service, and setting up a MySQL cluster is
> beyond the scope of this example.
>
> Also, changing a MySQL root passphrase isn’t as simple as changing
> a file on disk. You must use a query or a `mysqladmin` command to change the
> password in MySQL.

1.  Generate a random alphanumeric password for MySQL and store it as a Docker
    secret with the name `mysql_password` using the `docker secret create`
    command. To make the password shorter or longer, adjust the last argument of
    the `openssl` command. This is just one way to create a relatively random
    password. You can use another command to generate the password if you
    choose.

    > [!NOTE]
    >
    > After you create a secret, you cannot update it. You can only
    > remove and re-create it, and you cannot remove a secret that a service is
    > using. However, you can grant or revoke a running service's access to
    > secrets using `docker service update`. If you need the ability to update a
    > secret, consider adding a version component to the secret name, so that you
    > can later add a new version, update the service to use it, then remove the
    > old version.

    The last argument is set to `-`, which indicates that the input is read from
    standard input.

    ```console
    $ openssl rand -base64 20 | docker secret create mysql_password -

    l1vinzevzhj4goakjap5ya409
    ```

    The value returned is not the password, but the ID of the secret. In the
    remainder of this tutorial, the ID output is omitted.

    Generate a second secret for the MySQL `root` user. This secret isn't
    shared with the WordPress service created later. It's only needed to
    bootstrap the `mysql` service.

    ```console
    $ openssl rand -base64 20 | docker secret create mysql_root_password -
    ```

    List the secrets managed by Docker using `docker secret ls`:

    ```console
    $ docker secret ls

    ID                          NAME                  CREATED             UPDATED
    l1vinzevzhj4goakjap5ya409   mysql_password        41 seconds ago      41 seconds ago
    yvsczlx9votfw3l0nz5rlidig   mysql_root_password   12 seconds ago      12 seconds ago
    ```

    The secrets are stored in the encrypted Raft logs for the swarm.

2.  Create a user-defined overlay network which is used for communication
    between the MySQL and WordPress services. There is no need to expose the
    MySQL service to any external host or container.

    ```console
    $ docker network create -d overlay mysql_private
    ```

3.  Create the MySQL service. The MySQL service has the following
    characteristics:

    - Because the scale is set to `1`, only a single MySQL task runs.
      Load-balancing MySQL is left as an exercise to the reader and involves
      more than just scaling the service.
    - Only reachable by other containers on the `mysql_private` network.
    - Uses the volume `mydata` to store the MySQL data, so that it persists
      across restarts to the `mysql` service.
    - The secrets are each mounted in a `tmpfs` filesystem at
      `/run/secrets/mysql_password` and `/run/secrets/mysql_root_password`.
      They are never exposed as environment variables, nor can they be committed
      to an image if the `docker commit` command is run. The `mysql_password`
      secret is the one used by the non-privileged WordPress container to
      connect to MySQL.
    - Sets the environment variables `MYSQL_PASSWORD_FILE` and
      `MYSQL_ROOT_PASSWORD_FILE` to point to the
      files `/run/secrets/mysql_password` and `/run/secrets/mysql_root_password`.
      The `mysql` image reads the password strings from those files when
      initializing the system database for the first time. Afterward, the
      passwords are stored in the MySQL system database itself.
    - Sets environment variables `MYSQL_USER` and `MYSQL_DATABASE`. A new
      database called `wordpress` is created when the container starts, and the
      `wordpress` user has full permissions for this database only. This
      user cannot create or drop databases or change the MySQL
      configuration.

      ```console
      $ docker service create \
           --name mysql \
           --replicas 1 \
           --network mysql_private \
           --mount type=volume,source=mydata,destination=/var/lib/mysql \
           --secret source=mysql_root_password,target=mysql_root_password \
           --secret source=mysql_password,target=mysql_password \
           -e MYSQL_ROOT_PASSWORD_FILE="/run/secrets/mysql_root_password" \
           -e MYSQL_PASSWORD_FILE="/run/secrets/mysql_password" \
           -e MYSQL_USER="wordpress" \
           -e MYSQL_DATABASE="wordpress" \
           mysql:latest
      ```

4.  Verify that the `mysql` container is running using the `docker service ls` command.

    ```console
    $ docker service ls

    ID            NAME   MODE        REPLICAS  IMAGE
    wvnh0siktqr3  mysql  replicated  1/1       mysql:latest
    ```

5.  Now that MySQL is set up, create a WordPress service that connects to the
    MySQL service. The WordPress service has the following characteristics:

    - Because the scale is set to `1`, only a single WordPress task runs.
      Load-balancing WordPress is left as an exercise to the reader, because of
      limitations with storing WordPress session data on the container
      filesystem.
    - Exposes WordPress on port 30000 of the host machine, so that you can access
      it from external hosts. You can expose port 80 instead if you do not have
      a web server running on port 80 of the host machine.
    - Connects to the `mysql_private` network so it can communicate with the
      `mysql` container, and also publishes port 80 to port 30000 on all swarm
      nodes.
    - Has access to the `mysql_password` secret, but specifies a different
      target file name within the container. The WordPress container uses
      the mount point `/run/secrets/wp_db_password`.
    - Sets the environment variable `WORDPRESS_DB_PASSWORD_FILE` to the file
      path where the secret is mounted. The WordPress service reads the
      MySQL password string from that file and add it to the `wp-config.php`
      configuration file.
    - Connects to the MySQL container using the username `wordpress` and the
      password in `/run/secrets/wp_db_password` and creates the `wordpress`
      database if it does not yet exist.
    - Stores its data, such as themes and plugins, in a volume called `wpdata`
      so these files  persist when the service restarts.

    ```console
    $ docker service create \
         --name wordpress \
         --replicas 1 \
         --network mysql_private \
         --publish published=30000,target=80 \
         --mount type=volume,source=wpdata,destination=/var/www/html \
         --secret source=mysql_password,target=wp_db_password \
         -e WORDPRESS_DB_USER="wordpress" \
         -e WORDPRESS_DB_PASSWORD_FILE="/run/secrets/wp_db_password" \
         -e WORDPRESS_DB_HOST="mysql:3306" \
         -e WORDPRESS_DB_NAME="wordpress" \
         wordpress:latest
    ```

6.  Verify the service is running using `docker service ls` and
    `docker service ps` commands.

    ```console
    $ docker service ls

    ID            NAME       MODE        REPLICAS  IMAGE
    wvnh0siktqr3  mysql      replicated  1/1       mysql:latest
    nzt5xzae4n62  wordpress  replicated  1/1       wordpress:latest
    ```

    ```console
    $ docker service ps wordpress

    ID            NAME         IMAGE             NODE  DESIRED STATE  CURRENT STATE           ERROR  PORTS
    aukx6hgs9gwc  wordpress.1  wordpress:latest  moby  Running        Running 52 seconds ago   
    ```

    At this point, you could actually revoke the WordPress service's access to
    the `mysql_password` secret, because WordPress has copied the secret to its
    configuration file `wp-config.php`. Don't do that for now, because we
    use it later to facilitate rotating the MySQL password.

7.  Access `http://localhost:30000/` from any swarm node and set up WordPress
    using the web-based wizard. All of these settings are stored in the MySQL
    `wordpress` database. WordPress automatically generates a password for your
    WordPress user, which is completely different from the password WordPress
    uses to access MySQL. Store this password securely, such as in a password
    manager. You need it to log into WordPress after
    [rotating the secret](#example-rotate-a-secret).

    Go ahead and write a blog post or two and install a WordPress plugin or
    theme to verify that WordPress is fully operational and its state is saved
    across service restarts.

8.  Do not clean up any services or secrets if you intend to proceed to the next
    example, which demonstrates how to rotate the MySQL root password.

### Example: Rotate a secret

This example builds upon the previous one. In this scenario, you create a new
secret with a new MySQL password, update the `mysql` and `wordpress` services to
use it, then remove the old secret.

> [!NOTE]
>
> Changing the password on a MySQL database involves running extra
> queries or commands, as opposed to just changing a single environment variable
> or a file, since the image only sets the MySQL password if the database doesn’t
> already exist, and MySQL stores the password within a MySQL database by default.
> Rotating passwords or other secrets may involve additional steps outside of
> Docker.

1.  Create the new password and store it as a secret named `mysql_password_v2`.

    ```console
    $ openssl rand -base64 20 | docker secret create mysql_password_v2 -
    ```

2.  Update the MySQL service to give it access to both the old and new secrets.
    Remember that you cannot update or rename a secret, but you can revoke a
    secret and grant access to it using a new target filename.

    ```console
    $ docker service update \
         --secret-rm mysql_password mysql

    $ docker service update \
         --secret-add source=mysql_password,target=old_mysql_password \
         --secret-add source=mysql_password_v2,target=mysql_password \
         mysql
    ```

    Updating a service causes it to restart, and when the MySQL service restarts
    the second time, it has access to the old secret under
    `/run/secrets/old_mysql_password` and the new secret under
    `/run/secrets/mysql_password`.

    Even though the MySQL service has access to both the old and new secrets
    now, the MySQL password for the WordPress user has not yet been changed.

    > [!NOTE]
    >
    > This example does not rotate the MySQL `root` password.

3.  Now, change the MySQL password for the `wordpress` user using the
    `mysqladmin` CLI. This command reads the old and new password from the files
    in `/run/secrets` but does not expose them on the command line or save them
    in the shell history.

    Do this quickly and move on to the next step, because WordPress loses
    the ability to connect to MySQL.

    First, find the ID of the `mysql` container task.

    ```console
    $ docker ps --filter name=mysql -q

    c7705cf6176f
    ```

    Substitute the ID in the command below, or use the second variant which
    uses shell expansion to do it all in a single step.

    ```console
    $ docker container exec <CONTAINER_ID> \
        bash -c 'mysqladmin --user=wordpress --password="$(< /run/secrets/old_mysql_password)" password "$(< /run/secrets/mysql_password)"'
    ```

    Or:

    ```console
    $ docker container exec $(docker ps --filter name=mysql -q) \
        bash -c 'mysqladmin --user=wordpress --password="$(< /run/secrets/old_mysql_password)" password "$(< /run/secrets/mysql_password)"'
    ```

4.  Update the `wordpress` service to use the new password, keeping the target
    path at `/run/secrets/wp_db_password`. This triggers a rolling restart of
    the WordPress service and the new secret is used.

    ```console
    $ docker service update \
         --secret-rm mysql_password \
         --secret-add source=mysql_password_v2,target=wp_db_password \
         wordpress    
    ```

5.  Verify that WordPress works by browsing to http://localhost:30000/ on any
    swarm node again. Use the WordPress username and password
    from when you ran through the WordPress wizard in the previous task.

    Verify that the blog post you wrote still exists, and if you changed any
    configuration values, verify that they are still changed.

6.  Revoke access to the old secret from the MySQL service and
    remove the old secret from Docker.

    ```console
    $ docker service update \
         --secret-rm mysql_password \
         mysql

    $ docker secret rm mysql_password
    ```


7.  Run the following commands to remove the WordPress service, the MySQL container,
    the `mydata` and `wpdata` volumes, and the Docker secrets:

    ```console
    $ docker service rm wordpress mysql

    $ docker volume rm mydata wpdata

    $ docker secret rm mysql_password_v2 mysql_root_password
    ```

## Build support for Docker Secrets into your images

If you develop a container that can be deployed as a service and requires
sensitive data, such as a credential, as an environment variable, consider
adapting your image to take advantage of Docker secrets. One way to do this is
to ensure that each parameter you pass to the image when creating the container
can also be read from a file.

Many of the Docker Official Images in the
[Docker library](https://github.com/docker-library/), such as the
[wordpress](https://github.com/docker-library/wordpress/)
image used in the above examples, have been updated in this way.

When you start a WordPress container, you provide it with the parameters it
needs by setting them as environment variables. The WordPress image has been
updated so that the environment variables which contain important data for
WordPress, such as `WORDPRESS_DB_PASSWORD`, also have variants which can read
their values from a file (`WORDPRESS_DB_PASSWORD_FILE`). This strategy ensures
that backward compatibility is preserved, while allowing your container to read
the information from a Docker-managed secret instead of being passed directly.

> [!NOTE]
>
> Docker secrets do not set environment variables directly. This was a
> conscious decision, because environment variables can unintentionally be leaked
> between containers (for instance, if you use `--link`).

## Use Secrets in Compose

```yaml

services:
   db:
     image: mysql:latest
     volumes:
       - db_data:/var/lib/mysql
     environment:
       MYSQL_ROOT_PASSWORD_FILE: /run/secrets/db_root_password
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD_FILE: /run/secrets/db_password
     secrets:
       - db_root_password
       - db_password

   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     ports:
       - "8000:80"
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD_FILE: /run/secrets/db_password
     secrets:
       - db_password


secrets:
   db_password:
     file: db_password.txt
   db_root_password:
     file: db_root_password.txt

volumes:
    db_data:
```

This example creates a simple WordPress site using two secrets in
a Compose file.

The top-level element `secrets` defines two secrets `db_password` and
`db_root_password`.

When deploying, Docker creates these two secrets and populates them with the
content from the file specified in the Compose file.

The `db` service uses both secrets, and `wordpress` is using one.

When you deploy, Docker mounts a file under `/run/secrets/<secret_name>` in the
services. These files are never persisted on disk, but are managed in memory.

Each service uses environment variables to specify where the service should look
for that secret data.

More information on short and long syntax for secrets can be found in the
[Compose Specification](/reference/compose-file/secrets.md).
