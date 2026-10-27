---
description: Deploy services to a swarm
keywords: guide, swarm mode, swarm, service
title: Deploy services to a swarm
toc_max: 4
---

See [Create, update, and remove Swarm services](service-lifecycle.md).

## Create a service

See [Create a service](service-lifecycle.md#create-a-service).

### gMSA for Swarm

See [gMSA for Swarm](service-windows.md#gmsa-for-swarm).

### Create a service using an image on a private registry

See [Create a service using an image on a private registry](service-images.md#create-a-service-using-an-image-on-a-private-registry).

### Provide credential specs for managed service accounts

See [Provide credential specs for managed service accounts](service-windows.md#provide-credential-specs-for-managed-service-accounts).

## Update a service

See [Update a service](service-lifecycle.md#update-a-service).

## Remove a service

See [Remove a service](service-lifecycle.md#remove-a-service).

## Service configuration details

See [Service configuration details](service-lifecycle.md#service-configuration-details).

### Configure the runtime environment

See [Configure the runtime environment](service-lifecycle.md#configure-the-runtime-environment).

### Update the command an existing service runs

See [Update the command an existing service runs](service-lifecycle.md#update-the-command-an-existing-service-runs).

### Specify the image version a service should use

See [Specify the image version a service should use](service-images.md#specify-the-image-version-a-service-should-use).

### Update a service's image after creation

See [Update a service's image after creation](service-images.md#update-a-services-image-after-creation).

#### If the manager resolves the tag

See [If the manager resolves the tag](service-images.md#if-the-manager-resolves-the-tag).

#### If the manager cannot resolve the tag

See [If the manager cannot resolve the tag](service-images.md#if-the-manager-cannot-resolve-the-tag).

### Publish ports

See [Publish ports](service-ports.md#publish-ports).

#### Publish a service's ports using the routing mesh

See [Publish a service's ports using the routing mesh](service-ports.md#publish-a-services-ports-using-the-routing-mesh).

##### Example: Run a three-task Nginx service on 10-node swarm

See [Example: Run a three-task Nginx service on 10-node swarm](service-ports.md#example-run-a-three-task-nginx-service-on-10-node-swarm).

#### Publish a service's ports directly on the swarm node

See [Publish a service's ports directly on the swarm node](service-ports.md#publish-a-services-ports-directly-on-the-swarm-node).

##### Example: Run an `nginx` web server service on every swarm node

See [Example: Run an `nginx` web server service on every swarm node](service-ports.md#example-run-an-nginx-web-server-service-on-every-swarm-node).

### Connect the service to an overlay network

See [Connect the service to an overlay network](service-networks.md#connect-the-service-to-an-overlay-network).

### Grant a service access to secrets

To create a service with access to Docker-managed secrets, use the `--secret`
flag. For more information, see
[Docker secret lifecycle and platform support](secrets-context.md)

### Customize a service's isolation mode

See [Customize a service's isolation mode](service-windows.md#customize-a-services-isolation-mode).

### Control service placement

See [Control service placement](service-placement.md#control-service-placement).

#### Replicated or global services

See [Replicated or global services](service-placement.md#replicated-or-global-services).

#### Reserve memory or CPUs for a service

See [Reserve memory or CPUs for a service](service-placement.md#reserve-memory-or-cpus-for-a-service).

##### Out Of Memory Exceptions (OOME)

See [Out Of Memory Exceptions (OOME)](service-placement.md#out-of-memory-exceptions-oome).

#### Placement constraints

See [Placement constraints](service-placement.md#placement-constraints).

#### Placement preferences

See [Placement preferences](service-placement.md#placement-preferences).

### Configure a service's update behavior

See [Configure a service's update behavior](service-updates.md#configure-a-services-update-behavior).

### Roll back to the previous version of a service

In case the updated version of a service doesn't function as expected, it's
possible to manually roll back to the previous version of the service using
`docker service update`'s `--rollback` flag. This reverts the service
to the configuration that was in place before the most recent
`docker service update` command.

Other options can be combined with `--rollback`; for example,
`--update-delay 0s`, to execute the rollback without a delay between tasks:

```console
$ docker service update \
  --rollback \
  --update-delay 0s
  my_web
```

You can configure a service to roll back automatically if a service update fails
to deploy. See [Automatically roll back if an update fails](#automatically-roll-back-if-an-update-fails).

Manual rollback is handled at the server side, which allows manually-initiated
rollbacks to respect the new rollback parameters. Note that `--rollback` cannot
be used in conjunction with other flags to `docker service update`.

### Automatically roll back if an update fails

See [Automatically roll back if an update fails](service-updates.md#automatically-roll-back-if-an-update-fails).

### Give a service access to volumes or bind mounts

See [Give a service access to volumes or bind mounts](service-storage.md#give-a-service-access-to-volumes-or-bind-mounts).

#### Data volumes

See [Data volumes](service-storage.md#data-volumes).

#### Bind mounts

See [Bind mounts](service-storage.md#bind-mounts).

### Create services using templates

See [Create services using templates](service-templates.md#create-services-using-templates).

#### Template example

See [Template example](service-templates.md#template-example).

## Learn More

* [Swarm administration guide](admin_guide.md)
* [Docker Engine command line reference](/reference/cli/docker/)
* [Swarm mode tutorial](swarm-tutorial/_index.md)
