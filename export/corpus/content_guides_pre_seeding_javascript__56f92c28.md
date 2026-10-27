---
title: "Pre-seed the database using JavaScript code"
description: "Pre-seed the database using JavaScript code"
---

## Setup and context

[Docker Desktop](prerequisites.md#docker-desktop).

[Launch and connect to Postgres](pre-seeding-start.md).

Database setup: [SQL script](pre-seeding-sql.md) or [Dockerfile and Compose](pre-seeding-image.md).

[PostgreSQL shell procedures](postgresql/psql.md).

## Pre-seed the database using JavaScript code


Now that you have learned how to seed the database using various methods like SQL script, mounting volumes etc., it's time to try to achieve it using JavaScript code. 

1. Create a .env file with the following:

   ```plaintext
   POSTGRES_USER=postgres
   POSTGRES_DB_HOST=localhost
   POSTGRES_DB=sampledb
   POSTGRES_PASSWORD=mysecretpassword
   POSTGRES_PORT=5432
   ```

2. Create a new JavaScript file called seed.js with the following content:

   The following JavaScript code imports the `dotenv` package which is used to load environment variables from an `.env` file. The `.config()` method reads the `.env` file and sets the environment variables as properties of the `process.env` object. This let you to securely store sensitive information like database credentials outside of your code.

   Then, it creates a new Pool instance from the pg library, which provides a connection pool for efficient database interactions. The `seedData` function is defined to perform the database seeding operations.
It is called at the end of the script to initiate the seeding process. The try...catch...finally block is used for error handling. 

   ```plaintext
   require('dotenv').config();  // Load environment variables from .env file
   const { Pool } = require('pg');

   // Create a new pool using environment variables
   const pool = new Pool({
     user: process.env.POSTGRES_USER,
     host: process.env.POSTGRES_DB_HOST,
     database: process.env.POSTGRES_DB,
     port: process.env.POSTGRES_PORT,
     password: process.env.POSTGRES_PASSWORD,
   });

   const seedData = async () => {
     try {
        // Drop the table if it already exists (optional)
        await pool.query(`DROP TABLE IF EXISTS todos;`);

        // Create the table with the correct structure
        await pool.query(`
          CREATE TABLE todos (
            id SERIAL PRIMARY KEY,
            task VARCHAR(255) NOT NULL,
            completed BOOLEAN DEFAULT false
              );
        `   );

        // Insert seed data
        await pool.query(`
          INSERT INTO todos (task, completed) VALUES
          ('Watch netflix', false),
          ('Finish podcast', false),
          ('Pick up kid', false);
          `);
          console.log('Database seeded successfully!');
        } catch (err) {
          console.error('Error seeding the database', err);
        } finally {
          pool.end();
       }
     };

     // Call the seedData function to run the script
     seedData();
     ```

3.  Kick off the seeding process

    ```console
    $ node seed.js
    ```

    You should see the following command:

    ```plaintext
    Database seeded successfully!
    ```

4.  Verify if the database is seeded correctly:

    ```console
    $ docker exec -it postgres psql -h localhost -U postgres sampledb
    ```

    ```console
    sampledb=# SELECT * FROM todos;
    id |      task      | completed
    ----+----------------+-----------
    1 | Watch netflix  | f
    2 | Finish podcast | f
    3 | Pick up kid    | f
    (3 rows)  
    ```
