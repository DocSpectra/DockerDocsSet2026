---
title: Networking and connectivity
description: This module shows how to connect to PostgreSQL in Docker in two common ways; from another container (internal network) and from your host machine (external access).
keywords:
  - Networking PostgreSQL Docker
weight: 30
---

This guide covers two common ways to connect to PostgreSQL running in Docker:

- **Container-to-container**: Connect from your application container to PostgreSQL over a private Docker network. No ports need to be exposed to the host.
- **Host-to-container**: Connect from your laptop or development machine using `localhost` and a published port.

**Prerequisite**: This guide assumes you have PostgreSQL running with persistent storage. If you don't, follow the [Immediate Setup & Data Persistence](/guides/postgresql/immediate-setup-and-data-persistence/) guide first.

## Internal network access (container-to-container)

[Internal network access (container-to-container)](connect-from-containers.md).

## Connecting from the Host (external access)

[Connecting from the Host (external access)](connect-from-host.md).

## Using Docker Compose for networking

[Using Docker Compose for networking](compose-networking.md).

## Troubleshooting

[Troubleshooting](connection-troubleshooting.md).
