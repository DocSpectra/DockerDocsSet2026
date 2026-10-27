---
description: Visualizing your PostgreSQL databases with pgAdmin
keywords: pgadmin, container-supported development
title: Visualizing your PostgreSQL databases with pgAdmin
linktitle: Visualizing your PostgreSQL databases with pgAdmin
summary: |
  Explore how to add pgAdmin to your development stack and make it as easy as possible for your teammates to navigate through your PostgreSQL databases.
tags: [databases]
params:
  time: 10 minutes
---

[pgAdmin and PostgreSQL development](pgadmin-context.md).

In this guide you will learn how to:

1. Add pgAdmin to your application stack
2. Configure pgAdmin to automatically connect to the development database

## Adding pgAdmin to your stack

[Adding pgAdmin to your stack](add-pgadmin.md).

## Configuring pgAdmin to auto-connect to the database

[Configuring pgAdmin to auto-connect to the database](pgadmin-auto-connect.md).

## Conclusion

Using containers makes it easy to not only run your application's dependencies, but also additional tools to help with troubleshooting and debugging. 

When you add tools, think about the experience and possible friction your teammates might experience and how you might be able to remove it. In this case, you were able to take an extra step to add configuration to automatically configure and connect the databases, saving your teammates valuable time.
