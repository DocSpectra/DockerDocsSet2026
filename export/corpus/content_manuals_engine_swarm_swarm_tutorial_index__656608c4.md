---
description: Getting Started tutorial for Docker Engine Swarm mode
keywords: tutorial, cluster management, swarm mode, docker engine, get started
title: Getting started with Swarm mode
toc_max: 4
---

This tutorial introduces you to the features of Docker Engine Swarm mode. You
may want to familiarize yourself with the [key concepts](../key-concepts.md)
before you begin.

The tutorial guides you through:

* Initializing a cluster of Docker Engines in swarm mode
* Adding nodes to the swarm
* Deploying application services to the swarm
* Managing the swarm once you have everything running

This tutorial uses Docker Engine CLI commands entered on the command line of a
terminal window.

If you are brand new to Docker, see [About Docker Engine](../../_index.md).

## Set up

Read [Swarm host and network prerequisites](../prerequisites.md) before starting the tutorial.

### Three networked host machines

See [Host machines](../prerequisites.md#three-networked-host-machines).

#### Install Docker Engine on Linux machines

See [Install Docker Engine on Linux](../prerequisites.md#install-docker-engine-on-linux-machines).

### The IP address of the manager machine

See [Manager IP address](../prerequisites.md#the-ip-address-of-the-manager-machine).

### Open protocols and ports between the hosts

See [Required ports and network hardening](../prerequisites.md#open-protocols-and-ports-between-the-hosts).

## Next steps

Next, you'll create a swarm. 

{{< button text="Create a swarm" url="create-swarm.md" >}}
