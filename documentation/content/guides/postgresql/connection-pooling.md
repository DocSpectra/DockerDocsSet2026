---
title: "PostgreSQL connection pooling and pooling modes"
description: "PostgreSQL connection pooling and pooling modes"
---

## PgBouncer: Lightweight connection pooling

PostgreSQL creates a new process for every client connection, which consumes significant RAM. What happens when you have 1,000 concurrent users? PgBouncer solves exactly this problem.

PgBouncer is a lightweight proxy that pools connections, allowing thousands of applications to share a small number of actual database backends. Think of it as a traffic controller: everyone wants to pass through simultaneously, but the controller regulates the flow to prevent congestion.

### Pooling modes

PgBouncer offers three distinct pooling modes:

| Mode | Description | Use case |
|------|-------------|----------|
| **Session** | Connection assigned for entire session duration | Long-lived connections, session variables |
| **Transaction** | Connection returned after each transaction ends | Web applications, microservices (most common) |
| **Statement** | Connection returned after every SQL statement | Simple queries, no multi-statement transactions |

### When to use PgBouncer

PgBouncer becomes essential when you encounter:

- "too many connections" errors
- High memory consumption due to connection overhead
- Many short-lived connections (web applications, serverless functions)
- Need to serve thousands of clients with limited database connections
