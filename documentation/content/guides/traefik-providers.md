---
title: "Traefik providers and routing labels"
description: "Traefik providers and routing labels"
---

## Docker provider

One of the unique features of Traefik is its ability to be configured in many ways. When using the Docker provider, Traefik gets its configuration from other running containers using [labels](https://docs.docker.com/config/labels-custom-metadata/). Traefik will watch engine events (for container starts and stops), extract the labels, and update its configuration.

While there are [many Traefik-monitored labels](https://doc.traefik.io/traefik/routing/providers/docker/), the two most common will be:

- `traefik.http.routers.<service-name>.rule` - used to indicate the routing rule ([view all of the available rules here](https://doc.traefik.io/traefik/routing/routers/#rule))
- `traefik.http.services.<service-name>.loadbalancer.server.port` - indicates the port Traefik should forward the request to. Note that this container port does not need to be exposed on your host machine ([read about port detection here](https://doc.traefik.io/traefik/providers/docker/#port-detection))

## File provider

The [File provider](https://doc.traefik.io/traefik/providers/file/) lets you define the routing rules in a YAML document.
