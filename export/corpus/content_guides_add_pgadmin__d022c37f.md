---
title: "Adding pgAdmin to your stack"
description: "Adding pgAdmin to your stack"
---

## Setup and context

[pgAdmin and PostgreSQL development](pgadmin-context.md).

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## Adding pgAdmin to your stack

1. In your `compose.yaml` file, add the `pgadmin` service next to your existing `postgres` service:

    ```yaml
    services:
      postgres:
        image: postgres:18
        environment:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: secret
          POSTGRES_DB: demo

      pgadmin:
        image: dpage/pgadmin4:9.8
        ports:
          - 5050:80
        environment:
          # Required by pgAdmin
          PGADMIN_DEFAULT_EMAIL: demo@example.com
          PGADMIN_DEFAULT_PASSWORD: secret

          # Don't require the user to login
          PGADMIN_CONFIG_SERVER_MODE: 'False'

          # Don't require a "master" password after logging in
          PGADMIN_CONFIG_MASTER_PASSWORD_REQUIRED: 'False'
    ```

2. Start the Compose stack with the following command:

    ```console
    $ docker compose up
    ```

    After the image is downloaded the container starts, you will see output that looks similar to the following indicating pgAdmin is ready:

    ```console
    pgadmin-1   | [2025-09-22 15:52:47 +0000] [1] [INFO] Starting gunicorn 23.0.0
    pgadmin-1   | [2025-09-22 15:52:47 +0000] [1] [INFO] Listening at: http://[::]:80 (1)
    pgadmin-1   | [2025-09-22 15:52:47 +0000] [1] [INFO] Using worker: gthread
    pgadmin-1   | [2025-09-22 15:52:47 +0000] [119] [INFO] Booting worker with pid: 119
    ```

3. Open pgAdmin by going to http://localhost:5050.

4. Once in the admin panel, select the **Add New Server** link to define a new server. Enter the following details:

    - **General** tab:
        - **Name**: `postgres`
    - **Connection** tab:
        - **Host name/address**: `postgres`
        - **Username**: `postgres`
        - **Password**: `secret`
        - Enable the **Save password?** field

    > [!IMPORTANT]
    >
    > These connection details assume you are using the previous Compose file snippet. If you are using an existing Compose file,
    > adjust the connection details as required. The **Host name/address** field should match the name of your postgres service.

5. Select the **Save** button to create the new database.

You now have pgAdmin setup and connected to your containerized database. Feel free to navigate around, view the tables, and explore your database.
