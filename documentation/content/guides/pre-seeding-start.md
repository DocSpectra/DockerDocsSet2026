---
title: "Launching Postgres"
description: "Launching Postgres"
---

## Setup and context

[Docker Desktop](prerequisites.md#docker-desktop).

## Launching Postgres

Launch a quick demo of Postgres by using the following steps:

1. Open the terminal and run the following command to start a Postgres container.

   This example will launch a Postgres container, expose port `5432` onto the host to let a native-running application to connect to it with the password `mysecretpassword`.

   ```console
   $ docker run -d --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword postgres
   ```

2. Verify that Postgres is up and running by selecting the container and checking the logs on Docker Dashboard.

   ```plaintext
   PostgreSQL Database directory appears to contain a database; Skipping initialization
 
   2024-09-08 09:09:47.136 UTC [1] LOG:  starting PostgreSQL 16.4 (Debian 16.4-1.pgdg120+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
   2024-09-08 09:09:47.137 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
   2024-09-08 09:09:47.137 UTC [1] LOG:  listening on IPv6 address "::", port 5432
   2024-09-08 09:09:47.139 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
   2024-09-08 09:09:47.142 UTC [29] LOG:  database system was shut down at 2024-09-08 09:07:09 UTC
   2024-09-08 09:09:47.148 UTC [1] LOG:  database system is ready to accept connections
   ```

3. Connect to Postgres from the local system.

   The `psql` is the PostgreSQL interactive shell that is used to connect to a Postgres database and let you start executing SQL commands. Assuming that you already have `psql` utility installed on your local system, it's time to connect to the Postgres database. Run the following command on your local terminal:

   ```console
   $ docker exec -it postgres psql -h localhost -U postgres
   ```

   You can now execute any SQL queries or commands you need within the `psql` prompt.

   Use `\q` or `\quit` to exit from the Postgres interactive shell.
