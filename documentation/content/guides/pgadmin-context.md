---
title: "pgAdmin and PostgreSQL development"
description: "pgAdmin and PostgreSQL development"
---

Many applications use PostgreSQL databases in the application stack. However, not all developers are knowledgeable about navigating and working with PostgreSQL databases.

Fortunately, when you use containers in development, it is easy to add additional services to help with troubleshooting and debugging.

The [pgAdmin](https://www.pgadmin.org/) tool is a popular open-source tool designed to help administer and visualize PostgreSQL databases.

## pgAdmin in containers

pgAdmin 4 is the industry-standard open source management tool for PostgreSQL. When deployed in Docker, it typically runs in **Server Mode**, providing a multi-user web interface to manage one or more database instances.

While you can accomplish everything from the command line using `psql`, a visual interface significantly simplifies writing complex queries, visualizing table structures, and exploring database objects.

### Key considerations

When running pgAdmin in Docker, keep these points in mind:

- **Image**: Use the official `dpage/pgadmin4` image
- **Networking**: In a Docker Compose environment, pgAdmin connects to the database using the internal service name (for example, `db:5432`) rather than `localhost`
