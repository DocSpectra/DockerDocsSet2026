---
title: Configure Windows service credentials and isolation
---

## Prerequisites and shared procedures

See [Create, update, and remove Swarm services](service-lifecycle.md) and [How services work](how-swarm-mode-works/services.md).

## gMSA for Swarm

> [!NOTE]
>
> This example only works for a Windows container.

Swarm now allows using a Docker config as a gMSA credential spec - a requirement for Active Directory-authenticated applications. This reduces the burden of distributing credential specs to the nodes they're used on. 

The following example assumes a gMSA and its credential spec (called credspec.json) already exists, and that the nodes being deployed to are correctly configured for the gMSA.

To use a config as a credential spec, first create the Docker config containing the credential spec:

```console
$ docker config create credspec credspec.json
```

Now, you should have a Docker config named credspec, and you can create a service using this credential spec. To do so, use the --credential-spec flag with the config name, like this:

```console
$ docker service create --credential-spec="config://credspec" <your image>
```

Your service uses the gMSA credential spec when it starts, but unlike a typical Docker config (used by passing the --config flag), the credential spec is not mounted into the container.

## Provide credential specs for managed service accounts

 In Enterprise Edition 3.0, security is improved through the centralized distribution and management of Group Managed Service Account(gMSA) credentials using Docker config functionality. Swarm now allows using a Docker config as a gMSA credential spec, which reduces the burden of distributing credential specs to the nodes on which they are used. 

> [!NOTE]
>
> This option is only applicable to services using Windows containers.

 Credential spec files are applied at runtime, eliminating the need for host-based credential spec files or registry entries - no gMSA credentials are written to disk on worker nodes. You can make credential specs available to Docker Engine running swarm kit worker nodes before a container starts. When deploying a service using a gMSA-based config, the credential spec is passed directly to the runtime of containers in that service.

 The `--credential-spec` must be in one of the following formats:

 - `file://<filename>`: The referenced file must be present in the `CredentialSpecs` subdirectory in the docker data directory, which defaults to `C:\ProgramData\Docker\` on Windows. For example, specifying `file://spec.json` loads `C:\ProgramData\Docker\CredentialSpecs\spec.json`.
- `registry://<value-name>`: The credential spec is read from the Windows registry on the daemon’s host. 
- `config://<config-name>`: The config name is automatically converted to the config ID in the CLI. 
The credential spec contained in the specified `config` is used.

 The following simple example retrieves the gMSA name and JSON contents from your Active Directory (AD) instance:

 ```console
$ name="mygmsa"
$ contents="{...}"
$ echo $contents > contents.json
```

Make sure that the nodes to which you are deploying are correctly configured for the gMSA.

 To use a config as a credential spec, create a Docker config in a credential spec file named `credpspec.json`. 
 You can specify any name for the name of the `config`. 

```console
$ docker config create --label com.docker.gmsa.name=mygmsa credspec credspec.json
```

Now you can create a service using this credential spec. Specify the `--credential-spec` flag with the config name:

```console
$ docker service create --credential-spec="config://credspec" <your image>
```

 Your service uses the gMSA credential spec when it starts, but unlike a typical Docker config (used by passing the --config flag), the credential spec is not mounted into the container.

## Customize a service's isolation mode

> [!IMPORTANT]
>
> This setting applies to Windows hosts only and is ignored for Linux hosts.

Docker allows you to specify a swarm service's isolation
mode. The isolation mode can be one of the following:

- `default`: Use the default isolation mode configured for the Docker host, as
  configured by the `-exec-opt` flag or `exec-opts` array in `daemon.json`. If
  the daemon does not specify an isolation technology, `process` is the default
  for Windows Server, and `hyperv` is the default (and only) choice for
  Windows 10.

- `process`: Run the service tasks as a separate process on the host.

  > [!NOTE]
  >
  > `process` isolation mode is only supported on Windows Server.
  > Windows 10 only supports `hyperv` isolation mode.

- `hyperv`: Run the service tasks as isolated `hyperv` tasks. This increases
  overhead but provides more isolation.

You can specify the isolation mode when creating or updating a new service using
the `--isolation` flag.
