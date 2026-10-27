---
title: "Pre-seed the database by bind-mounting a SQL script"
description: "Pre-seed the database by bind-mounting a SQL script"
---

## Setup and context

[Docker Desktop](prerequisites.md#docker-desktop).

[Launch and connect to Postgres](pre-seeding-start.md).

[PostgreSQL initialization behavior and existing-data caveat](postgresql/initialization.md).

[Volumes](/manuals/engine/storage/volumes.md) and [networking in Compose](/manuals/compose/how-tos/networking.md).

## Pre-seed the database by bind-mounting a SQL script

In Docker, mounting refers to making files or directories from the host system accessible within a container. This let you to share data or configuration files between the host and the container, enabling greater flexibility and persistence.

Now that you have learned how to launch Postgres and pre-seed the database using an SQL script, it’s time to learn how to mount an SQL file directly into the Postgres containers’ initialization directory (`/docker-entrypoint-initdb.d`). The `/docker-entrypoint-initdb.d` is a special directory in PostgreSQL Docker containers that is used for initializing the database when the container is first started

Make sure you stop any running Postgres containers (along with volumes) to prevent port conflicts before you follow the steps:

```console
$ docker container stop postgres
```

1. Modify the `seed.sql` with the following entries:

   ```sql
   CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE
   );

   INSERT INTO users (name, email) VALUES
    ('Alpha', 'alpha@example.com'),
    ('Beta', 'beta@example.com'),
    ('Gamma', 'gamma@example.com')
   ON CONFLICT (email) DO NOTHING;
   ```
   
2. Create a text file named `Dockerfile` and copy the following content.

   ```plaintext
   # syntax=docker/dockerfile:1
   FROM postgres:18
   COPY seed.sql /docker-entrypoint-initdb.d/
   ```

   This Dockerfile copies the `seed.sql` script directly into the PostgreSQL container's initialization directory.
   

3. Use Docker Compose.
   
   Using Docker Compose makes it even easier to manage and deploy the PostgreSQL container with the seeded database. This compose.yml file defines a Postgres service named `db` using the latest Postgres image, which sets up a database with the name `sampledb`, along with a user `postgres` and a password `mysecretpassword`. 

   ```yaml
   services:
     db:
       build:
         context: .
         dockerfile: Dockerfile
       container_name: my_postgres_db
       environment:
         POSTGRES_USER: postgres
         POSTGRES_PASSWORD: mysecretpassword
         POSTGRES_DB: sampledb
       ports:
         - "5432:5432"
       volumes:
         - data_sql:/var/lib/postgresql   # Persistent data storage

   volumes:
     data_sql:
    ```
  
    It maps port `5432` on the host to the container's `5432`, let you access to the Postgres database from outside the container. It also define `data_sql` for persisting the database data, ensuring that data is not lost when the container is stopped.

    It is important to note that the port mapping to the host is only necessary if you want to connect to the database from non-containerized programs. If you containerize the service that connects to the DB, you should connect to the database over a custom bridge network.

4.  Bring up the Compose service.

    Assuming that you've placed the `seed.sql` file in the same directory as the Dockerfile, execute the following command:

    ```console
    $ docker compose up -d --build
    ```

5.  It’s time to verify if the table `users` get populated with the data. 

    ```console
    $ docker exec -it my_postgres_db psql -h localhost -U postgres sampledb
    ```

    ```sql 
    sampledb=# SELECT * FROM users;
      id | name  |       email
    ----+-------+-------------------
       1 | Alpha | alpha@example.com
       2 | Beta  | beta@example.com
       3 | Gamma | gamma@example.com
     (3 rows)

    sampledb=#
    ```
