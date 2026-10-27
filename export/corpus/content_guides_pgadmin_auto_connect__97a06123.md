---
title: "Configuring pgAdmin to auto-connect to the database"
description: "Configuring pgAdmin to auto-connect to the database"
---

## Setup and context

[Add pgAdmin to the stack](add-pgadmin.md).

[pgAdmin and PostgreSQL development](pgadmin-context.md).

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## Configuring pgAdmin to auto-connect to the database

Although you have pgAdmin running, it would be nice if you could simply open the app without needing to configure the database connection. Reducing the setup steps would be a great way to make it easier for teammates to get value from this tool.

Fortunately, there is an ability to auto-connect to the database.

> [!WARNING]
>
> In order to auto-connect, the database credentials are shared using plaintext files. During local development, this is often acceptable as local data is not real customer data.
> However, if you are using production or sensitive data, this practice is strongly discouraged.

1. First, you need to define the server itself, which pgAdmin does using a `servers.json` file. 

    Add the following to your `compose.yaml` file to define a config file for the `servers.json` file:

    ```yaml
    configs:
      pgadmin-servers:
        content: |
          {
            "Servers": {
              "1": {
                "Name": "Local Postgres",
                "Group": "Servers",
                "Host": "postgres",
                "Port": 5432,
                "MaintenanceDB": "postgres",
                "Username": "postgres",
                "PassFile": "/config/pgpass"
              }
            }
          }
    ```

2. The `servers.json` file defines a `PassFile` field, which is a reference to a [postgreSQL password files](https://www.postgresql.org/docs/current/libpq-pgpass.html). These are often referred to as a pgpass file.

    Add the following config to your `compose.yaml` file to define a pgpass file:

    ```yaml
    config:
      pgadmin-pgpass:
        content: |
          postgres:5432:*:postgres:secret
    ```

    This will indicate any connection requests to `postgres:5432` using the username `postgres` should provide a password of `secret`.

3. In your `compose.yaml`, update the `pgadmin` service to inject the config files:

    ```yaml
    services:
      pgadmin:
        ...
        configs:
          - source: pgadmin-pgpass
            target: /config/pgpass
            uid: "5050"
            gid: "5050"
            mode: 0400
          - source: pgadmin-servers
            target: /pgadmin4/servers.json
            mode: 0444
    ```

4. Update the application stack by running `docker compose up` again:

    ```console
    $ docker compose up
    ```

5. Once the application is restarted, open your browser to http://localhost:5050. You should be able to access the database without any logging in or configuration.
