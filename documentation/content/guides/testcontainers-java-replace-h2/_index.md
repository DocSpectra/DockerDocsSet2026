---
title: Replace H2 with a real database for testing
linkTitle: Replace H2 database
description: Learn how to replace an H2 in-memory database with a real PostgreSQL database for testing using Testcontainers.
keywords: testcontainers, java, testing, h2, postgresql, spring boot, spring data jpa, jdbc
summary: |
  Replace your H2 in-memory test database with a real PostgreSQL instance
  using the Testcontainers special JDBC URL — a one-line change.
toc_min: 1
toc_max: 2
tags: [testing-with-docker]
languages: [java]
params:
  time: 15 minutes
---

[All Testcontainers guides](/testcontainers/#guides)

<!-- Source: https://github.com/testcontainers/tc-guide-replace-h2-with-real-database-for-testing -->

In this guide, you will learn how to:

- Understand the drawbacks of using H2 in-memory databases for testing
- Replace H2 with a real PostgreSQL database using the Testcontainers special JDBC URL
- Use the Testcontainers JUnit 5 extension for more control over the container
- Test both Spring Data JPA and JdbcTemplate-based repositories

## Prerequisites

- Java 17+
- Maven or Gradle
- A Docker environment supported by Testcontainers

> [!NOTE]
> If you're new to Testcontainers, visit the
> [Testcontainers overview](https://testcontainers.com/getting-started/) to learn more about
> Testcontainers and the benefits of using it.

## Guide steps

1. [The H2 problem](/guides/testcontainers-java-replace-h2/problem-with-h2/)
2. [JDBC URL approach](/guides/testcontainers-java-replace-h2/jdbc-url-approach/)
3. [JUnit 5 extension](/guides/testcontainers-java-replace-h2/junit-extension-approach/)

## Find a specific task

- [Initialize the database with a script](/guides/testcontainers-java-replace-h2/jdbc-url-approach/#initialize-the-database-with-a-script)
- [Test JdbcTemplate-based repositories](/guides/testcontainers-java-replace-h2/jdbc-url-approach/#testing-jdbctemplate-based-repositories)
