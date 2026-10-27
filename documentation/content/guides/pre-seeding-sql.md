---
title: "Pre-seed the Postgres database using a SQL script"
description: "Pre-seed the Postgres database using a SQL script"
---

## Setup and context

[Docker Desktop](prerequisites.md#docker-desktop).

[Launch and connect to Postgres](pre-seeding-start.md).

[PostgreSQL shell procedures](postgresql/psql.md).

## Pre-seed the Postgres database using a SQL script

Now that you've familiarized yourself with Postgres, it's time to see how to pre-seed it with sample data. In this demonstration, you'll first create a script that holds SQL commands. The script defines the database, and table structure and inserts sample data. Then you will connect the database to verify the data.

Assuming that you have an existing Postgres database instance up and running, follow these steps to seed the database.

1. Create an empty file named `seed.sql` and add the following content.

   ```sql
   CREATE DATABASE sampledb;

   \c sampledb

   CREATE TABLE users (
     id SERIAL PRIMARY KEY,
     name VARCHAR(50),
     email VARCHAR(100) UNIQUE
   );

   INSERT INTO users (name, email) VALUES
     ('Alpha', 'alpha@example.com'),
     ('Beta', 'beta@example.com'),
     ('Gamma', 'gamma@example.com');  
   ```

   The SQL script creates a new database called `sampledb`, connects to it, and creates a `users` table. The table includes an auto-incrementing `id` as the primary key, a `name` field with a maximum length of 50 characters, and a unique `email` field with up to 100 characters.

   After creating the table, the `INSERT` command inserts three users into the `users` table with their respective names and emails. This setup forms a basic database structure to store user information with unique email addresses.

2. Seed the database.

   It’s time to feed the content of the `seed.sql` directly into the database by using the `<` operator. The command is used to execute a SQL script named `seed.sql` against a Postgres database named `sampledb`. 

   ```console
   $ cat seed.sql | docker exec -i postgres psql -h localhost -U postgres -f-
   ```

   Once the query is executed, you will see the following results:

   ```plaintext
   CREATE DATABASE
   You are now connected to database "sampledb" as user "postgres".
   CREATE TABLE
   INSERT 0 3
   ```

3. Run the following `psql` command to verify if the table named users is populated in the database `sampledb` or not. 

   ```console
   $ docker exec -it postgres psql -h localhost -U postgres sampledb
   ```

   You can now run `\l` in the `psql` shell to list all the databases on the Postgres server.

   ```console
   sampledb=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges
   -----------+----------+----------+------------+------------+------------+-----------------+-----------------------
   postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            |
   sampledb  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            |
   template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
             |          |          |            |            |            |                 | postgres=CTc/postgres
   template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
             |          |          |            |            |            |                 | postgres=CTc/postgres
   (4 rows)
   ```

   To retrieve all the data from the users table, enter the following query:

   ```console
   sampledb=# SELECT * FROM users;
   id | name  |       email
   ----+-------+-------------------
    1 | Alpha | alpha@example.com
    2 | Beta  | beta@example.com
    3 | Gamma | gamma@example.com
   (3 rows)
   ```
  
   Use `\q` or `\quit` to exit from the Postgres interactive shell.
